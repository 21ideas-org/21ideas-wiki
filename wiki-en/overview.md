---
title: "Overview: Bitcoin Knowledge Synthesis"
category: overview
tags: [bitcoin, wiki, synthesized]
language: en
source: "Synthesized from raw/ sources + glossary"
updated: "2026-04-10"
quality: canonical
sources: []
synthesized_date: "2026-04-10"
completeness: high
---

# Overview: Bitcoin Knowledge Synthesis

*A synthesis of the 21ideas.org source library — ~308 articles, 8 books, multiple article series.*

> This page describes the **English** wiki (`wiki-en/`). A parallel **Russian** wiki lives in `wiki-ru/`: same `raw/` sources and schema, but Russian pages are not word-for-word translations of the English text. 

---

## What This Knowledge Base Is About

21ideas.org is a Russian-language Bitcoin education platform. Its source library covers Bitcoin from every angle: philosophy, economics, technical protocol, history, and practical self-custody. The material skews toward Bitcoin maximalism (Bitcoin only, not crypto), Austrian economics, cypherpunk philosophy, and privacy-focused self-sovereignty.

---

## The Core Argument (Synthesized)

**Bitcoin is the first money in history that no one can inflate, confiscate, or censor — and this matters more than most people realize.**

The argument builds in layers:

**1. Fiat money is broken by design.**
Central banks create [[en/concepts/money|fiat]] money by decree. This inflates away savings, enables wars, subsidizes bad banks, and distorts economic signals. The fiat system is not a neutral technology — it is a political tool. See: [[en/books/fiat-standard|The Fiat Standard]], [[en/concepts/money|Money]], [[en/history/timeline|Timeline]].

**2. Bitcoin solves the double-spend problem without trusted intermediaries.**
Before Bitcoin, digital money required banks to track who owns what. Bitcoin uses [[en/concepts/proof-of-work|Proof of Work]] and a public ledger so that anyone can verify ownership without trusting anyone. This is [[en/entities/satoshi-nakamoto|Satoshi]]'s breakthrough. See: [[en/entities/satoshi-nakamoto|Satoshi Nakamoto]], [[en/books/inventing-bitcoin|Inventing Bitcoin]].

**3. 21 million is not negotiable.**
The hard cap is enforced by math and network consensus, not by any company or government. [[en/concepts/scarcity|Scarcity]] — unlike gold, oil, or fiat — is *absolute* in Bitcoin. The [[en/concepts/scarcity|21M cap]] is enforced by every [[en/concepts/governance|full node]]. See: [[en/concepts/scarcity|Scarcity]], [[en/concepts/governance|Governance]].

**4. Bitcoin is the culmination of cypherpunk ideas developed over 20 years.**
eCash → Hashcash → b-money → Bit Gold → RPOW → Bitcoin. Each precursor solved some problems, left others. [[en/entities/satoshi-nakamoto|Satoshi]] read all of them and synthesized them into a working system. See: [[en/entities/cypherpunks|Cypherpunks]], [[en/series/genesis-files|Genesis Files]], [[en/history/pre-bitcoin-cypherpunks|Pre-Bitcoin cypherpunks]].

**5. Privacy and self-custody are not optional extras — they are the point.**
If you trust a third party with your bitcoin, you do not have Bitcoin — you have an IOU. If your transactions are tracked, financial freedom is an illusion. See: [[en/concepts/privacy|Privacy]], [[en/concepts/security|Security]], [[en/practice/storage|Storage]], [[en/practice/privacy-practice|Privacy practice]].

**6. Lightning Network extends Bitcoin to everyday payments.**
On-chain Bitcoin is slow and expensive for small payments. The [[en/concepts/lightning-network|Lightning Network]] adds instant, near-free micropayments as a second layer, without changing Bitcoin's base rules. [[en/concepts/segwit|SegWit]] (2017) was the prerequisite that enabled it.

**7. Altcoins are not alternatives — they are distractions.**
Proof-of-Stake systems cannot actually achieve consensus (the "validator cartel" problem). Every altcoin reintroduces centralization, trusted parties, or inflation. The sources are explicit: Bitcoin, not crypto. See: [[en/philosophy/overview|Philosophy overview]], [[en/concepts/proof-of-work|Proof of Work]].

---

## Key Tension: Accessibility vs. Sovereignty

A recurring tension in the source material: the easiest Bitcoin experience (custodial exchanges, KYC, custodial Lightning wallets) is antithetical to Bitcoin's purpose. The site pushes hard toward self-custody, no-KYC acquisition, and running your own node — while acknowledging this is harder than just buying on an exchange.

