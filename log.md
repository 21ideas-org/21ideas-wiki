---
title: "Wiki operations log"
category: topics
quality: reference
sources: []
tags: [bitcoin, wiki, reference]
synthesized_date: "2026-04-10"
completeness: high
language: en
---

# Log

**Single append-only log for the whole repository.** Record work that affects **`wiki-en/`**, **`wiki-ru/`**, or both (ingest, lint, structural passes, index/overview updates). Path: repo root `log.md` (not per-language copies).

Format: `## [YYYY-MM-DD] operation | description`

---

## [2026-04-10] maintenance | Operational log moved to repository root

**Scope:** Consolidate changelog into one file for bilingual maintenance.

**Changes:**
- **Moved:** `wiki-en/log.md` → `log.md` (repo root).
- **Updated:** This file’s intro and historical notes clarify **EN-only** vs **bilingual** sessions.
- **Docs:** `WIKI-GUIDE.md` now points to root `log.md`.
- **Git:** Removed root-level `log.md` from `.gitignore` so the operational log stays commit-tracked.

**Layers affected:** Meta (documentation + logging only).

---

## [2026-04-10] maintenance | RU concept page standardization + stronger wikilinking standard

**Layers:** Russian wiki (`wiki-ru/`) + meta docs.

**Changes:**
- **Standardized pages:** `wiki-ru/concepts/decentralization.md`, `wiki-ru/concepts/deflation.md`, `wiki-ru/concepts/difficulty-adjustment.md`
  - Frontmatter normalized (quoted scalars; consistent ordering)
  - Removed reader-facing `raw/...` mentions from page bodies, replaced with `21ideas.org` links already listed in `sources:`
  - Replaced `## Связанные термины` / `## Связанные страницы` with a single `## Дополнительные материалы` section (pipe links)
- **Wikilinking quality bar raised:** `PAGE-ENHANCEMENT-STANDARD.md` now explicitly requires a deliberately thorough linking sweep (terms, concepts, entities) and adds a pre-flight checklist line to prevent missed obvious links.

**Notes:**
- Mechanical-only changes; no intended changes to substantive claims.

## [2026-04-07] ingest | Initial bulk ingest — 308 source files across 4 categories

**Layers:** English wiki only (`wiki-en/`; entries below use legacy path `wiki/` for the same tree).

**Scope:** All markdown files in `raw/` — Books (8), Theory (economics, history, philosophy, protocol, security, lightning, privacy, future), Practice (buy, hodl, interact, lightning, privacy, security), Start.

**Processed:**
- ~308 source files read and synthesized
- 9 concept pages created
- 5 entity pages created
- 8 book summaries created
- 5 series pages created
- 3 history pages created
- 1 philosophy overview created
- 4 practice guides created
- `wiki-en/index.md` and `wiki-en/overview.md` created (as `index.md` / `overview.md` in the English tree)

**Key findings:**
- `raw/` content is in Russian; first-pass wiki synthesis was in English (`wiki-en/`).
- Site is 21ideas.org — Russian-language Bitcoin education platform curated by Tony
- Strong coverage of: monetary theory (Austrian school), Bitcoin history/timeline, privacy tools (Samourai/Whirlpool/Dojo), Lightning Network, self-custody, cypherpunk philosophy
- Major article series: Gradually Then Suddenly (Parker Lewis, 17 parts), Discovering Bitcoin (Zucco, 7 parts), Genesis Files (van Wirdum, 5 parts), Silk Road (6 parts), Bitcoin Astronomy (3 parts), OXT Research (4 parts)
- Books translated/summarized: Inventing Bitcoin, Sovereignty Through Mathematics, Bullish Case, Fiat Standard, Price of Tomorrow, Sovereign Individual, Blocksize War, 21 Ways
- Notable: Samourai Wallet developers arrested April 2024 (DOJ); `freesamourai.md` article present
- Tools/practice: Coldcard, SeedSigner, Phoenix, Mutiny, LNbits, Alby, Hodl Hodl, RoboSats, GrapheneOS, RoninDojo, Dojo

**Source count by category:**
- Books: ~100 files (8 books, chapter-by-chapter)
- Theory: ~120 files
- Practice: ~30 files
- Start: 6 files

---

## [2026-04-07] ingest | Session 3 — Glossary, protocol upgrades, OXT series, Gigi series, dissidents, network effects

