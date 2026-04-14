# Lint report — 21ideas Bitcoin Wiki

_Last pass: 2026-04-14 (targeted: wiki-en/ only)_

## Summary

| Layer | Pages | Bad wikilink prefix | Broken targets | Block `sources:` | Body `---` | Body `#` | `raw/` in body | Missing FM keys | Missing `reviewed` | Off-allowlist tags |
|-------|------:|--------------------:|---------------:|-----------------:|----------:|---------:|---------------:|----------------:|-------------------:|-------------------:|
| wiki-en | 78 | 3 | 7 | 1 | 4 | 1 | 12 | 2 | 3 | 0 |

## Detail (by layer)

### `wiki-en/`

- **Invalid cross-prefix / layer wikilinks** (3):
  - `('wiki-en/overview.md', '[[ru/...]]')`
  - `('wiki-en/overview.md', '[[ru/overview|Russian wiki overview]]')`
  - `('wiki-en/overview.md', '[[ru/index|Russian wiki index]]')`

- **Broken wikilink targets** (7):
  - `('wiki-en/concepts/governance.md', '[[en/concepts/bitcoin-node\\|Full nodes]]', 'concepts/bitcoin-node\\.md')`
  - `('wiki-en/concepts/governance.md', '[[en/concepts/mining\\|Miners]]', 'concepts/mining\\.md')`
  - `('wiki-en/concepts/governance.md', '[[en/concepts/bitcoin-core\\|Bitcoin Core]]', 'concepts/bitcoin-core\\.md')`
  - `('wiki-en/concepts/governance.md', '[[en/concepts/bip\\|BIPs]]', 'concepts/bip\\.md')`
  - `('wiki-en/concepts/security.md', '[[en/practice/storage\\|Coldcard]]', 'practice/storage\\.md')`
  - `('wiki-en/concepts/security.md', '[[en/concepts/multisig\\|multisig]]', 'concepts/multisig\\.md')`
  - `('wiki-en/glossary.md', '[[en/concepts/lightning network]]', 'concepts/lightning network.md')`

- **`raw/` in body** (12):
  - `('wiki-en/contribute.md', 'The wiki is built from immutable source files in `raw/` — anchored in [21ideas.org](https://21ideas.')`
  - `('wiki-en/contribute.md', 'Use docs/INGEST-SKILL.md to add the following article to raw/.')`
  - `('wiki-en/contribute.md', 'URL is always required. Everything else improves results but is optional. The agent handles subdirec')`
  - `('wiki-en/entities/gigi.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/entities/parker-lewis.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/entities/saifedean-ammous.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/glossary.md', '*Source: `raw/Start/glossary.md` — the master Bitcoin term reference for 21ideas.org. All terms defi')`
  - `('wiki-en/history/pre-bitcoin-cypherpunks.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/overview.md', '> This page describes the **English** wiki (`wiki-en/`). A parallel **Russian** wiki lives in `wiki-')`
  - `('wiki-en/practice/buying.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/practice/privacy-practice.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`
  - `('wiki-en/practice/running-a-node.md', '*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source artic')`

- **Standalone `---` in body** (4):
  - `wiki-en/glossary.md`
  - `wiki-en/index.md`
  - `wiki-en/overview.md`
  - `wiki-en/series/oxt-research.md`

- **`#` as first body heading** (1):
  - `('wiki-en/glossary.md', '# Glossary')`

- **Block / list `sources:`** (1):
  - `wiki-en/glossary.md`

- **Missing required YAML keys** (2):
  - `('wiki-en/contribute.md', ['completeness', 'quality', 'sources', 'synthesized_date', 'tags'])`
  - `('wiki-en/support.md', ['completeness', 'quality', 'sources', 'synthesized_date', 'tags'])`

- **Missing `reviewed`** (3):
  - `wiki-en/contribute.md`
  - `wiki-en/glossary.md`
  - `wiki-en/support.md`

## Suggested follow-ups

- Orphans / `index.md` coverage: not implemented in this tool (human review).
- Scalar quoting in frontmatter: only partially enforceable; fix by hand or extend the tool.
- After mechanical fixes, re-run with `--write-report` and append `docs/log.md` per CLAUDE.md.
