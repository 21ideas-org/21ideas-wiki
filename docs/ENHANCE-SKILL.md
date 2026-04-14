# ENHANCE-SKILL — Single-Page Polish for 21ideas Bitcoin Wiki

Polishes an existing wiki page: frontmatter compliance, body style, wikilink
enrichment, and content quality audit. Maintainer-facing operation.

For creating new pages from `raw/`, see `docs/WIKI-SKILL.md`.
For adding source material to `raw/`, see `docs/INGEST-SKILL.md`.

---

## Zero-Tolerance Rules

1. **Do not change substantive wording, headings, tables, or meaning** unless
   the content quality audit reveals an unsupported claim — in that case, flag
   it rather than silently rewriting it.
2. **Never fabricate `sources:` URLs.** If no URL exists in the `raw/` file's
   `url:` field, `sources: []` stays as-is.
3. **Never link to pages or anchors not in the link map.**
4. **Never use `raw/...` paths in the page body.**
5. **Never open the body with a `#` heading. Never use `---` in the body.**

---

## Before Starting: Two Script Checks

```bash
# 1. Regenerate link maps if any pages were added since the last run
python3 tools/build_link_map.py

# 2. Read the link map for the layer you are enhancing
docs/link-map-en.md   # for wiki-en/ pages
docs/link-map-ru.md   # for wiki-ru/ pages
```

---

## Step 1 — Mechanical Scan (EN pages only)

Before touching content, fix all legacy antipatterns in `wiki-en/` pages:

- `source:` singular → rename to `sources:` as inline array
- `sources:` as block YAML → collapse to inline array `sources: ["url"]`
- `*Tags: ...*` italic line in body → remove
- `# Title` heading in body → remove
- `---` horizontal rules in body → remove
- `raw/...` citations in body → replace with `https://21ideas.org/...` if a URL exists in `sources:`, otherwise remove
- `## Related Terms` → rename to `## Related pages`, convert to pipe-syntax links
- `]]]` triple-bracket links → strip extra `]`
- `[[wiki-en/...]]` or `[[wiki-ru/...]]` prefixes → fix to `[[en/...]]` or `[[ru/...]]`
- Missing `reviewed:` → add as last frontmatter field
- Unquoted scalar frontmatter fields → add double quotes
- Wrong frontmatter field order → reorder to canonical sequence (see Step 2)

---

## Step 2 — Frontmatter Standardization

Enforce this exact field order with double-quoted scalars:

```yaml
---
title: "Page title"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/..."]
synthesized_date: "2026-04-XX"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol]
updated: "2026-04-XX"
reviewed: "2026-04-XX"
---
```

- `reviewed:` is always the last field
- `tags` is an unquoted flow sequence; total 3–8 tags; only allowlist tags (see `CLAUDE.md`)
- `sources` is an inline array of quoted strings

---

## Step 3 — Wikilink Enrichment

Read the link map for the page's language layer. Scan the full page and apply:

**Pass A — Concept backbone:** primary subject on first introduction; named
people and organizations; spine concepts the page depends on; explicitly
mentioned protocol upgrades or systems.

**Pass B — Glossary sweep:** remaining terms in the page that have a
`[glossary]` entry in the map and are substantively used (not in passing).

**Resolution rule:**
- First mention → dedicated page entry
- Meaningful second mention in a different `##` section where the term is
  being defined → `[glossary]` entry
- All other repetitions → no link

**Hard rules:**
- `wiki-en/` pages: `[[en/...]]` only. `wiki-ru/` pages: `[[ru/...]]` only.
- No wikilinks inside markdown table cells.
- Fix any malformed links found (`]]]`, wrong prefixes, broken targets).

---

## Step 4 — Content Quality Audit

Answer all four questions. If a gap is found, add a named item to
`docs/WIKI-BACKLOG.md` — do not silently declare done on a thin page.

1. **Coverage** — Does the page reflect the `raw/` source adequately, or are
   sections present in source missing or thin here?
2. **Thin sections** — Does any `##` section have fewer than two substantive
   sentences? Expand with `raw/` material or fold it.
3. **Unsupported claims** — Can every factual assertion be traced to `raw/` or
   an existing wiki page? Flag anything that cannot.
4. **Concept completeness** — Does the page explain the concept (mechanism,
   significance, implications) or only name it?

If gaps require substantive new content from `raw/`, stop and run
`docs/WIKI-SKILL.md` Mode B (Update) instead.

---

## Step 5 — Section Structure

- Remove any `## Related Terms` / `## Связанные термины` section entirely
- Ensure exactly one closing nav section:
  - EN: `## Related pages` with pipe-syntax `[[en/...]]` links
  - RU: `## Дополнительные материалы` with pipe-syntax `[[ru/...]]` links
- Ensure exactly one sources section:
  - EN: `## Sources`
  - RU: `## Источники`
- Every `https://21ideas.org/...` URL used inline must appear in both
  `sources:` frontmatter and the sources section (deduplicated)

---

## Step 6 — Lint and Log

```bash
python3 tools/lint.py --layer <en|ru> --write-report
```

Fix any issues. Then append to `docs/log.md`:

```
## [YYYY-MM-DD] enhance | <page path>
**Changes:** <frontmatter fixed, wikilinks added, antipatterns removed>
**Content audit:** <solid / gaps found — list / Mode B required>
**Lint:** 0 issues
```

If content gaps were found, also add to `docs/WIKI-BACKLOG.md`:
```
- [ ] **<slug>** — <describe gap>
```

---

## Definition of Done

- [ ] All legacy antipatterns removed (EN pages)
- [ ] Frontmatter in canonical order; all scalars double-quoted; `reviewed:` last
- [ ] Pass A and Pass B wikilinks applied; all targets verified via link map
- [ ] Content quality audit answered; gaps documented if found
- [ ] Closing nav and sources sections correctly named and formatted
- [ ] `python3 tools/lint.py` → 0 issues
- [ ] `docs/log.md` appended; `docs/WIKI-BACKLOG.md` updated if gaps found