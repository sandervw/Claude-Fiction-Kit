"""Generic HTTP fetcher for crawl/convert scripts."""

from __future__ import annotations

import requests

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)


def fetch_html(
    url: str,
    *,
    user_agent: str = DEFAULT_USER_AGENT,
    timeout: int = 20,
    encoding: str | None = None,
) -> str:
    response = requests.get(
        url,
        headers={"User-Agent": user_agent},
        timeout=timeout,
    )
    response.raise_for_status()
    if encoding:
        response.encoding = encoding
    return response.text
