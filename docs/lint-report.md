# Lint report — 21ideas Bitcoin Wiki

_Last pass: 2026-04-14 (targeted: wiki-en/ only)_

## Summary

| Layer | Pages | Bad wikilink prefix | Broken targets | Block `sources:` | Body `---` | Body `#` | `raw/` in body | Missing FM keys | Missing `reviewed` | Off-allowlist tags |
|-------|------:|--------------------:|---------------:|-----------------:|----------:|---------:|---------------:|----------------:|-------------------:|-------------------:|
| wiki-en | 78 | 3 | 6 | 1 | 11 | 9 | 24 | 2 | 11 | 16 |

## Detail (by layer)

### `wiki-en/`

- **Invalid cross-prefix / layer wikilinks** (3):
  - `('wiki-en/overview.md', '[[ru/...]]')`
  - `('wiki-en/overview.md', '[[ru/overview|Russian wiki overview]]')`
  - `('wiki-en/overview.md', '[[ru/index|Russian wiki index]]')`

- **Broken wikilink targets** (6):
  - `('wiki-en/concepts/governance.md', '[[en/concepts/bitcoin-node\\|Full nodes]]', 'concepts/bitcoin-node\\.md')`
  - `('wiki-en/concepts/governance.md', '[[en/concepts/mining\\|Miners]]', 'concepts/mining\\.md')`
  - `('wiki-en/concepts/governance.md', '[[en/concepts/bitcoin-core\\|Bitcoin Core]]', 'concepts/bitcoin-core\\.md')`
  - `('wiki-en/concepts/governance.md', '[[en/concepts/bip\\|BIPs]]', 'concepts/bip\\.md')`
  - `('wiki-en/concepts/security.md', '[[en/practice/storage\\|Coldcard]]', 'practice/storage\\.md')`
  - `('wiki-en/concepts/security.md', '[[en/concepts/multisig\\|multisig]]', 'concepts/multisig\\.md')`

- **`raw/` in body** (24):
  - `('wiki-en/contribute.md', 'The wiki is built from immutable source files in `raw/` — anchored in [21ideas.org](https://21ideas.')`
  - `('wiki-en/contribute.md', 'Use docs/INGEST-SKILL.md to add the following article to raw/.')`
  - `('wiki-en/contribute.md', 'URL is always required. Everything else improves results but is optional. The agent handles subdirec')`
  - `('wiki-en/entities/gigi.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/entities/parker-lewis.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/entities/saifedean-ammous.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/glossary.md', '*Source: `raw/Start/glossary.md` — the master Bitcoin term reference for 21ideas.org. All terms defi')`
  - `('wiki-en/history/pre-bitcoin-cypherpunks.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/history/timeline.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/overview.md', '> This page describes the **English** wiki (`wiki-en/`). A parallel **Russian** wiki lives in `wiki-')`
  - `('wiki-en/practice/buying.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/practice/privacy-practice.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/practice/running-a-node.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/series/discovering-bitcoin.md', '*Author: Giacomo Zucco (BHB Network) | Parts: 7 | Source: `raw/Theory/economics/discovering-bitcoin/')`
  - `('wiki-en/series/genesis-files.md', '*Author: Aaron van Wirdum (Bitcoin Magazine) | Parts: 5 + intro | Source: `raw/Theory/history/genesi')`
  - `('wiki-en/series/gradually-then-suddenly.md', '*Author: Parker Lewis | Platform: Unchained Capital blog | Parts: 17 | Source: `raw/Theory/economics')`
  - `('wiki-en/series/oxt-research.md', '*Authors: Samourai Wallet team (TDevD and others) | Parts: 4 | Source: `raw/Theory/privacy/oxt/` | T')`
  - `('wiki-en/series/silk-road.md', '*Source: `raw/Theory/history/silk-road/` | Parts: 6 | Tags: series, history, Ross-Ulbricht, darknet*')`
  - `('wiki-en/series/silk-road.md', 'Source: `raw/Theory/philosophy/bitcoin-equals-freedom.md`')`
  - `('wiki-en/series/what-i-learned-from-bitcoin.md', '*Author: Gigi (dergigi) | Parts: 3 planned (1 available in library) | Source: `raw/Theory/philosophy')`
  - `('wiki-en/series/what-i-learned-from-bitcoin.md', 'Only Part 1 (Philosophical Teachings) is in the raw/ library. The series exists in full on dergigi.c')`
  - `('wiki-en/series/what-i-learned-from-bitcoin.md', 'Source: `raw/Theory/philosophy/what-i-learned-from-bitcoin/1-philosophical-teachings.md`')`
  - `('wiki-en/topics/bitcoin-dissidents.md', 'Source: `raw/Theory/philosophy/bitcoin-dissidents.md` (CoinDesk article, December 2020, translated b')`
  - `('wiki-en/topics/network-effects.md', 'Source: `raw/Theory/economics/seven-network-effects-of-bitcoin.md` (Trace Mayer, WeUseCoins, June 20')`

