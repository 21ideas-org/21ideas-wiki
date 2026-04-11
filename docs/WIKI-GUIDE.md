# 21ideas Bitcoin Wiki — Guide

This repository is a bilingual Bitcoin wiki built from the 21ideas.org source library in `raw/`. See **`raw/README.md`** for how that tree is organized (books, theory, practice, start).

- **English layer**: `wiki-en/` (synthesized from Russian sources into English)
- **Russian layer**: `wiki-ru/` (parallel Russian wiki, grounded in the same source library; not a translation)

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
  - Use the concept pages as a structured curriculum: money → PoW → mining → scarcity → governance → upgrades → privacy/security.
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

- `wiki-en/`: **76** markdown pages total (**73** content pages excluding index/overview + glossary); operations log is **`docs/log.md`** (bilingual).
- `wiki-ru/`: **76** markdown pages total (**73** content pages excluding index/overview/log + glossary)

### Trust markers and consistency (both languages)

Every wiki page includes:
- Required YAML frontmatter fields: `title`, `category`, `quality`, `sources`, `synthesized_date`, `completeness`, `language`, `tags`. Enhanced pages also carry `updated` and `reviewed` (always the last field).
- **Frontmatter style:** scalar fields use **double-quoted** strings; `tags` is an unquoted flow list; `sources` is an inline array of quoted URLs — e.g. `sources: ["https://21ideas.org/..."]`. Full schema in `CLAUDE.md`.
- A `## Sources` / `## Источники` section (URLs when present, otherwise a clear note).
- Rich internal linking. No `#` title heading in the body — Quartz renders the frontmatter `title` as the page heading.

### Bilingual wikilink discipline 

- In `wiki-en/`: internal links use the explicit `[[en/...]]` prefix.
- In `wiki-ru/`: internal links use the explicit `[[ru/...]]` prefix.

This prevents accidental cross-language resolution in shared Obsidian vaults.

## Repository structure

- `raw/` — immutable 21ideas.org source markdown files (source of truth); **`raw/README.md`** describes folders and conventions
- `wiki-en/` — English wiki pages
- `wiki-ru/` — Russian wiki pages
- `docs/` — maintainer and process documentation
  - `WIKI-GUIDE.md` — this guide
  - `PAGE-ENHANCEMENT-STANDARD.md` — single-page polish checklist
  - `WIKI-BACKLOG.md` — short-lived backlog
  - `lint-report.md` — lint summaries (typically updated during batch work)
  - `log.md` — append-only operational log for **both** `wiki-en/` and `wiki-ru/`
- `CLAUDE.md` (repo root) — project rules: frontmatter schema + bilingual lint rules

## How maintenance works (high level)

- New source files are added to `raw/` (never edited by the agent).
- The agent updates wiki pages, indexes, and logs while preserving provenance.
- Lint checks focus on:
  - required frontmatter
  - bilingual link prefixes
  - broken links and structural issues

## Working with the agent

`CLAUDE.md` is loaded automatically in every Cursor session — you never need to @mention it. The agent follows its operation checklists (Ingest, Enhance, Lint, Query) without prompting.

`docs/PAGE-ENHANCEMENT-STANDARD.md` is **not** auto-loaded. Always include `@docs/PAGE-ENHANCEMENT-STANDARD.md` in enhance prompts so the agent has the full standard in context from the start.

### Prompt patterns

| Task | Example prompt | Extra @mention needed? |
|---|---|---|
| **Ingest** | `"Ingest raw/Theory/protocol/musig2.md into both wiki layers"` | No |
| **Enhance** | `"Enhance wiki-ru/concepts/mempool.md @docs/PAGE-ENHANCEMENT-STANDARD.md"` | Yes — include `@docs/PAGE-ENHANCEMENT-STANDARD.md` |
| **Enhance batch** | `"Enhance all pages in wiki-ru/concepts/ that are missing the reviewed field @docs/PAGE-ENHANCEMENT-STANDARD.md"` | Yes |
| **Lint** | `"Run a full bilingual lint on both wiki-en/ and wiki-ru/"` | No |
| **Lint (targeted)** | `"Run a targeted lint on wiki-ru/entities/"` | No |
| **Query** | `"What does 21ideas say about Lightning privacy? File it as a wiki page if worth keeping."` | No |

The agent appends to `docs/log.md` and updates `docs/lint-report.md` automatically as part of every operation — you do not need to ask for it separately.

## Releases

Previous release: `v0.1.3` (bilingual wikilink architecture + lint rules).

## Support

⚡️ Found the project useful? [Zap](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) [Tony](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) a coffee.