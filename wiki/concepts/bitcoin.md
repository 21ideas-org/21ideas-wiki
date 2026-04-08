---
title: "Bitcoin"
category: concepts
tags: [bitcoin, wiki, fundamentals, protocol, money]
updated: "2026-04-07"
quality: canonical
sources: ["https://21ideas.org/start/start"]
synthesized_date: "2026-04-07"
completeness: high
---

# Bitcoin

*Tags: fundamentals, protocol, money*

---

## One-Line Definition

Bitcoin is a decentralized peer-to-peer electronic cash system that solves the double-spend problem without trusted intermediaries, with a fixed supply of 21 million units enforced by cryptography and network consensus.

---

## The Problem Bitcoin Solves

Before Bitcoin, digital money required a trusted third party (a bank, PayPal, etc.) to prevent double-spending — the ability to spend the same money twice. Banks maintain ledgers and can reverse transactions; this gives them power over money flows.

Bitcoin solves double-spending differently: it makes all accounts and transactions *public* without revealing personal identity. When a bitcoin is spent, it is publicly recorded in the blockchain — everyone can verify it was not spent twice. The record is maintained by a distributed network with no single point of control.

Sources: `raw/Start/start.md`, `raw/Books/izobretaem-bitkoin/`

---

## Core Properties

| Property | Description |
|----------|-------------|
| **Decentralized** | No company, government, or individual controls it |
| **Fixed supply** | 21 million BTC maximum, enforced by protocol |
| **Permissionless** | Anyone can transact without approval |
| **Censorship-resistant** | No party can block valid transactions |
| **Pseudonymous** | Transactions are public; identities are not |
| **Trustless** | No need to trust any counterparty |
| **Programmable** | Scripts enable conditional spending ([[concepts/security|multisig]], timelocks, etc.) |

---

## How It Works (High Level)

1. **Transactions** — signed messages transferring ownership of [[concepts/utxo|UTXOs]] from one address to another
2. **Mempool** — transactions broadcast to the network wait in a [[glossary|mempool]] until confirmed
3. **[[concepts/mining|Mining]]** — [[concepts/mining|miners]] compete to include transactions in a block by solving a [[concepts/proof-of-work|Proof of Work]] puzzle
4. **Blockchain** — a chain of blocks, each referencing the previous; tamper-evident by design
5. **[[concepts/governance|Full nodes]]** — nodes download and verify every block independently; they enforce the rules
6. **Consensus rules** — all nodes agree on the same rules; violations are rejected

---

## Key Numbers

| Parameter | Value |
|-----------|-------|
| Total supply | 21,000,000 BTC |
| Smallest unit | 1 satoshi = 0.00000001 BTC |
| Block time | ~10 minutes |
| [[concepts/scarcity|Halving]] interval | ~210,000 blocks (~4 years) |
| Current [[concepts/scarcity|block reward]] (2024) | 3.125 BTC |
| Last bitcoin mined | ~year 2140 |
| Difficulty adjustment | Every 2,016 blocks (~2 weeks) |

---

## Why Bitcoin Specifically

The sources are explicit: Bitcoin is not interchangeable with "crypto" or "blockchain." Bitcoin has properties that no other system has achieved:
- The longest [[concepts/proof-of-work|PoW]] chain (most security)
- Highest Lindy effect (oldest, most battle-tested)
- Fixed supply with credibly neutral [[concepts/governance|governance]]
- No pre-mine, no founder reward, no central entity

See [[philosophy/overview]] for the full argument against altcoins.

---

## Key Upgrades

| Upgrade | Date | What It Added |
|---------|------|--------------|
| [[concepts/segwit|SegWit]] | Aug 2017 | Fixed transaction malleability; enabled Lightning; ~2x block capacity |
| [[concepts/taproot|Taproot]] | Nov 2021 | [[concepts/taproot|Schnorr]] signatures, [[concepts/taproot|MAST]], improved privacy and smart contract flexibility |
| [[concepts/taproot|MuSig2]] | 2023+ | Efficient N-of-N [[concepts/taproot|Schnorr]] multisig |

---

## Sources

- [Original article on 21ideas.org](https://21ideas.org/start/start)

---

## Related Terms

[[glossary|Glossary]] | [[concepts/proof-of-work|Proof of Work]] | [[concepts/scarcity|scarcity]] | [[concepts/mining|mining]] | [[concepts/utxo|UTXO]] | [[concepts/governance|governance]] | [[concepts/segwit|SegWit]] | [[concepts/taproot|Taproot]] | [[concepts/lightning-network|Lightning Network]] | [[concepts/security|self-custody]]

## Related Pages

- [[concepts/proof-of-work]] — the consensus mechanism
- [[concepts/scarcity]] — why 21 million
- [[concepts/governance]] — who controls Bitcoin
- [[concepts/utxo]] — the accounting model
- [[concepts/protocol-stack]] — layered view of Bitcoin's architecture (P2P, base chain, Lightning, apps)
- [[entities/satoshi-nakamoto]] — the creator
- [[books/inventing-bitcoin]] — best technical primer
- [[series/gradually-then-suddenly]] — Parker Lewis's case for Bitcoin as money
