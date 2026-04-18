"""Generic BeautifulSoup subtree -> Markdown conversion.

Pass a BS4 Tag that wraps the content you want converted; boilerplate
(nav, sidebars, etc.) should be stripped by the caller before this runs.
"""

from __future__ import annotations

from bs4 import NavigableString, Tag

from modules.utils.markdown_writer import MarkdownBuilder, clean_text

INLINE_EMPHASIS = {"i": "*", "em": "*", "b": "**", "strong": "**"}
HEADING_TAGS = {f"h{i}": i for i in range(1, 7)}


def html_node_to_markdown(node: Tag) -> str:
    md = MarkdownBuilder()
    _render_block_children(node, md, in_blockquote=False)
    return md.build()


def _render_block_children(parent: Tag, md: MarkdownBuilder, *, in_blockquote: bool) -> None:
    for child in parent.children:
        if isinstance(child, NavigableString):
            text = str(child).strip()
            if text:
                md.paragraph(text)
            continue
        if not isinstance(child, Tag):
            continue
        _render_block(child, md, in_blockquote=in_blockquote)


def _render_block(tag: Tag, md: MarkdownBuilder, *, in_blockquote: bool) -> None:
    name = tag.name.lower()

    if name in HEADING_TAGS:
        text = clean_text(list(_inline_fragments(tag)))
        if text:
            md.heading(text, level=HEADING_TAGS[name])
        return

    if name == "p":
        text = clean_text(list(_inline_fragments(tag)))
        if not text:
            return
        if in_blockquote:
            md.blockquote(text)
        else:
            md.paragraph(text)
        return

    if name == "blockquote":
        _render_block_children(tag, md, in_blockquote=True)
        md.blank_line()
        return

    if name == "hr":
        md.rule()
        return

    if name == "br":
        md.blank_line()
        return

    # Unknown block: descend into its children.
    _render_block_children(tag, md, in_blockquote=in_blockquote)


def _inline_fragments(tag: Tag):
    for child in tag.children:
        if isinstance(child, NavigableString):
            yield str(child)
            continue
        if not isinstance(child, Tag):
            continue
        name = child.name.lower()
        if name == "br":
            yield " "
            continue
        marker = INLINE_EMPHASIS.get(name)
        if marker:
            inner = clean_text(list(_inline_fragments(child)))
            if inner:
                yield f"{marker}{inner}{marker}"
            continue
        yield from _inline_fragments(child)
