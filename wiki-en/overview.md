---
title: "Introduction to 21wiki"
category: "overview"
quality: "synthesized"
sources: []
synthesized_date: "2026-04-10"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, overview, navigation]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

21wiki is a Bitcoin knowledge base grounded in the immutable 21ideas.org source library (articles, books, and series) and fundamental Bitcoin-only materials organized into a navigable map.

## About the project

21ideas.org is a Bitcoin-only education project. Over time it accumulated a large source library: books, long-form series, practical guides, and conceptual explainers across economics, protocol, history, privacy, and security.

This wiki does not replace the original materials. It is a structured map and entry point: if a topic clicks, follow the links and read the primary sources referenced by each page.

## How to read

### If you are just getting started

1. Read [[en/concepts/bitcoin|Bitcoin]] — a baseline understanding of the protocol
2. Use [[en/glossary|Glossary]] — definitions for common terms
3. Read [[en/concepts/money|Money]] — why the concept of money matters
4. Continue with [[en/books/inventing-bitcoin|Inventing Bitcoin]] or [[en/books/sovereignty-through-mathematics|Sovereignty Through Mathematics]] — both compress the essentials into a short book

### If you care about history

1. [[en/history/pre-bitcoin-cypherpunks|Pre-Bitcoin: The Cypherpunk Era]] — where Bitcoin came from
2. [[en/entities/cypherpunks|Cypherpunks]] — people and ideas that shaped Bitcoin
3. [[en/series/genesis-files|Genesis Files]] — deep dives into every major precursor
4. [[en/history/timeline|Bitcoin Timeline]] — key events in chronological order
5. [[en/history/blocksize-war|The Blocksize War (2015-2017)]] — the scaling conflict that defined Bitcoin governance in practice

### If you care about economics

1. [[en/concepts/money|Money]] — what money is and how it evolves
2. [[en/concepts/cantillon-effect|Cantillon Effect]] — how inflation redistributes wealth
3. [[en/concepts/scarcity|Scarcity]] — why \(21\,000\,000\) matters
4. [[en/series/gradually-then-suddenly|Gradually, Then Suddenly]] — Parker Lewis’s essay series

### If you care about philosophy and culture

1. [[en/philosophy/overview|Philosophy Overview]] — philosophical foundations of Bitcoin
2. [[en/books/21-ways|21 Ways]] — 21 frames for understanding Bitcoin
3. [[en/topics/bitcoin-dissidents|Bitcoin for Dissidents]] — Bitcoin as an escape from coercion
4. [[en/topics/network-effects|Bitcoin's Seven Network Effects]] — why the network hardens over time

### If you want to start using Bitcoin

1. [[en/practice/buying|Buying Bitcoin]] — acquiring bitcoin
2. [[en/practice/storage|Storage & Self-Custody]] — holding your own keys safely
3. [[en/practice/lightning-tools|Lightning Tools]] — everyday Lightning payments
4. [[en/concepts/security|Security]] — the threat model of self-sovereignty
5. [[en/practice/privacy-practice|Privacy in Practice]] — coin control, CoinJoin, Tor
6. [[en/practice/running-a-node|Running a Bitcoin Node]] — independently verifying the rules

### If you care about the technical side

1. [[en/concepts/proof-of-work|Proof of Work]] — the consensus mechanism
2. [[en/concepts/mining|Mining]] — how blocks are produced
3. [[en/concepts/utxo|UTXOs (Unspent Transaction Outputs)]] — Bitcoin’s balance model
4. [[en/concepts/segwit|SegWit (Segregated Witness)]] and [[en/concepts/taproot|Taproot]] — major protocol upgrades
5. [[en/concepts/protocol-stack|Bitcoin Protocol Stack]] — layered architecture
6. [[en/concepts/lightning-network|Lightning Network]] — payment channels on top of the base layer

## Wiki structure

```
wiki-en/
├── index.md                    ← directory of all pages
├── overview.md                 ← this file
├── glossary.md                 ← term definitions
├── concepts/                   ← 35 conceptual pages
├── entities/                   ← 12 people / groups
├── history/                    ← 3 history pages
├── philosophy/                 ← 1 philosophy page
├── books/                      ← 8 books
├── series/                     ← 7 article series
├── practice/                   ← 5 practical guides
└── topics/                     ← 2 topic pages
```

## About quality

Each page includes YAML frontmatter metadata:

- `quality: "synthesized"` — a topic distilled from multiple sources
- `quality: "reference"` — a description of a specific source (book, series)
- `completeness: "high"` / `"medium"` / `"low"` — how fully the topic is covered

Pages marked `completeness: "medium"` or `"low"` can be expanded as more sources are ingested.

## Navigation in Obsidian

In Obsidian, use:
- **Graph view** — a visual map of connections between pages
- **Backlinks** — what links to the current page
- **wikilinks** — navigation between articles
- **Dataview** ([plugin](obsidian://show-plugin?id=dataview)) — query pages by tags and metadata

## Get involved

- Start here: [Contribute to 21wiki](./contribute)
- If the wiki helped you: [Support 21wiki](./support)
- Suggest a topic or report an error: [open a GitHub Issue](https://github.com/21ideas-org/21ideas-wiki/issues/new/choose)

## Related pages

- [[en/index|English wiki index]]
- [[en/glossary|Glossary]]
- [[en/concepts/bitcoin|Bitcoin]]
- [[en/concepts/money|Money]]
- [[en/concepts/proof-of-work|Proof of Work]]
- [[en/concepts/scarcity|Scarcity]]
- [[en/concepts/security|Security]]
- [[en/concepts/lightning-network|Lightning Network]]
- [[en/history/timeline|Bitcoin Timeline]]
- [[en/series/genesis-files|Genesis Files]]
- [[en/philosophy/overview|Philosophy Overview]]
- [[ru/overview|Russian wiki overview]]
- [[ru/index|Russian wiki index]]
