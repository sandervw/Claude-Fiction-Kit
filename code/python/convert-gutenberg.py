#!/usr/bin/env python3
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

import re
import sys
from html.parser import HTMLParser
from html import unescape
from pathlib import Path

# Section IDs to skip entirely (case-sensitive, matches h2 id attribute)
SKIP_SECTIONS = {
    'CONTENTS',
    'ILLUSTRATIONS',
    'DEDICATION',
}


class GutenbergToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self.output = []
        self.current_text = []

        # State tracking
        self.in_body = False
        self.in_pg_header = False
        self.in_pg_footer = False
        self.in_h2 = False
        self.in_subhead = False
        self.in_paragraph = False
        self.in_poetry = False
        self.in_stanza = False
        self.in_blockquote = False
        self.in_titlepage = False
        self.skip_section = False
        self.skip_content = False

        # Metadata extraction
        self.title = ""
        self.author = ""
        self.source_url = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        classes = attrs_dict.get('class', '').split()
        tag_id = attrs_dict.get('id', '')

        # Extract metadata from meta tags
        if tag == 'meta':
            name = attrs_dict.get('name', '')
            content = attrs_dict.get('content', '')
            if name == 'dc.title' and not self.title:
                self.title = content
            elif name == 'dc.creator' and not self.author:
                # Clean up author format (e.g., "Eddison, Eric Rücker, 1882-1945")
                parts = content.split(',')
                if len(parts) >= 2:
                    self.author = f"{parts[1].strip()} {parts[0].strip()}"
                else:
                    self.author = content

        # Extract source URL
        if tag == 'link' and attrs_dict.get('rel') == 'dcterms.isFormatOf':
            self.source_url = attrs_dict.get('href', '')

        # Skip Gutenberg boilerplate
        if 'pg-header' in classes or tag_id == 'pg-header':
            self.in_pg_header = True
            self.skip_content = True
            return
        if 'pg-footer' in classes or tag_id == 'pg-footer':
            self.in_pg_footer = True
            self.skip_content = True
            return

        # Skip page numbers
        if 'pagenum' in classes:
            self.skip_content = True
            return

        # Skip images
        if 'figcenter' in classes:
            self.skip_content = True
            return

        # Skip title page
        if 'titlepage' in classes:
            self.in_titlepage = True
            self.skip_content = True
            return

        if tag == 'body':
            self.in_body = True
            return

        if not self.in_body or self.skip_content:
            return

        # Check for sections to skip
        if tag == 'h2':
            if tag_id in SKIP_SECTIONS:
                self.skip_section = True
                return
            else:
                self.skip_section = False

        # Skip content in excluded sections
        if self.skip_section:
            return

        if tag == 'div' and 'chapter' in classes:
            return

        if tag == 'h2' and self.in_body:
            self.in_h2 = True
            self.current_text = []
            return

        if tag == 'div' and 'subhead' in classes:
            self.in_subhead = True
            self.current_text = []
            return

        if tag == 'p':
            self.in_paragraph = True
            self.current_text = []
            return

        if tag == 'div' and 'poetry' in classes:
            self.in_poetry = True
            self.output.append("\n")
            return

        if tag == 'div' and 'stanza' in classes:
            self.in_stanza = True
            return

        if tag == 'blockquote':
            self.in_blockquote = True
            return

        # Line breaks in poetry
        if tag == 'br' and self.in_poetry:
            self.current_text.append('\n')
            return

        # Inline formatting
        if tag in ('i', 'em'):
            self.current_text.append('*')
            return
        if tag in ('b', 'strong'):
            self.current_text.append('**')
            return

    def handle_endtag(self, tag):
        if tag == 'section':
            if self.in_pg_header:
                self.in_pg_header = False
                self.skip_content = False
                return
            if self.in_pg_footer:
                self.in_pg_footer = False
                self.skip_content = False
                return

        if tag == 'span' and self.skip_content:
            self.skip_content = False
            return

        if tag == 'div':
            if self.skip_content:
                if self.in_titlepage:
                    self.in_titlepage = False
                self.skip_content = False
                return
            if self.in_poetry:
                if self.in_stanza:
                    self.in_stanza = False
                    self.output.append("\n")
                else:
                    self.in_poetry = False
                return
            if self.in_subhead:
                self.in_subhead = False
                text = self._clean_text()
                if text:
                    self.output.append(f"*{text}*\n\n")
                return

        if self.skip_content or self.skip_section:
            return

        if tag == 'h2' and self.in_h2:
            self.in_h2 = False
            text = self._clean_text()
            if text:
                self.output.append(f"\n---\n\n## {text}\n\n")
            return

        if tag == 'p' and self.in_paragraph:
            self.in_paragraph = False
            text = self._clean_text()
            if text:
                if self.in_blockquote:
                    self.output.append(f"> {text}\n>\n")
                else:
                    self.output.append(f"{text}\n\n")
            return

        if tag == 'blockquote':
            self.in_blockquote = False
            self.output.append("\n")
            return

        # Inline formatting
        if tag in ('i', 'em'):
            self.current_text.append('*')
            return
        if tag in ('b', 'strong'):
            self.current_text.append('**')
            return

    def handle_data(self, data):
        if self.skip_content or self.in_pg_header or self.in_pg_footer:
            return
        if self.skip_section:
            return
        if self.in_h2 or self.in_subhead or self.in_paragraph:
            self.current_text.append(data)

    def _clean_text(self):
        """Join current text and normalize whitespace."""
        text = ''.join(self.current_text).strip()
        text = re.sub(r'\s+', ' ', text)
        self.current_text = []
        return text

    def get_markdown(self):
        return ''.join(self.output)

    def get_header(self):
        """Generate markdown header from extracted metadata."""
        title = self.title or "Unknown Title"
        author = self.author or "Unknown Author"
        source = self.source_url or "Project Gutenberg"

        return f"""# {title}

*{author}*

*Source: {source}. Public domain.*

"""


def convert(input_path: str, output_path: str = None):
    """Convert a Gutenberg HTML file to Markdown."""
    input_file = Path(input_path)

    if output_path is None:
        output_file = input_file.with_suffix('.md')
    else:
        output_file = Path(output_path)

    # Read and parse
    html_content = input_file.read_text(encoding='utf-8')

    parser = GutenbergToMarkdown()
    parser.feed(html_content)

    markdown = parser.get_markdown()

    # Clean up
    markdown = unescape(markdown)
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    markdown = re.sub(r'\*\*\*\*+', '', markdown)  # Remove bold artifacts
    markdown = markdown.strip()

    # Add header
    markdown = parser.get_header() + markdown

    # Write output
    output_file.write_text(markdown, encoding='utf-8')

    print(f"Converted: {input_file.name} -> {output_file.name}")
    print(f"Title: {parser.title or 'Unknown'}")
    print(f"Author: {parser.author or 'Unknown'}")
    print(f"Output size: {len(markdown):,} characters")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    convert(input_path, output_path)


if __name__ == "__main__":
    main()
