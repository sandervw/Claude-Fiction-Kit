from __future__ import annotations

import re

from modules.utils.file_pipeline import resolve_paths, read_file


def split_md_by_h2(filename: str) -> list[dict]:
    """Split a markdown file from input/ into sections by ## headers.

    Returns a list of {name, text} objects where 'name' is the header
    and 'text' is everything below it until the next ## (or end of file).
    """

    input_file, _ = resolve_paths(filename, output_suffix=".json")
    content = read_file(input_file)

    # Split on ## headers, keeping the header text
    sections = re.split(r"^## (.+)$", content, flags=re.MULTILINE)

    # sections[0] is everything before the first ##, then alternating name/text pairs
    results = []
    for i in range(1, len(sections), 2):
        name = sections[i].strip()
        text = sections[i + 1].strip()
        results.append({"name": name, "text": text})

    return results
