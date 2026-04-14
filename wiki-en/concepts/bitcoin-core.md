---
title: "Bitcoin Core"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/kto-kontroliruet-bitkoin-kor/", "https://21ideas.org/izobretaem-bitkoin/glava-8", "https://21ideas.org/o-zakostenenii-protokola"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, governance, node]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## What Bitcoin Core is (and is not)

The sources consistently draw a line between:

- **Bitcoin (the protocol / rules)** — what [[en/concepts/bitcoin-node|nodes]] enforce ([[en/concepts/governance|governance]])
- **Bitcoin Core (a software implementation)** — the most widely used codebase that implements those rules

[Who controls Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/) argues Core is best understood as a **coordination hub for development**, not a governing body. If Core disappeared, development could move elsewhere; users are not forced to run any update.

## Why it dominates in practice

[[en/books/inventing-bitcoin|*Inventing Bitcoin*]] notes there are many implementations, but most nodes converge on Bitcoin Core because consensus failures are catastrophic: if two implementations interpret rules differently, the network can split.

The Lopp article adds two practical reasons:

- There is no complete written "spec"; the most widely used implementation becomes the safest reference point.
- Core concentrates the most review, testing, and operational hardening.

Source: [Who controls Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/)

## How changes flow (BIPs, review, and releases)

The sources emphasize that code changes are:

- Proposed publicly (pull requests)
- Reviewed by many contributors
- Merged by maintainers with limited privileges
- Distributed as releases — but **no auto-update** is imposed on node operators

This sits inside the broader upgrade process described as [[en/concepts/bip|BIPs]] and [[en/concepts/forks|soft forks / hard forks]].

## Maintainers, signatures, and "don't trust GitHub"

The [Who controls Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/) article highlights a security posture: GitHub itself is not a trust root. Maintainers sign merges with PGP keys; users and developers can verify a chain of signed merges via Core tooling (e.g., `verify-commits`).

This does not create perfect safety — but it reduces the attack surface from "anyone who can touch GitHub" to "someone who can subvert signing keys and process."

## Ossification vs evolution (why this matters)

[On ossification](https://21ideas.org/o-zakostenenii-protokola) frames a tension: as a protocol grows, coordinating changes becomes harder; prematurely freezing change can push complexity to higher layers and reintroduce trust and [[en/concepts/decentralization|centralization]]. The article argues for careful, consensus-driven evolution rather than forced stasis.

## Sources

- [Who controls Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/)
- [Inventing Bitcoin — Ch. 8 (rules and implementations)](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [On ossification](https://21ideas.org/o-zakostenenii-protokola)

## Related pages

- [[en/concepts/governance|Governance — who enforces rules (and who doesn't)]]
- [[en/concepts/bitcoin-node|Bitcoin node — what a node does vs miners]]
- [[en/concepts/bip|BIP — proposals and activation context]]
- [[en/concepts/forks|Forks — incompatible rule changes and chain splits]]
- [[en/concepts/third-parties|Third parties — why verification removes trusted third party risk]]
- [[en/practice/running-a-node|Running a node — practical guide to running Bitcoin Core]]
