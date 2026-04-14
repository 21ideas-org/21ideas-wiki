# 21ideas Bitcoin Wiki — Guide

This repository is a bilingual Bitcoin wiki built from the [21ideas.org](https://21ideas.org) source library in `raw/`. See **`raw/README.md`** for how that tree is organized (books, theory, practice, start).

- **English layer**: `wiki-en/` 
- **Russian layer**: `wiki-ru/` 

Both layers use trust markers and strict linking rules.

## How to start (recommended)

1. Clone the repo and open it as an Obsidian vault.
2. Start with the language index:
   - English: `wiki-en/index.md`
   - Russian: `wiki-ru/index.md`
3. Then open the overview:
   - English: `wiki-en/overview.md`
   - Russian: `wiki-ru/overview.md`

## What you can use the wiki for

- **Learning Bitcoin end-to-end**
  - Use the concept pages as a structured curriculum: money → PoW → mining → scarcity → governance → privacy → security.
- **Fast lookups**
  - Each language layer contains a glossary page:
    - `wiki-en/glossary.md`
    - `wiki-ru/glossary.md`
- **Reading paths**
  - Use the series pages to go deeper by theme (economics, history, privacy, philosophy).
- **Checking provenance**
  - Pages contain YAML trust markers and a `## Sources` section linking back to 21ideas.org when a canonical URL exists.
- **Graph-based exploration**
  - In Obsidian, Graph View becomes useful once you follow links from `index.md` and hub concept pages.
- **Maintaining a compounding knowledge base**
  - Add new immutable source files to `raw/`, then run an ingest/update workflow that updates the wiki incrementally without losing provenance.

### Current page counts 

- `wiki-en/`: **76** markdown pages total (**73** content pages excluding index, overview + glossary); operations log is **`docs/log.md`** (bilingual).
- `wiki-ru/`: **76** markdown pages total (**73** content pages excluding index, overview + glossary)

### Trust markers and consistency (both languages)

Every wiki page includes:
- Required YAML frontmatter fields: `title`, `category`, `quality`, `sources`, `synthesized_date`, `completeness`, `language`, `tags`. Enhanced pages also carry `updated` and `reviewed`.
- **Frontmatter style:** Full schema in `CLAUDE.md`.
- A `## Sources` / `## Источники` section (URLs when present, otherwise a clear note).
- Rich internal linking. No `#` title heading in the body — Quartz renders the frontmatter `title` as the page heading.

### Bilingual wikilink discipline 

- In `wiki-en/`: internal links use the explicit `[[en/...]]` prefix.
- In `wiki-ru/`: internal links use the explicit `[[ru/...]]` prefix.

This prevents accidental cross-language resolution in shared Obsidian vaults.

## Repository structure

- `raw/` — immutable 21ideas.org source markdown files (source of truth); **`raw/README.md`** describes folders and conventions
- `raw/README.md` — raw directory structure
- `wiki-en/` — English wiki pages
- `wiki-ru/` — Russian wiki pages
- `docs/` — maintainer and process documentation
  - `WIKI-GUIDE.md` — this guide
  - `PAGE-ENHANCEMENT-STANDARD.md` — superseded by `ENHANCE-SKILL.md`; kept for reference
  - `WIKI-SKILL.md` — wiki page generation skill (new ingest + update modes)
  - `ENHANCE-SKILL.md` — single-page polish skill; use instead of PAGE-ENHANCEMENT-STANDARD.md
  - `link-map-en.md` — generated wikilink map for wiki-en/ (do not edit manually)
  - `link-map-ru.md` — generated wikilink map for wiki-ru/ (do not edit manually)
  - `INGEST-SKILL.md` — raw source ingestion workflow; use before the wiki ingest step
  - `WIKI-BACKLOG.md` — short-lived backlog
  - `lint-report.md` — mechanical lint output (**English**); last run wins (see `--layer` scope below)
  - `log.md` — append-only operational log for **both** `wiki-en/` and `wiki-ru/`
- `tools/` — lint.py (mechanical lint), check_duplicate.py, derive_slug.py, check_series.py, build_link_map.py, check_parity.py. See `tools/README.md` for interface reference.
- `CLAUDE.md` (repo root) — project rules: frontmatter schema + bilingual lint rules

## How maintenance works (high level)

- New source files are added to `raw/` (never edited by the agent) using the workflow in docs/INGEST-SKILL.md. See CONTRIBUTING.md for the full source acceptance policy.
- **Link maps:** run `python3 tools/build_link_map.py` from the repo root to regenerate `docs/link-map-en.md` and `docs/link-map-ru.md` after adding or renaming wiki pages. Agents read these maps before wikilinking — never scan the directory tree directly.
- The agent updates wiki pages, indexes, and logs while preserving provenance.
- **Lint:** run `python3 tools/lint.py` from the repo root (see `CLAUDE.md` → **Lint**). Use `--write-report` to refresh `docs/lint-report.md` (English headings and labels; vault paths and quoted snippets may be Russian). Choose `--layer ru`, `--layer en`, or `--layer both` so the report matches the pass you intend.

## Working with the agent

`CLAUDE.md` is loaded automatically in every Cursor session — you never need to @mention it. The agent follows its operation checklists (Ingest, Enhance, Lint, Query) without prompting.

`docs/PAGE-ENHANCEMENT-STANDARD.md` is **not** auto-loaded. Always include `@docs/ENHANCE-SKILL.md` in enhance prompts so the agent has the full standard in context from the start.

### Prompt patterns

| Task | Example prompt | Extra @mention needed? |
|---|---|---|
| **Raw ingest** | `"Use docs/INGEST-SKILL.md to add the following article to raw/. URL: https://..."` | No — skill is self-contained |
| **Ingest** | `"Ingest raw/Theory/protocol/musig2.md into both wiki layers"` | No |
| **Enhance** | `"Enhance wiki-ru/concepts/mempool.md @docs/ENHANCE-SKILL.md"` | Yes — include `@docs/ENHANCE-SKILL.md` |
| **Enhance batch** | `"Enhance all pages in wiki-ru/concepts/ that are missing the reviewed field @docs/ENHANCE-SKILL.md"` | Yes |
| **Lint** | `"Run a full bilingual lint on both wiki-en/ and wiki-ru/"` — agent should run `python3 tools/lint.py --layer both --write-report` and append `docs/log.md` | No |
| **Lint (targeted RU)** | `"Run a targeted lint on wiki-ru/"` — e.g. `python3 tools/lint.py --layer ru --write-report` + `docs/log.md` | No |
| **Lint (targeted EN)** | `"Run a targeted lint on wiki-en/"` — e.g. `python3 tools/lint.py --layer en --write-report` + `docs/log.md` | No |
| **Query** | `"What does 21ideas say about Lightning privacy? File it as a wiki page if worth keeping."` | No |

For **lint** passes, ask the agent explicitly; it should run **`tools/lint.py`** with **`--write-report`** (and the right **`--layer`**) then append **`docs/log.md`**. For ingest/enhance, agents still append **`docs/log.md`** per `CLAUDE.md` even if you do not repeat that in the prompt.

## Releases

Previous release: [v1.0.0](https://github.com/21ideas-org/21ideas-wiki/releases/tag/v1.0.0).

## Support

⚡️ Found the project useful? [Zap](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) [Tony](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) a coffee.