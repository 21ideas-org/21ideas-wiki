---
title: "Third Parties (and Why Bitcoin Removes Them)"
category: concepts
tags: [bitcoin, wiki, trust, third-parties, intermediaries, security, censorship-resistance]
quality: reference
sources:
  - "https://21ideas.org/doverennye-tretyi-storony"
  - "https://21ideas.org/izobretaem-bitkoin/glava-2"
  - "https://21ideas.org/21-sposob/glava-1-bitcoin-eto-ideya"
synthesized_date: "2026-04-09"
completeness: high
language: en
---

# Third Parties (and Why Bitcoin Removes Them)

*Tags: trust, intermediaries, security holes, censorship*

---

## What the sources mean by “third parties”

In the “trusted third parties are security holes” framing (Nick Szabo), a **trusted third party (TTP)** is not “a helpful service” — it is a **security vulnerability**: a place where a protocol quietly assumes a third party will behave correctly, stay available, resist coercion, and not abuse power.

Szabo’s suggested language swap is blunt and useful: “trusted” often really means **“vulnerable to.”**

Source: `raw/Theory/protocol/trusted-third-parties.md`

---

## Why intermediaries exist in legacy money

*Inventing Bitcoin* models banks and payment processors as centralized **ledgers** (databases) that:

- Authenticate users (accounts, passwords, KYC)
- Enforce ordering (preventing double spending)
- Reverse or refuse transactions

This works — but it concentrates control and creates a single point that can be coerced, hacked, censored, or used for rent extraction.

Source: `raw/Books/izobretaem-bitkoin/glava-2.md`

---

## How Bitcoin removes the need to trust them

Bitcoin replaces “a ledger you can access only through the bank” with:

- A shared, replicated ledger ([[en/concepts/blockchain]])
- Local verification by independent participants ([[en/concepts/governance]] and [[en/practice/running-a-node]])
- Ordering secured by [[en/concepts/proof-of-work|Proof of Work]]

The point is not “no one provides services.” It is that the **base layer does not require trusting a specific institution** to define balances, settle finality, or allow participation.

See also the network-wide coordination and incentive framing in “Bitcoin is an idea”: Bitcoin as an unstoppable protocol-level idea that persists beyond any single organization.

Source: `raw/Books/21-sposob/glava-1-bitcoin-eto-ideya.md`

---

## What Bitcoin does *not* eliminate

The sources imply a crucial distinction:

- **Protocol-level** trust minimization: anyone can validate; no privileged ledger operator is required.
- **Service-level** convenience: exchanges, hosted wallets, explorers, and custodians can exist — but they reintroduce third-party risk.

This is why self-custody and running your own node are framed as sovereignty tools: they reduce reliance on external TTPs.

---

## Sources

- [Trusted Third Parties Are Security Holes](https://21ideas.org/doverennye-tretyi-storony)
- [Inventing Bitcoin — Ch. 2 (removing the intermediary)](https://21ideas.org/izobretaem-bitkoin/glava-2)
- [21 Ways — Ch. 1: Bitcoin is an idea](https://21ideas.org/21-sposob/glava-1-bitcoin-eto-ideya)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/bitcoin|Bitcoin]] | [[en/concepts/double-spend|double spend]] | [[en/concepts/governance|governance]] | [[en/concepts/decentralization|decentralization]] | [[en/concepts/censorship-resistance|censorship resistance]] | [[en/concepts/security|security]] | [[en/concepts/privacy|privacy]]

## Related Pages

- [[en/concepts/double-spend]] — why legacy systems rely on ledger keepers
- [[en/concepts/governance]] — nodes enforce rules; no one can force upgrades
- [[en/concepts/bitcoin-node]] — why local validation matters
- [[en/concepts/bitcoin-core]] — Core as the dominant implementation (not a ruler)
- [[en/practice/running-a-node]] — practical “don’t trust, verify”
