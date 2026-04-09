---
title: "Difficulty Adjustment"
category: concepts
tags: [bitcoin, wiki, mining, protocol, consensus]
language: en
quality: reference
sources:
  - "https://21ideas.org/difficulty/"
  - "https://21ideas.org/mining-walkthrough"
  - "https://21ideas.org/izobretaem-bitkoin/glava-4"
synthesized_date: "2026-04-09"
completeness: high
---

# Difficulty Adjustment

*Tags: block time, retargeting, PoW target*

---

## Purpose

**Difficulty adjustment** keeps Bitcoin’s average **block interval near ~10 minutes** despite unpredictable **hash rate** (miners joining or leaving). Every **2,016 blocks** (~two weeks at target), nodes recalculate the **PoW target** from observed **block timestamps**.

It is presented in the sources as **underappreciated** but essential: it stabilizes **issuance predictability**, aligns **incentives**, and is a core **consensus** mechanism.

Sources: `raw/Theory/protocol/difficulty.md`, `raw/Books/izobretaem-bitkoin/glava-4.md`

---

## Mechanics (simplified)

- Miners hash block headers until they find a value **below the current target** (often visualized as a hash with leading zeros).
- **Target** and **difficulty** are two views of the same requirement: smaller target ⇒ harder mining.
- **Retarget:** compare actual time for the last 2,016 blocks to the **expected** 2,016 × 10 minutes; scale difficulty so the next period trends back toward the target interval.
- **Hash rate is not measured directly** — only **inter-block times** (from timestamps) inform the adjustment, so it is **statistical**, not exact science.

The article notes **historical extremes** (large up/down jumps) as illustrations of how aggressively the algorithm can respond.

Source: `raw/Theory/protocol/difficulty.md`

---

## Security and stability

Together with **PoW**, adjustment makes sudden **hash rate drops** (e.g. geographic bans) survivable: difficulty **falls** after the period, restoring block production toward the schedule without manual intervention.

See [[en/concepts/mining]] for the full mining loop and [[en/concepts/scarcity]] for issuance.

---

## Sources

- [On Bitcoin mining difficulty adjustment](https://21ideas.org/difficulty/)
- [Mining walkthrough](https://21ideas.org/mining-walkthrough)
- [Inventing Bitcoin — Ch. 4 (mining)](https://21ideas.org/izobretaem-bitkoin/glava-4)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/mining|mining]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/scarcity|halving / issuance]] | [[en/concepts/bitcoin|Bitcoin]]

## Related Pages

- [[en/concepts/mining]] — nonces, pools, block rewards
- [[en/concepts/proof-of-work]] — why energy binds security to time
- [[en/concepts/scarcity]] — predictable new supply
- [[en/concepts/blockchain]] — chaining work across time
