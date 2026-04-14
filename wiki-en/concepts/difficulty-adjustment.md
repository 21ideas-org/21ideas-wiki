---
title: "Difficulty Adjustment"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/difficulty/", "https://21ideas.org/mining-walkthrough", "https://21ideas.org/izobretaem-bitkoin/glava-4"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, mining, difficulty-adjustment]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## Purpose

**Difficulty adjustment** keeps Bitcoin's average **block interval near ~10 minutes** despite unpredictable **hash rate** ([[en/concepts/mining|miners]] joining or leaving). Every **2,016 blocks** (~two weeks at target), [[en/concepts/bitcoin-node|nodes]] recalculate the **[[en/concepts/proof-of-work|PoW]] target** from observed **block timestamps**.

It is presented in the sources as **underappreciated** but essential: it stabilizes **issuance predictability**, aligns **incentives**, and is a core **consensus** mechanism.

## Mechanics (simplified)

- Miners hash block headers until they find a value **below the current target** (often visualized as a hash with leading zeros).
- **Target** and **difficulty** are two views of the same requirement: smaller target ⇒ harder mining.
- **Retarget:** compare actual time for the last 2,016 blocks to the **expected** 2,016 × 10 minutes; scale difficulty so the next period trends back toward the target interval.
- **Hash rate is not measured directly** — only **inter-block times** (from timestamps) inform the adjustment, so it is **statistical**, not exact science.

The [difficulty article](https://21ideas.org/difficulty/) notes **historical extremes** (large up/down jumps) as illustrations of how aggressively the algorithm can respond.

## Security and stability

Together with **[[en/concepts/proof-of-work|PoW]]**, adjustment makes sudden **hash rate drops** (e.g. geographic bans) survivable: difficulty **falls** after the period, restoring block production toward the schedule without manual intervention.

See [[en/concepts/mining|mining]] for the full mining loop and [[en/concepts/scarcity|scarcity]] for issuance.

## Sources

- [On Bitcoin mining difficulty adjustment](https://21ideas.org/difficulty/)
- [Mining walkthrough](https://21ideas.org/mining-walkthrough)
- [Inventing Bitcoin — Ch. 4 (mining)](https://21ideas.org/izobretaem-bitkoin/glava-4)

## Related pages

- [[en/concepts/mining|Mining — nonces, pools, block rewards, and the full mining loop]]
- [[en/concepts/proof-of-work|Proof of Work — why energy binds security to time]]
- [[en/concepts/scarcity|Scarcity — predictable new supply enforced by the halving schedule]]
- [[en/concepts/blockchain|Blockchain — chaining work across time]]
- [[en/concepts/bitcoin-node|Bitcoin node — nodes that recalculate the target each period]]
