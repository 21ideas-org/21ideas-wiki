---
title: "Inventing Bitcoin"
author: Yan Pritzker
category: books
tags: [bitcoin, wiki, books, technical, primer]
sources: ["https://21ideas.org/izobretaem-bitkoin/", "https://21ideas.org/glossary/"]
updated: "2026-04-07"
quality: reference
synthesized_date: "2026-04-07"
completeness: high
---

# Inventing Bitcoin

*Author: Yan Pritzker | Source: `raw/Books/izobretaem-bitkoin/` | Tags: book, technical, beginner*

---

## Summary

A short (100-page) technical primer that builds Bitcoin from first principles for non-technical readers. Instead of explaining Bitcoin as it exists, Pritzker asks: "How would *you* invent Bitcoin if you were trying to solve the digital cash problem?" Each chapter introduces one piece of the puzzle.

This is one of the recommended starting points for technical understanding. The site creator Tony lists it as a top beginner book.

---

## Argument

Bitcoin's design is not arbitrary — each component exists to solve a specific problem. Understanding those problems makes the solution obvious in retrospect:

1. You need a ledger (blockchain)
2. The ledger needs to be distributed (no single point of failure)
3. You need a way to agree on the ledger without trusting anyone ([[concepts/proof-of-work|PoW]] + longest chain rule)
4. You need accounts without identity (public/private key cryptography)
5. You need to prevent inflation (fixed [[concepts/scarcity|block reward]]s + [[concepts/scarcity|halving]] schedule)
6. You need rules everyone follows (consensus rules enforced by [[concepts/governance|full nodes]])

---

## Chapters (9)

1. What is Bitcoin?
2. Eliminating intermediaries — why banks are unnecessary
3. Proof of Work — the key breakthrough
4. Mining — how blocks are created
5. Securing the ledger — why rewriting history is expensive
6. Forks and 51% attacks — consensus edge cases
7. Accounts without identity — public/private key cryptography
8. Who sets the rules — governance and consensus
9. What's next — Lightning Network and the future

---

## Key Insights

- **PoW is the key**: everything else follows from solving the double-spend problem with unforgeable costliness
- **Full nodes enforce the rules**: miners produce blocks but nodes validate them
- **The blockchain is a chain of PoW**: each block references the previous, making rewriting exponentially expensive
- **Bitcoin's rules are code, not decree**: anyone can audit the rules; no authority can override them

---

## Best For

- Technical beginners wanting to understand *how* Bitcoin works
- Engineers who want a first-principles derivation
- Readers who have basic numeracy and comfort with logical argument

---

## Sources

- [Original article on 21ideas.org](https://21ideas.org/izobretaem-bitkoin)

---

## Related Terms

[[glossary|Glossary]] | [[concepts/bitcoin|Bitcoin]] | [[concepts/proof-of-work|Proof of Work]] | [[concepts/scarcity|scarcity]] | [[concepts/governance|governance]] | [[concepts/mining|mining]] | [[concepts/utxo|UTXO]] | [[books/sovereignty-through-mathematics|Sovereignty Through Mathematics]]

## Related Pages

- [[concepts/bitcoin]] — the system explained here
- [[concepts/proof-of-work]] — chapter 3's subject
- [[concepts/governance]] — chapter 8's subject
- [[books/sovereignty-through-mathematics]] — philosophical companion
