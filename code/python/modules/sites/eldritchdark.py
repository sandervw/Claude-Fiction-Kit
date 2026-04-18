"""Parser for eldritchdark.com story pages.

Page layout (verified against /writings/short-stories/35/the-dark-age):
    <div id="contents">
        <div id="heading"><h1>TITLE</h1><h2>AUTHOR</h2></div>
        <p>...story paragraphs...</p>
        <p id="bib">Bibliographic Citation</p>
        <div id="btt">Top of Page</div>
        <p id="footer">Last Modified: ...</p>
    </div>
    <div id="navcontainer">...site nav...</div>
"""

from __future__ import annotations

from dataclasses import dataclass

from bs4 import BeautifulSoup

from modules.utils.html_to_markdown import html_node_to_markdown

SITE_NAME = "Eldritch Dark"
DEFAULT_AUTHOR = "Clark Ashton Smith"

DROP_IDS = {"heading", "btt", "bib", "footer", "navcontainer"}
DROP_TAGS = {"script", "style"}


@dataclass
class Metadata:
    title: str = ""
    author: str = ""
    source_url: str = ""


def parse_story(html: str, source_url: str) -> tuple[str, Metadata]:
    soup = BeautifulSoup(html, "html.parser")
    meta = _extract_metadata(soup, source_url)

    contents = soup.select_one("div#contents")
    if contents is None:
        raise ValueError("Could not find <div id='contents'> in page")

    for el in contents.find_all(id=DROP_IDS):
        el.decompose()
    for el in contents.find_all(DROP_TAGS):
        el.decompose()

    markdown = html_node_to_markdown(contents)
    return markdown, meta


def _extract_metadata(soup: BeautifulSoup, source_url: str) -> Metadata:
    heading = soup.select_one("div#heading")
    title = ""
    author = DEFAULT_AUTHOR
    if heading is not None:
        h1 = heading.find("h1")
        h2 = heading.find("h2")
        if h1 is not None:
            title = h1.get_text(strip=True)
        if h2 is not None:
            author = h2.get_text(strip=True) or DEFAULT_AUTHOR
    if not title:
        title_tag = soup.find("title")
        if title_tag is not None:
            title = title_tag.get_text(strip=True).split(" by ")[0]
    return Metadata(title=title, author=author, source_url=source_url)
