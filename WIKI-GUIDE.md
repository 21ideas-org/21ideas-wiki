# 21ideas Bitcoin Wiki — Guide

This repository is a bilingual Bitcoin wiki built from the 21ideas.org source library in `raw/`.

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

- `wiki-en/`: **76** markdown pages total (**73** content pages excluding index/overview + glossary); operations log is repo root `log.md` (bilingual).
- `wiki-ru/`: **76** markdown pages total (**73** content pages excluding index/overview/log + glossary)

### Trust markers and consistency (both languages)

Every wiki page includes:
- required YAML frontmatter fields (title, category, quality, sources, synthesized_date, completeness, language, tags)
- **Frontmatter style:** scalar fields (`title`, `category`, `quality`, `language`, `completeness`, dates) use **double-quoted** strings for consistent parsing (Obsidian, Quartz on GitHub Pages). `tags` are an unquoted flow list of allowlisted names (see `CLAUDE.md`).
- a `## Sources` / `## Источники` section (URLs when present, otherwise a clear note)
- rich internal linking

### Bilingual wikilink discipline 

- In `wiki-en/`: internal links use the explicit `[[en/...]]` prefix.
- In `wiki-ru/`: internal links use the explicit `[[ru/...]]` prefix.

This prevents accidental cross-language resolution in shared Obsidian vaults.

## Repository structure

- `raw/` — immutable 21ideas.org source markdown files (source of truth)
- `wiki-en/` — English wiki pages
- `wiki-ru/` — Russian wiki pages
- `lint-report.md` — lint summaries (typically updated during batch work)
- `CLAUDE.md` — project rules: frontmatter schema + bilingual lint rules
- `log.md` (repo root) — append-only operational log for **both** `wiki-en/` and `wiki-ru/`

## How maintenance works (high level)

- New source files are added to `raw/` (never edited by the agent).
- The agent updates wiki pages, indexes, and logs while preserving provenance.
- Lint checks focus on:
  - required frontmatter
  - bilingual link prefixes
  - broken links and structural issues

## Releases

Previous release: `v0.1.3` (bilingual wikilink architecture + lint rules).

## Support

⚡️ Found the project useful? [Zap](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) [Tony](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) a coffee.