---

## Strongest Original Sources (by influence across the library)

| Source | Theme | Key Insight |
|--------|-------|-------------|
| Parker Lewis — *Gradually, Then Suddenly* | Monetary theory | Bitcoin critiques are backwards; Bitcoin IS money |
| Giacomo Zucco — *Discovering Bitcoin* | History of money | 7-step logical derivation from barter to Lightning |
| Aaron van Wirdum — *Genesis Files* | Cypherpunk history | Bitcoin's intellectual lineage: 20 years of failed predecessors |
| Nick Szabo — *Shelling Out* | Monetary anthropology | Money emerged spontaneously; unforgeable costliness is the key |
| Nick Szabo — *Social Scalability* | Protocol design | Bitcoin is computationally wasteful but socially efficient |
| Gigi — *21 Ways* | Philosophy | 21 frames for understanding Bitcoin |
| Saifedean Ammous — *Fiat Standard* | Macroeconomics | Fiat money analyzed as an engineering failure |
| Alex Gladstein — *Petrodollar / Structural Adjustment* | Geopolitics | USD hegemony harms the Global South; Bitcoin as exit |
| Eric Hughes — *Cypherpunks Manifesto* | Privacy | "Cypherpunks write code"; privacy as social good |
| Robert Breedlove — *Masters and Slaves of Money* | Philosophy of money | All money is a claim on human time; inflation steals time |

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/bitcoin|Bitcoin]] | [[en/concepts/money|sound money]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/scarcity|scarcity]] | [[en/concepts/privacy|privacy]] | [[en/concepts/security|self-custody]] | [[en/concepts/lightning-network|Lightning Network]] | [[en/entities/satoshi-nakamoto|Satoshi Nakamoto]] | [[en/entities/cypherpunks|cypherpunks]]

---

## What's Not Well Covered

- Technical cryptography (elliptic curves, SHA-256 internals) — mentioned but not deep-dived
- Mining economics / hardware specifics
- Regulatory landscape (mentioned but not systematically tracked)
- Non-Russian Bitcoin communities / non-Western perspectives (except Gladstein's HRF work)
- DeFi / altcoins / Web3 — intentionally covered only when context requires

---

## Navigation in Obsidian

In Obsidian, use **Graph view** for the link map, **Backlinks** to see inbound references, and **wikilinks** to move between articles. The [Dataview](obsidian://show-plugin?id=dataview) plugin can query pages by frontmatter tags and categories.

---

## Maintaining the wiki

1. Add new immutable material under `raw/`.
2. Run an LLM/agent ingest or edit pass grounded in those sources (see `CLAUDE.md` for frontmatter, tags, and `[[en/...]]` link rules).
3. Update **`wiki-en/index.md`** when you add or retire pages (and the Russian **`wiki-ru/index.md`** when the Russian layer changes).
4. Append a dated entry to **`log.md` at the repository root** — single changelog for **both** `wiki-en/` and `wiki-ru/`.
5. After batch lint work, refresh **`lint-report.md`** in the root when applicable.

Project layout, counts, and reader onboarding: **`README.md`**, **`WIKI-GUIDE.md`**. Per-page polish prompts: **`PAGE-ENHANCEMENT-STANDARD.md`**.

---

## Wiki status (2026-04-10)

The English layer (`wiki-en/`) has **76** markdown files (**73** content pages if you exclude `index.md`, this overview, and `glossary.md`). Approximate breakdown:

- **Concepts (35)**: Core Bitcoin protocol, economics, privacy, security, upgrades (e.g. SegWit, Taproot), mempool, forks, BIPs, precursors (b-money, Bit Gold, RPOW), and related topics
- **Entities (12)**: Including Satoshi, Hal Finney, Nick Szabo, cypherpunks, Adam Back, Tim May, Eric Hughes, David Chaum, Phil Zimmermann, and others
- **Books (8)**, **Series (7)**, **History (3)**, **Philosophy (1)**, **Practice (5)**, **Topics (2)**, plus **Glossary (1)**

The Russian layer (`wiki-ru/`) is built to the same conventions with **`[[ru/...]]`** links. YAML frontmatter on every page supports tooling such as Dataview; cross-links are dense by design.

*"Publish via Quartz or browse in Obsidian — see README."*

---

## Related pages

- [[en/index|English wiki index]]
- [[en/glossary|Glossary]]
- [[ru/overview|Russian wiki overview]]
- [[ru/index|Russian wiki index]]
