"""
Cross-references names from a JSON results file against .txt files in a folder.
For each person in results, finds all files containing both their first and last name.
Appends matching filenames as a "cases-involved" array on each result object.

Usage:
    python match_cases.py <json_file> <search_folder>
"""

import json
import os
import re
import sys


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def build_name_patterns(results: list[dict]) -> list[tuple[re.Pattern, re.Pattern]]:
    """Compile word-boundary regex patterns for each (first, last) name pair."""
    return [
        (
            re.compile(r"\b" + re.escape(r["first_name"].lower()) + r"\b"),
            re.compile(r"\b" + re.escape(r["last_name"].lower()) + r"\b"),
        )
        for r in results
    ]


def scan_files(folder: str, name_patterns: list[tuple[re.Pattern, re.Pattern]]) -> list[list[str]]:
    """
    Single-pass scan: read each .txt file once, check against ALL name patterns.
    Returns a list (per person) of matching filenames.
    """
    matches = [[] for _ in name_patterns]

    for filename in os.listdir(folder):
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(folder, filename)
        try:
            with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                content = f.read().lower()
        except (OSError, IOError):
            continue

        for i, (first_pat, last_pat) in enumerate(name_patterns):
            if first_pat.search(content) and last_pat.search(content):
                matches[i].append(filename)

    return matches


def main():
    if len(sys.argv) != 3:
        print("Usage: python match_cases.py <json_file> <search_folder>")
        sys.exit(1)

    json_path = sys.argv[1]
    search_folder = sys.argv[2]

    data = load_json(json_path)
    results = data["results"]

    name_patterns = build_name_patterns(results)
    matches = scan_files(search_folder, name_patterns)

    # Append matches to each result object
    for result, filenames in zip(results, matches):
        result["cases-involved"] = sorted(filenames)

    save_json(json_path, data)
    print(f"Done. Updated {len(results)} records in '{json_path}'.")


if __name__ == "__main__":
    main()