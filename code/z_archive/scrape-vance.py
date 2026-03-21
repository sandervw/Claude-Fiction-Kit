"""
Scrape Jack Vance books from msgbrains.com and save as markdown.

Books:
  - The Eyes of the Overworld (43 pages)
  - Cugel's Saga (89 pages)
  - The Dying Earth (45 pages)
  - Rhialto the Marvellous (56 pages)

Usage:
  pip install beautifulsoup4 requests markdownify
  python scrape-vance.py
"""

import time
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BOOKS = [
    {
        "title": "The Dying Earth",
        "base_url": "https://msgbrains.com/english-books/681-the-dying-earth-by-jack-vance.html/reader_page/",
        "pages": 45,
        "output": "../../sources/literature/The-Dying-Earth.md",
    },
    {
        "title": "The Eyes of the Overworld",
        "base_url": "https://msgbrains.com/english-books/682--the-eyes-of-the-overworld-by-jack-vance-.html/reader_page/",
        "pages": 43,
        "output": "../../sources/literature/The-Eyes-of-the-Overworld.md",
    },
    {
        "title": "Cugel's Saga",
        "base_url": "https://msgbrains.com/english-books/679-cugels-saga-by-jack-vance.html/reader_page/",
        "pages": 89,
        "output": "../../sources/literature/Cugels-Saga.md",
    },
    {
        "title": "Rhialto the Marvellous",
        "base_url": "https://msgbrains.com/english-books/680-rhialto-the-marvellous-by-jack-vance-.html/reader_page/",
        "pages": 56,
        "output": "../../sources/literature/Rhialto-the-Marvellous.md",
    },
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Pages that are front-matter (title, copyright, TOC) -- skip these
# Set to 0 to include everything; adjust after inspecting output
SKIP_FRONT_PAGES = 0


def fetch_page(url: str) -> str | None:
    """Fetch a single page and extract the reader_content div as markdown."""
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    content_div = soup.find("div", id="reader_content")

    if not content_div:
        print(f"  WARNING: No reader_content found at {url}")
        return None

    # Remove images (cover art, decorative separators)
    for img in content_div.find_all("img"):
        img.decompose()

    # Convert to markdown
    raw_md = md(str(content_div), heading_style="ATX", strip=["div"])

    # Clean up excessive blank lines
    lines = raw_md.split("\n")
    cleaned = []
    blank_count = 0
    for line in lines:
        if line.strip() == "":
            blank_count += 1
            if blank_count <= 2:
                cleaned.append("")
        else:
            blank_count = 0
            cleaned.append(line)

    return "\n".join(cleaned).strip()


def scrape_book(book: dict) -> None:
    """Scrape all pages of a book and write to a single markdown file."""
    title = book["title"]
    base_url = book["base_url"]
    total_pages = book["pages"]
    output_path = book["output"]

    print(f"\n{'='*60}")
    print(f"Scraping: {title} ({total_pages} pages)")
    print(f"{'='*60}")

    all_content = []
    all_content.append(f"# {title}\n")
    all_content.append(f"**by Jack Vance**\n")

    for page_num in range(1, total_pages + 1):
        url = f"{base_url}{page_num}"
        print(f"  Page {page_num}/{total_pages}...", end=" ", flush=True)

        try:
            content = fetch_page(url)
            if content:
                all_content.append(content)
                print("OK")
            else:
                print("EMPTY")
        except requests.RequestException as e:
            print(f"ERROR: {e}")

        # Be polite -- small delay between requests
        if page_num < total_pages:
            time.sleep(1.5)

    # Write output
    full_text = "\n\n".join(all_content)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"\nSaved to: {output_path}")


def main():
    for book in BOOKS:
        scrape_book(book)
    print("\nDone!")


if __name__ == "__main__":
    main()
