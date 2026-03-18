#!/usr/bin/env python3
"""
Clean and format Karl Edward Wagner text files to Markdown.

Usage:
    python clean_wagner.py input.txt output.md

Features:
- Fixes encoding issues (em-dashes, smart quotes, etc.)
- Detects headings dynamically (Parts, Chapters with Roman numerals, sub-sections)
- Formats as clean Markdown with proper heading hierarchy
- Works across multiple Wagner books without hardcoding chapter names
"""

import re
import sys
from pathlib import Path


def fix_encoding(text: str) -> str:
    """Fix common encoding artifacts from OCR/conversion."""
    replacements = {
        '\x97': '—',           # em-dash (most common)
        '\x96': '–',           # en-dash
        '\x93': '"',           # left double quote
        '\x94': '"',           # right double quote
        '\x91': ''',           # left single quote
        '\x92': ''',           # right single quote
        '\x85': '…',           # ellipsis
        '�': '—',              # replacement character (usually em-dash)
        '\r\n': '\n',          # Windows line endings
        '\r': '\n',            # Old Mac line endings
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text


def is_roman_numeral(s: str) -> bool:
    """Check if a string is a valid Roman numeral."""
    s = s.strip().upper()
    if not s:
        return False
    # Match Roman numerals I through L (covers most chapter counts)
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, s))


def is_part_heading(line: str) -> bool:
    """Check if line is a Part heading (e.g., 'PART ONE', 'Part Two')."""
    return bool(re.match(r'^PART\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|\d+)\s*$', 
                         line.strip(), re.IGNORECASE))


def is_toc_line(line: str) -> bool:
    """Check if line looks like a table of contents entry."""
    # TOC entries typically have Roman numeral followed by period and title
    return bool(re.match(r'^[IVXLC]+\.\s+.+', line.strip()))


def detect_title_author(lines: list) -> tuple:
    """Extract title and author from the beginning of the file."""
    title = None
    author = None
    
    for i, line in enumerate(lines[:10]):  # Check first 10 lines
        line = line.strip()
        if not line:
            continue
        if title is None:
            title = line
        elif author is None and not line.startswith('To '):  # Skip dedication
            author = line
            break
    
    return title, author


def find_toc_bounds(lines: list) -> tuple:
    """Find the start and end of the table of contents."""
    toc_start = None
    toc_end = None
    
    for i, line in enumerate(lines):
        stripped = line.strip().lower()
        if stripped == 'contents':
            toc_start = i
        elif toc_start is not None:
            # Look for "PART ONE" (all caps) which marks the actual body start
            if re.match(r'^PART\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|\d+)$', 
                       line.strip()):
                toc_end = i
                break
    
    return toc_start, toc_end


def find_body_start(lines: list) -> int:
    """Find where the actual body text begins (first all-caps PART heading)."""
    for i, line in enumerate(lines):
        if re.match(r'^PART\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|\d+)$', 
                   line.strip()):
            return i
    return 0


def process_text(text: str) -> str:
    """Process the text and convert to Markdown."""
    # Fix encoding first
    text = fix_encoding(text)
    
    lines = text.split('\n')
    output_lines = []
    
    # Detect title and author
    title, author = detect_title_author(lines)
    
    # Find TOC bounds to skip it
    toc_start, toc_end = find_toc_bounds(lines)
    
    # Find where body actually starts
    body_start = find_body_start(lines)
    
    i = 0
    in_frontmatter = True
    found_first_part = False
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip empty lines at very beginning
        if i == 0 and not stripped:
            i += 1
            continue
        
        # Handle title
        if i == 0 and stripped and title:
            output_lines.append(f'# {title}')
            output_lines.append('')
            i += 1
            continue
        
        # Handle author (second non-empty line)
        if in_frontmatter and stripped == author and i < 5:
            output_lines.append(f'**{author}**')
            output_lines.append('')
            i += 1
            continue
        
        # Skip table of contents section entirely
        if toc_start is not None and toc_end is not None:
            if i >= toc_start and i < toc_end:
                i += 1
                continue
        
        # Handle Part headings (H2) - must be all caps to be body heading
        if re.match(r'^PART\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN|\d+)$', stripped):
            in_frontmatter = False
            found_first_part = True
            # Normalize to title case
            part_text = stripped.title()
            output_lines.append('')
            output_lines.append(f'## {part_text}')
            output_lines.append('')
            i += 1
            continue
        
        # Handle standalone Roman numerals (chapter numbers)
        if is_roman_numeral(stripped) and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            # If next line is non-empty and not another Roman numeral, it's likely the chapter title
            if next_line and not is_roman_numeral(next_line) and not is_part_heading(next_line):
                chapter_num = stripped.upper()
                chapter_title = next_line
                output_lines.append('')
                output_lines.append(f'### {chapter_num}. {chapter_title}')
                output_lines.append('')
                i += 2
                continue
        
        # Handle "Prologue", "Epilogue", or similar standalone section headers
        if stripped.lower() in ('prologue', 'epilogue', 'introduction', 'preface', 'afterword'):
            output_lines.append('')
            output_lines.append(f'### {stripped.title()}')
            output_lines.append('')
            i += 1
            continue
        
        # Handle embedded tales/sub-sections (e.g., "Imel's Tale")
        if re.match(r"^[A-Z][a-z']+('s)?\s+Tale$", stripped):
            output_lines.append('')
            output_lines.append(f'#### {stripped}')
            output_lines.append('')
            i += 1
            continue
        
        # Handle section breaks (*****) 
        if re.match(r'^\*{3,}\s*$', stripped):
            output_lines.append('')
            output_lines.append('---')
            output_lines.append('')
            i += 1
            continue
        
        # Handle epigraph attribution (lines starting with — or enclosed in parens)
        if stripped.startswith('—') or (stripped.startswith('(') and stripped.endswith(')')):
            output_lines.append(f'*{stripped}*')
            i += 1
            continue
        
        # Skip dedication and epigraph section formatting for cleaner output
        if in_frontmatter and not found_first_part:
            # Keep frontmatter as blockquotes
            if stripped.startswith('To ') or stripped.startswith('To the '):
                output_lines.append(f'> {stripped}')
                i += 1
                continue
            # Format epigraph/poetry lines (before TOC)
            if stripped and not is_toc_line(stripped):
                if toc_start is None or i < toc_start:
                    # Check if it's the letter attribution
                    if stripped.startswith('\\x97') or stripped.startswith('—'):
                        output_lines.append(f'> *{stripped}*')
                    else:
                        output_lines.append(f'> {stripped}')
                    i += 1
                    continue
        
        # Regular paragraph text
        if stripped:
            output_lines.append(stripped)
        else:
            output_lines.append('')
        
        i += 1
    
    # Clean up multiple consecutive blank lines
    result = '\n'.join(output_lines)
    result = re.sub(r'\n{3,}', '\n\n', result)
    
    return result.strip() + '\n'


def main():
    if len(sys.argv) < 2:
        print("Usage: python clean_wagner.py input.txt [output.md]")
        print("  If output.md is not specified, writes to input_cleaned.md")
        sys.exit(1)
    
    input_path = Path(sys.argv[1])
    
    if len(sys.argv) >= 3:
        output_path = Path(sys.argv[2])
    else:
        output_path = input_path.with_suffix('.md')
        output_path = output_path.with_stem(input_path.stem + '_cleaned')
    
    # Read input file
    try:
        with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {input_path}")
        sys.exit(1)
    
    # Process text
    result = process_text(text)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)
    
    print(f"Cleaned file written to: {output_path}")


if __name__ == '__main__':
    main()
