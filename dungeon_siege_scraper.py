#!/usr/bin/env python3
"""
Dungeon Siege Wiki Monster Scraper
Extracts monster names and descriptions from the Fandom wiki.

Features:
- Uses MediaWiki API (bypasses JavaScript challenges)
- Polite 2-second delay between requests
- Progress saving: automatically resumes if interrupted
- Deduplicates entries from "Wanted Pages" section
"""

import json
import time
import re
import os
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://dungeonsiege.fandom.com"
API_URL = f"{BASE_URL}/api.php"
ENEMIES_PAGE = "Enemies_(Dungeon_Siege)"

# Respectful delay between requests (seconds)
REQUEST_DELAY = 2.0

# Progress file - stores state between runs
PROGRESS_FILE = "scraper_progress.json"

# Headers for API requests
HEADERS = {
    "User-Agent": "DungeonSiegeMonsterScraper/1.0 (Educational/Research purposes)"
}


def load_progress() -> dict:
    """Load progress from previous run, if it exists."""
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return {"completed_urls": [], "monsters": [], "failed": []}


def save_progress(completed_urls: list, monsters: list, failed: list):
    """Save current progress to disk."""
    progress = {
        "completed_urls": completed_urls,
        "monsters": monsters,
        "failed": failed
    }
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=2, ensure_ascii=False)


def clear_progress():
    """Remove progress file after successful completion."""
    if os.path.exists(PROGRESS_FILE):
        os.remove(PROGRESS_FILE)


def api_request(params: dict) -> dict | None:
    """Make a request to the MediaWiki API."""
    try:
        response = requests.get(API_URL, params=params, headers=HEADERS, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"  [ERROR] API request failed: {e}")
        return None


def get_page_links(page_title: str) -> list[str]:
    """Get all internal links from a wiki page using the API."""
    params = {
        'action': 'parse',
        'page': page_title,
        'format': 'json',
        'prop': 'links'
    }

    data = api_request(params)
    if not data or 'parse' not in data:
        return []

    links = data['parse'].get('links', [])
    # Filter to namespace 0 (main articles) only
    return [link['*'] for link in links if link.get('ns') == 0]


def get_page_content(page_title: str) -> tuple[str, str] | None:
    """
    Get a page's rendered HTML content using the API.
    Returns (title, html_content) or None if failed.
    """
    params = {
        'action': 'parse',
        'page': page_title,
        'format': 'json',
        'prop': 'text|displaytitle'
    }

    data = api_request(params)
    if not data or 'parse' not in data:
        return None

    parse_data = data['parse']
    title = parse_data.get('displaytitle', page_title)
    # Remove HTML tags from display title
    title = re.sub(r'<[^>]+>', '', title)
    html = parse_data.get('text', {}).get('*', '')

    return (title, html)


def filter_monster_pages(page_titles: list[str]) -> list[str]:
    """
    Filter a list of page titles to only include likely monster pages.
    Returns filtered list of page titles.
    """
    # Skip non-monster pages
    skip_patterns = [
        "Enemies_", "Enemies (", "List_of_", "List of ",
        "Quests_", "Quests (", "Locations_", "Locations (",
        "Items_", "Items (", "Spells_", "Spells (",
        "Books_", "Books (", "Characters_", "Characters (",
        "Races_", "Races (", "Companion", "Dungeon Siege",
        "Statistics_", "Statistics (", "Classes_", "Classes (",
        "Portal:", "Template:", "User:",
    ]

    # Skip region/location pages
    location_pages = [
        "Farmlands", "Crypt of the Sacred Blood", "Ancient Crypt",
        "Stonebridge", "Elddim", "Glitterdelve", "Crystwind",
        "Wesrin Cross", "Hovart's Folly", "Glitterdelve Mine",
        "Crystwind Old Mines", "Frostspire Mountain", "Fallraen",
        "Glacern", "Alpine Caverns", "Glacial Caverns", "Subterranean River",
        "Dark Forest", "Cloud Forest", "Eastern Swamp", "Lang Mire",
        "Goblin Warrens", "Bonepicker", "Redwood Gap", "Temple Ruins",
        "Fortress Kroth", "Hall of Skulls", "Cliffs of Fire", "Quillrabe",
        "Droog Village", "Castle Ehb", "Castle Hiroth", "Vault of Eternity",
        "Volcanic Caverns", "Endless Desert", "Arhok", "Halls of the Lost",
        "Coastal Bluffs", "Illicor", "Dark Jungle", "Fen of the Frozen",
        "Trader Camp", "Mountain of the Dead", "Lair of Cicatrix",
        "Demlock", "Tower of Kmethekt", "Xot's Badlands", "Xulphae's Cove",
        "Fortress Emarard", "Great Clock", "Mount Kreth", "Chicken Level"
    ]

    monsters = []
    skip_pattern_count = 0
    skip_location_count = 0

    for title in page_titles:
        # Check skip patterns
        if any(pattern in title for pattern in skip_patterns):
            skip_pattern_count += 1
            continue

        # Check locations
        if title in location_pages:
            skip_location_count += 1
            continue

        monsters.append(title)

    print(f"  Filtered: {skip_pattern_count} by pattern, {skip_location_count} locations")
    print(f"  Kept {len(monsters)} monster pages")

    return monsters