**Layers:** English wiki only (`wiki-en/`; paths below show historical `wiki/` prefix).

**Scope:** Gap-filling pass over previously unprocessed `raw/Theory/` files; full glossary extraction; two new topic pages.

**Source files read:**
- `raw/Start/glossary.md` — Master glossary (~895 lines, read in 4 chunks)
- `raw/Theory/protocol/segwit.md` — SegWit technical explanation (Greg Walker / Unchained)
- `raw/Theory/protocol/taproot.md` — Taproot: BIP340-342, Schnorr, MAST
- `raw/Theory/protocol/bitcoin-address-types.md` — Address types P2PK through P2TR (Tom Honzik)
- `raw/Theory/protocol/mining-walkthrough.md` — Mining mechanics (Arman The Parman)
- `raw/Theory/privacy/oxt/oxt-1.md` through `oxt-4.md` — OXT Research series (Samourai team)
- `raw/Theory/philosophy/what-i-learned-from-bitcoin/1-philosophical-teachings.md` — Gigi Part 1
- `raw/Theory/philosophy/bitcoin-dissidents.md` — Gladstein/CoinDesk on Bitcoin under authoritarianism
- `raw/Theory/economics/seven-network-effects-of-bitcoin.md` — Trace Mayer, WeUseCoins 2015