- **Standalone `---` in body** (11):
  - `wiki-en/glossary.md`
  - `wiki-en/index.md`
  - `wiki-en/overview.md`
  - `wiki-en/series/discovering-bitcoin.md`
  - `wiki-en/series/genesis-files.md`
  - `wiki-en/series/gradually-then-suddenly.md`
  - `wiki-en/series/oxt-research.md`
  - `wiki-en/series/silk-road.md`
  - `wiki-en/series/what-i-learned-from-bitcoin.md`
  - `wiki-en/topics/bitcoin-dissidents.md`
  - `wiki-en/topics/network-effects.md`

- **`#` as first body heading** (9):
  - `('wiki-en/glossary.md', '# Glossary')`
  - `('wiki-en/series/discovering-bitcoin.md', '# Discovering Bitcoin')`
  - `('wiki-en/series/genesis-files.md', '# Genesis Files')`
  - `('wiki-en/series/gradually-then-suddenly.md', '# Gradually, Then Suddenly')`
  - `('wiki-en/series/oxt-research.md', '# OXT Research: Understanding Bitcoin Privacy')`
  - `('wiki-en/series/silk-road.md', '# Silk Road')`
  - `('wiki-en/series/what-i-learned-from-bitcoin.md', '# What I Learned From Bitcoin')`
  - `('wiki-en/topics/bitcoin-dissidents.md', '# Bitcoin for Dissidents')`
  - `('wiki-en/topics/network-effects.md', "# Bitcoin's Seven Network Effects")`

- **Block / list `sources:`** (1):
  - `wiki-en/glossary.md`

- **Missing required YAML keys** (2):
  - `('wiki-en/contribute.md', ['completeness', 'quality', 'sources', 'synthesized_date', 'tags'])`
  - `('wiki-en/support.md', ['completeness', 'quality', 'sources', 'synthesized_date', 'tags'])`

- **Missing `reviewed`** (11):
  - `wiki-en/contribute.md`
  - `wiki-en/glossary.md`
  - `wiki-en/series/discovering-bitcoin.md`
  - `wiki-en/series/genesis-files.md`
  - `wiki-en/series/gradually-then-suddenly.md`
  - `wiki-en/series/oxt-research.md`
  - `wiki-en/series/silk-road.md`
  - `wiki-en/series/what-i-learned-from-bitcoin.md`
  - `wiki-en/support.md`
  - `wiki-en/topics/bitcoin-dissidents.md`
  - `wiki-en/topics/network-effects.md`

- **Tags outside allowlist** (16):
  - `('wiki-en/series/discovering-bitcoin.md', 'series')`
  - `('wiki-en/series/discovering-bitcoin.md', 'zucco')`
  - `('wiki-en/series/genesis-files.md', 'series')`
  - `('wiki-en/series/genesis-files.md', 'cypherpunks')`
  - `('wiki-en/series/gradually-then-suddenly.md', 'series')`
  - `('wiki-en/series/gradually-then-suddenly.md', 'parker-lewis')`
  - `('wiki-en/series/oxt-research.md', 'series')`
  - `('wiki-en/series/oxt-research.md', 'blockchain-analysis')`
  - `('wiki-en/series/silk-road.md', 'series')`
  - `('wiki-en/series/silk-road.md', 'adoption')`
  - `('wiki-en/series/what-i-learned-from-bitcoin.md', 'series')`
  - `('wiki-en/series/what-i-learned-from-bitcoin.md', 'gigi')`
  - `('wiki-en/topics/bitcoin-dissidents.md', 'human-rights')`
  - `('wiki-en/topics/bitcoin-dissidents.md', 'activism')`
  - `('wiki-en/topics/network-effects.md', 'adoption')`
  - `('wiki-en/topics/network-effects.md', 'network-effects')`

## Suggested follow-ups

- Orphans / `index.md` coverage: not implemented in this tool (human review).
- Scalar quoting in frontmatter: only partially enforceable; fix by hand or extend the tool.
- After mechanical fixes, re-run with `--write-report` and append `docs/log.md` per CLAUDE.md.
