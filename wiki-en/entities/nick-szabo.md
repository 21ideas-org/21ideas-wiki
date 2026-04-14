---
title: "Nick Szabo"
category: "entities"
quality: "synthesized"
sources: ["https://21ideas.org/gf/genesis-1/", "https://21ideas.org/gf/genesis-4/"]
synthesized_date: "2026-04-07"
completeness: "medium"
language: "en"
tags: [bitcoin, wiki, entity, history]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## Who He Is

**Nick Szabo** is a cryptographer, computer scientist, and legal scholar who was a central figure in the [[en/entities/cypherpunks|cypherpunk]] movement. He is best known for:
- Inventing **[[en/concepts/bit-gold|Bit Gold]]** (~1998–2005) — a direct precursor to Bitcoin
- Coining the term **smart contracts** (1994)
- Writing **"Shelling Out"** — monetary anthropology tracing the origins of [[en/concepts/money|money]]
- Writing **"Money, Blockchains, and Social Scalability"** — the key theoretical defense of Bitcoin's [[en/concepts/proof-of-work|PoW]] design

Szabo is widely suspected to be [[en/entities/satoshi-nakamoto|Satoshi Nakamoto]]; he has denied it.

## Bit Gold (1998–2005)

Bit Gold was a proposed digital currency where:
1. A participant generates a proof of work (solving a cryptographic puzzle)
2. The PoW string is broadcast to the network and timestamped
3. Previous PoW strings are included in new PoW strings, creating a chain

Bit Gold solved digital scarcity through unforgeable costliness (PoW). Its unsolved problem: the chain required a trusted time-stamping service, and the value of different PoW strings was unequal (unlike satoshis). Bitcoin solved both with its [[en/concepts/blockchain|blockchain]] consensus and uniform unit.

Source: [Genesis Files, Part IV](https://21ideas.org/gf/genesis-4/)

## "Shelling Out" (2002)

A foundational essay tracing the origins of [[en/concepts/money|money]] through archaeological and anthropological evidence. Key argument: collectibles (shells, beads, rare stones) served as proto-money for hundreds of thousands of years because they had **unforgeable costliness** — they required real resources to produce, making them hard to counterfeit or inflate.

This is the theoretical foundation for why [[en/concepts/proof-of-work|PoW]] gives Bitcoin monetary value: like ancient collectibles, the costliness of [[en/concepts/mining|mining]] is what makes the token [[en/concepts/scarcity|scarce]] and trustworthy.

## "Trusted Third Parties Are Security Holes" (2001)

Szabo argues that every [[en/concepts/third-parties|trusted third party]] is a security hole: a potential point of failure, compromise, or coercion. The entire point of cryptographic protocols is to reduce or eliminate reliance on trusted parties. Bitcoin is the culmination of this principle applied to money.

## "Money, Blockchains, and Social Scalability" (2017)

Key essay defending Bitcoin's design choices. Central argument:

> "Bitcoin trades computational inefficiency for social scalability."

Money is an **institutional technology** that allows humans to cooperate beyond Dunbar's number (~150). The traditional mechanism is trusted institutions (banks, governments). Bitcoin replaces institutional trust with mathematical verification — allowing global economic cooperation without trusted intermediaries.

The computational "waste" of PoW is not waste; it is the price of eliminating trusted parties at planetary scale.

## Sources

- [Genesis Files, Part I](https://21ideas.org/gf/genesis-1/)
- [Genesis Files, Part IV](https://21ideas.org/gf/genesis-4/)

## Related pages

- [[en/entities/satoshi-nakamoto|Satoshi Nakamoto — synthesized Szabo's work into Bitcoin]]
- [[en/entities/hal-finney|Hal Finney — fellow cypherpunk]]
- [[en/entities/cypherpunks|Cypherpunks — the broader movement]]
- [[en/concepts/bit-gold|Bit Gold — Szabo's direct Bitcoin precursor]]
- [[en/concepts/proof-of-work|Proof of Work — grounded in Szabo's "unforgeable costliness"]]
- [[en/concepts/money|Money — informed by "Shelling Out"]]
- [[en/concepts/third-parties|Third Parties — "Trusted Third Parties Are Security Holes"]]
- [[en/series/genesis-files|Genesis Files — Bit Gold as Bitcoin precursor]]