**New wiki files created (9)** — under `wiki-en/` (logged historically as `wiki/`):
1. `glossary.md` — Comprehensive ~100-term glossary with wikilinks; Cyrillic A–Э plus Latin abbreviations (AML, ASIC, BIP, BOLT, HTLC, KYC, P2P, PoW, UTxO, etc.)
2. `concepts/segwit.md` — SegWit: legacy vs SegWit tx structure, malleability fix, block weight, Bech32, Lightning prereq
3. `concepts/taproot.md` — BIP340/341/342; Schnorr vs ECDSA; MAST; P2TR; MuSig2; practical impact table
4. `concepts/mining.md` — SHA-256 mechanics, nonce iteration, difficulty formula, hash rate units, ASIC hardware, mining pools, block reward halving table, energy/environment
5. `concepts/address-types.md` — Address types P2PK through P2TR; practical recommendations
6. `series/oxt-research.md` — 4-part series: CIOH heuristic, change detection, CoinJoin/Whirlpool defenses, self-analysis workflow
7. `series/what-i-learned-from-bitcoin.md` — Gigi's series: all 7 philosophical lessons detailed
8. `topics/bitcoin-dissidents.md` — Belarus (BYSOL), Nigeria (#EndSARS/Feminist Coalition), Hong Kong (HKFP), Russia (Navalny)
9. `topics/network-effects.md` — Trace Mayer's 7 network effects: speculation → merchant → consumer → security → developer → financialization → reserve currency

**Updated wiki files (1):**
- `index.md` — Added: 4 new concepts, 2 new series, Topics section (2 pages), Glossary section

**Total session 3 files:** 9 created, 1 updated  
**Cumulative wiki files:** ~49 pages (English layer)

---

## [2026-04-07] maintenance | Wikilink pass — added inline wikilinks and Related Terms sections to all 44 wiki files

**Layers:** English wiki only (`wiki-en/`).

**Scope:** Full wikilink enrichment — all existing pages updated, 2 new concept stubs created.

**Operations performed:**
- Added wikilinks throughout body text wherever glossary/concept terms appear (first or most meaningful occurrence per section)
- Added `## Related Terms` section to every page (inline links separated by ` | `, placed before any existing Related Pages section)
- Created 2 new stub concept pages for high-value terms that lacked dedicated pages

**Term → Page mapping applied (key mappings):**
- mining, miners, hash rate, ASIC, SHA-256, difficulty adjustment → `concepts/mining`
- PoW, Proof of Work, unforgeable costliness → `concepts/proof-of-work`
- scarcity, 21M cap, halving, block reward, stock-to-flow → `concepts/scarcity`
- governance, full node, BIP, soft fork, hard fork → `concepts/governance`
- SegWit, transaction malleability, block weight, Bech32, TXID → `concepts/segwit`
- Taproot, Schnorr, MAST, MuSig2, P2TR → `concepts/taproot`
- Lightning Network, payment channel, HTLC → `concepts/lightning-network`
- UTXO, UTXOs → `concepts/utxo`
- privacy, KYC, CoinJoin → `concepts/privacy`
- seed phrase, hardware wallet, multisig, self-custody, cold storage → `concepts/security`
- money, fiat, sound money, time preference → `concepts/money`
- Cantillon effect → `concepts/cantillon-effect`
- Hashcash → `concepts/hashcash`
- address types, P2TR → `concepts/address-types`
- Satoshi Nakamoto → `entities/satoshi-nakamoto`
- Hal Finney → `entities/hal-finney`
- Nick Szabo → `entities/nick-szabo`
- cypherpunks → `entities/cypherpunks`
- Gigi → `entities/gigi`
- blocksize war → `history/blocksize-war`
- blockchain analysis → `series/oxt-research`
- Whirlpool, Dojo, RoninDojo → `practice/privacy-practice`
- Coldcard, SeedSigner → `practice/storage`
- Hodl Hodl, P2P exchange → `practice/buying`

**Files updated (44):** (paths relative to `wiki-en/`) concepts/bitcoin, concepts/money, concepts/proof-of-work, concepts/lightning-network, concepts/scarcity, concepts/privacy, concepts/security, concepts/utxo, concepts/governance, concepts/segwit, concepts/taproot, concepts/mining, concepts/address-types, entities/satoshi-nakamoto, entities/hal-finney, entities/nick-szabo, entities/cypherpunks, entities/gigi, history/timeline, history/pre-bitcoin-cypherpunks, history/blocksize-war, philosophy/overview, books/* (8), series/* (7), practice/* (4), topics/* (2), overview

**New stub pages created (2):**
- `concepts/hashcash.md` — Adam Back's 1997 Proof of Work anti-spam; Hashcash vs Bitcoin mining comparison table
- `concepts/cantillon-effect.md` — Cantillon on money non-neutrality; fiat era; Bitcoin as Cantillon-resistant money

**Total session 4 files:** 2 created, 46 updated (44 wiki pages + index.md + log)  
**Cumulative wiki files:** ~51 pages (English layer)

---

## [2026-04-09] ingest | Nine new bilingual concept pages (batch 1)

**Layers:** **Both** — `wiki-en/concepts/` and `wiki-ru/concepts/` (mirrored slugs).

**Scope:** Core protocol and economics concepts synthesized from `raw/` (Start guide, *Inventing Bitcoin*, *Sovereignty Through Mathematics*, difficulty article, blocksize-war book).

**Created (18 files):**
- **`wiki-en/concepts/`** — deflation, forks, decentralization, double-spend, byzantine-generals-problem, mempool, bip, difficulty-adjustment, blockchain
- **`wiki-ru/concepts/`** — same slugs (Russian mirror pages; not translations of EN prose — same sources, RU layer conventions)

**Also updated:** `wiki-en/index.md`, `wiki-ru/index.md`, `lint-report.md` (root), this log.

**Lint:** Targeted bilingual check on new pages only — frontmatter complete; `[[en/...]]` / `[[ru/...]]` prefixes verified; cross-links validated against existing pages.

---

## [2026-04-09] ingest | Batch 3 — Whitepaper, AML, cypherpunk entities, and Genesis Files predecessors (bilingual)

**Layers:** **Both** — concepts + entities in `wiki-en/` and `wiki-ru/`.

**Scope:** Missing concept + entity pages in both languages, grounded in `raw/` (Genesis Files series, cypherpunk/crypto-anarchist manifestos, PGP practice guide, 21ideas whitepaper page).

**Created (20 files):**
- **`wiki-en/concepts/`** — bitcoin-whitepaper, aml, b-money, bit-gold, rpow  
- **`wiki-ru/concepts/`** — same slugs  
- **`wiki-en/entities/`** — adam-back, tim-may, eric-hughes, david-chaum, phil-zimmermann  
- **`wiki-ru/entities/`** — same slugs  

**Also updated:** `wiki-en/index.md`, `wiki-ru/index.md`, `lint-report.md` (root), this log.

**Lint:** Targeted bilingual check on Batch 3 pages only — required frontmatter verified; `[[en/...]]` / `[[ru/...]]` prefixes verified.

---

## Related pages

- [[en/index|English wiki index]]
- [[ru/index|Russian wiki index]]
- [[en/overview|English overview]]
- [[ru/overview|Russian overview]]
- [[en/concepts/bitcoin|Bitcoin (EN)]]
- [[en/glossary|English glossary]]
