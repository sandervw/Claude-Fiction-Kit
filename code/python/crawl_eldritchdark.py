"""Crawl a story page from eldritchdark.com and write clean Markdown.

Usage:
    python crawl_eldritchdark.py <url> [output-stem]
    python crawl_eldritchdark.py --urls urls.txt

When output-stem is omitted, the URL's last path segment is used
(e.g. 'the-dark-age' -> output/the-dark-age.md).
"""

from __future__ import annotations

import sys
from pathlib import Path

from modules.sites.eldritchdark import SITE_NAME, parse_story
from modules.utils.file_pipeline import (
    get_project_root,
    print_summary,
    write_file,
)
from modules.utils.http_fetcher import fetch_html
from modules.utils.markdown_writer import clean_markdown, format_header
from modules.utils.slugify import url_to_slug


def crawl(url: str, output_stem: str | None = None) -> Path:
    html = fetch_html(url)
    body_md, meta = parse_story(html, source_url=url)
    body_md = clean_markdown(body_md)
    header = format_header(
        title=meta.title or "Unknown Title",
        author=meta.author or "Unknown Author",
        source=f"{url}. {SITE_NAME}",
    )
    markdown = header + body_md

    stem = output_stem or url_to_slug(url)
    output_file = (
        get_project_root(anchor=__file__, levels_up=3) / "output" / f"{stem}.md"
    )
    write_file(output_file, markdown)
    print_summary(
        url,
        output_file.name,
        len(markdown),
        title=meta.title or "Unknown",
        author=meta.author or "Unknown",
    )
    return output_file


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    if args[0] == "--urls":
        if len(args) < 2:
            print("Error: --urls requires a file path")
            sys.exit(1)
        url_file = Path(args[1])
        urls = [line.strip() for line in url_file.read_text().splitlines() if line.strip()]
        for url in urls:
            crawl(url)
        return

    url = args[0]
    output_stem = args[1] if len(args) > 1 else None
    crawl(url, output_stem)


if __name__ == "__main__":
    main()
