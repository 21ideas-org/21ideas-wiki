---
title: "Mempool"
category: concepts
tags: [bitcoin, wiki, protocol, mining, transactions]
language: en
quality: reference
sources:
  - "https://21ideas.org/izobretaem-bitkoin/glava-5"
  - "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5"
synthesized_date: "2026-04-09"
completeness: high
---

# Mempool

*Tags: unconfirmed transactions, fee market, mining*

---

## Definition

The **mempool** (memory pool) is where nodes keep **unconfirmed transactions** they have heard about on the network. **Miners** select transactions from their mempool when building a candidate block — typically prioritizing by **fee rate** (fee per unit of block space).

Sources: `raw/Books/izobretaem-bitkoin/glava-5.md`, `raw/Books/Suverenitet-posredstvom-matematiki/chapter-5.md`

---

## Behavior during reorgs

If a block is **orphaned** (another chain tip wins under PoW rules), transactions from the dropped block are returned to the mempool **if they remain valid** under the new best chain. Conflicting spends are resolved by chain rules and ordering.

Source: `raw/Books/izobretaem-bitkoin/glava-5.md`

---

## Not yet “in time” for the network

Until included in a valid block, a transaction has **no consensus-defined timestamp** in the same sense as a confirmed spend — the network’s notion of ordering is anchored in **blocks**, not the mempool alone.

---

## Sources

- [Inventing Bitcoin — Ch. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Sovereignty Through Mathematics — Ch. 5](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/mining|mining]] | [[en/concepts/utxo|UTXO]] | [[en/concepts/forks|reorganization]] | [[en/concepts/difficulty-adjustment|difficulty adjustment]] | [[en/concepts/bitcoin|Bitcoin]]

## Related Pages

- [[en/concepts/mining]] — block construction from the mempool
- [[en/concepts/utxo]] — what inputs/outputs miners must validate
- [[en/concepts/forks]] — stale blocks and mempool recycling
- [[en/concepts/scarcity]] — block space as a scarce resource
- [[en/concepts/lightning-network]] — moving activity off-chain from mempool competition
