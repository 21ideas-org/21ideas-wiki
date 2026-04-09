---
title: "Bitcoin Core"
category: concepts
tags: [bitcoin, wiki, bitcoin-core, full-node, software, open-source, governance, upgrades]
quality: reference
sources:
  - "https://21ideas.org/kto-kontroliruet-bitkoin-kor/"
  - "https://21ideas.org/izobretaem-bitkoin/glava-8"
  - "https://21ideas.org/o-zakostenenii-protokola"
synthesized_date: "2026-04-09"
completeness: high
language: en
---

# Bitcoin Core

*Tags: implementation, full node software, open source, upgrades*

---

## What Bitcoin Core is (and is not)

The sources consistently draw a line between:

- **Bitcoin (the protocol / rules)** — what nodes enforce ([[en/concepts/governance]])
- **Bitcoin Core (a software implementation)** — the most widely used codebase that implements those rules

“Who controls Bitcoin Core?” argues Core is best understood as a **coordination hub for development**, not a governing body. If Core disappeared, development could move elsewhere; users are not forced to run any update.

Source: `raw/Theory/protocol/who-controls-bitcoin-core.md`

---

## Why it dominates in practice

*Inventing Bitcoin* notes there are many implementations, but most nodes converge on Bitcoin Core because consensus failures are catastrophic: if two implementations interpret rules differently, the network can split.

The Lopp article adds two practical reasons:

- There is no complete written “spec”; the most widely used implementation becomes the safest reference point.
- Core concentrates the most review, testing, and operational hardening.

Sources: `raw/Books/izobretaem-bitkoin/glava-8.md`, `raw/Theory/protocol/who-controls-bitcoin-core.md`

---

## How changes flow (BIPs, review, and releases)

The sources emphasize that code changes are:

- Proposed publicly (pull requests)
- Reviewed by many contributors
- Merged by maintainers with limited privileges
- Distributed as releases — but **no auto-update** is imposed on node operators

This sits inside the broader upgrade process described as BIPs and soft forks / hard forks.

See [[en/concepts/bip]] and [[en/concepts/forks]].

Source: `raw/Theory/protocol/who-controls-bitcoin-core.md`, `raw/Books/izobretaem-bitkoin/glava-8.md`

---

## Maintainers, signatures, and “don’t trust GitHub”

The “who controls” article highlights a security posture: GitHub itself is not a trust root. Maintainers sign merges with PGP keys; users and developers can verify a chain of signed merges via Core tooling (e.g., `verify-commits`).

This does not create perfect safety — but it reduces the attack surface from “anyone who can touch GitHub” to “someone who can subvert signing keys and process.”

Source: `raw/Theory/protocol/who-controls-bitcoin-core.md`

---

## Ossification vs evolution (why this matters)

“On ossification” frames a tension: as a protocol grows, coordinating changes becomes harder; prematurely freezing change can push complexity to higher layers and reintroduce trust and centralization. The article argues for careful, consensus-driven evolution rather than forced stasis.

Source: `raw/Theory/protocol/on-ossification.md`

---

## Sources

- [Who controls Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/)
- [Inventing Bitcoin — Ch. 8 (rules and implementations)](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [On ossification](https://21ideas.org/o-zakostenenii-protokola)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/governance|governance]] | [[en/concepts/bip|BIP]] | [[en/concepts/forks|forks]] | [[en/concepts/bitcoin-node|Bitcoin node]] | [[en/practice/running-a-node|running a node]]

## Related Pages

- [[en/concepts/governance]] — who enforces rules (and who doesn’t)
- [[en/concepts/bitcoin-node]] — what a node does vs miners
- [[en/concepts/bip]] — proposals and activation context
- [[en/concepts/forks]] — incompatible rule changes and chain splits
- [[en/concepts/third-parties]] — why verification removes TTP risk
