---
title: "Double Spend"
category: concepts
tags: [bitcoin, wiki, protocol, security, consensus]
language: en
quality: canonical
sources:
  - "https://21ideas.org/start/start"
  - "https://21ideas.org/izobretaem-bitkoin/glava-1"
  - "https://21ideas.org/izobretaem-bitkoin/glava-5"
  - "https://21ideas.org/izobretaem-bitkoin/glava-6"
synthesized_date: "2026-04-09"
completeness: high
---

# Double Spend

*Tags: digital cash, consensus, mining*

---

## The problem

**Double spending** means using the **same money twice**. Physical cash is hard to spend twice because you hand over a token once. Digital information is easy to copy — before Bitcoin, the usual fix was a **trusted ledger keeper** (bank, card network) that checked balances and ordering.

The beginner guide: digital money “like a computer file” could be copied; banks prevented double spends by tracking accounts.

Source: `raw/Start/start.md`

---

## Bitcoin’s approach

Bitcoin makes **ownership transfers public** (pseudonymous addresses, not necessarily real names) and orders them in a **single agreed history** secured by **Proof of Work** and **full-node validation**.

Satoshi’s forum post (quoted in *Inventing Bitcoin*): the P2P network acts like a **distributed timestamp server**, marking the **first spend** of a coin; information is easy to spread and hard to suppress.

**After confirmation:** blocks bury spends under **PoW**; rewriting history requires redoing that work — prohibitively expensive deep in the chain.

**51% context:** The sources stress that miners **cannot** spend others’ coins without valid signatures; with majority hash power, an attacker’s realistic leverage is **reordering or censoring** their *own* spends — e.g. **double-spending** by building a private chain that later replaces the public one — not forging arbitrary balances.

Sources: `raw/Start/start.md`, `raw/Books/izobretaem-bitkoin/glava-1.md`, `raw/Books/izobretaem-bitkoin/glava-5.md`, `raw/Books/izobretaem-bitkoin/glava-6.md`, `raw/Books/vojna-za-razmer-bloka/glava-7.md`

---

## Unconfirmed transactions

While a transaction is only in the **mempool**, acceptance is **probabilistic** — the recipient bears **zero-confirmation risk**. More confirmations reduce the probability of a chain reorganization undoing the payment.

---

## Sources

- [What is Bitcoin? (theory guide)](https://21ideas.org/start/start)
- [Inventing Bitcoin — Ch. 1](https://21ideas.org/izobretaem-bitkoin/glava-1)
- [Inventing Bitcoin — Ch. 5](https://21ideas.org/izobretaem-bitkoin/glava-5)
- [Inventing Bitcoin — Ch. 6](https://21ideas.org/izobretaem-bitkoin/glava-6)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/utxo|UTXO]] | [[en/concepts/mining|mining]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/mempool|mempool]] | [[en/concepts/blockchain|blockchain]]

## Related Pages

- [[en/concepts/bitcoin]] — double spend as the headline problem solved
- [[en/concepts/utxo]] — inputs consumed once per valid history
- [[en/concepts/mining]] — ordering and confirmation
- [[en/concepts/byzantine-generals-problem]] — agreement without trust
- [[en/concepts/forks]] — reorganizations and chain choice
