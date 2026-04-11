#!/usr/bin/env python3
"""
Mechanical lint for wiki-en/ and wiki-ru/ (21ideas Bitcoin Wiki).

Usage:
  python3 tools/lint.py                  # both layers, stdout only
  python3 tools/lint.py --layer ru       # wiki-ru only
  python3 tools/lint.py --layer en       # wiki-en only
  python3 tools/lint.py --write-report   # overwrite docs/lint-report.md
  python3 tools/lint.py --strict         # exit 1 if any issue is found

Keep checks aligned with CLAUDE.md → Lint (mechanical checks).
Requires Python 3.9+ (stdlib only).

When using --write-report, docs/lint-report.md is written in English (section titles,
table headers, follow-ups). File paths and quoted tuples may contain non-English text
from the vault.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

# Repo root = parent of tools/
ROOT = Path(__file__).resolve().parent.parent

ALLOW_TAGS = frozenset(
    {
        "bitcoin",
        "wiki",
        "concept",
        "entity",
        "glossary",
        "protocol",
        "economics",
        "history",
        "philosophy",
        "security",
        "privacy",
        "governance",
        "scaling",
        "mining",
        "synthesized",
        "reference",
        "stub",
        "utxo",
        "lightning",
        "bip",
        "node",
        "fork",
        "censorship-resistance",
        "decentralization",
        "double-spend",
        "difficulty-adjustment",
        "third-party",
        "whitepaper",
        "aml",
        "addresses",
        "multisig",
        "taproot",
        "segwit",
    }
)

REQUIRED_FM_KEYS = frozenset(
    {
        "title",
        "category",
        "quality",
        "sources",
        "synthesized_date",
        "completeness",
        "language",
        "tags",
    }
)

HUB_FILES = frozenset({"index.md", "overview.md"})


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter_inner, body) or (None, full_text) if no FM."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


def fm_keys(fm_raw: str) -> set[str]:
    keys: set[str] = set()
    for line in fm_raw.splitlines():
        m = re.match(r"^([a-z_]+):\s*", line)
        if m:
            keys.add(m.group(1))
    return keys


def fm_line_value(fm_raw: str, key: str) -> str | None:
    for line in fm_raw.splitlines():
        m = re.match(rf"^{key}:\s*(.*)$", line)
        if m:
            return m.group(1).strip()
    return None


def is_block_sources(fm_raw: str) -> bool:
    if re.search(r"^sources:\s*\n\s*-\s", fm_raw, re.MULTILINE):
        return True
    seen = False
    for line in fm_raw.splitlines():
        if line.strip() == "sources:":
            seen = True
            continue
        if seen:
            if line.strip().startswith("- "):
                return True
            break
    return False


def parse_tags_flow(fm_raw: str) -> list[str] | None:
    m = re.search(r"^tags:\s*(.+)$", fm_raw, re.MULTILINE)
    if not m:
        return None
    tl = m.group(1).strip()
    if not tl.startswith("["):
        return None
    inner = tl.strip("[]")
    out: list[str] = []
    for t in re.split(r",\s*", inner):
        t = t.strip().strip("\"'")
        if t:
            out.append(t)
    return out


def bad_tags_for_fm(fm_raw: str) -> list[str]:
    tags = parse_tags_flow(fm_raw)
    if not tags:
        return []
    return [t for t in tags if t not in ALLOW_TAGS]


def lint_layer(layer: str) -> dict:
    """layer is 'wiki-en' or 'wiki-ru'. Returns structured results."""
    wiki_root = ROOT / layer
    prefix = "en" if layer == "wiki-en" else "ru"
    wrong = []
    if layer == "wiki-ru":
        wrong = [
            (r"\[\[wiki-ru/[^\]]+\]\]", "bad_wiki_ru_prefix"),
            (r"\[\[wiki-en/[^\]]+\]\]", "bad_wiki_en_prefix"),
            (r"\[\[en/[^\]]+\]\]", "wrong_layer_en_link"),
        ]
    else:
        wrong = [
            (r"\[\[wiki-en/[^\]]+\]\]", "bad_wiki_en_prefix"),
            (r"\[\[wiki-ru/[^\]]+\]\]", "bad_wiki_ru_prefix"),
            (r"\[\[ru/[^\]]+\]\]", "wrong_layer_ru_link"),
        ]

    all_pages = {p.relative_to(wiki_root).as_posix() for p in wiki_root.rglob("*.md")}
    link_re = re.compile(
        rf"\[\[{re.escape(prefix)}/([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]"
    )

    results: dict = {
        "layer": layer,
        "pages": 0,
        "bad_links": [],
        "broken_targets": [],
        "raw_in_body": [],
        "body_hr": [],
        "body_h1": [],
        "sources_block": [],
        "missing_fm": [],
        "missing_keys": [],
        "bad_tag_rows": [],
        "missing_reviewed": [],
        "wrong_lang": [],
    }

    for path in sorted(wiki_root.rglob("*.md")):
        results["pages"] += 1
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        fm_raw, body = split_frontmatter(text)

        if fm_raw is None:
            if path.name not in HUB_FILES:
                results["missing_fm"].append(rel)
            continue

        for pattern, _kind in wrong:
            for m in re.finditer(pattern, body):
                results["bad_links"].append((rel, m.group(0)))

        for line in body.splitlines():
            if "raw/" in line:
                results["raw_in_body"].append((rel, line.strip()[:100]))

        if any(re.match(r"^---\s*$", ln) for ln in body.splitlines()):
            results["body_hr"].append(rel)

        blines = [ln for ln in body.splitlines() if ln.strip()]
        if blines:
            first = blines[0].lstrip()
            if first.startswith("# ") and not first.startswith("##"):
                results["body_h1"].append((rel, first[:70]))

        if is_block_sources(fm_raw):
            results["sources_block"].append(rel)

        if path.name in HUB_FILES:
            continue

        keys = fm_keys(fm_raw)
        miss = REQUIRED_FM_KEYS - keys
        if miss:
            results["missing_keys"].append((rel, sorted(miss)))

        exp_lang = "en" if layer == "wiki-en" else "ru"
        lang = fm_line_value(fm_raw, "language")
        if lang is not None and lang.strip("\"'") != exp_lang:
            results["wrong_lang"].append((rel, lang))

        if "reviewed" not in keys:
            results["missing_reviewed"].append(rel)

        for t in bad_tags_for_fm(fm_raw):
            results["bad_tag_rows"].append((rel, t))

        for m in link_re.finditer(body):
            tgt = m.group(1).rstrip("/")
            if not tgt.endswith(".md"):
                tgt = f"{tgt}.md"
            if tgt not in all_pages:
                results["broken_targets"].append((rel, m.group(0), tgt))

    return results


def count_issues(r: dict) -> int:
    n = 0
    for k, v in r.items():
        if k in ("layer", "pages"):
            continue
        if isinstance(v, list):
            n += len(v)
    return n


def severity_error(r: dict) -> bool:
    """True if link discipline or broken graph targets exist."""
    return bool(r["bad_links"] or r["broken_targets"])


def format_report_md(results: list[dict], scope: str) -> str:
    """Build docs/lint-report.md body: English prose and labels only."""
    today = dt.date.today().isoformat()
    lines = [
        "# Lint report — 21ideas Bitcoin Wiki",
        "",
        f"_Last pass: {today} ({scope})_",
        "",
        "## Summary",
        "",
        "| Layer | Pages | Bad wikilink prefix | Broken targets | Block `sources:` | Body `---` | Body `#` | `raw/` in body | Missing FM keys | Missing `reviewed` | Off-allowlist tags |",
        "|-------|------:|--------------------:|---------------:|-----------------:|----------:|---------:|---------------:|----------------:|-------------------:|-------------------:|",
    ]
    for r in results:
        lines.append(
            "| {layer} | {pages} | {bad} | {brk} | {src} | {hr} | {h1} | {raw} | {mk} | {rev} | {tags} |".format(
                layer=r["layer"],
                pages=r["pages"],
                bad=len(r["bad_links"]),
                brk=len(r["broken_targets"]),
                src=len(r["sources_block"]),
                hr=len(r["body_hr"]),
                h1=len(r["body_h1"]),
                raw=len(r["raw_in_body"]),
                mk=len(r["missing_keys"]),
                rev=len(r["missing_reviewed"]),
                tags=len(r["bad_tag_rows"]),
            )
        )
    lines.extend(
        [
            "",
            "## Detail (by layer)",
            "",
        ]
    )
    for r in results:
        lines.append(f"### `{r['layer']}/`")
        lines.append("")
        for label, key in [
            ("Invalid cross-prefix / layer wikilinks", "bad_links"),
            ("Broken wikilink targets", "broken_targets"),
            ("`raw/` in body", "raw_in_body"),
            ("Standalone `---` in body", "body_hr"),
            ("`#` as first body heading", "body_h1"),
            ("Block / list `sources:`", "sources_block"),
            ("Missing / bad frontmatter", "missing_fm"),
            ("Missing required YAML keys", "missing_keys"),
            ("Missing `reviewed`", "missing_reviewed"),
            ("Wrong `language`", "wrong_lang"),
            ("Tags outside allowlist", "bad_tag_rows"),
        ]:
            items = r[key]
            if not items:
                continue
            lines.append(f"- **{label}** ({len(items)}):")
            cap = 40
            for item in items[:cap]:
                lines.append(f"  - `{item}`")
            if len(items) > cap:
                lines.append(f"  - … +{len(items) - cap} more")
            lines.append("")
    lines.extend(
        [
            "## Suggested follow-ups",
            "",
            "- Orphans / `index.md` coverage: not implemented in this tool (human review).",
            "- Scalar quoting in frontmatter: only partially enforceable; fix by hand or extend the tool.",
            "- After mechanical fixes, re-run with `--write-report` and append `docs/log.md` per CLAUDE.md.",
            "",
        ]
    )
    return "\n".join(lines)


def print_stdout(results: list[dict]) -> None:
    for r in results:
        print(f"=== {r['layer']}/ ({r['pages']} pages) ===")
        errs = severity_error(r)
        if errs:
            print("  STATUS: errors (bad or broken wikilinks)")
        else:
            print("  STATUS: no wikilink errors")
        n = count_issues(r)
        print(f"  Total flagged rows: {n}")
        if r["bad_links"]:
            print("  bad_links:", len(r["bad_links"]))
        if r["broken_targets"]:
            print("  broken_targets:", len(r["broken_targets"]))
        if r["sources_block"]:
            print("  sources_block:", len(r["sources_block"]))
        if r["body_hr"]:
            print("  body_hr files:", len(r["body_hr"]))
        if r["body_h1"]:
            print("  body_h1:", len(r["body_h1"]))
        if r["raw_in_body"]:
            print("  raw_in_body:", len(r["raw_in_body"]))
        if r["missing_fm"]:
            print("  missing_fm:", len(r["missing_fm"]))
        if r["missing_keys"]:
            print("  missing_keys:", len(r["missing_keys"]))
        if r["missing_reviewed"]:
            print("  missing_reviewed:", len(r["missing_reviewed"]))
        if r["wrong_lang"]:
            print("  wrong_lang:", len(r["wrong_lang"]))
        if r["bad_tag_rows"]:
            print("  bad_tag_rows:", len(r["bad_tag_rows"]))
        print()


def main() -> int:
    ap = argparse.ArgumentParser(description="Lint wiki-en/ and wiki-ru/ (mechanical checks).")
    ap.add_argument(
        "--layer",
        choices=("en", "ru", "both"),
        default="both",
        help="Which wiki tree to scan (default: both).",
    )
    ap.add_argument(
        "--write-report",
        action="store_true",
        help="Overwrite docs/lint-report.md with Markdown output.",
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if any issue is reported (any category).",
    )
    ap.add_argument(
        "--strict-links",
        action="store_true",
        help="Exit 1 only for invalid wikilink prefixes or broken targets.",
    )
    args = ap.parse_args()

    layers: list[str] = []
    if args.layer in ("both", "en"):
        layers.append("wiki-en")
    if args.layer in ("both", "ru"):
        layers.append("wiki-ru")

    results = [lint_layer(L) for L in layers]
    print_stdout(results)

    if args.write_report:
        scope = (
            "full bilingual"
            if len(results) > 1
            else f"targeted: {results[0]['layer']}/ only"
        )
        out = ROOT / "docs" / "lint-report.md"
        out.write_text(format_report_md(results, scope), encoding="utf-8")
        print(f"Wrote {out.relative_to(ROOT)}", file=sys.stderr)

    if args.strict_links:
        if any(severity_error(r) for r in results):
            return 1
        return 0
    if args.strict:
        if any(count_issues(r) > 0 for r in results):
            return 1
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
