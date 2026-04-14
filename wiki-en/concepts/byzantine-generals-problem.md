---
title: "Byzantine Generals Problem"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8"]
synthesized_date: "2026-04-09"
completeness: "medium"
language: "en"
tags: [bitcoin, wiki, concept, protocol, security]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## What it is (in the 21ideas framing)

The **Byzantine generals problem** is a classic formulation in distributed systems: how can participants **agree on true state** when they **do not know or trust** each other, and when some actors may **lie** or **fail**?

[[en/books/sovereignty-through-mathematics|*Sovereignty Through Mathematics*]] states plainly: in the author's view, the **[[en/concepts/blockchain|Bitcoin blockchain]]'s job** under consensus rules is to solve this problem — enabling **trust-minimized agreement** on valid information flowing through the network.

The same chapter cautions: **"blockchain" alone** does not guarantee decentralization; **Bitcoin** is the substantive innovation — treat generic blockchain marketing skeptically.

## How Bitcoin maps to it

Bitcoin combines:

- **Explicit rules** (script, signatures, inflation schedule, etc.) every [[en/concepts/bitcoin-node|full node]] can enforce locally
- **[[en/concepts/proof-of-work|Proof of Work]]** to make **one global ordering** expensive to forge
- **Economic alignment** so rewriting deep history costs more than honest mining under normal assumptions

See [[en/concepts/proof-of-work|Proof of Work]], [[en/concepts/governance|governance]], and [[en/concepts/double-spend|double spend]] for the operational details.

## Sources

- [Sovereignty Through Mathematics — Ch. 8](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8)

## Related pages

- [[en/concepts/bitcoin|Bitcoin — system overview]]
- [[en/concepts/blockchain|Blockchain — the data structure that implements this consensus]]
- [[en/concepts/proof-of-work|Proof of Work — Sybil resistance and global ordering]]
- [[en/concepts/double-spend|Double spend — the monetary-specific attack BGP prevents]]
- [[en/concepts/decentralization|Decentralization — why "no leader" agreement is hard]]
- [[en/concepts/governance|Governance — how Bitcoin's rules are enforced in practice]]
- [[en/books/sovereignty-through-mathematics|Sovereignty Through Mathematics — full book context]]
