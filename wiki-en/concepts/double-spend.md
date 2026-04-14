---
title: "Double Spend"
category: "concepts"
quality: "canonical"
sources: ["https://21ideas.org/start/start", "https://21ideas.org/izobretaem-bitkoin/glava-1", "https://21ideas.org/izobretaem-bitkoin/glava-5", "https://21ideas.org/izobretaem-bitkoin/glava-6"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, security, double-spend]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## The problem

**Double spending** means using the **same money twice**. Physical cash is hard to spend twice because you hand over a token once. Digital information is easy to copy — before Bitcoin, the usual fix was a [[en/concepts/third-parties|trusted ledger keeper]] (bank, card network) that checked balances and ordering.

The beginner guide: digital money "like a computer file" could be copied; banks prevented double spends by tracking accounts.

## Bitcoin's approach

Bitcoin makes **ownership transfers public** (pseudonymous addresses, not necessarily real names) and orders them in a **single agreed history** secured by [[en/concepts/proof-of-work|Proof of Work]] and [[en/concepts/bitcoin-node|full-node validation]].

[[en/entities/satoshi-nakamoto|Satoshi]]'s forum post (quoted in [[en/books/inventing-bitcoin|*Inventing Bitcoin*]]): the P2P network acts like a **distributed timestamp server**, marking the **first spend** of a coin; information is easy to spread and hard to suppress.

**After confirmation:** blocks bury spends under **PoW**; rewriting history requires redoing that work — prohibitively expensive deep in the [[en/concepts/blockchain|chain]].

**51% context:** The sources stress that [[en/concepts/mining|miners]] **cannot** spend others' coins without valid signatures; with majority hash power, an attacker's realistic leverage is **reordering or censoring** their *own* spends — e.g. **double-spending** by building a private chain that later replaces the public one — not forging arbitrary balances.

## Unconfirmed transactions

While a transaction is only in the [[en/concepts/mempool|mempool]], acceptance is **probabilistic** — the recipient bears **zero-confirmation risk**. More confirmations reduce the probability of a chain reorganization undoing the payment.

## Sources

- [What is Bitcoin? (theory guide)](https://21ideas.org/start/start)
- [Inventing Bitcoin — Ch. 1](https://21ideas.org/izobretaem-bitkoin/glava-1)
- [Inventing Bitcoin — Ch. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Inventing Bitcoin — Ch. 6](https://21ideas.org/izobretaem-bitkoin/glava-6)

## Related pages

- [[en/concepts/bitcoin|Bitcoin — double spend as the headline problem Bitcoin solves]]
- [[en/concepts/proof-of-work|Proof of Work — ordering and confirmation via unforgeable costliness]]
- [[en/concepts/utxo|UTXO — inputs consumed exactly once per valid history]]
- [[en/concepts/mining|Mining — ordering transactions and confirming blocks]]
- [[en/concepts/mempool|Mempool — where unconfirmed transactions wait]]
- [[en/concepts/blockchain|Blockchain — the tamper-evident chain that buries past spends]]
- [[en/concepts/byzantine-generals-problem|Byzantine generals problem — agreement without trust]]
- [[en/concepts/forks|Forks — reorganizations and chain choice]]
