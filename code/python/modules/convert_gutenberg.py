"""
Convert Project Gutenberg HTML books to clean Markdown.

Usage:
    python convert-gutenberg.py <input.html> [output.md]

If output is not specified, uses the input filename with .md extension.

The script:
- Strips Gutenberg header/footer boilerplate
- Skips table of contents, illustrations list, title pages
- Converts chapters (h2 tags) to ## headers
- Converts subheadings to italicized text
- Preserves italics and bold formatting
- Handles blockquotes and poetry blocks
- Cleans up whitespace and artifacts

You may need to customize the SKIP_SECTIONS list and tweak the header
for different books.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser

from modules.utils.markdown_writer import (
    MarkdownBuilder,
    clean_markdown,
    clean_text,
    format_header,
)
from modules.utils.file_pipeline import (
    read_file,
    resolve_paths,
    write_file,
    print_summary,
)

SKIP_SECTIONS = {'CONTENTS', 'ILLUSTRATIONS', 'DEDICATION'}


@dataclass
class ParserState:
    current_text: list[str] = field(default_factory=list)
    in_body: bool = False
    in_pg_header: bool = False
    in_pg_footer: bool = False
    in_h2: bool = False
    in_subhead: bool = False
    in_paragraph: bool = False
    in_poetry: bool = False
    in_stanza: bool = False
    in_blockquote: bool = False
    in_titlepage: bool = False
    skip_section: bool = False
    skip_content: bool = False


@dataclass
class BookMetadata:
    title: str = ""
    author: str = ""
    source_url: str = ""


class GutenbergToMarkdown(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.state = ParserState()
        self.meta = BookMetadata()
        self.md = MarkdownBuilder()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        s = self.state
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        tag_id = attrs_dict.get('id', '')

        if tag == 'meta':
            self._extract_metadata(attrs_dict)
        if tag == 'link' and attrs_dict.get('rel') == 'dcterms.isFormatOf':
            self.meta.source_url = attrs_dict.get('href', '')

        if 'pg-header' in classes or tag_id == 'pg-header':
            s.in_pg_header, s.skip_content = True, True
            return
        if 'pg-footer' in classes or tag_id == 'pg-footer':
            s.in_pg_footer, s.skip_content = True, True
            return
        if 'pagenum' in classes or 'figcenter' in classes:
            s.skip_content = True
            return
        if 'titlepage' in classes:
            s.in_titlepage, s.skip_content = True, True
            return

        if tag == 'body':
            s.in_body = True
            return
        if not s.in_body or s.skip_content:
            return

        if tag == 'h2':
            if tag_id in SKIP_SECTIONS:
                s.skip_section = True
                return
            s.skip_section = False
        if s.skip_section:
            return
        if tag == 'div' and 'chapter' in classes:
            return

        if tag == 'h2' and s.in_body:
            s.in_h2, s.current_text = True, []
            return
        if tag == 'div' and 'subhead' in classes:
            s.in_subhead, s.current_text = True, []
            return
        if tag == 'p':
            s.in_paragraph, s.current_text = True, []
            return
        if tag == 'div' and 'poetry' in classes:
            s.in_poetry = True
            self.md.blank_line()
            return
        if tag == 'div' and 'stanza' in classes:
            s.in_stanza = True
            return
        if tag == 'blockquote':
            s.in_blockquote = True
            return
        if tag == 'br' and s.in_poetry:
            s.current_text.append('\n')
            return
        if tag in ('i', 'em'):
            s.current_text.append('*')
        elif tag in ('b', 'strong'):
            s.current_text.append('**')

    def handle_endtag(self, tag: str) -> None:
        s = self.state
        if tag == 'section':
            if s.in_pg_header:
                s.in_pg_header, s.skip_content = False, False
                return
            if s.in_pg_footer:
                s.in_pg_footer, s.skip_content = False, False
                return

        if tag == 'span' and s.skip_content:
            s.skip_content = False
            return

        if tag == 'div':
            if s.skip_content:
                if s.in_titlepage:
                    s.in_titlepage = False
                s.skip_content = False
                return
            if s.in_poetry:
                if s.in_stanza:
                    s.in_stanza = False
                    self.md.blank_line()
                else:
                    s.in_poetry = False
                return
            if s.in_subhead:
                s.in_subhead = False
                text = clean_text(s.current_text)
                s.current_text = []
                if text:
                    self.md.raw(f"*{text}*\n\n")
                return

        if s.skip_content or s.skip_section:
            return

        if tag == 'h2' and s.in_h2:
            s.in_h2 = False
            text = clean_text(s.current_text)
            s.current_text = []
            if text:
                self.md.heading(text)
            return

        if tag == 'p' and s.in_paragraph:
            s.in_paragraph = False
            text = clean_text(s.current_text)
            s.current_text = []
            if text:
                if s.in_blockquote:
                    self.md.blockquote(text)
                else:
                    self.md.paragraph(text)
            return

        if tag == 'blockquote':
            s.in_blockquote = False
            self.md.blank_line()
            return
        if tag in ('i', 'em'):
            s.current_text.append('*')
        elif tag in ('b', 'strong'):
            s.current_text.append('**')

    def handle_data(self, data: str) -> None:
        s = self.state
        if s.skip_content or s.in_pg_header or s.in_pg_footer or s.skip_section:
            return
        if s.in_h2 or s.in_subhead or s.in_paragraph:
            s.current_text.append(data)

    def _extract_metadata(self, attrs_dict: dict[str, str]) -> None:
        name = attrs_dict.get('name', '')
        content = attrs_dict.get('content', '')
        if name == 'dc.title' and not self.meta.title:
            self.meta.title = content
        elif name == 'dc.creator' and not self.meta.author:
            parts = content.split(',')
            if len(parts) >= 2:
                self.meta.author = f"{parts[1].strip()} {parts[0].strip()}"
            else:
                self.meta.author = content

    def get_markdown(self) -> str:
        return self.md.build()

    def get_header(self) -> str:
        return format_header(
            title=self.meta.title or "Unknown Title",
            author=self.meta.author or "Unknown Author",
            source=(self.meta.source_url or "Project Gutenberg") + ". Public domain",
        )


def convert(filename: str, output_path: str | None = None) -> None:
    try:
        input_file, output_file = resolve_paths(
            filename, output_path, anchor=__file__, levels_up=3
        )
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    html_content = read_file(input_file)
    parser = GutenbergToMarkdown()
    parser.feed(html_content)

    markdown = clean_markdown(parser.get_markdown())
    markdown = parser.get_header() + markdown

    write_file(output_file, markdown)
    input_file.unlink()

    print_summary(
        input_file.name,
        output_file.name,
        len(markdown),
        deleted=True,
        title=parser.meta.title or "Unknown",
        author=parser.meta.author or "Unknown",
    )


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    convert(input_path, output_path)


if __name__ == "__main__":
    main()