def extract_description_from_html(html: str) -> str:
    """
    Extract description from page HTML.
    Looks for content under the 'Description' header, stopping at the next header.
    Falls back to first paragraphs if no Description section exists.
    """
    soup = BeautifulSoup(html, "html.parser")

    description_parts = []

    # Try to find the "Description" header
    description_header = None
    for h2 in soup.find_all('h2'):
        span = h2.find('span', class_='mw-headline')
        if span and span.get_text(strip=True) == 'Description':
            description_header = h2
            break

    if description_header:
        # Collect all paragraphs after the Description header until next header
        for sibling in description_header.find_next_siblings():
            if sibling.name in ['h2', 'h3']:
                break
            if sibling.name == 'p':
                text = sibling.get_text(separator=' ', strip=True)
                if text and len(text) > 10:
                    description_parts.append(text)
    else:
        # Fallback: get first paragraphs from the content div
        content_div = soup.find('div', class_='mw-parser-output')
        if content_div:
            for elem in content_div.children:
                if not hasattr(elem, 'name'):
                    continue
                if elem.name in ['h2', 'h3', 'table']:
                    break
                if elem.name == 'p':
                    text = elem.get_text(separator=' ', strip=True)
                    if text and len(text) > 10:
                        description_parts.append(text)

    description = " ".join(description_parts)

    # Clean up description
    description = re.sub(r'\[\d+\]', '', description)  # Remove citation markers
    description = re.sub(r'\s+', ' ', description)      # Normalize whitespace

    return description.strip()


def scrape_monsters() -> list[dict]:
    """Main scraping function. Returns list of monster info dicts."""

    # Load any existing progress
    progress = load_progress()
    completed_pages = set(progress["completed_urls"])  # Now stores page titles
    monsters = progress["monsters"]
    failed = progress["failed"]

    if completed_pages:
        print(f"Resuming from previous run: {len(completed_pages)} pages already scraped.")

    print("Fetching monster links from enemies list page...")
    all_page_titles = get_page_links(ENEMIES_PAGE)

    if not all_page_titles:
        print("Failed to fetch enemies list. Aborting.")
        return monsters

    print(f"Found {len(all_page_titles)} total links on page.")
    print("Filtering for monster pages...")
    monster_pages = filter_monster_pages(all_page_titles)

    # Filter out already-completed pages
    remaining_pages = sorted(set(monster_pages) - completed_pages)

    print(f"Remaining to scrape: {len(remaining_pages)}")

    if not remaining_pages:
        print("All pages already scraped!")
        return monsters

    # Estimate time remaining
    est_minutes = (len(remaining_pages) * REQUEST_DELAY) / 60
    print(f"Estimated time: ~{est_minutes:.1f} minutes")
    print("-" * 40)

    try:
        for i, page_title in enumerate(remaining_pages, 1):
            print(f"[{i}/{len(remaining_pages)}] Scraping: {page_title}")

            time.sleep(REQUEST_DELAY)

            result = get_page_content(page_title)
            if not result:
                failed.append(page_title)
                completed_pages.add(page_title)
                save_progress(list(completed_pages), monsters, failed)
                continue

            name, html = result
            description = extract_description_from_html(html)

            monster_info = {
                "name": name,
                "description": description,
                "url": f"{BASE_URL}/wiki/{page_title.replace(' ', '_')}"
            }
            monsters.append(monster_info)

            completed_pages.add(page_title)

            # Save progress after each page
            save_progress(list(completed_pages), monsters, failed)

    except KeyboardInterrupt:
        print("\n\nInterrupted! Progress saved. Run again to resume.")
        save_progress(list(completed_pages), monsters, failed)
        raise

    if failed:
        print(f"\nFailed to scrape {len(failed)} pages:")
        for page in failed:
            print(f"  - {page}")

    return monsters


def main():
    print("=" * 60)
    print("Dungeon Siege Wiki Monster Scraper")
    print("=" * 60)
    
    try:
        monsters = scrape_monsters()
    except KeyboardInterrupt:
        print("Exiting. Run again to resume from where you left off.")
        return
    
    if not monsters:
        print("No monsters scraped. Exiting.")
        return
    
    # Sort by name
    monsters.sort(key=lambda m: m["name"].lower())
    
    # Output to JSON
    output_file = "dungeon_siege_monsters.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(monsters, f, indent=2, ensure_ascii=False)
    
    # Clear progress file on successful completion
    clear_progress()
    
    print(f"\n{'=' * 60}")
    print(f"Done! Scraped {len(monsters)} monsters.")
    print(f"Output saved to: {output_file}")
    print("=" * 60)


if __name__ == "__main__":
    main()
