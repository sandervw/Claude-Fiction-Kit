"""
Cleanup script for OCR'd text of Vance's "The Dying Earth".

Pipeline:
  1. Strip page numbers and their surrounding blank lines
  2. Strip OCR garbage lines and orphan fragments
  3. Convert story titles to ## headers
  4. Clean individual lines (OCR artifacts)
  5. Rejoin hyphenated line breaks (across blank lines left by step 1)
  6. Merge multi-line paragraphs into single lines
  7. Collapse redundant blank lines
"""

import re
import sys
from pathlib import Path

INPUT = Path(__file__).resolve().parents[1].parent / "sources" / "literature" / "Vance - The Dying Earth.md"
OUTPUT = INPUT  # overwrite in place

# ── Patterns ───────────────────────────────────────────────────
TITLE_RE = re.compile(r"^[0-9]+[,.\s]+([A-Z][A-Z\s']+)$")
PAGE_NUM_RE = re.compile(r"^\d{1,3}$")


def is_ocr_garbage(line: str) -> bool:
    """Lines that are mostly 1-3 char 'words' -- OCR noise."""
    words = line.split()
    if len(words) < 4:
        return False
    short = sum(1 for w in words if len(w) <= 3)
    return short / len(words) > 0.6


def is_orphan_fragment(line: str) -> bool:
    """Single nonsense word sitting alone between paragraphs."""
    return bool(re.match(r"^[A-Za-z]{2,10}$", line)) and line != line.upper()


def clean_line(line: str) -> str:
    """Fix common OCR artifacts on a single line."""
    # Remove stray copyright symbols
    line = line.replace("©", "")

    # Remove leading underscores (OCR indent artifacts)
    line = re.sub(r"^[_]+\s*", "", line)

    # Remove leading stray single-quote before quotes/caps
    line = re.sub(r"^'\s*(?=[A-Z\"])", "", line)

    # Remove trailing stray colons/periods (OCR noise)
    line = re.sub(r"\s+[:.]$", "", line)

    # Fix ".and" -> ". and" (missing space)
    line = re.sub(r"\.and\b", ". and", line)

    # Fix known OCR misreads
    line = line.replace("he-selected", "he selected")
    line = re.sub(r"\banal\b", "around", line)
    line = re.sub(r"i speocass", "depositing", line)

    # Fix "pee al!" -> "gaze" ... actually too specific, leave garbled text
    # but fix the stray quote before "Turjan
    line = re.sub(r'^"(?=[A-Z][a-z])', "", line)

    # Collapse multiple spaces
    line = re.sub(r"  +", " ", line)

    return line.strip()


def process(text: str) -> str:
    raw_lines = text.split("\n")

    # ── Step 1: Remove page numbers and surrounding blank lines ──
    # A page number is a standalone number on a line, typically
    # preceded and followed by blank lines. Remove all three.
    filtered = []
    i = 0
    while i < len(raw_lines):
        stripped = raw_lines[i].strip()
        if PAGE_NUM_RE.match(stripped):
            # Remove preceding blank line if present
            if filtered and filtered[-1].strip() == "":
                filtered.pop()
            # Skip the page number itself
            i += 1
            # Skip following blank line if present
            if i < len(raw_lines) and raw_lines[i].strip() == "":
                i += 1
            continue
        filtered.append(raw_lines[i])
        i += 1

    # ── Step 2: Remove garbage and fragments, convert titles, clean lines ──
    cleaned = []
    for line in filtered:
        stripped = line.strip()

        if stripped == "":
            cleaned.append("")
            continue

        if is_ocr_garbage(stripped):
            continue

        if is_orphan_fragment(stripped):
            continue

        # Convert story titles to ## headers
        m = TITLE_RE.match(stripped)
        if m:
            title = m.group(1).strip().title()
            cleaned.append(f"## {title}")
            continue

        cleaned.append(clean_line(stripped))

    # ── Step 3: Rejoin hyphenated line breaks ──
    # A line ending in "[a-z]-" should join with the next non-blank
    # line if it starts with lowercase. Also absorb any blank lines
    # between them (they were artifacts of page-number removal).
    rejoined = []
    i = 0
    while i < len(cleaned):
        line = cleaned[i]

        if line and re.search(r"[a-z]-$", line):
            # Find next non-blank line
            j = i + 1
            blanks_between = []
            while j < len(cleaned) and cleaned[j] == "":
                blanks_between.append(j)
                j += 1
            if j < len(cleaned) and cleaned[j] and cleaned[j][0].islower():
                # Join: remove trailing hyphen, concatenate
                line = line[:-1] + cleaned[j]
                # Skip everything between i and j (inclusive)
                i = j + 1
                rejoined.append(line)
                continue
            else:
                # Not a line-break hyphen; keep as-is (compound word at line end)
                rejoined.append(line)
                i += 1
                continue

        rejoined.append(line)
        i += 1

    # ── Step 4: Merge paragraph lines ──
    # Consecutive non-blank lines = one paragraph. Blank line = break.
    merged = []
    para_buf = []

    for line in rejoined:
        if line == "":
            if para_buf:
                merged.append(" ".join(para_buf))
                para_buf = []
            merged.append("")
        elif line.startswith("## ") or line.startswith("# "):
            if para_buf:
                merged.append(" ".join(para_buf))
                para_buf = []
            merged.append(line)
        else:
            para_buf.append(line)

    if para_buf:
        merged.append(" ".join(para_buf))

    # ── Step 5: Collapse runs of blank lines into one ──
    final = []
    prev_blank = False
    for line in merged:
        if line == "":
            if not prev_blank:
                final.append("")
            prev_blank = True
        else:
            prev_blank = False
            final.append(line)

    while final and final[-1] == "":
        final.pop()

    return "\n".join(final) + "\n"


def main():
    src = INPUT if len(sys.argv) < 2 else Path(sys.argv[1])
    dst = OUTPUT if len(sys.argv) < 3 else Path(sys.argv[2])

    text = src.read_text(encoding="utf-8")
    result = process(text)
    dst.write_text(result, encoding="utf-8")

    orig_lines = text.count("\n")
    new_lines = result.count("\n")
    print(f"Done. {orig_lines} -> {new_lines} lines ({orig_lines - new_lines} removed/merged)")
    print(f"Written to: {dst}")


if __name__ == "__main__":
    main()
