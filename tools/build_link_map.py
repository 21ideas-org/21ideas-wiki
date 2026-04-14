#!/usr/bin/env python3
"""
Generate static wikilink maps for the EN and RU layers.

Usage:
  python3 tools/build_link_map.py
  python3 tools/build_link_map.py --layer en
  python3 tools/build_link_map.py --layer ru
  python3 tools/build_link_map.py --dry-run
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence, Set, Tuple


@dataclass(frozen=True)
class Entry:
    term: str
    link: str
    label: Optional[str] = None  # e.g. "glossary"

    def to_line(self) -> str:
        if self.label:
            return f"{self.term} → {self.link} [{self.label}]"
        return f"{self.term} → {self.link}"


FRONTMATTER_BOUNDARY = "---"
EXCLUDE_FILENAMES = {"index.md", "overview.md", "glossary.md"}


def heading_to_anchor(heading_text: str) -> str:
    # Strip markdown formatting (bold, italic, backticks)
    text = re.sub(r"[*_`]", "", heading_text)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)  # strip non-alphanumeric except hyphen
    text = re.sub(r"\s+", "-", text.strip())
    return text


def _strip_inline_md(text: str) -> str:
    # Intentionally conservative: just remove common inline formatting markers.
    # (Anchor generation uses heading_to_anchor(), which does the same removal step.)
    return re.sub(r"[*_`]", "", text).strip()


def _read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _extract_frontmatter_block(markdown: str) -> Optional[str]:
    lines = markdown.splitlines()
    if not lines:
        return None
    if lines[0].strip() != FRONTMATTER_BOUNDARY:
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == FRONTMATTER_BOUNDARY:
            return "\n".join(lines[1:i])
    return None


def _parse_title_from_frontmatter(frontmatter: str) -> Optional[str]:
    # Minimal YAML parsing: locate a top-level "title:" scalar.
    for raw_line in frontmatter.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if not line.lower().startswith("title:"):
            continue
        value = line.split(":", 1)[1].strip()
        if not value:
            return None
        # Remove surrounding single/double quotes if present.
        if (value.startswith('"') and value.endswith('"')) or (
            value.startswith("'") and value.endswith("'")
        ):
            value = value[1:-1]
        return value.strip()
    return None


def iter_dedicated_pages(layer_dir: str) -> Iterable[Tuple[str, str, str]]:
    """
    Yield (title, category, slug) for markdown files under layer_dir that are
    in a category subdirectory (e.g. concepts/foo.md).
    """
    for root, _dirs, files in os.walk(layer_dir):
        for filename in files:
            if not filename.endswith(".md"):
                continue
            if filename in EXCLUDE_FILENAMES:
                continue

            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, layer_dir)

            parts = rel_path.split(os.sep)
            # Only include pages under a category directory: <category>/<slug>.md
            if len(parts) != 2:
                continue

            category = parts[0]
            slug = os.path.splitext(parts[1])[0]

            markdown = _read_text(full_path)
            fm = _extract_frontmatter_block(markdown)
            if fm is None:
                continue
            title = _parse_title_from_frontmatter(fm)
            if not title:
                continue

            yield (title, category, slug)


def iter_glossary_h3_terms(glossary_path: str) -> Iterable[str]:
    """
    Extract every level-3 heading (###) from the glossary as a term.
    """
    for raw_line in _read_text(glossary_path).splitlines():
        line = raw_line.rstrip()
        if not line.startswith("###"):
            continue
        # Require exactly "### " (avoid treating "####" as level-3).
        if not line.startswith("### "):
            continue
        heading = line[4:].strip()
        if not heading:
            continue
        yield _strip_inline_md(heading)


def build_entries_for_layer(repo_root: str, layer: str) -> List[Entry]:
    if layer not in {"en", "ru"}:
        raise ValueError(f"Unsupported layer: {layer}")

    layer_dir = os.path.join(repo_root, f"wiki-{layer}")
    glossary_path = os.path.join(layer_dir, "glossary.md")

    prefix = layer  # wikilink prefix: en or ru
    entries: List[Entry] = []

    for title, category, slug in iter_dedicated_pages(layer_dir):
        link = f"[[{prefix}/{category}/{slug}|{title}]]"
        entries.append(Entry(term=title, link=link))

    for heading in iter_glossary_h3_terms(glossary_path):
        anchor = heading_to_anchor(heading)
        link = f"[[{prefix}/glossary#{anchor}|{heading}]]"
        entries.append(Entry(term=heading, link=link, label="glossary"))

    entries.sort(key=lambda e: e.term.casefold())
    return entries


def render_markdown(layer: str, entries: Sequence[Entry]) -> str:
    layer_label = "EN" if layer == "en" else "RU"
    header = "\n".join(
        [
            f"# Link map — {layer_label} layer",
            "_Generated by tools/build_link_map.py — do not edit manually._",
            "_Regenerate after any ingest, enhance, or update pass: python3 tools/build_link_map.py_",
            "",
            "Agents: for each term, use the dedicated page link on first mention.",
            "Use the [glossary] entry for a meaningful second mention in a different",
            "## section where the term is being defined or explained in detail.",
            "Do not repeat the same link more than twice on one page.",
            "",
        ]
    )
    body = "\n".join(e.to_line() for e in entries)
    return header + body + "\n"


def write_or_print(path: str, content: str, dry_run: bool) -> None:
    if dry_run:
        sys.stdout.write(content)
        if not content.endswith("\n"):
            sys.stdout.write("\n")
        return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate link-map markdown files.")
    p.add_argument(
        "--layer",
        choices=["en", "ru"],
        help="Regenerate a single layer only.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print output to stdout, do not write files.",
    )
    return p.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    layers = [args.layer] if args.layer else ["en", "ru"]

    for layer in layers:
        entries = build_entries_for_layer(repo_root=repo_root, layer=layer)
        content = render_markdown(layer, entries)

        out_path = os.path.join(repo_root, "docs", f"link-map-{layer}.md")
        write_or_print(out_path, content, dry_run=args.dry_run)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

