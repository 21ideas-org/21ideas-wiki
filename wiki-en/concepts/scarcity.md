---
title: "Scarcity"
category: concepts
tags: [bitcoin, wiki, economics, supply, halving]
language: en
updated: "2026-04-07"
quality: reference
sources: ["https://21ideas.org/21-million-ne-podlezhit-obsuzhdeniyu/", "https://21ideas.org/pochemu-21-million/", "https://21ideas.org/bitcoin-myths/"]
synthesized_date: "2026-04-07"
completeness: high
---

# Scarcity

*Tags: economics, 21M, halving, supply*

---

## The 21 Million Cap

Bitcoin's protocol enforces a hard cap of 21 million BTC (2.1 quadrillion satoshis). This is achieved by:
- [[en/concepts/scarcity|Block rewards]] that [[en/concepts/scarcity|halve]] every ~210,000 blocks (~4 years)
- Starting at 50 BTC per block (2009), halving to 25, 12.5, 6.25, 3.125 (current, 2024)
- Last satoshi mined approximately year 2140
- After that, [[en/concepts/mining|miners]] are compensated only by transaction fees

The [[en/concepts/scarcity|21M cap]] is enforced by every [[en/concepts/governance|full node]] independently. No miner, developer, or government can change it without convincing the entire network to upgrade — and there is no economic incentive for any holder to accept inflation.

Source: `raw/Theory/economics/pochemu-21-million.md`, `raw/Theory/protocol/21-million-is-non-negotiable.md`

---

## Why 21 Million Specifically

The specific number comes from Satoshi's design: using integer satoshi arithmetic (avoiding floating point), given a 10-minute block time and the planned halving schedule, 21 million BTC is approximately what falls out. The exact number matters less than the *immutability* of whatever limit was chosen.

Robert Breedlove's framing: Bitcoin introduced a concept previously impossible in digital space — **absolute scarcity**. Anything digital can be copied. Bitcoin's [[en/concepts/scarcity|scarcity]] is not physical but cryptographic and social: the protocol + the network enforce it without any trusted party.

---

## Stock-to-Flow Ratio

| Asset | Annual Production | Stock | Stock-to-Flow |
|-------|------------------|-------|--------------|
| Gold | ~3,300 tons | ~200,000 tons | ~60x |
| Silver | ~27,000 tons | ~560,000 tons | ~20x |
| Bitcoin (2024) | ~164,250 BTC/yr | ~19.7M BTC | ~120x |
| Bitcoin (post-2028 halving) | ~82,125 BTC/yr | ~20M+ BTC | ~240x+ |

Bitcoin's stock-to-flow exceeds gold's after the 2020 halving. This is unprecedented for any monetary asset.

---

## The Halving

Every ~4 years, the block reward halves. Key halvings:
| Date | Block | Reward |
|------|-------|--------|
| Jan 2009 | Genesis | 50 BTC |
| Nov 2012 | 210,000 | 25 BTC |
| Jul 2016 | 420,000 | 12.5 BTC |
| May 2020 | 630,000 | 6.25 BTC |
| Apr 2024 | 840,000 | 3.125 BTC |
| ~2028 | 1,050,000 | 1.5625 BTC |

The halving is automatic and built into the protocol — it cannot be postponed or cancelled.

**Myths about halvings** (per `raw/Theory/protocol/myths-about-halving.md`):
- Price does not *automatically* rise after a halving (though supply shock + demand = price pressure)
- Miners will not all quit — difficulty adjusts downward if hash rate drops
- The network does not break — it adapts

---

## Digital Scarcity

Physical goods are scarce because matter is conserved. Information is not: any digital file can be copied at near-zero cost. Before Bitcoin, there was no mechanism for digital scarcity without a trusted third party maintaining the ledger.

Bitcoin creates digital scarcity through:
1. Consensus rules enforced by all [[en/concepts/governance|full nodes]]
2. [[en/concepts/proof-of-work|Proof of Work]] making history costly to rewrite
3. No central entity that can override these rules

The analogy to gold: gold is scarce because physics constrains how much exists and how fast it can be mined. Bitcoin is scarce because mathematics and cryptography constrain the protocol.

Source: `raw/Theory/economics/discovering-bitcoin/05-digital-scarcity.md`

---

## Number Zero and Bitcoin

Robert Breedlove draws a parallel between the invention of zero and Bitcoin (*The Number Zero and Bitcoin*). Zero was a paradigm-shifting concept that enabled modern mathematics. Bitcoin introduces an analogous concept: **absolute digital scarcity**. Like zero, it is both simple and revolutionary; like zero, it may take generations to appreciate.

---

## Sources

- https://21ideas.org/21-million-ne-podlezhit-obsuzhdeniyu/  
- https://21ideas.org/pochemu-21-million/  
- https://21ideas.org/bitcoin-myths/

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/bitcoin|Bitcoin]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/mining|mining]] | [[en/concepts/governance|governance]] | [[en/concepts/money|sound money]] | [[en/books/bullish-case|The Bullish Case for Bitcoin]] | [[en/books/sovereignty-through-mathematics|Sovereignty Through Mathematics]]

## Related Pages

- [[en/concepts/bitcoin]]] — the system
- [[en/concepts/proof-of-work]]] — how scarcity is enforced
- [[en/concepts/money]]] — why scarcity matters for money
- [[en/books/sovereignty-through-mathematics]]] — scarcity as core theme
- [[en/books/bullish-case]]] — scarcity as investment thesis
