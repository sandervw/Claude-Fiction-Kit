"""
Shared file I/O helpers for converter scripts.

Provides project-root resolution, input/output path conventions,
and a summary printer. Think of it as the plumbing that every
converter shares so they only have to worry about the transformation.
"""

from __future__ import annotations

from pathlib import Path


def get_project_root(anchor: str | Path = __file__, levels_up: int = 3) -> Path:
    """Resolve the project root by walking up from an anchor file.

    Args:
        anchor: The file to start from (typically __file__ of the caller).
        levels_up: How many parent directories to traverse.
    """
    return Path(anchor).resolve().parents[levels_up - 1]


def resolve_paths(
    filename: str,
    output_path: str | None = None,
    *,
    input_dir: str = "input",
    output_dir: str = "output",
    output_suffix: str = ".md",
    project_root: Path | None = None,
    anchor: str | Path = __file__,
    levels_up: int = 3,
) -> tuple[Path, Path]:
    """Resolve input and output file paths using project conventions.

    Returns (input_file, output_file). Raises FileNotFoundError if
    the input file does not exist.
    """
    root = project_root or get_project_root(anchor, levels_up)
    input_file = root / input_dir / filename

    if not input_file.exists():
        raise FileNotFoundError(f"File not found: {input_file}")

    if output_path is None:
        output_file = root / output_dir / input_file.with_suffix(output_suffix).name
    else:
        output_file = Path(output_path)

    return input_file, output_file


def read_file(path: Path, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as f:
        return f.read()


def write_file(path: Path, content: str, encoding: str = "utf-8") -> None:
    with open(path, "w", encoding=encoding) as f:
        f.write(content)


def print_summary(
    input_name: str,
    output_name: str,
    content_length: int,
    deleted: bool = False,
    **extra: str,
) -> None:
    """Print a short conversion summary to stdout."""
    print(f"Converted: {input_name} -> {output_name}")
    for label, value in extra.items():
        label_clean = label.replace("_", " ").title()
        print(f"{label_clean}: {value}")
    print(f"Output size: {content_length:,} characters")
    if deleted:
        print(f"Deleted: {input_name}")
