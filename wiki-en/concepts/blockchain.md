---
title: "Blockchain (Bitcoin)"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/start/start", "https://21ideas.org/izobretaem-bitkoin/glava-5", "https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, security]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## What it is in Bitcoin

In Bitcoin, the **blockchain** is the **append-only ledger**: a **linear chain of blocks** from the **genesis block** to the tip, each block committing to **transactions** and linking to the **previous block hash**. That link makes history **tamper-evident** — changing an old transaction changes its block's hash, which **breaks** every later block unless **all following [[en/concepts/proof-of-work|PoW]] is redone**.

[[en/books/inventing-bitcoin|*Inventing Bitcoin*]] warns the word is **overused in marketing**; in Bitcoin it is simply the **data structure** that orders issuance and spending.

## Consensus and copies

Thousands of participants hold **identical copies** synchronized by the protocol. The **consensus algorithm** compares work; users do not vote by headcount — a single **honest** peer with the **most-work valid chain** suffices for a new node to find the **true tip** if it is not **eclipsed** from the honest network.

## Skeptical framing from the same corpus

[[en/books/sovereignty-through-mathematics|*Sovereignty Through Mathematics*]] argues the important invention is **Bitcoin's consensus rules solving the [[en/concepts/byzantine-generals-problem|Byzantine generals problem]]** — **"blockchain"** without those rules is often **hype**.

## Sources

- [What is Bitcoin? (theory guide)](https://21ideas.org/start/start)
- [Inventing Bitcoin — Ch. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Sovereignty Through Mathematics — Ch. 8](https://21ideas.org/suverenitet-posredstvom-matematiki/glava-8)

## Related pages

- [[en/concepts/bitcoin|Bitcoin — how the blockchain fits the full system]]
- [[en/concepts/mining|Mining — how new blocks are produced]]
- [[en/concepts/proof-of-work|Proof of Work — the mechanism that makes the chain tamper-evident]]
- [[en/concepts/double-spend|Double spend — what transaction ordering prevents]]
- [[en/concepts/forks|Forks — competing tips and chain reorgs]]
- [[en/concepts/mempool|Mempool — where transactions wait before inclusion]]
- [[en/concepts/bitcoin-node|Bitcoin node — who validates blocks]]
- [[en/concepts/utxo|UTXO — the accounting model stored in the chain]]
