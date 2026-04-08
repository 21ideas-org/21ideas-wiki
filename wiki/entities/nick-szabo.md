---
title: "Nick Szabo"
category: entities
tags: [bitcoin, wiki, cypherpunks, history, entities]
source: "Synthesized from raw/ sources + glossary"
updated: "2026-04-07"
quality: synthesized
sources: []
synthesized_date: "2026-04-07"
completeness: medium
---

# Nick Szabo

*Tags: entity, person, cypherpunk, Bit-Gold, smart-contracts*

---

## Who He Is

[[entities/nick-szabo|Nick Szabo]] is a cryptographer, computer scientist, and legal scholar who was a central figure in the [[entities/cypherpunks|cypherpunk]] movement. He is best known for:
- Inventing **Bit Gold** (~1998–2005) — a direct precursor to Bitcoin
- Coining the term **smart contracts** (1994)
- Writing **"Shelling Out"** — monetary anthropology tracing the origins of [[concepts/money|money]]
- Writing **"Money, Blockchains, and Social Scalability"** — the key theoretical defense of Bitcoin's [[concepts/proof-of-work|PoW]] design

Szabo is widely suspected to be [[entities/satoshi-nakamoto|Satoshi Nakamoto]]; he has denied it.

---

## Bit Gold (1998–2005)

Bit Gold was a proposed digital currency where:
1. A participant generates a proof of work (solving a cryptographic puzzle)
2. The PoW string is broadcast to the network and timestamped
3. Previous PoW strings are included in new PoW strings, creating a chain

Bit Gold solved digital scarcity through unforgeable costliness (PoW). Its unsolved problem: the chain required a trusted time-stamping service, and the value of different PoW strings was unequal (unlike satoshis). Bitcoin solved both with its blockchain consensus and uniform unit.

Source: [[series/genesis-files]]

---

## "Shelling Out" (2002)

A foundational essay tracing the origins of [[concepts/money|money]] through archaeological and anthropological evidence. Key argument: collectibles (shells, beads, rare stones) served as proto-money for hundreds of thousands of years because they had **unforgeable costliness** — they required real resources to produce, making them hard to counterfeit or inflate.

This is the theoretical foundation for why [[concepts/proof-of-work|PoW]] gives Bitcoin monetary value: like ancient collectibles, the costliness of [[concepts/mining|mining]] is what makes the token [[concepts/scarcity|scarce]] and trustworthy.

Source: `raw/Theory/history/shelling-out.md`

---

## "Trusted Third Parties Are Security Holes" (2001)

Szabo argues that every trusted third party is a security hole: a potential point of failure, compromise, or coercion. The entire point of cryptographic protocols is to reduce or eliminate reliance on trusted parties. Bitcoin is the culmination of this principle applied to money.

Source: `raw/Theory/economics/trusted-third-parties.md`

---

## "Money, Blockchains, and Social Scalability" (2017)

Key essay defending Bitcoin's design choices. Central argument:

> "Bitcoin trades computational inefficiency for social scalability."

Money is an **institutional technology** that allows humans to cooperate beyond Dunbar's number (~150). The traditional mechanism is trusted institutions (banks, governments). Bitcoin replaces institutional trust with mathematical verification — allowing global economic cooperation without trusted intermediaries.

The computational "waste" of PoW is not waste; it is the price of eliminating trusted parties at planetary scale.

Source: `raw/Theory/economics/money-blockchains-and-social-scalability.md`

---

## Sources

*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source article.*

---

## Related Terms

[[glossary|Glossary]] | [[concepts/proof-of-work|Proof of Work]] | [[concepts/money|money]] | [[concepts/scarcity|scarcity]] | [[entities/satoshi-nakamoto|Satoshi Nakamoto]] | [[entities/hal-finney|Hal Finney]] | [[entities/cypherpunks|cypherpunks]] | [[series/genesis-files|Genesis Files]]

## Related Pages

- [[entities/satoshi-nakamoto]] — synthesized Szabo's work into Bitcoin
- [[entities/hal-finney]] — fellow cypherpunk
- [[entities/cypherpunks]] — the broader movement
- [[concepts/proof-of-work]] — grounded in Szabo's "unforgeable costliness"
- [[concepts/money]] — informed by "Shelling Out"
- [[series/genesis-files]] — Bit Gold as Bitcoin precursor
