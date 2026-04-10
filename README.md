# 21ideas Bitcoin Wiki

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/v/release/21ideas-org/21ideas-wiki)](https://github.com/21ideas-org/21ideas-wiki/releases/latest)

A living, AI-maintained Bitcoin knowledge base built **strictly from 21ideas.org source material** in `raw/`.

This repo contains two first-class wiki layers:

- **English wiki**: `wiki-en/` — synthesized from Russian `raw/` sources into English
- **Russian wiki**: `wiki-ru/` — a parallel, source-grounded Russian wiki (not a translation of the English pages)

Both layers follow strict conventions: required YAML frontmatter (trust markers), consistent tags, and bilingual wikilink discipline. **Frontmatter:** quote string scalars with double quotes (`title: "…"`, `category: "concepts"`, etc.); keep `tags` as a flow list — see `CLAUDE.md` and `PAGE-ENHANCEMENT-STANDARD.md` for the full schema (Quartz-friendly).

## What’s inside (current)

- **Source library**: `raw/` — immutable markdown sources from 21ideas.org
- **English wiki**: `wiki-en/` — **76** markdown pages total (**73** content pages excluding index/overview + glossary). Operational changelog: `log.md` at repo root (covers EN + RU).
- **Russian wiki**: `wiki-ru/` — **76** markdown pages total (**73** content pages excluding index/overview/log + glossary)

Coverage includes core Bitcoin concepts (protocol + economics), key protocol elements (PoW, mining, difficulty, forks, mempool, BIPs, etc.), cypherpunk history (Genesis Files + manifestos), and key entities.

## How to use

- **Open in Obsidian**: clone the repo and open it as a vault.
  - Start here:
    - `wiki-en/index.md`
    - `wiki-ru/index.md`
- **Navigate by topic**: use `wiki-en/overview.md` / `wiki-ru/overview.md`, then follow links.
- **Verify provenance**: every page contains trust markers (quality, completeness, synthesis date, and sources when available).

## Contributing / maintaining

- **Rules of the project** live in `CLAUDE.md` (frontmatter requirements + bilingual lint rules).
- **Per-page polish workflow:** use `PAGE-ENHANCEMENT-STANDARD.md` when standardizing a single page (frontmatter, wikilinks, sources, bottom nav). Record notable maintenance passes in the repo root `log.md` (bilingual).
- To extend the wiki: add new immutable sources to `raw/` and run an agent-driven ingest/update workflow that maintains structure, links, and trust markers.

Feel free to open issues or PRs if you spot gaps or want to contribute new syntheses. 
The wiki is designed to be agent-friendly.  
This wiki is a work in progress and will keep evolving as new material is added.  
Built as part of the [21ideas](https://21ideas.org) Bitcoin education project. 

## License

This project is licensed under the [MIT License](LICENSE) — feel free to fork, use, and build upon it.

## Support

⚡️ Found the project useful? [Zap](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) [Tony](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) a coffee.

