---
title: "Mempool"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/izobretaem-bitkoin/glava-5", "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, mining]
reviewed: "2026-04-14"
---

## Definition

The **mempool** (memory pool) is where [[en/concepts/bitcoin-node|nodes]] keep **unconfirmed transactions** they have heard about on the network. [[en/concepts/mining|Miners]] select transactions from their mempool when building a candidate block — typically prioritizing by **fee rate** (fee per unit of [[en/concepts/scarcity|block space]]).

Source: [Inventing Bitcoin — Ch. 5](https://21ideas.org/izobretaem-bitkoin/glava-5), [Sovereignty Through Mathematics — Ch. 5](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5)

## Behavior During Reorgs

If a block is [[en/concepts/forks|orphaned]] (another chain tip wins under [[en/concepts/proof-of-work|PoW]] rules), transactions from the dropped block are returned to the mempool **if they remain valid** under the new best chain. Conflicting spends are resolved by chain rules and ordering.

Source: [Inventing Bitcoin — Ch. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)

## Not Yet "In Time" for the Network

Until included in a valid block, a transaction has **no consensus-defined timestamp** in the same sense as a confirmed spend — the network's notion of ordering is anchored in **blocks**, not the mempool alone.

## Sources

- [Inventing Bitcoin — Ch. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Sovereignty Through Mathematics — Ch. 5](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-5)

## Related pages

- [[en/concepts/mining|Mining — block construction from the mempool]]
- [[en/concepts/utxo|UTXO — what inputs/outputs miners must validate]]
- [[en/concepts/forks|Forks — stale blocks and mempool recycling]]
- [[en/concepts/scarcity|Scarcity — block space as a scarce resource]]
- [[en/concepts/difficulty-adjustment|Difficulty adjustment — how hard blocks are to mine]]
- [[en/concepts/lightning-network|Lightning Network — moving activity off-chain from mempool competition]]
- [[en/concepts/bitcoin|Bitcoin — the base protocol]]
