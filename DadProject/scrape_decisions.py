"""
Iowa Workers' Compensation Decisions Scraper
=============================================
Scrapes PDF decisions from https://efile.iowaworkcomp.gov/decisions/
for the last 10 years (2016-2025), extracts text, and saves as .txt files.

Usage:
    python scrape_decisions.py [--output-dir OUTPUT_DIR] [--start-year YEAR] [--end-year YEAR]
                               [--keep-pdfs] [--delay SECONDS] [--timeout SECONDS]
                               [--max-retries N]
"""

import argparse
import logging
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import fitz  # PyMuPDF
import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_URL = "https://efile.iowaworkcomp.gov/decisions/"
YEAR_URL_MAP = {
    2025: "decisionscurrent.html",
    # 2024 down to any year follows the pattern decisions{YYYY}.html
}

DEFAULT_START_YEAR = 2016
DEFAULT_END_YEAR = 2025
DEFAULT_OUTPUT_DIR = "OutputPDFs"
DEFAULT_DELAY = 1.0        # seconds between PDF downloads (be polite)
DEFAULT_TIMEOUT = 60       # seconds per request
DEFAULT_MAX_RETRIES = 3

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def get_year_url(year: int) -> str:
    """Return the full URL for a given year's decisions page."""
    filename = YEAR_URL_MAP.get(year, f"decisions{year}.html")
    return urljoin(BASE_URL, filename)


def sanitize_filename(name: str) -> str:
    """Replace characters that are illegal in Windows/Linux filenames."""
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip()


def fetch_page(url: str, session: requests.Session, timeout: int) -> str | None:
    """GET an HTML page and return its text, or None on failure."""
    try:
        resp = session.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as exc:
        log.error("Failed to fetch %s: %s", url, exc)
        return None


def parse_decisions(html: str) -> list[dict]:
    """
    Parse a year page and return a list of dicts:
        {
            "case_number": str,
            "case_title": str,
            "doc_type": str,
            "pdf_url": str,
            "link_text": str,
        }
    """
    soup = BeautifulSoup(html, "html.parser")
    decisions = []

    # Each data row is <tr class="style_6"> with an <a> linking to a PDF
    for row in soup.find_all("tr", class_="style_6"):
        link = row.find("a", href=True)
        if not link:
            continue

        href = link["href"]
        # Only care about get.jsp PDF links
        if "get.jsp" not in href:
            continue

        # Extract cell contents in order:
        # cols: [empty/span2], case_title, case_number, doc_type, link_cell, date
        cells = row.find_all("td")

        case_number = ""
        case_title = ""
        doc_type = ""

        # The case number cell contains a bare <div> with just the number
        # The case title cell has <div class="style_7">
        # Walk cells and pull text
        text_cells = []
        for cell in cells:
            div = cell.find("div")
            text = div.get_text(strip=True) if div else cell.get_text(strip=True)
            text_cells.append(text)

        # Typical layout (with colspan=2 first cell):
        #   [0] "" (colspan 2), [1] case_title, [2] case_number,
        #   [3] doc_type, [4] link_text, [5] date
        # But colspan can shift indices. Find the case number by pattern.
        # Case numbers may or may not have a decimal suffix (e.g. 19003535.02 or 5053002)
        case_num_pattern = re.compile(r"^\d{5,}(\.\d+)?$")
        for i, t in enumerate(text_cells):
            if case_num_pattern.match(t):
                case_number = t
                # Title is the cell before, doc_type is the cell after
                if i > 0:
                    case_title = text_cells[i - 1]
                if i + 1 < len(text_cells):
                    doc_type = text_cells[i + 1]
                break

        if not case_number:
            # Fallback: try to extract from the link text filename
            link_text = link.get_text(strip=True)
            m = re.search(r"(\d{5,}(?:\.\d+)?)", link_text)
            if m:
                case_number = m.group(1)

        if not case_number:
            log.warning("Could not extract case number from row; skipping. Link: %s", href[:80])
            continue

        decisions.append({
            "case_number": case_number,
            "case_title": case_title,
            "doc_type": doc_type,
            "pdf_url": href,
            "link_text": link.get_text(strip=True),
        })

    return decisions


