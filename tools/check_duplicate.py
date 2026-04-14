#!/usr/bin/env python3
"""
Before ingesting a new raw/ file, check for duplicate URLs or slug path conflicts.

Usage (from repo root):
  python3 tools/check_duplicate.py --url "https://21ideas.org/..."
  python3 tools/check_duplicate.py --url "https://..." --slug my-article --subdir "Theory/protocol"

Invariant verified 2026-04-14: all raw/ files use a standalone top-level url: field; no nested or sources:-array URLs exist in this tree.

Requires Python 3.9+ (stdlib only).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

# Repo root = parent of tools/
ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"

EXIT_CLEAR = 0
EXIT_DUPLICATE_URL = 1
EXIT_SLUG_CONFLICT = 2


def _normalize_url_value(value: str) -> str:
    """
    Normalize a url: field or --url argument for comparison.
    Case-insensitive; ignores a trailing slash on the path.
    Full URLs: compare by URL path (no scheme/host/query/fragment).
    Non-URL strings: treat as a site path (e.g. taproot, sb/stanovlenie-1).
    """
    s = value.strip()
    if not s:
        return ""
    low = s.lower()
    if low.startswith("http://") or low.startswith("https://"):
        parsed = urlparse(s)
        path = (parsed.path or "/").strip("/")
        return path.lower()
    return s.rstrip("/").lower()


def _extract_url_from_frontmatter(content: str) -> str | None:
    """Return the first `url:` value in YAML frontmatter, or None if absent."""
    if not content.startswith("---"):
        return None
    lines = content.splitlines()
    if len(lines) < 2 or lines[0].strip() != "---":
        return None
    end: int | None = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None
    for line in lines[1:end]:
        m = re.match(r"^\s*url:\s*(.+?)\s*$", line)
        if not m:
            continue
        val = m.group(1).strip()
        if (
            (val.startswith('"') and val.endswith('"'))
            or (val.startswith("'") and val.endswith("'"))
        ) and len(val) >= 2:
            val = val[1:-1]
        return val if val else None
    return None


def _iter_raw_markdown_files() -> list[Path]:
    if not RAW.is_dir():
        return []
    return sorted(RAW.rglob("*.md"))


def _find_duplicate_url(
    normalized_target: str,
) -> Path | None:
    if not normalized_target:
        return None
    for path in _iter_raw_markdown_files():
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        raw_url = _extract_url_from_frontmatter(text)
        if raw_url is None:
            continue
        if _normalize_url_value(raw_url) == normalized_target:
            return path
    return None


def _slug_target_path(slug: str, subdir: str | None) -> Path:
    parts: list[str] = []
    if subdir:
        parts.extend(Path(subdir.replace("\\", "/")).parts)
    parts.append(f"{slug}.md")
    return RAW.joinpath(*parts)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check raw/ for duplicate url: or slug path before ingest."
    )
    parser.add_argument(
        "--url",
        required=True,
        help="Canonical article URL (or path) to compare against url: fields",
    )
    parser.add_argument(
        "--slug",
        default=None,
        help="Proposed filename without .md (optional)",
    )
    parser.add_argument(
        "--subdir",
        default=None,
        help='Target subdirectory under raw/, e.g. "Theory/protocol" (optional)',
    )
    args = parser.parse_args(argv)

    if not RAW.is_dir():
        print("ERROR: raw/ not found (run from repo root)", file=sys.stderr)
        return 1

    normalized = _normalize_url_value(args.url)
    dup = _find_duplicate_url(normalized)
    if dup is not None:
        rel = dup.relative_to(ROOT)
        print(f"DUPLICATE: {rel}")
        return EXIT_DUPLICATE_URL

    if args.slug:
        target = _slug_target_path(args.slug, args.subdir)
        if target.is_file():
            rel = target.relative_to(ROOT)
            print(f"SLUG_CONFLICT: {rel}")
            return EXIT_SLUG_CONFLICT

    print("CLEAR")
    return EXIT_CLEAR


if __name__ == "__main__":
    raise SystemExit(main())

# -----------------------------------------------------------------------------
# Manual test run (2026-04-14) against repo raw/ frontmatter:
#
# Verified url: extraction (first line of each file is the frontmatter key):
#   raw/Theory/protocol/taproot.md                    -> url: taproot
#   raw/Theory/economics/discovering-bitcoin/01-about-time.md -> url: sb/stanovlenie-1
#   raw/Start/bitcoin-myths.md                        -> url: bitcoin-myths
#
# $ python3 tools/check_duplicate.py --url "https://21ideas.org/taproot"
# DUPLICATE: raw/Theory/protocol/taproot.md
# (exit code 1)
#
# $ python3 tools/check_duplicate.py --url "https://21ideas.org/sb/stanovlenie-1"
# DUPLICATE: raw/Theory/economics/discovering-bitcoin/01-about-time.md
# (exit code 1)
#
# $ python3 tools/check_duplicate.py --url "https://21ideas.org/bitcoin-myths"
# DUPLICATE: raw/Start/bitcoin-myths.md
# (exit code 1)
#
# $ python3 tools/check_duplicate.py --url "https://21ideas.org/this-url-does-not-exist-in-raw-xyz"
# CLEAR
# (exit code 0)
#
# $ python3 tools/check_duplicate.py --url "https://21ideas.org/this-url-does-not-exist-in-raw-xyz" --slug taproot --subdir "Theory/protocol"
# SLUG_CONFLICT: raw/Theory/protocol/taproot.md
# (exit code 2)
