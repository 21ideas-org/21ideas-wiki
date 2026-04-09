---
title: "Byzantine Generals Problem"
category: concepts
tags: [bitcoin, wiki, distributed-systems, consensus, security]
language: en
quality: reference
sources:
  - "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8"
synthesized_date: "2026-04-09"
completeness: medium
---

# Byzantine Generals Problem

*Tags: distributed consensus, trust minimization*

---

## What it is (in the 21ideas framing)

The **Byzantine generals problem** is a classic formulation in distributed systems: how can participants **agree on true state** when they **do not know or trust** each other, and when some actors may **lie** or **fail**?

*Sovereignty Through Mathematics* states plainly: in the author’s view, the **Bitcoin blockchain’s job** under consensus rules is to solve this problem — enabling **trust-minimized agreement** on valid information flowing through the network.

The same chapter cautions: **“blockchain” alone** does not guarantee decentralization; **Bitcoin** is the substantive innovation — treat generic blockchain marketing skeptically.

Source: `raw/Books/Suverenitet-posredstvom-matematiki/chapter-8.md`

---

## How Bitcoin maps to it

Bitcoin combines:

- **Explicit rules** (script, signatures, inflation schedule, etc.) every **full node** can enforce locally
- **Proof of Work** to make **one global ordering** expensive to forge
- **Economic alignment** so rewriting deep history costs more than honest mining under normal assumptions

See [[en/concepts/proof-of-work]], [[en/concepts/governance]], and [[en/concepts/double-spend]] for the operational details.

---

## Sources

- [Sovereignty Through Mathematics — Ch. 8](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/governance|governance]] | [[en/concepts/double-spend|double spend]] | [[en/concepts/blockchain|blockchain]]

## Related Pages

- [[en/concepts/bitcoin]] — system overview
- [[en/concepts/proof-of-work]] — Sybil resistance and ordering
- [[en/concepts/double-spend]] — the monetary-specific attack
- [[en/concepts/decentralization]] — why “no leader” is hard
- [[en/books/sovereignty-through-mathematics]] — full book context
