---
title: "Forks (Bitcoin)"
category: concepts
tags: [bitcoin, wiki, protocol, consensus, governance]
language: en
quality: reference
sources:
  - "https://21ideas.org/izobretaem-bitkoin/glava-5"
  - "https://21ideas.org/izobretaem-bitkoin/glava-8"
  - "https://21ideas.org/vojna-za-razmer-bloka/"
synthesized_date: "2026-04-09"
completeness: high
---

# Forks (Bitcoin)

*Tags: consensus, soft fork, hard fork, chain split*

---

## Accidental forks (chain splits)

When two miners find valid blocks close together, different parts of the network may see different tips briefly. Bitcoin resolves this with **Nakamoto consensus**: nodes follow the valid chain with the **most accumulated Proof of Work** (often called the “longest” or “heaviest” chain). The losing block becomes **stale**; its transactions return to the **mempool** if they do not conflict with the winning chain.

This kind of fork is a normal network event, not a change to protocol rules.

Source: `raw/Books/izobretaem-bitkoin/glava-5.md`

---

## Soft forks vs hard forks (rule changes)

**Soft fork:** new rules are **stricter** (or additive in a backward-compatible way). Older nodes still accept blocks produced under the new rules as valid within their own rule set. Example from the sources: the **1 MB block size limit** introduced in September 2010 — old nodes still saw smaller blocks as valid.

**Hard fork:** rules expand or change in a way that makes previously invalid blocks valid (or vice versa in incompatible ways). Nodes that do not upgrade **reject** blocks from the new rule set, so persistent disagreement yields **two chains** and effectively **two assets** if both survive economically.

The sources give **Bitcoin Cash (August 2017)** as a hard fork driven by disagreement over block space and fees: proponents of larger blocks forked; the majority of validating nodes and economic activity remained on the chain that kept the 1 MB (weight-based) constraint, which the wiki treats as **Bitcoin**.

Source: `raw/Books/izobretaem-bitkoin/glava-8.md`

---

## Governance reality

Forks illustrate that **“Bitcoin” is what users, merchants, and node operators run and accept** — not what any single author, miner, or company declares. Hard forks without broad consensus produce **altcoins** that share history up to the split; they do not change the 21M cap on the chain that enforces it.

Sources: `raw/Books/izobretaem-bitkoin/glava-8.md`, `raw/Books/vojna-za-razmer-bloka/` (blocksize war narrative)

---

## Sources

- [Inventing Bitcoin — Ch. 5 (ledger security, chain splits)](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Inventing Bitcoin — Ch. 8 (who sets rules, soft/hard forks)](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [The Blocksize War (book on 21ideas)](https://21ideas.org/vojna-za-razmer-bloka/)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/governance|governance]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/bip|BIP]] | [[en/concepts/blockchain|blockchain]] | [[en/concepts/mempool|mempool]]

## Related Pages

- [[en/concepts/governance]] — nodes, miners, developers, users
- [[en/concepts/bip]] — how upgrades are proposed and activated
- [[en/history/blocksize-war]] — 2015–2017 conflict in outline
- [[en/books/blocksize-war]] — Jonathan Bier’s account
- [[en/concepts/segwit]] — major soft fork in that era
