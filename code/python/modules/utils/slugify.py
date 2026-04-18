"""Derive filesystem-safe slugs from URLs or arbitrary strings."""

from __future__ import annotations

import re
from urllib.parse import urlparse


def url_to_slug(url: str, fallback: str = "page") -> str:
    path = urlparse(url).path.rstrip("/")
    segment = path.rsplit("/", 1)[-1] if path else ""
    return slugify(segment) or fallback


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
