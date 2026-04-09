---
title: "Bitcoin Whitepaper"
category: concepts
quality: reference
sources:
  - "https://21ideas.org/whitepaper"
synthesized_date: "2026-04-09"
completeness: medium
language: en
tags: [bitcoin, wiki, whitepaper, satoshi, history, protocol, reference]
---

# Bitcoin Whitepaper

The **Bitcoin whitepaper** is the short technical document published by [[en/entities/satoshi-nakamoto|Satoshi Nakamoto]] on October 31, 2008, describing a “peer-to-peer electronic cash system.” In the 21ideas sources, it is treated as a **historical artifact** and an important conceptual entry-point — but not a full specification of Bitcoin as implemented.

## What it is (and what it is not)

From the 21ideas framing, the whitepaper is:

- A compact description of the core idea that became Bitcoin.
- A document that intentionally leaves out details and later-evolved terminology.

It is **not**:

- A comprehensive “protocol spec” that fully defines modern Bitcoin behavior.
- A complete map of every property Bitcoin ended up having in practice.

## Notable facts highlighted by the sources

The `raw/Books/whitepaper.md` source emphasizes several practical observations:

- The paper is short (a few thousand words) but triggered substantial early discussion.
- The term “blockchain” is absent; the paper describes a “timestamp server” instead.
- The paper cites earlier digital-money attempts, including **b-money** and **Hashcash**.

These points matter in the wiki because they connect the whitepaper to:

- [[en/concepts/blockchain]] — and why the sources prefer Bitcoin-specific language over “blockchain” hype.
- [[en/concepts/b-money]] and [[en/entities/adam-back|Adam Back]] (Hashcash) as precursors.

## Whitepaper vs. implementation reality

The source explicitly notes that developers maintain lists of known issues and terminological shifts between the paper and the real system, which is one reason 21ideas treats the document as **foundational but incomplete**.

This also connects to the idea that Bitcoin is enforced by what nodes run and validate in practice, not by any single PDF.

See:

- [[en/concepts/bitcoin-node]] — nodes validate the rules.
- [[en/concepts/bitcoin-core]] — the dominant implementation is an implementation, not the protocol itself.
- [[en/concepts/governance]] — upgrades happen socially + technically through adoption.

---

## Sources

- [Whitepaper (21ideas page)](https://21ideas.org/whitepaper)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/bitcoin|Bitcoin]] | [[en/entities/satoshi-nakamoto|Satoshi Nakamoto]] | [[en/concepts/blockchain|blockchain]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/b-money|b-money]] | [[en/concepts/hashcash|Hashcash]]

## Related Pages

- [[en/concepts/b-money]] — cited precursor; “first draft” framing in the sources
- [[en/concepts/bit-gold]] — near-miss precursor in the Genesis Files framing
- [[en/concepts/rpow]] — implemented prototype precursor; why centralization still mattered
- [[en/entities/adam-back]] — Hashcash; explicitly cited in the paper per the sources
- [[en/entities/david-chaum]] — eCash as the privacy-forward centralized predecessor
