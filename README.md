# 21ideas Bitcoin Wiki

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/v/release/21ideas-org/21ideas-wiki)](https://github.com/21ideas-org/21ideas-wiki/releases/latest)

A living, AI-maintained and human-curated Bitcoin knowledge base built **strictly from 21ideas.org source material** in `raw/`.

This repo contains two first-class wiki layers:

- **English wiki**: `wiki-en/` — synthesized from Russian `raw/` sources into English
- **Russian wiki**: `wiki-ru/` — a parallel, source-grounded Russian wiki (not a translation of the English pages)

Both layers follow strict conventions: required YAML frontmatter (trust markers), consistent tags, and bilingual wikilink discipline. Full schema and rules: **`CLAUDE.md`** (repo root).

## What's inside (current)

- **Source library**: `raw/` — immutable markdown sources from 21ideas.org (layout: **`raw/README.md`**)
- **English wiki**: `wiki-en/` — **76** markdown pages total (**73** content pages excluding index/overview + glossary). Operational changelog: **`docs/log.md`** (covers EN + RU).
- **Russian wiki**: `wiki-ru/` — **76** markdown pages total (**73** content pages excluding index/overview/log + glossary)

Coverage includes core Bitcoin concepts (protocol + economics), key protocol elements (PoW, mining, difficulty, forks, mempool, BIPs, etc.), cypherpunk history (Genesis Files + manifestos), and key entities.

## Documentation (`docs/`)

| File | Role |
|------|------|
| [`docs/WIKI-GUIDE.md`](docs/WIKI-GUIDE.md) | Reader and maintainer guide — includes agent prompt patterns |
| [`docs/PAGE-ENHANCEMENT-STANDARD.md`](docs/PAGE-ENHANCEMENT-STANDARD.md) | Full prompt + checklist for polishing a single wiki page |
| [`docs/WIKI-BACKLOG.md`](docs/WIKI-BACKLOG.md) | Short-lived backlog scratchpad |
| [`docs/log.md`](docs/log.md) | Append-only bilingual operations log |
| [`docs/lint-report.md`](docs/lint-report.md) | Lint summary from batch checks |

## How to use

- **Open in Obsidian**: clone the repo and open it as a vault.
  - Start here:
    - `wiki-en/index.md`
    - `wiki-ru/index.md`
- **Navigate by topic**: use `wiki-en/overview.md` / `wiki-ru/overview.md`, then follow links.
- **Verify provenance**: every page contains trust markers (quality, completeness, synthesis date, and sources when available).

## Working with the agent

`CLAUDE.md` is loaded automatically in every Cursor session — no @mention needed. Common prompts:

| Task | Prompt |
|---|---|
| Ingest a source | `"Ingest raw/Theory/protocol/musig2.md into both wiki layers"` |
| Enhance a page | `"Enhance wiki-ru/concepts/mempool.md @docs/PAGE-ENHANCEMENT-STANDARD.md"` |
| Full lint | `"Run a full bilingual lint on both wiki-en/ and wiki-ru/"` |

See **`docs/WIKI-GUIDE.md`** for the full prompt patterns table and notes on when to use each.

## How to ingest (manual)

1. Add new source markdown under the right subtree in **`raw/`** (see **`raw/README.md`**). Treat `raw/` files as read-only — never edit them to patch the wiki.
2. Run an **ingest** prompt (see above). The agent creates or updates pages in **`wiki-en/`** and **`wiki-ru/`**, refreshes both `index.md` files, and appends a dated entry to **`docs/log.md`**.

For bilingual health checks, run a lint prompt. Results are recorded in **`docs/lint-report.md`** automatically.

## Contributing / maintaining

- **Rules of the project** live in `CLAUDE.md` (frontmatter schema, tag allowlist, wikilink discipline, operation checklists).
- **Per-page polish workflow:** use `docs/PAGE-ENHANCEMENT-STANDARD.md` when standardizing a single page. Always include `@docs/PAGE-ENHANCEMENT-STANDARD.md` in your enhance prompt.
- Notable maintenance passes are recorded in **`docs/log.md`** (covers both EN and RU).

Feel free to open issues or PRs if you spot gaps or want to contribute new syntheses.
The wiki is designed to be agent-friendly.
This wiki is a work in progress and will keep evolving as new material is added.
Built as part of the [21ideas](https://21ideas.org) Bitcoin education project.

## License

This project is licensed under the [MIT License](LICENSE) — feel free to fork, use, and build upon it.

## Support

⚡️ Found the project useful? [Zap](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) [Tony](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) a coffee.
