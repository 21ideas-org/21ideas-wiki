---
title: "Proof of Work"
category: concepts
tags: [bitcoin, wiki, protocol, consensus, mining]
updated: "2026-04-07"
quality: reference
sources: ["https://21ideas.org/proof-of-work"]
synthesized_date: "2026-04-07"
completeness: high
---

# Proof of Work

*Tags: protocol, mining, consensus, security*

---

## What It Is

Proof of Work (PoW) is the consensus mechanism that secures [[concepts/bitcoin|Bitcoin]]. Miners compete to add new blocks by repeatedly hashing block data until their hash meets a difficulty target (starts with a certain number of zeros). The only way to find a valid hash is brute-force guessing — there is no shortcut.

When a valid block is found, the miner broadcasts it to the network and collects the [[concepts/scarcity|block reward]] + transaction fees. All other nodes verify the PoW and accept the block.

---

## Why It Matters

PoW anchors digital money to the physical world. Every valid block represents real energy expenditure — this expenditure cannot be faked or undone. [[entities/satoshi-nakamoto|Satoshi]]'s key insight: **unforgeable costliness** is what gives digital [[concepts/scarcity|scarcity]] meaning.

Adam Gibson's framing: PoW is like a court system for digital money. Physical enforcement makes cheating expensive. PoW makes rewriting history expensive — you would have to redo all the work of all blocks since the target, faster than the honest chain grows.

Source: `raw/Theory/protocol/proof-of-work.md`

---

## Hashcash: The Precursor

Adam Back invented [[concepts/hashcash|Hashcash]] in 1997 as an anti-spam tool. To send an email, you had to compute a proof of work — a small cost per email that is negligible for humans but catastrophic for spammers at scale. [[entities/satoshi-nakamoto|Satoshi]] adapted this concept directly for Bitcoin.

Source: [[series/genesis-files]]

---

## Difficulty Adjustment

Every 2,016 blocks (~2 weeks), the network adjusts the difficulty target so that blocks continue to arrive at ~10 minutes on average, regardless of how many miners join or leave. This is Bitcoin's homeostasis — it self-regulates without any central coordinator.

If [[concepts/mining|hash rate]] doubles, blocks would come every 5 minutes until adjustment. If half the miners quit, blocks slow to 20 minutes until adjustment. The [[concepts/mining|difficulty adjustment]] means Bitcoin is resilient to any level of miner participation.

Source: `raw/Theory/protocol/difficulty.md`

---

## The 51% Attack

If a single entity controlled more than 50% of the network's hash rate, they could:
- Double-spend their own transactions (reorg the chain)
- Prevent certain transactions from confirming

They *cannot*:
- Create new bitcoins
- Steal coins from other wallets
- Change the supply cap

Bitcoin has never experienced a successful 51% attack. With current hash rate levels, the hardware and energy cost is prohibitive.

---

## PoW vs. Proof of Stake

The sources contain a strong position on this: **Proof of Stake is not an alternative consensus mechanism — it is a validator cartel.**

Arguments against PoS:
- PoS cannot achieve genuine consensus without trusted initial distribution
- "Nothing at stake" problem: validators can vote for multiple forks with no cost
- Rich validators get richer (the cartel self-perpetuates)
- No physical anchor to objective reality — just social agreements all the way down

Ethereum's "difficulty bombs" (artificial increases forcing miners to migrate to PoS) demonstrate that PoS chains require coercive coordination — Bitcoin PoW does not.

Source: `raw/Theory/protocol/proof-of-stake-is-a-scam.md`, `raw/Theory/economics/only-the-strong-survive.md`

---

## Energy and Environment

The criticism that Bitcoin "wastes energy" is addressed across many sources. Key arguments:
- Bitcoin [[concepts/mining|mining]] consumes energy that has *already been produced* — often stranded, excess, or curtailed energy
- Jevons Paradox: efficiency gains in energy use tend to increase total energy consumption (not unique to Bitcoin)
- [[concepts/money|Fiat]] money infrastructure (banks, central banks, mints, armies that protect petrodollar) consumes vastly more energy
- Mining incentivizes renewable development (miners prefer cheap energy; cheapest energy is often stranded renewables)
- Energy use is the *price* of trustless monetary security; it is not waste

Source: `raw/Theory/economics/bitcoin-is-not-harmful-for-the-environment.md`, `raw/Theory/economics/gradually-then-suddenly/04-bitcoin-does-not-waste-energy.md`

---

## Sources

- [Original article on 21ideas.org](https://21ideas.org/proof-of-work)

---

## Related Terms

[[glossary|Glossary]] | [[concepts/bitcoin|Bitcoin]] | [[concepts/scarcity|scarcity]] | [[concepts/mining|mining]] | [[concepts/governance|governance]] | [[concepts/hashcash|Hashcash]] | [[entities/satoshi-nakamoto|Satoshi Nakamoto]] | [[entities/hal-finney|Hal Finney]] | [[entities/cypherpunks|cypherpunks]]

## Related Pages

- [[concepts/bitcoin]] — the system PoW secures
- [[concepts/scarcity]] — PoW enables digital scarcity
- [[entities/satoshi-nakamoto]] — adapted Hashcash to solve double-spend
- [[entities/hal-finney]] — RPOW (Reusable Proofs of Work)
- [[series/genesis-files]] — Adam Back and Hashcash prehistory
