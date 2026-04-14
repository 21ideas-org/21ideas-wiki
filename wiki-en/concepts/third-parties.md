---
title: "Third Parties (and Why Bitcoin Removes Them)"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/doverennye-tretyi-storony", "https://21ideas.org/izobretaem-bitkoin/glava-2", "https://21ideas.org/21-sposob/glava-1-bitcoin-eto-ideya"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, security, censorship-resistance, third-party, decentralization]
reviewed: "2026-04-14"
---

## What the Sources Mean by "Third Parties"

In the "trusted third parties are security holes" framing ([[en/entities/nick-szabo|Nick Szabo]]), a **trusted third party (TTP)** is not "a helpful service" — it is a **security vulnerability**: a place where a protocol quietly assumes a third party will behave correctly, stay available, resist coercion, and not abuse power.

Szabo's suggested language swap is blunt and useful: "trusted" often really means **"vulnerable to."**

Source: [Trusted Third Parties Are Security Holes](https://21ideas.org/doverennye-tretyi-storony)

## Why Intermediaries Exist in Legacy Money

*Inventing Bitcoin* models banks and payment processors as centralized **ledgers** (databases) that:

- Authenticate users (accounts, passwords, [[en/concepts/aml|KYC]])
- Enforce ordering (preventing [[en/concepts/double-spend|double spending]])
- Reverse or refuse transactions

This works — but it concentrates control and creates a single point that can be coerced, hacked, censored, or used for rent extraction.

Source: [Inventing Bitcoin — Ch. 2](https://21ideas.org/izobretaem-bitkoin/glava-2)

## How Bitcoin Removes the Need to Trust Them

Bitcoin replaces "a ledger you can access only through the bank" with:

- A shared, replicated ledger ([[en/concepts/blockchain|blockchain]])
- Local verification by independent participants ([[en/concepts/governance|governance]] and [[en/practice/running-a-node|running a node]])
- Ordering secured by [[en/concepts/proof-of-work|Proof of Work]]

The point is not "no one provides services." It is that the **base layer does not require trusting a specific institution** to define balances, settle finality, or allow participation.

See also the network-wide coordination and incentive framing in "Bitcoin is an idea": Bitcoin as an unstoppable protocol-level idea that persists beyond any single organization.

Source: [21 Ways — Ch. 1: Bitcoin is an idea](https://21ideas.org/21-sposob/glava-1-bitcoin-eto-ideya)

## What Bitcoin Does *Not* Eliminate

The sources imply a crucial distinction:

- **Protocol-level** trust minimization: anyone can validate; no privileged ledger operator is required.
- **Service-level** convenience: exchanges, hosted wallets, explorers, and custodians can exist — but they reintroduce third-party risk.

This is why self-custody and running your own [[en/concepts/bitcoin-node|node]] are framed as sovereignty tools: they reduce reliance on external TTPs.

## Sources

- [Trusted Third Parties Are Security Holes](https://21ideas.org/doverennye-tretyi-storony)
- [Inventing Bitcoin — Ch. 2 (removing the intermediary)](https://21ideas.org/izobretaem-bitkoin/glava-2)
- [21 Ways — Ch. 1: Bitcoin is an idea](https://21ideas.org/21-sposob/glava-1-bitcoin-eto-ideya)

## Related pages

- [[en/concepts/bitcoin|Bitcoin — the system that eliminates trusted intermediaries at the protocol level]]
- [[en/concepts/double-spend|Double Spend — the problem legacy systems solved with trusted ledgers]]
- [[en/concepts/blockchain|Blockchain — the shared ledger that replaces institutional databases]]
- [[en/concepts/bitcoin-node|Bitcoin Node — local validation as the "don't trust, verify" mechanism]]
- [[en/concepts/bitcoin-core|Bitcoin Core — the dominant implementation (not a ruler)]]
- [[en/concepts/decentralization|Decentralization — third-party elimination as a core design principle]]
- [[en/concepts/censorship-resistance|Censorship Resistance — what removing intermediaries enables]]
- [[en/practice/running-a-node|Running a node — practical self-sovereignty]]
