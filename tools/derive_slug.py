#!/usr/bin/env python3
"""
Derive a normalized filename slug from a 21ideas.org (or other) article URL.

Usage (from repo root):
  python3 tools/derive_slug.py "https://21ideas.org/theory/protocol/musig2/"

Convention note (sampled 2026-04-14): many raw/ filenames do not equal the last
segment of their url: field (e.g. book chapters use chapter-N.md while url: uses
cena/N). This tool only reflects the URL path; pick the on-disk filename separately
when those conventions apply.

Requires Python 3.9+ (stdlib only).

Exit status: 0 if a non-empty slug was produced; 1 if the slug is empty after
normalization (e.g. no path segment, or only non-Latin characters with no ASCII left).
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from urllib.parse import unquote, urlparse

# Strip from last path segment before slugify (common static-site suffixes).
_HTML_EXTENSIONS = (".html", ".htm")

# Slug output: raw/ uses ASCII-only stems (no non-Latin characters in filenames).
_MAX_LEN = 60

EXIT_OK = 0
EXIT_EMPTY_SLUG = 1

_EMPTY_WARNING = (
    "Warning: slug is empty after normalization — provide filename manually"
)


def _strip_html_extension(segment: str) -> str:
    low = segment.lower()
    for ext in _HTML_EXTENSIONS:
        if low.endswith(ext):
            return segment[: -len(ext)]
    return segment


def _slugify_segment(segment: str) -> str:
    """
    Lowercase ASCII slug: keep [a-z0-9-], fold Latin accents (NFKD), map everything
    else to hyphens (non-Latin letters become separators, matching no Cyrillic in
    existing raw/ stems).
    """
    segment = unicodedata.normalize("NFKD", segment)
    segment = "".join(ch for ch in segment if not unicodedata.combining(ch))
    out: list[str] = []
    for ch in segment.lower():
        if ch.isascii() and (ch.isalnum() or ch == "-"):
            out.append(ch)
        else:
            out.append("-")
    s = "".join(out)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def _truncate_hyphen_boundary(s: str, max_len: int = _MAX_LEN) -> str:
    if len(s) <= max_len:
        return s
    window = s[:max_len]
    last_hyp = window.rfind("-")
    if last_hyp > 0:
        return window[:last_hyp]
    return window[:max_len]


def derive_slug(url: str) -> str:
    parsed = urlparse(url.strip())
    path = unquote(parsed.path or "")
    path = path.rstrip("/")
    segments = [seg for seg in path.split("/") if seg]
    if not segments:
        return ""
    last = _strip_html_extension(segments[-1])
    slug = _slugify_segment(last)
    return _truncate_hyphen_boundary(slug)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Derive a normalized filename slug from a URL path."
    )
    parser.add_argument(
        "url",
        help="Article URL (path's last segment is used)",
    )
    args = parser.parse_args(argv)
    slug = derive_slug(args.url)
    print(slug)
    if not slug:
        print(_EMPTY_WARNING, file=sys.stderr)
        return EXIT_EMPTY_SLUG
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())

# -----------------------------------------------------------------------------
# Tests (2026-04-14): five real url: paths from raw/ expressed as 21ideas.org URLs.
# Commands run from repo root; stdout is the slug printed on one line.
#
# $ python3 tools/derive_slug.py "https://21ideas.org/musig2"
# musig2
#
# $ python3 tools/derive_slug.py "https://21ideas.org/taproot"
# taproot
#
# $ python3 tools/derive_slug.py "https://21ideas.org/seed-security"
# seed-security
#
# $ python3 tools/derive_slug.py "https://21ideas.org/pzv/bitkoin-ne-dlya-prestupnikov"
# bitkoin-ne-dlya-prestupnikov
#
# $ python3 tools/derive_slug.py "https://21ideas.org/sr/silkroad-1"
# silkroad-1
#
# Edge-case spot checks:
# $ python3 tools/derive_slug.py "https://21ideas.org/theory/protocol/musig2/?x=1#sec"
# musig2
#
# $ python3 tools/derive_slug.py "https://21ideas.org/article-name.html"
# article-name
#
# Empty slug (stderr warning, exit 1): e.g. https://21ideas.org/ or path segment
# with no ASCII letters/digits after normalization.
