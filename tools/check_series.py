#!/usr/bin/env python3
"""
Detect whether a raw/ article belongs to a series and list sibling parts on disk.

Usage (from repo root):
  python3 tools/check_series.py raw/Theory/economics/gradually-then-suddenly/03-bitcoin-is-not-too-volatile.md

Directory-only heuristics apply only when at least two sibling files share the same
numbered pattern (avoids false positives from a lone `21-*.md`-style name).

Requires Python 3.9+ (stdlib only).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Repo root = parent of tools/
ROOT = Path(__file__).resolve().parent.parent

# Filename: ...-N.md (trailing segment is digits)
_RE_SUFFIX_PART = re.compile(r"^(.+)-(\d+)$")

# Filename: NN-rest.md (Hugo-style chapter index)
_RE_PREFIX_PART = re.compile(r"^(\d{2})-(.+)$")

# Title / h1 (Russian + English)
_RE_CHAST_NUM = re.compile(r"(?:^|[\s.])Часть\s+(\d+)", re.IGNORECASE)
_RE_CHAST_ROMAN = re.compile(r"(?:^|[\s.])Часть\s+([IVX]+)\b", re.IGNORECASE)
_RE_PART_EN = re.compile(r"\bPart\s+(\d+)\b", re.IGNORECASE)
_RE_PART_EN_ROMAN = re.compile(r"\bPart\s+([IVX]+)\b", re.IGNORECASE)
_RE_NUM_CHAST = re.compile(r"(\d+)\s+часть\b", re.IGNORECASE)

_ROMAN_TO_INT = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6,
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    "X": 10,
    "XI": 11,
    "XII": 12,
}

# Body navigation hints
_RE_PREV_NEXT = re.compile(r"^\s*(Previous|Next)\s*:", re.IGNORECASE | re.MULTILINE)


def _strip_yaml_scalar(s: str) -> str:
    s = s.strip()
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    return s


def _parse_frontmatter_block(content: str) -> tuple[dict[str, str], str]:
    """Return (key -> raw value string, body after closing ---)."""
    if not content.startswith("---"):
        return {}, content
    lines = content.splitlines()
    if len(lines) < 2 or lines[0].strip() != "---":
        return {}, content
    end: int | None = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, content
    fm: dict[str, str] = {}
    for line in lines[1:end]:
        m = re.match(r"^([a-zA-Z0-9_]+)\s*:\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1).lower(), m.group(2).rstrip()
        fm[key] = val
    body = "\n".join(lines[end + 1 :])
    return fm, body


def _parse_int_loose(s: str) -> int | None:
    s = _strip_yaml_scalar(s.strip())
    if not s:
        return None
    if s.isdigit():
        return int(s)
    ru = _ROMAN_TO_INT.get(s.upper())
    if ru is not None:
        return ru
    return None


def _extract_title_h1(fm: dict[str, str]) -> str:
    parts = []
    for key in ("title", "h1"):
        if key in fm:
            parts.append(_strip_yaml_scalar(fm[key]))
    return " ".join(parts)


def _part_from_titles(text: str) -> int | None:
    for rx in (_RE_CHAST_NUM, _RE_PART_EN, _RE_NUM_CHAST):
        m = rx.search(text)
        if m:
            return int(m.group(1))
    for rx in (_RE_CHAST_ROMAN, _RE_PART_EN_ROMAN):
        m = rx.search(text)
        if m:
            r = m.group(1).upper()
            if r in _ROMAN_TO_INT:
                return _ROMAN_TO_INT[r]
    return None


def _collect_prefix_parts(directory: Path) -> list[int]:
    out: list[int] = []
    for p in sorted(directory.glob("*.md")):
        if p.name == "_index.md":
            continue
        m = _RE_PREFIX_PART.match(p.stem)
        if m:
            out.append(int(m.group(1)))
    return sorted(set(out))


def _collect_suffix_parts(directory: Path, base: str) -> list[int]:
    out: list[int] = []
    for p in sorted(directory.glob("*.md")):
        if p.name == "_index.md":
            continue
        m = re.match(rf"^{re.escape(base)}-(\d+)\.md$", p.name)
        if m:
            out.append(int(m.group(1)))
    return sorted(set(out))


def _format_int_list(nums: list[int]) -> str:
    return ", ".join(str(n) for n in nums)


def _missing_in_span(found: list[int]) -> tuple[list[int], int | None, int | None]:
    if not found:
        return [], None, None
    lo, hi = min(found), max(found)
    missing = [i for i in range(lo, hi + 1) if i not in found]
    return missing, lo, hi


def _unique_suffix_bases(directory: Path) -> set[str]:
    bases: set[str] = set()
    for p in directory.glob("*.md"):
        if p.name == "_index.md":
            continue
        m = _RE_SUFFIX_PART.match(p.stem)
        if m:
            bases.add(m.group(1))
    return bases


def analyze(path: Path) -> tuple[str, int]:
    """
    Return (report text, exit code). Exit code always 0 except read errors.
    """
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as e:
        return f"ERROR: cannot read file: {e}", 0

    fm, body = _parse_frontmatter_block(content)
    stem = path.stem
    parent_name = path.parent.name

    series_key = fm.get("series")
    part_key = fm.get("part")

    this_part: int | None = None
    base_slug: str | None = None
    suffix_base: str | None = None
    mode: str | None = None
    signals: list[str] = []

    # 1) Explicit frontmatter series: + part:
    if series_key is not None and part_key is not None:
        series_val = _strip_yaml_scalar(series_key.strip())
        this_part = _parse_int_loose(part_key)
        signals.append("frontmatter series:/part:")
        pp = _collect_prefix_parts(path.parent)
        sp = _collect_suffix_parts(path.parent, series_val)
        if len(pp) >= len(sp):
            mode = "prefix"
            base_slug = parent_name
        else:
            mode = "suffix"
            suffix_base = series_val
            base_slug = series_val

    # 2) Filename suffix ...-<n>
    if mode is None:
        m = _RE_SUFFIX_PART.match(stem)
        if m:
            suffix_base = m.group(1)
            base_slug = suffix_base
            this_part = int(m.group(2))
            mode = "suffix"
            signals.append("filename ...-<n>")

    # 3) Filename prefix NN-...
    if mode is None:
        m = _RE_PREFIX_PART.match(stem)
        if m:
            this_part = int(m.group(1))
            base_slug = parent_name
            mode = "prefix"
            signals.append("filename NN-...")

    titles = _extract_title_h1(fm)

    # 4) Title / h1
    if this_part is None:
        p = _part_from_titles(titles)
        if p is not None:
            this_part = p
            base_slug = parent_name
            if mode is None:
                mode = "prefix"
            signals.append("title/h1 part")

    # 5) Body Previous:/Next: — only if it helps set mode
    prev_next = bool(_RE_PREV_NEXT.search(body))
    if prev_next and mode is None:
        pp = _collect_prefix_parts(path.parent)
        if len(pp) >= 2:
            mode = "prefix"
            base_slug = base_slug or parent_name
            signals.append("body Previous/Next")
        else:
            bases = _unique_suffix_bases(path.parent)
            if len(bases) == 1:
                sb = bases.pop()
                if len(_collect_suffix_parts(path.parent, sb)) >= 2:
                    suffix_base = sb
                    base_slug = suffix_base
                    mode = "suffix"
                    signals.append("body Previous/Next")

    # 6) Directory pattern (siblings) when mode still unset — require 2+ parts
    #    so a lone `21-foo.md`-style name does not imply a series for neighbors.
    if mode is None:
        pp = _collect_prefix_parts(path.parent)
        if len(pp) >= 2:
            mode = "prefix"
            base_slug = parent_name
            p2 = _part_from_titles(titles)
            if p2 is not None:
                this_part = p2
            signals.append("directory pattern (prefix)")
        else:
            bases = _unique_suffix_bases(path.parent)
            if len(bases) == 1:
                sb = bases.pop()
                sp = _collect_suffix_parts(path.parent, sb)
                if len(sp) >= 2:
                    suffix_base = sb
                    base_slug = suffix_base
                    mode = "suffix"
                    p2 = _part_from_titles(titles)
                    if p2 is not None:
                        this_part = p2
                    signals.append("directory pattern (suffix)")

    if mode is None:
        return "NO_SERIES", 0

    if mode == "prefix":
        parts_found = _collect_prefix_parts(path.parent)
        eff_base = base_slug or parent_name
    else:
        sb = suffix_base or base_slug
        if sb is None:
            return "NO_SERIES", 0
        parts_found = _collect_suffix_parts(path.parent, sb)
        eff_base = sb

    missing, lo, hi = _missing_in_span(parts_found)

    hub = path.parent / "_index.md"
    hub_line = (
        f"Suggested hub file: {hub.relative_to(ROOT)}"
        if hub.is_file()
        else "Suggested hub file: (none — _index.md not found)"
    )

    lines = [
        "SERIES_DETECTED",
        f"Base: {eff_base}",
        f"This part: {this_part if this_part is not None else 'unknown'}",
        f"Parts found in raw/: {_format_int_list(parts_found)}",
    ]

    if missing:
        lines.append(
            f"Possibly missing (gaps within {lo}–{hi}): {_format_int_list(missing)}"
        )
    elif hi is not None:
        lines.append(
            f"Possibly missing: {hi + 1}, {hi + 2}, ... "
            "(unknown total — check source)"
        )
    else:
        lines.append("Possibly missing: ... (unknown total — check source)")

    lines.append(hub_line)
    lines.append(f"Signals: {', '.join(signals)}")

    return "\n".join(lines), 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Detect series membership for a raw/ markdown file."
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to a .md file under raw/",
    )
    args = parser.parse_args(argv)

    path = args.path
    if not path.is_file():
        print(f"ERROR: not a file: {path}", file=sys.stderr)
        return 1
    try:
        path.resolve().relative_to(ROOT / "raw")
    except ValueError:
        print("ERROR: path must be under raw/", file=sys.stderr)
        return 1

    report, code = analyze(path.resolve())
    print(report)
    return code


if __name__ == "__main__":
    raise SystemExit(main())

# -----------------------------------------------------------------------------
# Spot checks (2026-04-14), run from repo root:
#
# gradually-then-suddenly (NN-*.md): part 3; gap at 16 vs 1–17 on disk.
# discovering-bitcoin: parts 0–7; tail unknown after 7.
# genesis-files / silk-road: suffix base-*-<n>.md; intro uses directory suffix heuristic.
# Standalone article in a mixed folder: NO_SERIES (needs 2+ sibling numbered files).
