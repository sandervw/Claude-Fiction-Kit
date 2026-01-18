"""
Convert a text file to clean markdown format.
- Joins wrapped paragraph lines into single lines
- Formats chapter headers as ## headings
- Adds proper title/author header
"""

import re
import sys
from pathlib import Path


def convert_to_markdown(input_path: str, output_path: str = None):
    with open(input_path, 'r', encoding='utf-8-sig') as f:  # utf-8-sig handles BOM
        content = f.read()

    lines = content.split('\n')

    # Extract title and author from first few lines
    title = None
    author = None
    start_idx = 0

    for i, line in enumerate(lines[:20]):
        stripped = line.strip()
        if not title and stripped and not stripped.startswith('['):
            title = stripped
        elif title and not author and stripped.startswith('By '):
            author = stripped[3:]  # Remove "By "
            start_idx = i + 1
            break
        elif title and not author and stripped and not stripped.startswith('['):
            # Check if it looks like an author line
            if 'Robert' in stripped or 'Howard' in stripped:
                author = stripped.replace('By ', '')
                start_idx = i + 1
                break

    # Skip transcriber notes and find first chapter
    chapter_pattern = re.compile(r'^(\d+)\s+(.+)$')

    for i, line in enumerate(lines[start_idx:], start_idx):
        if chapter_pattern.match(line.strip()):
            start_idx = i
            break

    # Process content - join paragraphs and format chapters
    paragraphs = []
    current_para = []

    for line in lines[start_idx:]:
        stripped = line.strip()

        # Check for chapter heading
        chapter_match = chapter_pattern.match(stripped)
        if chapter_match:
            # Save current paragraph if exists
            if current_para:
                paragraphs.append(' '.join(current_para))
                current_para = []
            # Add chapter heading
            chapter_num, chapter_title = chapter_match.groups()
            paragraphs.append(f"\n## {chapter_num}. {chapter_title}\n")
        elif stripped == '':
            # Empty line - end of paragraph
            if current_para:
                paragraphs.append(' '.join(current_para))
                current_para = []
        else:
            # Continue building paragraph
            current_para.append(stripped)

    # Don't forget last paragraph
    if current_para:
        paragraphs.append(' '.join(current_para))

    # Build final markdown
    md_lines = [
        f"# {title}",
        "",
        f"*{author}*",
        "",
        "---",
        ""
    ]

    for para in paragraphs:
        if para.startswith('\n##'):
            md_lines.append(para.strip())
            md_lines.append("")
        else:
            md_lines.append(para)
            md_lines.append("")

    result = '\n'.join(md_lines)

    # Determine output path
    if output_path is None:
        input_p = Path(input_path)
        output_path = input_p.with_suffix('.md')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"Converted: {input_path} -> {output_path}")
    return output_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python convert_to_markdown.py <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    convert_to_markdown(input_file, output_file)
