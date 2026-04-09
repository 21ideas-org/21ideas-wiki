---
title: "Blockchain (Bitcoin)"
category: concepts
tags: [bitcoin, wiki, protocol, ledger, security]
language: en
quality: reference
sources:
  - "https://21ideas.org/start/start"
  - "https://21ideas.org/izobretaem-bitkoin/glava-5"
  - "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8"
synthesized_date: "2026-04-09"
completeness: high
---

# Blockchain (Bitcoin)

*Tags: ledger, chain of blocks, PoW, verification*

---

## What it is in Bitcoin

In Bitcoin, the **blockchain** is the **append-only ledger**: a **linear chain of blocks** from the **genesis block** to the tip, each block committing to **transactions** and linking to the **previous block hash**. That link makes history **tamper-evident** — changing an old transaction changes its block’s hash, which **breaks** every later block unless **all following PoW is redone**.

*Inventing Bitcoin* warns the word is **overused in marketing**; in Bitcoin it is simply the **data structure** that orders issuance and spending.

Sources: `raw/Books/izobretaem-bitkoin/glava-5.md`, `raw/Start/start.md`

---

## Consensus and copies

Thousands of participants hold **identical copies** synchronized by the protocol. The **consensus algorithm** compares work; users do not vote by headcount — a single **honest** peer with the **most-work valid chain** suffices for a new node to find the **true tip** if it is not **eclipsed** from the honest network.

Source: `raw/Start/start.md`, `raw/Books/izobretaem-bitkoin/glava-5.md`

---

## Skeptical framing from the same corpus

*Sovereignty Through Mathematics* argues the important invention is **Bitcoin’s consensus rules solving the Byzantine generals problem** — **“blockchain”** without those rules is often **hype**. See [[en/concepts/byzantine-generals-problem]].

Source: `raw/Books/Suverenitet-posredstvom-matematiki/chapter-8.md`

---

## Sources

- [What is Bitcoin? (theory guide)](https://21ideas.org/start/start)
- [Inventing Bitcoin — Ch. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Sovereignty Through Mathematics — Ch. 8](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/mining|mining]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/utxo|UTXO]] | [[en/concepts/double-spend|double spend]] | [[en/concepts/forks|fork / reorg]]

## Related Pages

- [[en/concepts/bitcoin]] — how blockchain fits the full system
- [[en/concepts/mining]] — how new blocks are produced
- [[en/concepts/double-spend]] — what ordering prevents
- [[en/concepts/forks]] — competing tips and reorgs
- [[en/concepts/mempool]] — transactions before inclusion
- [[en/concepts/governance]] — who validates blocks
