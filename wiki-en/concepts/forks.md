---
title: "Forks (Bitcoin)"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/izobretaem-bitkoin/glava-5", "https://21ideas.org/izobretaem-bitkoin/glava-8", "https://21ideas.org/vojna-za-razmer-bloka/"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, governance, fork]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## Accidental forks (chain splits)

When two [[en/concepts/mining|miners]] find valid blocks close together, different parts of the network may see different tips briefly. Bitcoin resolves this with **Nakamoto consensus**: [[en/concepts/bitcoin-node|nodes]] follow the valid chain with the **most accumulated [[en/concepts/proof-of-work|Proof of Work]]** (often called the "longest" or "heaviest" chain). The losing block becomes **stale**; its transactions return to the [[en/concepts/mempool|mempool]] if they do not conflict with the winning chain.

This kind of fork is a normal network event, not a change to protocol rules.

## Soft forks vs hard forks (rule changes)

**Soft fork:** new rules are **stricter** (or additive in a backward-compatible way). Older nodes still accept blocks produced under the new rules as valid within their own rule set. Example from the sources: the **1 MB block size limit** introduced in September 2010 — old nodes still saw smaller blocks as valid.

**Hard fork:** rules expand or change in a way that makes previously invalid blocks valid (or vice versa in incompatible ways). Nodes that do not upgrade **reject** blocks from the new rule set, so persistent disagreement yields **two chains** and effectively **two assets** if both survive economically.

The sources give **Bitcoin Cash (August 2017)** as a hard fork driven by disagreement over block space and fees: proponents of larger blocks forked; the majority of validating nodes and economic activity remained on the chain that kept the 1 MB (weight-based) constraint, which the wiki treats as **Bitcoin**.

Source: [Inventing Bitcoin — Ch. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)

## Governance reality

Forks illustrate that **"Bitcoin" is what users, merchants, and node operators run and accept** — not what any single author, miner, or company declares. Hard forks without broad consensus produce **altcoins** that share history up to the split; they do not change the [[en/concepts/scarcity|21M cap]] on the chain that enforces it.

## Sources

- [Inventing Bitcoin — Ch. 5 (ledger security, chain splits)](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Inventing Bitcoin — Ch. 8 (who sets rules, soft/hard forks)](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [The Blocksize War (book on 21ideas)](https://21ideas.org/vojna-za-razmer-bloka/)

## Related pages

- [[en/concepts/governance|Governance — nodes, miners, developers, users and who controls the rules]]
- [[en/concepts/proof-of-work|Proof of Work — the accumulated work that determines the valid chain]]
- [[en/concepts/mempool|Mempool — where stale-block transactions return after a reorg]]
- [[en/concepts/bip|BIP — how upgrades are proposed and activated]]
- [[en/concepts/segwit|SegWit — major soft fork activated in 2017]]
- [[en/history/blocksize-war|Blocksize War — the 2015–2017 conflict that produced Bitcoin Cash]]
- [[en/books/blocksize-war|The Blocksize War (book) — Jonathan Bier's full account]]