def download_pdf(
    url: str,
    dest: Path,
    session: requests.Session,
    timeout: int,
    max_retries: int,
) -> bool:
    """Download a PDF from a get.jsp URL. Returns True on success."""
    for attempt in range(1, max_retries + 1):
        try:
            resp = session.get(url, headers=HEADERS, timeout=timeout, stream=True)
            resp.raise_for_status()

            # Verify we actually got a PDF (check content-type or magic bytes)
            content_type = resp.headers.get("Content-Type", "")
            with open(dest, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Quick sanity check: PDF magic bytes
            with open(dest, "rb") as f:
                header = f.read(5)
            if header != b"%PDF-":
                log.warning("Downloaded file doesn't look like a PDF: %s (header: %s)", dest.name, header[:20])
                # Could be an HTML error page — keep it but warn
            return True

        except requests.RequestException as exc:
            log.warning("Attempt %d/%d failed for %s: %s", attempt, max_retries, dest.name, exc)
            if attempt < max_retries:
                time.sleep(2 * attempt)  # back off
    return False


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract all text from a PDF using PyMuPDF."""
    text_parts = []
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text_parts.append(page.get_text())
    except Exception as exc:
        log.error("Failed to extract text from %s: %s", pdf_path.name, exc)
    return "\n".join(text_parts)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Scrape Iowa WC decision PDFs.")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR,
                        help=f"Output directory (default: {DEFAULT_OUTPUT_DIR})")
    parser.add_argument("--start-year", type=int, default=DEFAULT_START_YEAR,
                        help=f"First year to scrape (default: {DEFAULT_START_YEAR})")
    parser.add_argument("--end-year", type=int, default=DEFAULT_END_YEAR,
                        help=f"Last year to scrape (default: {DEFAULT_END_YEAR})")
    parser.add_argument("--keep-pdfs", action="store_true",
                        help="Keep PDF files after text extraction")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY,
                        help=f"Delay between downloads in seconds (default: {DEFAULT_DELAY})")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                        help=f"HTTP timeout in seconds (default: {DEFAULT_TIMEOUT})")
    parser.add_argument("--max-retries", type=int, default=DEFAULT_MAX_RETRIES,
                        help=f"Max download retries per PDF (default: {DEFAULT_MAX_RETRIES})")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    session = requests.Session()

    # ------------------------------------------------------------------
    # Phase 1: Collect all decision metadata across years
    # ------------------------------------------------------------------
    all_decisions = []
    for year in range(args.start_year, args.end_year + 1):
        url = get_year_url(year)
        log.info("Fetching year page: %d (%s)", year, url)
        html = fetch_page(url, session, args.timeout)
        if html is None:
            log.error("Skipping year %d — could not fetch page.", year)
            continue
        decisions = parse_decisions(html)
        log.info("  Found %d decisions for %d", len(decisions), year)
        all_decisions.extend(decisions)
        time.sleep(0.5)  # small pause between year pages

    log.info("Total decisions found: %d", len(all_decisions))

    if not all_decisions:
        log.warning("No decisions found. Exiting.")
        sys.exit(0)

    # ------------------------------------------------------------------
    # Phase 2: Download PDFs, extract text, clean up
    # ------------------------------------------------------------------
    # Handle duplicate case numbers by appending a suffix
    case_number_counts: dict[str, int] = {}
    success_count = 0
    fail_count = 0

    for i, dec in enumerate(all_decisions, 1):
        case_num = dec["case_number"]

        # Build unique filename
        if case_num in case_number_counts:
            case_number_counts[case_num] += 1
            safe_name = f"case-{sanitize_filename(case_num)}_{case_number_counts[case_num]}"
        else:
            case_number_counts[case_num] = 1
            safe_name = f"case-{sanitize_filename(case_num)}"

        pdf_path = output_dir / f"{safe_name}.pdf"
        txt_path = output_dir / f"{safe_name}.txt"

        # Skip if txt already exists (resume support)
        if txt_path.exists():
            log.info("[%d/%d] Already extracted: %s", i, len(all_decisions), txt_path.name)
            success_count += 1
            continue

        log.info("[%d/%d] Downloading: %s  (%s)", i, len(all_decisions), safe_name, dec["case_title"][:50])
        ok = download_pdf(dec["pdf_url"], pdf_path, session, args.timeout, args.max_retries)
        if not ok:
            log.error("  FAILED to download %s", safe_name)
            fail_count += 1
            continue

        # Extract text
        text = extract_text_from_pdf(pdf_path)
        if not text.strip():
            log.warning("  No text extracted from %s (scanned PDF?)", safe_name)

        # Write .txt with metadata header
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(f"Case Number: {dec['case_number']}\n")
            f.write(f"Case Title:  {dec['case_title']}\n")
            f.write(f"Doc Type:    {dec['doc_type']}\n")
            f.write(f"Source:      {dec['link_text']}\n")
            f.write("=" * 72 + "\n\n")
            f.write(text)

        # Clean up PDF unless --keep-pdfs
        if not args.keep_pdfs and pdf_path.exists():
            pdf_path.unlink()

        success_count += 1
        time.sleep(args.delay)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    log.info("=" * 60)
    log.info("DONE. Extracted: %d  |  Failed: %d  |  Total: %d",
             success_count, fail_count, len(all_decisions))
    log.info("Output directory: %s", output_dir.resolve())


if __name__ == "__main__":
    main()
