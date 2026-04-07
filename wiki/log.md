# Log

Append-only record of wiki operations. Format: `## [YYYY-MM-DD] operation | description`

---

## [2026-04-07] ingest | Initial bulk ingest — 308 source files across 4 categories

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
- index.md and overview.md created

**Key findings:**
- Content is in Russian; wiki synthesis in English
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

**New wiki files created (9):**
1. `wiki/glossary.md` — Comprehensive ~100-term glossary with wikilinks; covers Cyrillic A–Э plus Latin abbreviations (AML, ASIC, BIP, BOLT, HTLC, KYC, P2P, PoW, UTxO, etc.)
2. `wiki/concepts/segwit.md` — SegWit full treatment: legacy vs SegWit tx structure, malleability fix, block weight, Bech32, Lightning prereq
3. `wiki/concepts/taproot.md` — BIP340/341/342; Schnorr vs ECDSA; MAST; P2TR; MuSig2; practical impact table
4. `wiki/concepts/mining.md` — SHA-256 mechanics, nonce iteration, difficulty formula, hash rate units, ASIC hardware, mining pools, block reward halving table, energy/environment
5. `wiki/concepts/address-types.md` — All address types with prefix/encoding/era/BTC-held table; practical recommendations
6. `wiki/series/oxt-research.md` — 4-part series: CIOH heuristic, change detection, CoinJoin/Whirlpool defenses, self-analysis workflow
7. `wiki/series/what-i-learned-from-bitcoin.md` — Gigi's series: all 7 philosophical lessons detailed
8. `wiki/topics/bitcoin-dissidents.md` — Belarus (BYSOL), Nigeria (#EndSARS/Feminist Coalition), Hong Kong (HKFP), Russia (Navalny) — Bitcoin under authoritarian regimes
9. `wiki/topics/network-effects.md` — Trace Mayer's 7 network effects: speculation → merchant → consumer → security → developer → financialization → reserve currency

**Updated wiki files (1):**
- `wiki/index.md` — Added: 4 new concepts, 2 new series, Topics section (2 pages), Glossary section

**Total session 3 files:** 9 created, 1 updated
**Cumulative wiki files:** ~49 pages
