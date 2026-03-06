"""
Reusable markdown building and cleanup utilities.

MarkdownBuilder accumulates markdown elements (headings, paragraphs,
blockquotes, etc.) into a list, then joins them into a final string.
Think of it like a StringIO but with markdown-aware methods.

clean_markdown() handles post-processing: collapsing excess newlines,
stripping stacked formatting artifacts, and unescaping HTML entities.
"""

from __future__ import annotations

import re
from html import unescape


class MarkdownBuilder:
    def __init__(self) -> None:
        self._parts: list[str] = []

    def heading(self, text: str, level: int = 2) -> None:
        prefix = "#" * level
        self._parts.append(f"\n---\n\n{prefix} {text}\n\n")

    def paragraph(self, text: str) -> None:
        self._parts.append(f"{text}\n\n")

    def blockquote(self, text: str) -> None:
        self._parts.append(f"> {text}\n>\n")

    def italic(self, text: str) -> None:
        self._parts.append(f"*{text}*")

    def bold(self, text: str) -> None:
        self._parts.append(f"**{text}**")

    def rule(self) -> None:
        self._parts.append("\n---\n\n")

    def blank_line(self) -> None:
        self._parts.append("\n")

    def raw(self, text: str) -> None:
        self._parts.append(text)

    def build(self) -> str:
        return "".join(self._parts)


def clean_text(fragments: list[str]) -> str:
    """Join text fragments, strip, and collapse internal whitespace."""
    text = "".join(fragments).strip()
    return re.sub(r'\s+', ' ', text)


def clean_markdown(text: str) -> str:
    """Post-process raw markdown: unescape HTML, collapse blank lines,
    strip stacked formatting artifacts like ****+."""
    text = unescape(text)
    text = re.sub(r'\*\*\*\*+', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def format_header(
    title: str = "Unknown Title",
    author: str = "Unknown Author",
    source: str = "Unknown Source",
    **extra: str,
) -> str:
    """Build a markdown header/frontmatter block from metadata fields."""
    lines = [f"# {title}", f"*{author}*", f"*Source: {source}.*"]
    for label, value in extra.items():
        label_clean = label.replace("_", " ").title()
        lines.append(f"*{label_clean}: {value}*")
    return "\n\n".join(lines) + "\n\n"
