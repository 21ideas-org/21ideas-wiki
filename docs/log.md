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

## [2026-04-11] enhance | wiki-ru/books/blocksize-war.md

**Changes:** Стандартизирован frontmatter (кавычки, `sources` в одну строку, теги только из allowlist, `reviewed` последним); убраны `#` в теле и горизонтальные `---`; первый блок оформлен как `## О книге` с читательской ссылкой на 21ideas; исправлена грамматика («противостояний» → «противостоянии»); добавлены wikilink’и (история войны за блок, Биткоин, биржа, софтфорк, UASF/BIP, форки, Bitcoin Core, майнеры, полные узлы, децентрализация); `## Связанные страницы` заменён на `## Дополнительные материалы` с pipe-ссылками и доп. пунктами (forks, bip).

---

## [2026-04-11] enhance | wiki-ru/history/pre-bitcoin-cypherpunks.md

**Changes:** Frontmatter по стандарту (кавычки, inline `sources`, теги из allowlist вместо cypherpunks/ecash/b-money/bit-gold/rpow, `reviewed` последним); убраны `#` и `---` в теле; вводный блок — `## Введение` со ссылкой на серию и [genesis-intro](https://21ideas.org/gf/genesis-intro); backbone + глоссарий: криптография, ключи, Чаум, Тим Мэй, Хьюз, PGP/Зиммерманн, Адам Бэк, Hashcash, PoW, нонс, майнинг, корректировка сложности, b-money, реестр, публичные ключи, Bit Gold, метки, RPOW, двойная трата, узлы, вознаграждение, комиссии; удалён блок со стрелкой «→ Подробнее»; `## Связанные страницы` → `## Дополнительные материалы` (pipe + david-chaum, b-money, bit-gold, rpow, whitepaper).

---

## [2026-04-11] enhance | wiki-ru/history/blocksize-war.md

**Changes:** Frontmatter (кавычки, inline `sources`, теги allowlist вместо blocksize-war/bitcoin-cash, добавлен `fork`, `reviewed` последним); убраны `#` и `---`; ввод — `## Введение`; wikilink’и: биткоин, блок, транзакции, комиссии, Bitcoin Core, полные узлы, децентрализация, Lightning, SegWit, хардфорк, майнеры, UASF/BIP, софтфорк, биржи, governance; списки с пустыми строками по markdownlint; `## Связанные страницы` → `## Дополнительные материалы` (+ forks, bip).

---

## [2026-04-11] enhance | wiki-ru/history/timeline.md

**Changes:** Удалены поле `source:` и отсылка к `raw/`; `sources: []`, теги только из allowlist (убраны timeline/events/milestones, добавлены mining, protocol, scarcity); кавычки у скаляров, `reviewed` последним; убраны `#` и все `---`; таблицы дополнены wikilink’ами (предыстория → сущности и концепты; рождение → whitepaper, генезис, coinbase, транзакция, биржа; рост → Silk Road, халвинг, биткоин; 2017 → форки/BCH, BIP; параметры → генезис, scarcity, халвинг); в блоке «Современность» январь 2024 поставлен перед апрелём 2024; добавлены `## Источники` (пояснение при пустых URL) и `## Дополнительные материалы` с pipe-ссылками.

---

## [2026-04-11] enhance | wiki-ru/philosophy/overview.md

**Changes:** Удалены `source:`/`raw/`; `sources: []`; теги allowlist (philosophy, economics, concept, third-party, decentralization вместо freedom/sovereignty/cypherpunks/money-as-technology); кавычки, `reviewed` последним; убраны `#` и `---`; `## Введение`; исправлена ссылка на глоссарий (было `[[ru/glossary|…]]` → `#Приватный ключ`); убран лишний пробел в `[[ru/concepts/scarcity|…]]`; wikilink’и: биткоин, деньги, инфляция, фиат, Тим Мэй, криптография, third-parties, биржа, транзакция, децентрализация, кошелёк; `## Источники` (пояснение); `## Связанные страницы` → `## Дополнительные материалы` (+ tim-may, third-parties, money, pipe-тексты).

---

## [2026-04-11] enhance | wiki-ru/topics/bitcoin-dissidents.md

**Changes:** Frontmatter (кавычки, inline `sources`, теги allowlist: убраны human-rights/activism, добавлены concept/privacy/security, `reviewed` последним); убраны `#` и `---`; `## Введение` + строка «Основа» с 21ideas URL; wikilink’и: bitcoin, censorship-resistance, money, инфляция, фиат, узлы, приватный ключ, транзакция, Сатоши; `## Связанные страницы` → `## Дополнительные материалы` (pipe + censorship-resistance, third-parties, security).

---

## [2026-04-11] enhance | wiki-ru/topics/network-effects.md

**Changes:** Frontmatter (кавычки, inline `sources`, теги allowlist вместо network-effects/adoption/lindy-effect/bitcoin-dominance: economics, mining, protocol, decentralization, concept; `reviewed` последним); убраны `#` и `---`; `## Введение` + «Основа» с 21ideas; wikilink’и: bitcoin, комиссии (глоссарий), privacy, mining, хешрейт, атака 51%, bitcoin-core, decentralization, scarcity, транзакция, forks; блок петли помечен как fenced code language `text` (MD040); `## Связанные страницы` → `## Дополнительные материалы` (+ decentralization, bitcoin-core, расширенные pipe для gradually-then-suddenly).

---

## [2026-04-11] enhance | wiki-ru/practice/buying.md

**Changes:** Frontmatter (кавычки, inline `sources`, теги allowlist вместо buying/exchange/p2p/kyc/robosats/hodl-hodl: privacy, security, aml, lightning, third-party, reference; `reviewed` последним); убраны `#` и `---`; `## Введение` + «Основа» с 21ideas; из тела убраны сторонние URL (`hodlhodl.com`, `robosats.com`) — только названия сервисов; wikilink’и: bitcoin, KYC, биржа, кошелёк, приватный ключ, privacy, Lightning, multisig, сид-фраза; пустые строки перед списками; `## Источники` с осмысленной подписью; `## Связанные страницы` → `## Дополнительные материалы` (+ third-party, lightning, aml).

---

## [2026-04-11] enhance | wiki-en/practice/lightning-tools.md

**Changes:** Удалены `source:`/`raw/`, тело без `raw/...` путей и без `---`/`#`; `sources` заполнен URL с полей `url:` в `raw/Practice/lightning/*.md` + индекс `practice/lightning`; теги allowlist (убран `practice`, добавлены multisig/concept); `reviewed` последним; введение с 21ideas; у каждого инструмента — читательская ссылка на гид; wikilink’и `[[en/...]]`: bitcoin, lightning-network, keys (glossary Private key), security, bip, running-a-node, utxo, privacy, aml (KYC), multisig; исправлены битые `]]]` в Related; удалены `*Tags:*` и секция «Related Terms»; `## Related pages` с pipe-описаниями; таблица — выравнивание MD060.

---

## [2026-04-11] enhance | wiki-ru/practice/privacy-practice.md

**Changes:** Удалены `source:`/`raw/` в метаданных и упоминание `raw/` в `## Источники`; `sources`: practice-privacy, privacy/coinjoin, privacy/ (пути из `raw/`); теги allowlist вместо coinjoin/coin-control/kyc/tor/practice; `reviewed` последним; убраны `#` и `---`; `## Введение` + «Основа» (2 строки, 21ideas); wikilink’и: bitcoin, транзакции, privacy, блокчейн, биржа, KYC, адреса, HD-кошелёк, майнинг, Lightning, bitcoin-node, utxo, lightning-tools; CoinJoin — ссылка на статью 21ideas в разделе; таблица P2P без сторонних URL (только названия); `## Связанные страницы` → `## Дополнительные материалы` (+ buying, aml, security); уровни угрозы оформлены с переносами строк.

---

## [2026-04-11] enhance | wiki-ru/practice/lightning-tools.md

**Changes:** Frontmatter: кавычки, полный `sources` как у EN (индекс practice/lightning + гиды из `raw/Practice/lightning`); теги allowlist (убраны phoenix/alby/lnbits/mutiny/wallets/practice, добавлены privacy/security/multisig/concept); `quality` reference, `reviewed` последним; убраны `#` и `---`; `## Введение` + «Основа»; у каждого инструмента ссылка на 21ideas; добавлен блок Mutiny; раздел ликвидности со ссылкой на гид; краткий блок про ончейн-приватность + ochishchaem URL; исправлено «Lighting» → «Lightning» Labs; Alby: убран сторонний домен в примере адреса; wikilink’и: bitcoin, транзакции, комиссии, кошелёк, ключи, security, узел, running-a-node, биржа; `## Связанные страницы` → нижний `## Дополнительные материалы` (running-a-node, privacy-practice, multisig).

---

## [2026-04-11] enhance | wiki-ru/practice/running-a-node.md

**Changes:** `title` унифицирован с формулировкой в `wiki-ru/index.md` («узла» вместо «ноды» в YAML); frontmatter: кавычки, inline `sources`, теги allowlist (убраны bitcoin-core/full-node/sovereignty/umbrel, добавлены governance/protocol/decentralization); `reviewed` последним; убраны `#` и `---`; `## Введение` + «Основа» (21ideas); убрана гиперссылка на bitcoin.org — текст про загрузку с официального сайта без стороннего URL; требования к диску: ГБ→ТБ для SSD (согласовано с ~600 ГБ цепочки в тексте); исправлен двойной пробел в FAQ; wikilink’и: bitcoin-node, нода, bitcoin, блокчейн, транзакции, блок, кошелёк, scarcity, майнеры, governance, blocksize-war, децентрализация, генезис, utxo, bitcoin-core, lightning; `## Связанные страницы` → `## Дополнительные материалы` (+ bitcoin-node, bitcoin-core, lightning-tools, security).

---

## [2026-04-11] enhance | wiki-ru/practice/storage.md

**Changes:** Frontmatter: кавычки, расширенный `sources` (practice/hodl + electrum/blue/coldcard/seedsigner из `raw/Practice/hodl`); теги allowlist вместо storage/hardware-wallet/vendor-имён; `reviewed` последним; убраны `#` и `---`; `## Введение` + «Основа»; убраны сторонние URL (`bluewallet.io`, `coldcard.com`, `seedsigner.com`); у каждого кошелька — ссылка на гид 21ideas; wikilink’и: security, bitcoin, кошелёк, приватный ключ, горячий/аппаратный кошелёк, холодное хранение, lightning, адреса, utxo, комиссии, multisig, сид-фраза; `## Связанные страницы` → `## Дополнительные материалы` (+ lightning-tools, running-a-node).

---

## [2026-04-11] enhance | wiki-ru/series/bitcoin-astronomy.md

**Changes:** Frontmatter: порядок полей, inline `sources` (ba + ba/1–3 из `raw/Theory/future/bitcoin-astronomy`), кавычки; теги allowlist (убраны bitcoin-astronomy/future/hyperbitcoinization/speculation/druv-bansal); `quality: synthesized`, `reviewed` последним; убраны `#` в теле и горизонтальные `---`; «Основа» + ссылки на части; в таблице названия частей — ссылки на 21ideas; wikilink’и: bitcoin, money, glossary#Инфляция, lightning-network, blockchain, proof-of-work; `## Связанные страницы` → `## Дополнительные материалы` (pipe-описания); блок `## Источники` с четырьмя URL.

---

## [2026-04-11] enhance | wiki-ru/series/discovering-bitcoin.md

**Changes:** `title` исправлен на автора по `raw` (Джакомо Зукко; убрана ошибочная «Ялда Хасрати» в YAML); frontmatter: порядок, inline `sources` (sb + stanovlenie-intro и 1–7 из `raw/Theory/economics/discovering-bitcoin`), кавычки; теги allowlist; `quality: synthesized`, `reviewed` последним; убраны `#` и `---`; «Основа» + компактные ссылки на вступление и части; таблица: только 21ideas в колонке «Название» (wikilink’и с `|` в ячейках не используются — ломают таблицу); в «Ключевых идеях»: money, инфляция, PoW, золотой стандарт; `## Связанные страницы` → `## Дополнительные материалы` (pipe); `## Источники` — полный список девяти URL.

---

## [2026-04-11] enhance | wiki-ru/series/genesis-files.md

**Changes:** Frontmatter: порядок, inline `sources` (+ хаб `https://21ideas.org/gf` из `raw/Theory/history/genesis-files/_index.md`), кавычки; теги allowlist (убраны genesis-files/ecash/bit-gold/cypherpunks вне списка; добавлены decentralization, hashcash); `quality: synthesized`, `reviewed` последним; убраны `#` и `---`; «Основа»; таблица: колонка «Материал» — только ссылки 21ideas (текст темы без wikilink’ов из‑за `|`); обзор: bitcoin, криптография, ключи, chaum, adam-back, hashcash, satoshi, whitepaper, b-money, реестр, double-spend, bit-gold, szabo, hal-finney, rpow; блок «Значение»: satoshi, difficulty-adjustment, blockchain, PoW; убрана отдельная стрелка «→ hashcash»; `## Связанные страницы` → `## Дополнительные материалы` (pipe); `## Источники` — семь URL.

---

## [2026-04-11] enhance | wiki-ru/series/gradually-then-suddenly.md

**Changes:** Frontmatter: порядок, inline `sources` (хаб `pzv` + 17 URL из `raw/Theory/economics/gradually-then-suddenly`, включая EN-эссе 16 по ссылке из `_index.md`); кавычки; теги allowlist (убраны gradually-then-suddenly/parker-lewis/bitcoin-is-money; добавлены philosophy, decentralization); `quality: synthesized`, `reviewed` последним; убраны `#` и `---`; «Основа» + пояснение про EN для эссе 16 (без `raw/` в теле); wikilink’и: parker-lewis, bitcoin, glossary#Фиат; в «Ключевых темах»: bitcoin, scarcity; таблица: колонка «Название» — ссылки на 21ideas, для 16 — пометка EN в колонке идеи; `## Связанные страницы` → `## Дополнительные материалы` (pipe); `## Источники` — 18 пунктов.

---

## [2026-04-11] enhance | wiki-ru/series/oxt-research.md

**Changes:** Frontmatter: порядок, inline `sources` (+ хаб `https://21ideas.org/privacy/oxt` из `raw/Theory/privacy/oxt/_index.md`), кавычки; теги allowlist (убраны oxt-research/chain-analysis/samourai; добавлены concept, security); `quality: synthesized`, `reviewed` последним; убраны `#` и `---`; «Основа»; таблица: колонка «Название» — ссылки на oxt-1…4; wikilink’и: privacy, транзакция, bitcoin, blockchain, utxo, address-types, lightning-network, privacy-practice#CoinJoin / #Coin Control; `## Связанные страницы` → `## Дополнительные материалы` (pipe); `## Источники` — пять URL (старый одиночный хаб вынесен в полный список).

---

## [2026-04-11] enhance | wiki-ru/series/silk-road.md

**Changes:** Frontmatter: порядок, inline `sources` (хаб `sr` + `silkroad-1`…`6` + доп. ссылки из `raw/Theory/history/silk-road/_index.md`: `bitcoin-svoboda`, `posts/ross`); кавычки; теги allowlist (убраны silk-road/ross-ulbricht/darknet/bitcoin-use-case); `quality: synthesized`, `reviewed` последним; убраны `#` и `---`; «Основа» + доп. 21ideas; таблица: колонка «Название» — ссылки на части; wikilink’и: bitcoin, privacy-practice#Tor/VPN, транзакция, oxt-research; `## Связанные страницы` → `## Дополнительные материалы` (pipe); `## Источники` — девять URL с заголовками по оглавлению `raw`.

---

## [2026-04-11] enhance | wiki-ru/series/what-i-learned-from-bitcoin.md

**Changes:** Frontmatter: порядок, inline `sources` — только хаб и часть 1 (в `raw/Theory/philosophy/what-i-learned-from-bitcoin` нет отдельных `url` для частей 2–3; URL не придумывались); кавычки; теги allowlist (убраны what-i-learned/gigi/technology); `quality: synthesized`, `reviewed` последним; убраны `#` и `---`; «Основа» с двумя 21ideas; wikilink’и: gigi, bitcoin, консенсус, нода, money, governance, инфляция, scarcity, криптография, decentralization, PoW; книга в лиде — курсив без сторонних URL; `## Связанные страницы` → `## Дополнительные материалы` (pipe); `## Источники` — два URL.

---

## [2026-04-11] lint | Targeted — wiki-ru/

**Scope:** Full tree `wiki-ru/` (76 `.md` files); checks per `CLAUDE.md` (frontmatter, `[[ru/...]]`, `sources:` shape, tags allowlist, `reviewed`, body `#` / `---`, `raw/` in body, broken link targets).

**Auto-fixed:** none (report-only pass).

**Flagged for review:** `[[wiki-ru/...]]` wikilinks (6 hits, 4 files); block `sources:` (37 files); off-allowlist tags (13 files); missing `reviewed:` (9 files); body `#` as first line (12 files); standalone `---` in body (31 files); `raw/` in body (`glossary.md`, `overview.md`).

**Output:** `docs/lint-report.md` overwritten.

---

## [2026-04-11] lint | Targeted — wiki-ru/

**Scope:** `python3 tools/lint.py --layer ru --write-report` (76 pages).

**Auto-fixed:** none.

**Result:** 0 flagged mechanical issues (no bad wikilink prefixes, no broken `[[ru/...]]` targets, block `sources:`, body `---` / `#`, `raw/` in body, missing keys, missing `reviewed`, or off-allowlist tags).

**Output:** `docs/lint-report.md` overwritten (English; RU-only pass).

---

## [2026-04-11] maintenance | wiki-ru inline sources, tags, body `---`

**Layers:** RU

**Changes:** Converted block/list `sources:` to inline `sources: ["..."]` on 28 paths (books, concepts, entities from lint list). Normalized `wiki-ru/books/21-ways.md` and `wiki-ru/concepts/byzantine-generals-problem.md` frontmatter (quoted scalars, flow `tags`). Allowlist tags: `inventing-bitcoin` (`proof-of-work` → `mining`), `parker-lewis` (dropped `scarcity`), `pre-bitcoin-cypherpunks` (`hashcash` → `protocol`), `timeline` (`scarcity` → `economics`), `genesis-files` (`hashcash` → `protocol`). Removed standalone `---` from bodies of the 28-file batch plus eight remaining concept pages (`address-types`, `aml`, `decentralization`, `deflation`, `difficulty-adjustment`, `double-spend`, `forks`, `governance`). **`python3 tools/lint.py --layer ru`:** 0 flagged rows. Regenerated `docs/lint-report.md` (RU-only pass).

---

## [2026-04-11] docs | Lint workflow + English reports (CLAUDE, README, WIKI-GUIDE)

**Changes:** `CLAUDE.md` — scope vs single `lint-report.md`, **report language = English**, agent output steps with `tools/lint.py --write-report`. `README.md` — `tools/lint.py` subsection, prompt table + health-check wording. `docs/WIKI-GUIDE.md` — `tools/` in tree, lint commands, targeted EN/RU rows, clarify log/report behavior. `tools/lint.py` — docstring note on English report output.

---

## [2026-04-11] meta | tools/lint.py + CLAUDE.md lint flow

**Scope:** Add `tools/lint.py` (stdlib-only mechanical checks for `wiki-en/` and `wiki-ru/`); document runner flags and agent workflow under **Lint** in `CLAUDE.md` (directory map + note to sync allowlist with script).

---

## [2026-04-11] lint | Targeted — wiki-ru/ (repeat pass)

**Scope:** Full `wiki-ru/` tree (76 files); same mechanical checks as prior lint.

**Auto-fixed:** none.

**Flagged:** block/multiline `sources:` (28 files, including regressed `books/21-ways.md`); standalone `---` in body (19 concept pages); missing `reviewed:` (`concepts/mining.md`); off-allowlist tags (5 rows: `proof-of-work`, `scarcity`×2, `hashcash`×2). Clean: no `[[wiki-ru/...]]`, no broken `[[ru/...]]`, no body `#`, no `raw/` in body.

**Output:** `docs/lint-report.md` overwritten.

---

## [2026-04-11] maintenance | wiki-ru hub + books + wikilinks + body style

**Layers:** RU

**Changes:** Заменены все `[[wiki-ru/...]]` на `[[ru/...]]` (`hashcash`, `mempool`, `money`, `glossary`); у `money.md` убран лишний `---` перед `## Источники`. Семь книг в `wiki-ru/books/`: inline `sources`, теги по allowlist, кавычки в frontmatter, `reviewed: "2026-04-11"`, убраны `#` в теле, удалены горизонтальные `---` между секциями, `## Связанные страницы` → `## Дополнительные материалы`. Хабы `index.md`, `overview.md`, `glossary.md`: frontmatter по схеме (`sources: []` у индекса/обзора), теги allowlist, `reviewed`, без `#` в начале тела, без разделителей `---` в теле; у глоссария — `category: "topics"`, закрывающая секция переименована. `entities/satoshi-nakamoto.md`, `tim-may.md`: inline `sources`, убран дублирующий `#`. `overview`: формулировка про добавление источника без пути `raw/`; `index`: убрано `source:` с `raw/`. `concepts/hashcash.md`: правка wikilink + ранее снятые `---` в теле.

---

## Related pages

- [[en/index|English wiki index]]
- [[ru/index|Russian wiki index]]
- [[en/overview|English overview]]
- [[ru/overview|Russian overview]]
- [[en/concepts/bitcoin|Bitcoin (EN)]]
- [[en/glossary|English glossary]]

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

## [2026-04-10] ingest | wiki-ru/entities/satoshi-nakamoto — ранний майнинг и гипотеза «Патоши»

**Layers:** Russian wiki (`wiki-ru/entities/`).

**Changes:**
- Расширена страница **`wiki-ru/entities/satoshi-nakamoto.md`**: новый раздел о раннем майнинге, эвристике «узора Патоши», троттлинге ~5 минут, доле хэшрейта и контраргументе к тезису «жадного майнера»; синтез по материалу `raw/Theory/protocol/was-satoshi-a-greedy-miner.md` и публикации [21ideas — «Был ли Сатоши жадным майнером?»](https://21ideas.org/byl-li-satoshi-zhadnym-majnerom). В теле страницы — только ссылки на 21ideas, без внешних URL из оригинала.
- В frontmatter добавлен третий `sources` URL, тег `mining` (в пределах лимита тегов), обновлены `synthesized_date`, `updated`, `reviewed`.

---

## [2026-04-10] maintenance | wiki-ru/concepts — full PAGE-ENHANCEMENT pass + meta docs

**Layers:** Russian wiki (`wiki-ru/concepts/`), project documentation.

**Changes:**
- **All concept pages:** Completed a vault-wide polish of **`wiki-ru/concepts/*.md`** using `PAGE-ENHANCEMENT-STANDARD.md`: YAML frontmatter with double-quoted scalars, field order, and tags strictly from `CLAUDE.md`; `[[ru/...]]` wikilinks with backbone + glossary sweeps (verified anchors); reader-facing **`https://21ideas.org/...`** citations in bodies (no `raw/...` paths for readers); bottom navigation unified as **`## Дополнительные материалы`** (pipe links). Intended as mechanical/provenance hygiene, not substantive rewrites.
- **Early batch (same pass):** Included among others `decentralization`, `deflation`, `difficulty-adjustment`; later tranches covered the remaining concepts (e.g. scarcity, security, segwit, taproot, third-parties, utxo) until the full `concepts/` tree was consistent.
- **Standard doc:** `PAGE-ENHANCEMENT-STANDARD.md` — raised wikilinking expectations and pre-flight checklist for single-page edits.
- **Repo docs:** `README.md` (structure, counts, pointers to `log.md` and the enhancement standard); `WIKI-BACKLOG.md` (backlog refresh).
- **Review:** Maintainer manually reviewed updated RU concept pages.

**Notes:** Operational changelog remains repo root `log.md` (see sibling entry same date).

---

## [2026-04-11] enhance | docs/PAGE-ENHANCEMENT-STANDARD.md
Changes: Made prompt fully language-neutral for EN and RU pages. Added Task 0 (pre-edit mechanical scan) listing all known wiki-en legacy antipatterns (source: field, block YAML sources, *Tags:* lines, # body heading, --- rules, raw/ citations, ## Related Terms, ]]] triple-bracket links, missing reviewed:, unquoted fields, field order). Reframed reference style examples to include EN context. Split glossary sweep checklist into separate RU and EN conditional sections; added EN anchor examples with caveat about bold-in-heading format. Made source citation label bilingual (Source: EN / Основа: RU). Expanded pre-flight checklist with EN-specific checks. Updated frontmatter example to show canonical field order and language: "en" note.
---

## [2026-04-11] enhance | wiki-en/concepts/address-types.md

**Changes:** Canonical frontmatter (quoted scalars, field order, `reviewed: "2026-04-11"` last); tags set to `[bitcoin, wiki, concept, protocol, addresses, taproot, segwit]`. Removed body `#` title, `*Tags:*` line, and all `---` horizontal rules. Replaced `raw/...` provenance with reader-facing `Source:` link to existing 21ideas URL. Added/fixed wikilinks (`[[en/concepts/bitcoin|Bitcoin]]`, glossary `#address`, `#public-key`, `#transaction`, `#fee`, `[[en/concepts/bip|BIP11/BIP16]]`, `[[en/concepts/multisig|multisig]]`, `[[en/concepts/taproot|MuSig2]]`); removed redundant duplicate SegWit links in P2WPKH; fixed `]]]` triple-bracket links. Merged `## Related Terms` / broken `## Related Pages` into `## Related pages` with pipe-syntax bullets. Aligned `## Sources` with the same 21ideas link text.

**Lint:** Not run (single-page enhance).

---

## [2026-04-11] maintenance | wiki-ru/index.md — раздел «Концепции»

**Layers:** RU

**Changes:** В таблицу `## Концепции` добавлены ссылки на четыре существовавшие страницы: `[[ru/concepts/bitcoin-core]]`, `[[ru/concepts/bitcoin-node]]`, `[[ru/concepts/censorship-resistance]]`, `[[ru/concepts/third-parties]]`. В frontmatter индекса обновлено поле `updated`.

---

## [2026-04-11] docs | README.md — счётчик страниц wiki-ru

**Layers:** Meta

**Changes:** В описании русского слоя убрано ошибочное «log» из списка исключений при подсчёте контентных страниц; формулировка приведена к той же схеме, что в `docs/WIKI-GUIDE.md` (исключаются только `index`, `overview` и `glossary` внутри `wiki-ru/`).

---

## [2026-04-11] maintenance | wiki-ru/overview.md — навигация и структура

**Layers:** RU

**Changes:** Проверены все `[[ru/...]]` — цели существуют. Обновлены счётчики в блоке «Структура вики» (35 концепций, 12 сущностей). Добавлены пути чтения: философия/темы (`philosophy/overview`, `books/21-ways`, оба `topics/*`); практика — `privacy-practice`, `running-a-node`; история — `blocksize-war`; техническая сторона — `lightning-network`. В «Связанные страницы» добавлены `philosophy/overview` и `history/timeline`. Обновлено поле `updated` во frontmatter.

---

## [2026-04-11] merge | `dev` → `main` — разрешение конфликтов

**Layers:** Meta + RU (`wiki-ru/index.md`, `wiki-ru/overview.md`, `wiki-ru/books/21-ways.md`)

**Changes:** Ручное слияние после `git merge dev` на `main`. **README.md** — сохранён блок про `tools/lint.py` и расширенное описание `lint-report`. **docs/WIKI-GUIDE.md** — строка Releases: актуальная ссылка на **v0.4.0**. **wiki-ru/index.md** — канонический frontmatter (`sources: []`, `reviewed`, кавычки), `category: "index"`, заголовок «Индекс 21wiki», вступление с атрибуцией Тони, без лишнего `---` после вступления. **wiki-ru/overview.md** — то же для overview: заголовок «Введение в 21wiki», теги `overview`/`navigation`, текст с Тони (пробел перед ссылкой), правка «low` можно». **wiki-ru/books/21-ways.md** — вступление без `#` в теле, уточнение про книгу с `dev`, ссылка `[[ru/concepts/bitcoin|Биткоин]]` вместо битой склейки.

---

## [2026-04-12] enhance | wiki-en/concepts/aml.md

**Changes:** Canonical frontmatter (quoted scalars, field order, `sources: ["https://21ideas.org/posts/aml-is-a-scam/"]`, `updated` / `reviewed` last); tags aligned to allowlist: `[bitcoin, wiki, concept, aml, privacy, censorship-resistance, third-party, security]` (dropped `kyc`, `fungibility`, `censorship`, `third-parties`, `surveillance`). Removed body `#` title, horizontal rules, `raw/...` citations, and duplicate/broken bottom sections (`Related Terms`, `Related Pages`). Opening ties to 21ideas via inline markdown link; `## Sources` lists the same URL. Wikilinks: glossary `#aml-anti-money-laundering`, `#kyc-know-your-customer`, `#exchange`, `#p2p-peer-to-peer`; concepts `third-parties`, `utxo`, `privacy`, `censorship-resistance`, `security`. Single `## Related pages` with pipe-syntax bullets.

**Lint:** Targeted check — no issues reported for this path in `tools/lint.py --layer en` categories (full EN tree still has legacy pages).

---

## [2026-04-12] enhance | wiki-en/concepts/b-money.md

**Changes:** Canonical frontmatter; `sources` collapsed to inline array (same two 21ideas URLs); `category` / scalars quoted; `tags` allowlist-only `[bitcoin, wiki, concept, history, protocol, security, whitepaper, double-spend]` (removed `b-money`, `cypherpunks`, `digital-cash`, `proof-of-work`); `updated` / `reviewed` last. Removed body `#` title, horizontal rules, and `raw/...` line — replaced with reader-facing links to Genesis III and whitepaper. Merged `## Related Terms` / `## Related Pages` into `## Related pages` (pipe bullets). Added backbone + glossary wikilinks: `money`, `bitcoin`, `third-parties`, `proof-of-work`, `bitcoin-whitepaper`, `decentralization`, `bit-gold`, `rpow`, `cypherpunks`, glossary `#smart-contract`, `#public-key`, `#ledger`, `#nakamoto-consensus`.

**Lint:** Targeted check — no issues for this path in `tools/lint.py --layer en`.

---

## [2026-04-12] fact-check | Satoshi pre-whitepaper correspondence (Adam Back / others)

**Layers:** Both (`wiki-ru/`, `wiki-en/`)

**Changes:** Removed incorrect framing that Adam Back was the sole (or sole surviving) pre-publication correspondent. **RU:** `wiki-ru/entities/satoshi-nakamoto.md` — Back as **one of the few** in private correspondence before the public whitepaper, with Wei Dai (b-money) named; `wiki-ru/entities/adam-back.md` — same clarification + related link to b-money. **EN:** `wiki-en/series/genesis-files.md` — replaced wrong claim that only Hal Finney was emailed before release; now Back as one of several, Dai named, Finney as among the first responders. `wiki-en/entities/satoshi-nakamoto.md` and `wiki-en/entities/adam-back.md` — aligned wording. **Meta:** `docs/WIKI-BACKLOG.md` research item marked resolved.

**Lint:** Run `tools/lint.py --strict-links` on touched paths recommended after merge.

---

## [2026-04-14] enhance | wiki-en/concepts/b-money.md

**Changes:** Added `[[en/concepts/governance|governance]]` wikilink in version 2 section. Fixed Related pages: reformatted all entries from long link-text pattern (`[[link|Name — description]]`) to `[[link|Name]] — description` format; added `[[en/concepts/hashcash|Hashcash]]`, `[[en/series/genesis-files|Genesis Files]]`, and `[[en/entities/cypherpunks|Cypherpunks]]` entries. Updated `reviewed` to 2026-04-14.

---

## [2026-04-14] enhance | wiki-en/concepts/aml.md

**Changes:** Page already fully compliant from previous pass — correct frontmatter order, valid tags, no legacy antipatterns. Updated `reviewed` to 2026-04-14. Note: source URL `https://21ideas.org/posts/aml-is-a-scam/` uses a non-standard `/posts/` path — may warrant verification.

---

## [2026-04-14] enhance | wiki-en/concepts/address-types.md

**Changes:** Frontmatter: corrected fabricated source URL `https://21ideas.org/en/bitcoin-address-types/` → `https://21ideas.org/sravnenie-tipov-bitcoin-adresov` (matching the URL already used in the body ×2); updated `updated` and `reviewed` to 2026-04-14. Wikilink corrected: `[[en/concepts/governance|soft fork]]` → `[[en/concepts/forks|soft fork]]` (dedicated page exists). No other changes needed — page already had correct structure, no `#` heading, no `---` rules, valid tags, canonical frontmatter order.

---

## [2026-04-14] enhance | wiki-en/books/sovereignty-through-mathematics.md

**Changes:** Frontmatter: removed `author` field; reordered to canonical sequence; quoted all scalars; removed invalid tags `books`/`cryptography`, kept `philosophy`, added `economics`; removed spurious glossary URL and normalized trailing slash on source URL; added `reviewed: "2026-04-14"`. Body: removed `# Sovereignty Through Mathematics` heading; removed italic `*Author... | Source: raw/...*` line; removed all six `---` horizontal rules. Wikilinks corrected: `[[en/concepts/governance|full node]]` → `[[en/concepts/bitcoin-node|full node]]` (Absolute Scarcity argument). New wikilinks: `[[en/concepts/proof-of-work|Proof of Work]]` (ch. 5 structure), `[[en/concepts/scarcity|Scarcity]]` (ch. 6 structure), `[[en/concepts/governance|governance]]` (ch. 8 structure), `[[en/entities/satoshi-nakamoto|Satoshi]]` (Immaculate Conception), `[[en/concepts/money|store of value]]` (HODL argument). Sources section: replaced `raw/` prose with reader-facing 21ideas.org link. Fixed all five `]]]` triple-bracket links. Merged `## Related Terms` + `## Related Pages` into `## Related pages` with pipe-syntax wikilinks; added `proof-of-work` and `satoshi-nakamoto` entries.

---

## [2026-04-14] enhance | wiki-en/books/sovereign-individual.md

**Changes:** Frontmatter: removed `author` field; reordered to canonical sequence; quoted all scalars; removed invalid tag `books`, kept `philosophy`/`history`; removed spurious glossary URL; added `reviewed: "2026-04-14"`. Body: removed `# The Sovereign Individual` heading; removed italic `*Authors... | Source: raw/...*` line; removed all eight `---` horizontal rules. New wikilinks: `[[en/concepts/bitcoin|Bitcoin]]` (Summary — first mention unlinked), `[[en/concepts/censorship-resistance|confiscate]]` (Why Bitcoin section). Sources section: replaced `raw/` prose with reader-facing 21ideas.org link. Fixed all four `]]]` triple-bracket links. Merged `## Related Terms` + `## Related Pages` into `## Related pages` with pipe-syntax wikilinks; added `censorship-resistance` and `cypherpunks` entries.

---

## [2026-04-13] enhance | wiki-en/books/price-of-tomorrow.md

**Changes:** Frontmatter: removed `author` field; reordered to canonical sequence; quoted all scalars; removed invalid tags `books`/`deflation`, kept `economics`, added `philosophy`; removed spurious glossary URL; added `reviewed: "2026-04-13"`. Body: removed `# The Price of Tomorrow` heading; removed italic `*Author... | Source: raw/...*` line; removed all seven `---` horizontal rules. New wikilinks: `[[en/concepts/deflation|deflationary]]` (Summary + Core Argument ×2), `[[en/concepts/scarcity|fixed supply]]` (Core Argument exit), `[[en/entities/saifedean-ammous|Saifedean Ammous]]` (Complementary section). Sources section: replaced `raw/` prose with reader-facing 21ideas.org link. Fixed all four `]]]` triple-bracket links. Merged `## Related Terms` + `## Related Pages` into `## Related pages` with pipe-syntax wikilinks; added `deflation` and `saifedean-ammous` entries.

---

## [2026-04-13] enhance | wiki-en/books/inventing-bitcoin.md

**Changes:** Frontmatter: removed `author` field; reordered to canonical sequence; quoted all scalars; removed invalid tags `books`/`technical`/`primer`, replaced with `concept`/`protocol`; removed spurious glossary URL and normalized trailing slash on real source URL; added `reviewed: "2026-04-13"`. Body: removed `# Inventing Bitcoin` heading; removed italic `*Author... | Source: raw/...*` line; removed all six `---` horizontal rules. Wikilinks corrected: `[[en/concepts/governance|full nodes]]` → `[[en/concepts/bitcoin-node|full nodes]]` (×1 in Argument). New wikilinks: `[[en/concepts/double-spend|digital cash problem]]` (Summary), `[[en/concepts/blockchain|blockchain]]` (Argument pt.1 + Key Insights), `[[en/concepts/proof-of-work|Proof of Work]]` (ch.3 + Key Insights), `[[en/concepts/mining|Mining]]`/`[[en/concepts/mining|miners]]` (ch.4 + Key Insights), `[[en/concepts/forks|Forks]]` (ch.6), `[[en/concepts/lightning-network|Lightning Network]]` (ch.9), `[[en/concepts/bitcoin-node|Full nodes]]` (Key Insights), `[[en/concepts/double-spend|double-spend]]` (Key Insights). Fixed all four `]]]` triple-bracket links. Merged `## Related Terms` + `## Related Pages` into `## Related pages` with pipe-syntax wikilinks.

---

## [2026-04-13] enhance | wiki-en/books/fiat-standard.md

**Changes:** Frontmatter: removed `author` field; reordered to canonical sequence; quoted all scalars; removed invalid tags `books`/`austrian-school`, kept `economics`, added `history`; removed spurious `https://21ideas.org/glossary/` from sources; added `reviewed: "2026-04-13"`. Body: removed `# The Fiat Standard` heading; removed italic `*Author... | Source: raw/...*` line; removed all six `---` horizontal rules. New wikilinks: `[[en/entities/saifedean-ammous|Saifedean Ammous]]` (Summary), `[[en/concepts/cantillon-effect|Cantillon Effect]]` (ch. 7 structure list), `[[en/concepts/mining|mining]]` (ch. 17 structure list). Fixed `[[en/concepts/money]]]` triple bracket in Key Arguments. Fixed all six `]]]` triple-bracket links in Related Pages. Merged `## Related Terms` + `## Related Pages` into `## Related pages` with pipe-syntax wikilinks.

---

## [2026-04-13] enhance | wiki-en/books/bullish-case.md

**Changes:** Frontmatter: removed `author` field; reordered to canonical sequence; quoted all scalars; removed invalid tags `books`/`monetary-theory`, added `philosophy`; removed spurious `https://21ideas.org/glossary/` from sources; added `reviewed: "2026-04-13"`. Body: removed `# The Bullish Case for Bitcoin` heading; removed italic `*Author... | Source: raw/...*` line; removed all five `---` horizontal rules. New wikilinks: `[[en/entities/nick-szabo|Szabo]]` (ch. 1 structure), `[[en/concepts/decentralization|Decentralization]]` (Core Argument), `[[en/concepts/bitcoin-node|nodes]]` (durability point), `[[en/concepts/privacy|privacy tools]]` (fungibility note). Sources section: replaced `raw/` prose with reader-facing 21ideas.org link. Fixed all five `]]]` triple-bracket links. Merged `## Related Terms` + `## Related Pages` into `## Related pages` with pipe-syntax wikilinks.

---

## [2026-04-13] enhance | wiki-en/books/blocksize-war.md

**Changes:** Frontmatter: removed `author` field; reordered to canonical sequence; quoted all scalars; removed invalid tag `books`, kept `history`/`governance`; removed spurious `https://21ideas.org/glossary/` from sources; added `reviewed: "2026-04-13"`. Body: removed `# The Blocksize War` heading; removed italic `*Author... | Source: raw/...*` line; removed all five `---` horizontal rules. Wikilinks corrected: `[[en/concepts/governance|full node]]` → `[[en/concepts/bitcoin-node|full node]]` (×4); `[[en/concepts/governance|hard fork]]` → `[[en/concepts/forks|hard fork]]`. New wikilinks added: `[[en/concepts/forks|soft fork]]` (ch. 5 + "Why It Matters"), `[[en/concepts/forks|hard forks/soft forks]]` ("Why It Matters"), `[[en/concepts/bitcoin-core|Bitcoin Core]]` (Key Takeaways), `[[en/concepts/segwit|SegWit2x]]`, `[[en/concepts/scarcity|21M cap]]`. Fixed all four `]]]` triple-bracket links. Sources section: replaced `raw/` prose with reader-facing 21ideas.org link. Merged `## Related Terms` + `## Related Pages` into `## Related pages` with pipe-syntax wikilinks; added forks and bitcoin-core entries.

---

## [2026-04-13] enhance | wiki-en/books/21-ways.md

**Changes:** Frontmatter: removed non-standard `author` field; reordered to canonical sequence; quoted all scalars; replaced invalid tags `books`/`gigi` with `philosophy`/`economics`; added `reviewed: "2026-04-13"` as last field. Body: removed `# 21 Ways` heading; removed italic `*Author: Gigi... | Source: raw/...` tag line; removed all three `---` horizontal rules. Wikilinks added in table: `[[en/concepts/governance|consensus]]` (frame 2), `[[en/concepts/blockchain|blockchain]]` (frame 8), `[[en/concepts/decentralization|Decentralized]]` (frame 10), `[[en/concepts/lightning-network|Lightning]]` (frame 12), `[[en/concepts/mining|mining]]` (frame 16), `[[en/concepts/censorship-resistance|Financial censorship resistance]]` (frame 19). Fixed triple-bracket `]]]` links throughout. Merged `## Related Terms` and `## Related Pages` into single `## Related pages` with pipe-syntax wikilinks. Added `## Sources` section.

---

## [2026-04-14] enhance | wiki-en/concepts/bip.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; replaced invalid tag `upgrades` with `bip`; added `updated: "2026-04-14"` and `reviewed: "2026-04-14"` (last field). Body: removed `# BIP (Bitcoin Improvement Proposal)` H1 heading; removed `*Tags: standards process, soft fork activation*` italic line; removed all four `---` horizontal rules; removed `Source: raw/...` and `Sources: raw/...` citations — replaced with reader-facing 21ideas.org inline links; removed duplicate/garbled paragraph in "Activation in practice" section. New wikilinks: `[[en/concepts/bitcoin-core|Bitcoin Core]]`, `[[en/books/inventing-bitcoin|Inventing Bitcoin]]`, `[[en/concepts/bitcoin-node|nodes]]`, `[[en/concepts/forks|soft forks]]` (×2), `[[en/concepts/segwit|SegWit]]`, `[[en/concepts/mining|miners]]`, `[[en/concepts/governance|governance]]` (with display text). Removed `## Related Terms` section; renamed `## Related Pages` → `## Related pages`; converted all bullets to pipe-syntax with descriptive display text.

---

## [2026-04-14] enhance | wiki-en/concepts/bit-gold.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; replaced invalid tags `bit-gold`/`cypherpunks`/`proof-of-work`/`digital-scarcity` → `concept`/`history`/`protocol`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Bit Gold` H1 heading; removed `raw/...` inline path — replaced with reader-facing 21ideas.org link; removed two `---` horizontal rules. New wikilinks: `[[en/entities/nick-szabo|Nick Szabo]]`, `[[en/concepts/scarcity|scarce]]`, `[[en/concepts/proof-of-work|Proof-of-work]]` (×2), `[[en/concepts/third-parties|Trusted third parties]]`, `[[en/concepts/bitcoin-whitepaper|Bitcoin whitepaper]]`, `[[en/concepts/b-money|b-money]]`, `[[en/concepts/hashcash|Hashcash]]`, `[[en/concepts/byzantine-generals-problem|Byzantine-fault-resistant consensus]]`. Fixed bare wikilinks in "Relationship to Bitcoin" section. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets converted to pipe-syntax with descriptive display text; added hashcash, genesis-files entries.

---

## [2026-04-14] enhance | wiki-en/concepts/bitcoin-core.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; replaced invalid tags `bitcoin-core`/`full-node`/`software`/`open-source`/`upgrades` → `concept`/`protocol`/`node`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Bitcoin Core` H1; removed `*Tags: ...*` italic line; removed all five `---` horizontal rules; removed five `raw/...` inline citations — replaced with reader-facing 21ideas.org links. Wikilinks: fixed bare `[[en/concepts/governance]]` and `[[en/concepts/bip]]` and `[[en/concepts/forks]]` to pipe-syntax; added `[[en/concepts/bitcoin-node|nodes]]`, `[[en/books/inventing-bitcoin|Inventing Bitcoin]]`, `[[en/concepts/decentralization|centralization]]`. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `running-a-node` entry.

---

## [2026-04-14] enhance | wiki-en/concepts/bitcoin-node.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; replaced invalid tags `full-node`/`validation`/`sovereignty`/`p2p` → `concept`/`protocol`/`decentralization`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Bitcoin Node` H1; removed `*Tags: ...*` italic line; removed all five `---` horizontal rules; removed five `raw/...` inline citations — one replaced with reader-facing 21ideas.org Source line, others removed (covered by bottom `## Sources` section). New wikilinks: `[[en/concepts/governance|consensus rules]]`, `[[en/books/inventing-bitcoin|Inventing Bitcoin]]`, `[[en/concepts/third-parties|third parties]]`, `[[en/concepts/bitcoin-core|Bitcoin Core]]`, `[[en/concepts/mining|miners]]`, `[[en/concepts/governance|governance]]` (with display text). Fixed bare `[[en/concepts/bitcoin-core]]` and `[[en/concepts/governance]]`. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `decentralization` entry.

---

## [2026-04-14] enhance | wiki-en/concepts/bitcoin-whitepaper.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; quoted all scalars; removed invalid tags `satoshi`/`reference`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Bitcoin Whitepaper` H1; removed `raw/Books/whitepaper.md` inline path — replaced with reader-facing 21ideas.org link; removed two `---` horizontal rules. New/fixed wikilinks: `[[en/concepts/b-money|b-money]]` and `[[en/concepts/hashcash|Hashcash]]` (Notable facts); `[[en/concepts/blockchain|Blockchain]]` (bare → display text); `[[en/concepts/bitcoin-node|Bitcoin node]]`, `[[en/concepts/bitcoin-core|Bitcoin Core]]`, `[[en/concepts/governance|governance]]` (bare → display text, inline See list collapsed to prose). Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `satoshi-nakamoto`, `hashcash`, `proof-of-work` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/bitcoin.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalars; removed invalid tags `fundamentals`/`money` → added `concept`/`economics`; added `reviewed: "2026-04-14"` (last). Body: removed `# Bitcoin` H1; removed `*Tags: fundamentals, protocol, money*` italic line; removed all eight `---` horizontal rules; removed `Sources: raw/...` citation (bottom `## Sources` section covers it). Wikilink fixes: `[[en/concepts/governance|Full nodes]]` → `[[en/concepts/bitcoin-node|Full nodes]]` (wrong target); `[[en/concepts/security|multisig]]` → `[[en/concepts/multisig|multisig]]` (dedicated page); `[[en/glossary|mempool]]` → `[[en/concepts/mempool|mempool]]` (dedicated page). New wikilinks: `[[en/concepts/double-spend|double-spend problem]]`, `[[en/concepts/third-parties|trusted third party]]`, `[[en/concepts/blockchain|blockchain]]`, `[[en/concepts/censorship-resistance|Censorship-resistant]]`, `[[en/concepts/difficulty-adjustment|Difficulty adjustment]]`. Fixed 8× `]]]` triple-bracket links in Related Pages. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text.

---

## [2026-04-14] enhance | wiki-en/concepts/blockchain.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; removed invalid tag `ledger`, added `concept`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Blockchain (Bitcoin)` H1; removed `*Tags: ...*` italic line; removed all four `---` horizontal rules; removed three `raw/...` inline citations — replaced book mentions with proper wikilinks instead. New wikilinks: `[[en/concepts/proof-of-work|PoW]]`, `[[en/books/inventing-bitcoin|Inventing Bitcoin]]`, `[[en/books/sovereignty-through-mathematics|Sovereignty Through Mathematics]]`, `[[en/concepts/byzantine-generals-problem|Byzantine generals problem]]` (bare → display text). Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; corrected `[[en/concepts/governance]]` ("who validates blocks") → `[[en/concepts/bitcoin-node|Bitcoin node — who validates blocks]]`; added `proof-of-work` and `utxo` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/byzantine-generals-problem.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; removed invalid tags `distributed-systems`/`consensus` → added `concept`/`protocol`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Byzantine Generals Problem` H1; removed `*Tags: ...*` italic line; removed all three `---` horizontal rules; removed `Source: raw/...` citation — replaced book mention with wikilink instead. New wikilinks: `[[en/books/sovereignty-through-mathematics|Sovereignty Through Mathematics]]`, `[[en/concepts/blockchain|Bitcoin blockchain]]`, `[[en/concepts/bitcoin-node|full node]]`, `[[en/concepts/proof-of-work|Proof of Work]]` (in body); fixed bare `[[en/concepts/proof-of-work]]`, `[[en/concepts/governance]]`, `[[en/concepts/double-spend]]` to pipe-syntax. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `blockchain` and `governance` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/cantillon-effect.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalars; removed invalid tags `monetary-theory`/`fiat` → added `concept`; added `reviewed: "2026-04-14"` (last). Body: removed `# Cantillon Effect` H1; removed `*Tags: ...*` italic line; removed all six `---` horizontal rules; removed `Source: raw/...` citation — replaced with reader-facing 21ideas.org link. New wikilinks: `[[en/entities/saifedean-ammous|Saifedean Ammous]]` (×2 — in "Fiat Era" and synthesis section); converted bare inline URL `https://21ideas.org/hozyaeva-i-raby-deneg` in synthesis section to `[Masters and Slaves of Money](url)` markdown link. Fixed 4× `]]]` triple-bracket links in Related Pages. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `mining`, `proof-of-work`, `gradually-then-suddenly` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/censorship-resistance.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; removed invalid tags `permissionless`/`nodes`/`proof-of-work` → added `concept`/`protocol`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Censorship Resistance` H1; removed `*Tags: ...*` italic line; removed all five `---` horizontal rules; removed four `raw/...` inline citations — replaced with reader-facing 21ideas.org links inline or removed (raw/Books/21-sposob had no corresponding frontmatter URL). New wikilinks: `[[en/concepts/proof-of-work|PoW]]`, `[[en/concepts/difficulty-adjustment|difficulty]]` (first section); `[[en/concepts/bitcoin-node|nodes]]` (×2 in "cannot be banned" section), `[[en/concepts/mining|miners]]`; fixed bare `[[en/concepts/bitcoin-node]]` and `[[en/concepts/bitcoin-core]]` to display text. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `difficulty-adjustment` and `mining` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/decentralization.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; added tags `concept`/`decentralization` (all existing tags valid); added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Decentralization` H1; removed `*Tags: ...*` italic line; removed all four `---` horizontal rules; removed four `raw/...` inline citations — two replaced with reader-facing 21ideas.org Source lines, others removed (covered by bottom `## Sources`). New wikilinks: `[[en/entities/satoshi-nakamoto|Satoshi]]`, `[[en/books/sovereignty-through-mathematics|Sovereignty Through Mathematics]]`, `[[en/concepts/difficulty-adjustment|difficulty adjustment]]`, `[[en/concepts/proof-of-work|Proof of Work]]`, `[[en/concepts/bip|BIP9]]`, `[[en/history/blocksize-war|blocksize-war]]`, `[[en/concepts/bitcoin-node|fully validating nodes]]`, `[[en/concepts/blockchain|blockchain]]`. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `bitcoin-node`, `censorship-resistance`, `satoshi-nakamoto` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/deflation.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; removed invalid tags `money`/`scarcity` → added `concept`; updated third source URL to chapter-specific `/glava-10` path; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Deflation (and Bitcoin)` H1; removed `*Tags: ...*` italic line; removed all three `---` horizontal rules; removed inline `raw/...` paths from mixed Sources sentence — replaced with wikilinks integrated into prose. New wikilinks: `[[en/concepts/scarcity|fixed supply]]`, `[[en/books/sovereignty-through-mathematics|Sovereignty Through Mathematics]]`, `[[en/concepts/money|money]]`, `[[en/concepts/scarcity|scarcity and the halving schedule]]`; fixed bare `[[en/concepts/cantillon-effect]]` → display text. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `cantillon-effect` and `fiat-standard` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/difficulty-adjustment.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; removed invalid tag `consensus` → added `concept`/`difficulty-adjustment`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Difficulty Adjustment` H1; removed `*Tags: ...*` italic line; removed all four `---` horizontal rules; removed two `raw/...` inline citations — one replaced with reader-facing inline link, other removed (covered by bottom `## Sources`). New wikilinks: `[[en/concepts/mining|miners]]`, `[[en/concepts/bitcoin-node|nodes]]`, `[[en/concepts/proof-of-work|PoW]]` (×2); fixed bare `[[en/concepts/mining]]` and `[[en/concepts/scarcity]]` to display text. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `bitcoin-node` entry.

---

## [2026-04-14] enhance | wiki-en/concepts/double-spend.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; removed invalid tag `consensus` → added `concept`/`double-spend`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Double Spend` H1; removed `*Tags: ...*` italic line; removed all four `---` horizontal rules; removed two `raw/...` inline citations. New wikilinks: `[[en/concepts/third-parties|trusted ledger keeper]]`, `[[en/concepts/proof-of-work|Proof of Work]]`, `[[en/concepts/bitcoin-node|full-node validation]]`, `[[en/entities/satoshi-nakamoto|Satoshi]]`, `[[en/books/inventing-bitcoin|Inventing Bitcoin]]`, `[[en/concepts/blockchain|chain]]`, `[[en/concepts/mining|miners]]`, `[[en/concepts/mempool|mempool]]`. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `proof-of-work`, `mempool`, `blockchain` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/forks.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalars; removed invalid tag `consensus` → added `concept`/`fork`; added `updated`/`reviewed: "2026-04-14"` (last). Body: removed `# Forks (Bitcoin)` H1; removed `*Tags: ...*` italic line; removed all four `---` horizontal rules; removed three `raw/...` inline citations — one replaced with reader-facing Source line, others removed. New wikilinks: `[[en/concepts/mining|miners]]`, `[[en/concepts/bitcoin-node|nodes]]`, `[[en/concepts/proof-of-work|Proof of Work]]`, `[[en/concepts/mempool|mempool]]`, `[[en/concepts/scarcity|21M cap]]`. Removed `## Related Terms`; merged with `## Related Pages` → `## Related pages`; all bullets pipe-syntax with descriptive text; added `proof-of-work`, `mempool` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/utxo.md

**Changes:** Frontmatter: removed spurious `source:` (singular) field; reordered to canonical sequence; quoted all scalar fields; removed invalid tag `accounting` (not in allowlist) → kept `[bitcoin, wiki, concept, protocol, utxo]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# UTXOs` H1; removed `*Tags: ...*` italic line; removed 6 `---` horizontal rules; removed 1 `raw/...` citation → replaced with 3 reader-facing Source lines distributed across relevant sections. Fixed `[[en/concepts/governance|full node]]` ×2 → `[[en/concepts/bitcoin-node|full node]]`. Fixed `[[en/concepts/privacy|KYC]]` → `[[en/concepts/aml|KYC]]`. Fixed `[[en/concepts/privacy]]]` triple bracket → `[[en/concepts/privacy|privacy countermeasures]]`. New wikilinks: `[[en/concepts/multisig|multisig]]` in Lightning Channels section. Reformatted Sources section from bare URLs to named markdown links. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format, fixed all `]]]` triple brackets; added `multisig`, `segwit`, `address-types`, `bitcoin-node`, `oxt-research` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/third-parties.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `trust`, `intermediaries` (not in allowlist); corrected `third-parties` → `third-party` (allowlist form); kept `[bitcoin, wiki, concept, security, censorship-resistance, third-party, decentralization]`; added `reviewed: "2026-04-14"` as last field (no `updated`). Body: removed `# Third Parties` H1; removed `*Tags: ...*` italic line; removed 4 `---` horizontal rules; removed 3 `raw/...` citations — all replaced with reader-facing Source lines using matching frontmatter URLs. New wikilinks: `[[en/entities/nick-szabo|Nick Szabo]]` in first section; `[[en/concepts/aml|KYC]]` in Why Intermediaries section; `[[en/concepts/double-spend|double spending]]`; `[[en/concepts/blockchain|blockchain]]`; `[[en/concepts/bitcoin-node|node]]` in conclusion. Fixed bare wikilinks `[[en/concepts/governance]]`, `[[en/practice/running-a-node]]` → pipe-syntax. Removed `## Related Terms` pipe-list; converted `## Related Pages` bare-link bullets → `## Related pages` with description-inside-pipe format; added `blockchain`, `bitcoin-core`, `censorship-resistance` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/taproot.md

**Changes:** Frontmatter: removed spurious `source:` (singular) field; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `upgrade` and `schnorr` (not in allowlist) → kept `[bitcoin, wiki, concept, protocol, taproot, privacy]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Taproot` H1; removed `*Tags: ...*` italic line; removed 8 `---` horizontal rules; removed 1 `raw/...` citation → replaced with `Source: [Taproot](https://21ideas.org/taproot)`. Fixed 3 self-referential `[[en/concepts/taproot|...]]` links → plain text (`Schnorr`, `MuSig2`, `MAST`). Fixed `[[en/concepts/security|multisig]]` ×3 → `[[en/concepts/multisig|multisig]]`. Fixed `[[en/concepts/governance|soft fork]]` → `[[en/concepts/forks|soft fork]]`. Fixed `[[en/concepts/segwit|malleability]]` → plain text (coverage in SegWit page is implicit). Fixed 6 `]]]` triple brackets in body (security refs + Related Pages). New wikilinks: `[[en/concepts/bip|BIPs]]` in What It Is; `[[en/concepts/address-types|address types]]` inline in Address Type section. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format; added `forks`, `utxo`, `bip` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/segwit.md

**Changes:** Frontmatter: removed spurious `source:` (singular) field; reordered to canonical sequence; quoted all scalar fields; removed invalid tag `upgrade` (not in allowlist) → kept `[bitcoin, wiki, concept, protocol, segwit]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# SegWit` H1; removed `*Tags: ...*` italic line; removed 6 `---` horizontal rules; removed 1 `raw/...` citation (with third-party learnmeabitcoin.com ref) → replaced with `Source: [SegWit](https://21ideas.org/segwit)`. Fixed 5 self-referential `[[en/concepts/segwit|...]]` links → plain text (`TXID` ×2, `malleability`, `block weight`, `Bech32`). Fixed `[[en/concepts/governance|hard fork]]` and `[[en/concepts/governance|soft fork]]` ×2 → `[[en/concepts/forks|...]]`. Fixed `[[en/history/blocksize-war]]]` and `[[en/concepts/lightning-network]]]` triple brackets in body. Added `[[en/concepts/bitcoin-core|Bitcoin Core]]` in Blocksize War section; `[[en/concepts/address-types|address types]]` inline in Bech32 paragraph. Moved Blocksize War chapter Source lines inline. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format, fixed all `]]]` triple brackets; added `forks`, `bitcoin-core`, `books/blocksize-war` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/security.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tag `custody` (not in allowlist) → kept `[bitcoin, wiki, concept, security, multisig]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Security` H1; removed `*Tags: ...*` italic line; removed 9 `---` horizontal rules; removed 7 `raw/...` citations — 6 replaced with reader-facing Source lines using matching frontmatter URLs, 1 dropped (PGP, no matching URL) with prose rephrased. Fixed 3 self-referential `[[en/concepts/security|...]]` links → plain text `seed phrase`, `Hardware wallets`, `[[en/concepts/multisig|Multisig]]`. Fixed `[[en/concepts/governance|BIP]]` → `[[en/concepts/bip|BIP]]`. Removed unverifiable `[[en/glossary|PSBT]]` anchor link → plain text `PSBT`. Reformatted Sources section from bare URLs to named markdown links. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format, fixed all `]]]` triple brackets; added `taproot`, `cypherpunks` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/scarcity.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `supply` and `halving` (not in allowlist) → kept `[bitcoin, wiki, concept, economics]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Scarcity` H1; removed `*Tags: ...*` italic line; removed 6 `---` horizontal rules; removed 3 `raw/...` citations — 2 replaced with reader-facing Source lines using matching frontmatter URLs, 1 inline reference reworded to Source line. Fixed 4 self-referential `[[en/concepts/scarcity|...]]` links → `[[en/concepts/mining|Block rewards]]`, plain text `halve`, plain text `21M cap`, plain text `scarcity`. Fixed `[[en/concepts/governance|full node]]` ×2 → `[[en/concepts/bitcoin-node|full node]]`. Added `[[en/concepts/difficulty-adjustment|difficulty adjusts]]` in Halvings myths section. Reformatted Sources section from bare URLs to named markdown links. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format, fixed all `]]]` triple brackets; added `difficulty-adjustment`, `governance` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/rpow.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalar fields; removed 5 invalid tags (`rpow`, `proof-of-work`, `hal-finney`, `digital-cash` not in allowlist; `history` kept) → `[bitcoin, wiki, concept, history, protocol]`; added `reviewed: "2026-04-14"` as last field (no `updated`). Body: removed `# RPOW` H1; removed 2 `---` horizontal rules; removed inline `raw/...` path citation in "How the system works" section — rephrased to reference [[en/series/genesis-files|Genesis Files Part V]]. New wikilinks: `[[en/series/genesis-files|Genesis Files Part V]]` in Problem section; `[[en/concepts/hashcash|Hashcash]]`; `[[en/concepts/proof-of-work|PoW]]`. Converted bare wikilink `See:` block in "Relationship to Bitcoin" to inline prose with pipe-syntax links. Removed `## Related Terms` pipe-list; converted `## Related Pages` bare-link bullets → `## Related pages` with description-inside-pipe format; added `hashcash`, `proof-of-work`, `double-spend`, `third-parties`, `series/genesis-files` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/protocol-stack.md

**Changes:** Frontmatter: removed spurious `source:` (singular) field; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `architecture` and `layers` (not in allowlist) → kept `[bitcoin, wiki, concept, protocol, lightning, scaling]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Bitcoin Protocol Stack` H1; removed `*Tags: ...*` italic line; removed 9 `---` horizontal rules; removed raw/ mention from Sources section; removed `See also:` navigation block from intro (covered by Related pages). Fixed 14+ `]]]` triple-bracket links throughout body and Related Pages. New wikilinks: `[[en/concepts/bitcoin-node|nodes]]` in Layer 0; `[[en/concepts/blockchain|blockchain]]` in Layer 1; `[[en/concepts/multisig|multisig]]` in Layer 2. Removed `## Related Terms` glossary-list (HTLC, BOLT, MAST, Witness, Gossip protocol — all defined in body text); converted `## Related Pages` → `## Related pages` with description-inside-pipe format; added `blockchain` and `multisig` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/proof-of-work.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tag `consensus` (not in allowlist) → kept `[bitcoin, wiki, concept, protocol, mining]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Proof of Work` H1; removed `*Tags: ...*` italic line; removed 7 `---` horizontal rules; removed 5 `raw/...` citations — 1 replaced with reader-facing Source line, 1 converted to wikilink Source, 3 removed (no matching URLs in frontmatter). Fixed 5 `]]]` triple-bracket links in Related Pages; fixed `[[en/series/genesis-files]]]` in Hashcash Source line. Fixed `[[en/concepts/mining|difficulty adjustment]]` → `[[en/concepts/difficulty-adjustment|difficulty adjustment]]`. New wikilinks: `[[en/concepts/bitcoin-node|nodes]]` in What It Is section; `[[en/entities/adam-back|Adam Back]]` in Hashcash section (was unlinked); added `[[en/series/gradually-then-suddenly|Gradually, Then Suddenly]]` reference in Energy section. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format; added `difficulty-adjustment`, `adam-back` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/privacy.md

**Changes:** Frontmatter: fixed unquoted URL in `sources:` array; reordered to canonical sequence; quoted all scalar fields; removed invalid tag `coinjoin` (not in allowlist) → kept `[bitcoin, wiki, concept, privacy, security]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Privacy` H1; removed `*Tags: ...*` italic line; removed ~9 `---` horizontal rules; removed 11 `raw/...` citations — all dropped (only one 21ideas.org URL in frontmatter; no per-section URLs available to fabricate). Fixed 2 self-referential `[[en/concepts/privacy|...]]` links → `[[en/concepts/aml|KYC]]` (×2; aml.md covers KYC) and plain text `CoinJoin`. Fixed 5 `]]]` triple-bracket links in Related Pages. New wikilinks: `[[en/concepts/utxo|UTXO]]` in Whirlpool section; `[[en/concepts/lightning-network|Lightning]]` in Lightning section; `[[en/concepts/bitcoin-core|Bitcoin Core]]` in tools table; `[[en/series/oxt-research|OXT Research]]` inline in Blockchain Analysis section. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format; added `aml`, `utxo`, `bitcoin-core`, `buying` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/multisig.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tag `custody` (not in allowlist) → kept `[bitcoin, wiki, concept, security, multisig, taproot]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Multisig (Multisignature)` H1; removed `*Tags: ...*` italic line; removed 9 `---` horizontal rules; removed intro-level `See also:` navigation block (covered by Related pages); removed raw/ mention from Sources section. Fixed 11+ `]]]` triple-bracket links throughout body and Related Pages. Replaced Sources section prose with markdown links. Removed `## Related Terms` glossary-style list (PSBT, Output Descriptor, Quorum, Air-gapped, MuSig2 definitions); converted `## Related Pages` → `## Related pages` with description-inside-pipe format; added `segwit` entry.

---

## [2026-04-14] enhance | wiki-en/concepts/money.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `monetary-theory` and `austrian-school` (not in allowlist) → kept `[bitcoin, wiki, concept, economics, philosophy]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Money` H1; removed `*Tags: ...*` italic line; removed ~8 `---` horizontal rules; removed 6 `raw/...` citations — all replaced with reader-facing 21ideas.org Source lines using matching URLs from frontmatter. Fixed `[[en/history/timeline]]]` triple bracket; removed raw/ portion of that line → replaced with markdown link. Fixed 2 self-referential `[[en/concepts/money|...]]` links → plain text (`Sound money`, `time preference`). Added new wikilink `[[en/concepts/deflation|deflation]]` in Deflation section. Reformatted Sources section from bare URLs to named markdown links. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format, fixed all `]]]` triple brackets; added `cantillon-effect`, `deflation`, `proof-of-work` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/mining.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `sha256` and `pow` (not in allowlist) → kept `[bitcoin, wiki, concept, mining, protocol]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Mining` H1; removed `*Tags: ...*` italic line; removed ~10 `---` horizontal rules; removed 2 `raw/...` citations — 1 replaced with reader-facing Source line, 1 removed with wikilink preserved. Fixed 4 self-referential `[[en/concepts/mining|...]]` links → plain text (`mining`, `SHA-256` ×2, `ASIC`). Fixed `[[en/glossary|mempool]]` → `[[en/concepts/mempool|mempool]]`. Fixed `[[en/concepts/scarcity]]]` and `[[en/series/gradually-then-suddenly]]]` triple brackets. New wikilinks: `[[en/concepts/difficulty-adjustment|difficulty target]]` (×2), `[[en/concepts/bitcoin-node|nodes]]` in Difficulty section, `[[en/concepts/proof-of-work|PoW]]` in Energy section. Removed `## Related Terms` pipe-list; converted `## Related Pages` → `## Related pages` with description-inside-pipe format; added `difficulty-adjustment`, `mempool`, `bitcoin-node`, `network-effects` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/mempool.md

**Changes:** Frontmatter: collapsed block `sources:` to inline array; reordered to canonical sequence; quoted all scalar fields (`category`, `quality`, `language`, `completeness`); removed invalid tag `transactions` → replaced with `concept`; added `reviewed: "2026-04-14"` as last field (no `updated` field, so `reviewed` follows `tags` directly). Body: removed `# Mempool` H1; removed `*Tags: ...*` italic line; removed 4 `---` horizontal rules; removed 2 `raw/...` citations — both replaced with reader-facing 21ideas.org Source lines. New wikilinks: `[[en/concepts/bitcoin-node|nodes]]`, `[[en/concepts/mining|Miners]]`, `[[en/concepts/scarcity|block space]]`, `[[en/concepts/forks|orphaned]]`, `[[en/concepts/proof-of-work|PoW]]`. Removed `## Related Terms` pipe-list; replaced bare-link `## Related Pages` with `## Related pages` using description-inside-pipe format; added `difficulty-adjustment` entry.

---

## [2026-04-14] enhance | wiki-en/concepts/lightning-network.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `layer-2` and `payments` (not in allowlist) → replaced with `concept`, `scaling`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Lightning Network` H1; removed `*Tags: ...*` italic line; removed 8 `---` horizontal rules; removed 5 `raw/...` citations — 4 replaced with reader-facing 21ideas.org Source lines, 1 removed (no matching URL). Fixed 2 self-referential `[[en/concepts/lightning-network|...]]` links → plain text (`payment channel`, `HTLC`). Fixed `[[en/concepts/security|multisig]]` → `[[en/concepts/multisig|multisig]]` (2 instances). Fixed `[[en/practice/lightning-tools]]]` triple bracket. Reformatted Sources section from plain URLs to markdown links. Removed `## Related Terms` pipe-list and `## Related Pages` with triple-bracket links; merged into single `## Related pages` with description-inside-pipe format; added `segwit`, `multisig`, `taproot` entries.

---

## [2026-04-14] enhance | wiki-en/concepts/hashcash.md

**Changes:** Frontmatter: added `reviewed: "2026-04-14"` as last field (was missing). Body: removed `# Hashcash` H1; removed five `---` horizontal rules. New wikilinks: `[[en/concepts/bitcoin-whitepaper|Bitcoin whitepaper]]` in Satoshi's Adaptation section; `[[en/concepts/bit-gold|Bit Gold]]` in Why It Matters section. Related pages: descriptions moved inside pipe syntax; added `[[en/concepts/bit-gold|Bit Gold — Nick Szabo's successor concept]]` entry; added descriptive text to all entity entries.

---

## [2026-04-14] enhance | wiki-en/concepts/governance.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields (`category`, `quality`, `language`, `completeness`); added `reviewed: "2026-04-14"` as last field. Body: removed `*Tags: governance, decentralization, protocol, consensus*` italic line; removed `# Bitcoin Governance` H1; removed all `---` horizontal rules; removed four `raw/...` citations — two replaced with reader-facing 21ideas.org Source lines, two removed. Fixed four self-referential `[[en/concepts/governance|...]]` links → `[[en/concepts/bip|BIP]]`, `[[en/concepts/forks|Soft fork]]`, `[[en/concepts/forks|Hard fork]]`, `[[en/concepts/bitcoin-node|full node]]`. Fixed two `]]]` triple-bracket links. New wikilinks: `[[en/concepts/bitcoin-node|Full nodes]]` and `[[en/concepts/mining|Miners]]` in table; `[[en/concepts/bitcoin-core|Bitcoin Core]]` (two instances); `[[en/concepts/bip|BIPs]]` in table. Renamed `## Related Terms` → `## Related pages`; converted inline pipe-list to bullet format with descriptive text; added `[[en/concepts/forks|Forks]]` entry. Added `## Sources` section.

---

## [2026-04-14] enhance | wiki-en/entities/adam-back.md

**Changes:** Frontmatter: collapsed block-YAML `sources:` to inline array; quoted all scalar fields; removed invalid tags `cypherpunks`, `hashcash`, `proof-of-work` (not in allowlist) → `[bitcoin, wiki, entity, history]`; added `updated` and `reviewed: "2026-04-14"` as last field; reordered to canonical sequence. Body: removed `# Adam Back` H1; removed 2 `---` horizontal rules; replaced `raw/Theory/history/genesis-files/genesis-2.md` path citation with `[Genesis Files, Part II](https://21ideas.org/gf/genesis-2)`. New wikilinks: `[[en/entities/cypherpunks|cypherpunk]]`, `[[en/concepts/hashcash|Hashcash]]`, `[[en/concepts/bitcoin-whitepaper|Bitcoin whitepaper]]` in intro; `[[en/concepts/proof-of-work|proof-of-work]]` in Why-He-Matters section; `[[en/concepts/double-spend|double spending]]` in Hashcash section; `[[en/entities/satoshi-nakamoto|Satoshi]]` in Relationship section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; converted bare wikilinks to description-inside-pipe format; added `cypherpunks`, `b-money`, `genesis-files` entries.
**Content audit:** Solid for medium-completeness entity page. One hedged claim ("In widely cited accounts, Back contacted Satoshi before whitepaper post") goes beyond the 21ideas sources but is appropriately flagged with "widely cited accounts" language — not fabricated.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/cypherpunks.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tag `cypherpunks` (not in allowlist) → `[bitcoin, wiki, entity, history, philosophy]`; added `updated` and `reviewed: "2026-04-14"` as last field. Body: removed `# Cypherpunks` H1; removed `*Tags: entity, movement, history, privacy, cryptography*` italic line; removed 6 `---` horizontal rules; replaced 4 `raw/...` citations with named Source lines using 21ideas.org URLs. Removed wikilinks from table cells (Key Figures and Progression tables) per no-links-in-table-cells rule. Fixed self-referential `[[en/entities/cypherpunks|Cypherpunks]]` → plain text. New wikilinks in body prose: `[[en/entities/eric-hughes|Eric Hughes]]`, `[[en/entities/tim-may|Timothy May]]` in intro; `[[en/concepts/segwit|SegWit]]` in Crypto Anarchist section; `[[en/entities/satoshi-nakamoto|Satoshi Nakamoto]]`, `[[en/concepts/hashcash|Hashcash]]`, `[[en/entities/adam-back|Back]]`, `[[en/concepts/b-money|b-money]]`, `[[en/concepts/bitcoin-whitepaper|whitepaper]]` in Progression section; `[[en/entities/phil-zimmermann|Philip Zimmermann]]` in PGP section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 6 `]]]` triple brackets; converted bare links to description-inside-pipe format; added `eric-hughes`, `tim-may`, `adam-back`, `david-chaum`, `privacy`, `bitcoin` entries.
**Content audit:** Solid for medium-completeness entity page. Coverage across all four source manifesto articles is adequate.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/david-chaum.md

**Changes:** Frontmatter: collapsed block-YAML `sources:` to inline array; quoted all scalar fields; removed invalid tags `ecash`, `digicash`, `cypherpunks` (not in allowlist) → `[bitcoin, wiki, entity, privacy, history]`; added `updated` and `reviewed: "2026-04-14"` as last field; reordered to canonical sequence. Body: removed `# David Chaum` H1; removed 2 `---` horizontal rules; replaced `raw/Theory/history/genesis-files/genesis-1.md` path citation with `[Genesis Files, Part I](https://21ideas.org/gf/genesis-1)`. New wikilinks: `[[en/entities/cypherpunks|cypherpunk]]` and `[[en/concepts/privacy|privacy]]` in intro; `[[en/concepts/censorship-resistance|censorship resistance]]` and `[[en/concepts/third-parties|third parties]]` in Why-Chaum-Matters section (fixing bare links). Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; converted bare wikilinks to description-inside-pipe format; added `cypherpunks`, `privacy`, `genesis-files` entries.
**Content audit:** Solid for medium-completeness entity page. Coverage of eCash, DigiCash, and broader significance is adequate.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/eric-hughes.md

**Changes:** Frontmatter: collapsed block-YAML `sources:` to inline array; quoted all scalar fields; removed invalid tags `cypherpunks`, `manifesto` (not in allowlist) → `[bitcoin, wiki, entity, privacy, history]`; added `updated` and `reviewed: "2026-04-14"` as last field; reordered to canonical sequence. Body: removed `# Eric Hughes` H1; removed 2 `---` horizontal rules; replaced `raw/Theory/philosophy/cypherpunks-manifesto.md` path citation with `[Cypherpunk's Manifesto](https://21ideas.org/manifest-shifropanka)`. New wikilinks: `[[en/entities/cypherpunks|cypherpunk]]` and `[[en/concepts/privacy|privacy]]` in intro. Fixed 3 bare wikilinks in Why-This-Matters section → `[[en/concepts/third-parties|third parties]]`, `[[en/concepts/censorship-resistance|censorship resistance]]`, `[[en/concepts/privacy|privacy]]`. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 3 bare wikilinks to description-inside-pipe format; added `censorship-resistance` and `bitcoin` entries.
**Content audit:** Solid for medium-completeness entity page.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/gigi.md

**Changes:** Frontmatter: removed spurious `source:` field; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `author`, `entities` (not in allowlist) → `[bitcoin, wiki, entity, philosophy]`; added `updated` and `reviewed: "2026-04-14"` as last field. Body: removed `# Gigi (dergigi)` H1; removed `*Tags: entity, person, Bitcoin-philosopher, author*` italic line; removed 5 `---` horizontal rules; removed 6 `raw/...` source citations (sources: [] — no public URLs). Fixed `[[en/concepts/mining|difficulty adjustment]]` → `[[en/concepts/difficulty-adjustment|difficulty adjustment]]`. Fixed `[[en/books/21-ways]]]` triple bracket. New wikilinks: `[[en/concepts/bitcoin|Bitcoin]]` in Who-He-Is; `[[en/series/what-i-learned-from-bitcoin|What I Learned From Bitcoin]]` in Key Works; `[[en/concepts/blockchain|blockchain]]` in Core Themes. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 4 `]]]` triple brackets; converted bare links to description-inside-pipe; added `what-i-learned-from-bitcoin` and `proof-of-work` entries.
**Content audit:** Solid for medium-completeness entity page. sources: [] is intentional — all articles are raw/-only with no public 21ideas.org URLs.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/hal-finney.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `cypherpunks`, `entities` (not in allowlist) → `[bitcoin, wiki, entity, history]`; fixed double-slash URL `gf/genesis-5//` → `gf/genesis-5/`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Hal Finney` H1; removed `*Tags: entity, person, cypherpunk, Bitcoin-pioneer*` italic line; removed 5 `---` horizontal rules; replaced 2 `raw/...` citations with named Source lines. Fixed duplicate `[[en/entities/cypherpunks|cypherpunk]]` in same section → plain text on second mention. Fixed `[[en/concepts/security|cold storage]]` wrong target → `[[en/glossary#cold-storage|cold storage]]`. Converted plain URLs in Sources section to markdown links. New wikilinks: `[[en/concepts/rpow|RPOW]]` in Who-He-Was bullet; `[[en/entities/adam-back|Adam Back]]`, `[[en/concepts/hashcash|Hashcash]]`, `[[en/concepts/double-spend|double-spending]]`, `[[en/concepts/blockchain|blockchain]]` in RPOW section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 5 `]]]` triple brackets; converted bare links to description-inside-pipe; added `rpow` and `proof-of-work` entries.
**Content audit:** Solid for medium-completeness entity page. All major claims traceable to cited 21ideas.org sources.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/nick-szabo.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `cypherpunks`, `entities` (not in allowlist) → `[bitcoin, wiki, entity, history]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Nick Szabo` H1; removed `*Tags: entity, person, cypherpunk, Bit-Gold, smart-contracts*` italic line; removed 6 `---` horizontal rules; replaced `Source: [[en/series/genesis-files]]]` (malformed wikilink used as citation) with `[Genesis Files, Part IV](https://21ideas.org/gf/genesis-4/)`; removed 3 `raw/...` citations (no public URLs). Fixed self-referential `[[en/entities/nick-szabo|Nick Szabo]]` → plain text. Converted plain URLs in Sources section to markdown links. New wikilinks: `[[en/concepts/bit-gold|Bit Gold]]` in intro bullet; `[[en/concepts/blockchain|blockchain]]` in Bit Gold section; `[[en/concepts/third-parties|trusted third party]]` in TTPs section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 6 `]]]` triple brackets; converted bare links to description-inside-pipe; added `bit-gold` and `third-parties` entries.
**Content audit:** Solid for medium-completeness entity page. "Shelling Out" and Social Scalability essays have no public 21ideas.org URLs — raw/ only. Adequately covered in body text.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/parker-lewis.md

**Changes:** Frontmatter: removed spurious `source:` field; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `entities`, `parker-lewis`, `gradually-then-suddenly` (not in allowlist) → `[bitcoin, wiki, entity, economics]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Parker Lewis` H1; removed `*Tags: entity, person, economist, writer, Unchained-Capital*` italic line; removed 5 `---` horizontal rules. Fixed 4 `]]]` triple brackets in intro See-also block → proper pipe-syntax inline links. Fixed 4 `]]]` triple brackets in Relationship-to-Other-Works section → pipe-syntax inline links. Fixed 5 `]]]` triple brackets in Related Pages. Removed `## Related Terms` definitional bullet list (no wikilinks). Renamed `## Related Pages` → `## Related pages`. New wikilinks: `[[en/concepts/bitcoin|Bitcoin]]` in Background; `[[en/concepts/multisig|multisig]]` in Background; `[[en/concepts/lightning-network|Lightning]]` in Key Essays (Bitcoin Is Not Too Slow). Added `bitcoin` and `lightning-network` entries to Related pages.
**Content audit:** Solid. sources: [] is intentional — all articles are raw/-only with no public 21ideas.org URLs.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/phil-zimmermann.md

**Changes:** Frontmatter: collapsed block-YAML `sources:` to inline array; quoted all scalar fields; removed invalid tags `pgp`, `cryptography`, `cypherpunks` (not in allowlist) → `[bitcoin, wiki, entity, privacy, security, history]`; added `updated` and `reviewed: "2026-04-14"` as last field; reordered to canonical sequence. Body: removed `# Phil Zimmermann` H1; removed 2 `---` horizontal rules; replaced `raw/Practice/security/pgp.md` path citation with `[21ideas PGP practice guide](https://21ideas.org/pgp-verify)`. New wikilinks: `[[en/entities/cypherpunks|cypherpunk]]` in intro; `[[en/concepts/bitcoin|Bitcoin]]` in PGP section; `[[en/series/genesis-files|Genesis Files Part II]]` in cypherpunk context section; `[[en/concepts/privacy|privacy]]` in cypherpunk context section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 2 bare wikilinks to description-inside-pipe; added `privacy` and `genesis-files` entries.
**Content audit:** Solid for medium-completeness entity page.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/saifedean-ammous.md

**Changes:** Frontmatter: removed spurious `source:` field; added `sources: []`; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `entities`, `austrian-school`, `bitcoin-standard` (not in allowlist) → `[bitcoin, wiki, entity, economics]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Saifedean Ammous` H1; removed `*Tags: entity, person, economist, author, Austrian-school*` italic line; removed 9 `---` horizontal rules. Fixed 15+ `]]]` triple brackets throughout intro, body sections, and Related Pages. New wikilinks: `[[en/concepts/money|money]]` in Central Thesis; `[[en/concepts/bitcoin|Bitcoin]]` in Bitcoin Standard section; `[[en/concepts/decentralization|decentralization]]` in Altcoins section; `[[en/entities/parker-lewis|Parker Lewis]]` fixing triple bracket; `[[en/concepts/cantillon-effect|Cantillon Effect]]` fixing triple bracket; `[[en/books/fiat-standard|Fiat Standard]]`, `[[en/concepts/money|Money]]`, `[[en/concepts/scarcity|Scarcity]]`, `[[en/concepts/cantillon-effect|Cantillon Effect]]` in Influence section (all fixing triple brackets). Removed `## Related Terms` definitional bullet list; renamed `## Related Pages` → `## Related pages`; converted bare links to description-inside-pipe; added `bitcoin` and `decentralization` entries. Added `## Sources` section (was missing entirely).
**Content audit:** Solid, high-completeness entity page. sources: [] intentional — synthesized from raw/ only.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/satoshi-nakamoto.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `satoshi`, `entities` (not in allowlist) → `[bitcoin, wiki, entity, history]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Satoshi Nakamoto` H1; removed `*Tags: entity, person, Bitcoin-creator, anonymous*` italic line; removed 6 `---` horizontal rules; replaced 2 `raw/...` citations with named Source lines using 21ideas.org URLs; converted 4 plain URLs in Sources section to markdown links. Fixed `[[en/concepts/governance|full nodes]]` wrong target → `[[en/concepts/bitcoin-node|full nodes]]`. Fixed `[[en/history/blocksize-war]]]` triple bracket → `[[en/history/blocksize-war|The Blocksize War]]` (verified file exists). Fixed `[[en/series/genesis-files]]]` triple bracket → pipe syntax. Fixed `[[en/concepts/governance]]]` triple bracket → `[[en/concepts/governance|Bitcoin Governance]]`. New wikilinks: `[[en/concepts/bitcoin-whitepaper|Bitcoin whitepaper]]` in Identity; `[[en/concepts/double-spend|double-spend problem]]`, `[[en/concepts/blockchain|blockchain]]`, `[[en/concepts/hashcash|Hashcash]]`, `[[en/concepts/b-money|b-money]]` in Whitepaper section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 7 `]]]` triple brackets; converted bare links to description-inside-pipe; added `bitcoin-whitepaper`, `governance`, `blocksize-war` entries.
**Content audit:** Solid for medium-completeness entity page. All claims traceable to cited 21ideas.org sources.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/entities/tim-may.md

**Changes:** Frontmatter: collapsed block-YAML `sources:` to inline array; quoted all scalar fields; removed invalid tags `cypherpunks`, `crypto-anarchy` (not in allowlist) → `[bitcoin, wiki, entity, privacy, history]`; added `updated` and `reviewed: "2026-04-14"` as last field; reordered to canonical sequence. Body: removed `# Tim May` H1; removed 2 `---` horizontal rules; replaced `raw/Theory/philosophy/crypto-anarchist-manifesto.md` path citation with `[Crypto Anarchist Manifesto](https://21ideas.org/manifest-kriptoanarhista)`. New wikilinks: `[[en/entities/cypherpunks|cypherpunk]]` and `[[en/concepts/bitcoin|Bitcoin]]` in intro; `[[en/concepts/censorship-resistance|censored]]` in manifesto section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; converted 3 bare wikilinks to description-inside-pipe; added `eric-hughes`, `privacy`, `bitcoin` entries.
**Content audit:** Solid for medium-completeness entity page.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/history/blocksize-war.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; quoted URL in `sources:` inline array (was unquoted); removed invalid tag `blocksize-war` (not in allowlist) → `[bitcoin, wiki, history, governance]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# The Blocksize War (2015–2017)` H1; removed `*Tags: history, governance, SegWit, Bitcoin-Cash, UASF*` italic line; removed 8 `---` horizontal rules; converted plain URL in Sources section to markdown link. Fixed self-referential `[[en/history/blocksize-war|Blocksize War]]` → plain text (2 instances). Fixed `Source: [[en/books/blocksize-war]]]` triple bracket → `[[en/books/blocksize-war|The Blocksize War]]`. Fixed 8 wrong `[[en/concepts/governance|...]]` link targets: `hard fork`/`hard forks` → `[[en/concepts/forks|...]]`, `soft fork`/`soft forks` → `[[en/concepts/forks|...]]`, `full node`/`full nodes` → `[[en/concepts/bitcoin-node|...]]`, `BIP` → `[[en/concepts/bip|BIP]]`. New wikilinks: `[[en/concepts/decentralization|decentralization]]` in Core Dispute; `[[en/entities/satoshi-nakamoto|Satoshi Nakamoto]]` in Craig Wright section; `[[en/concepts/governance|Bitcoin governance]]` in Legacy. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 5 `]]]` triple brackets; converted bare links to description-inside-pipe; added `forks`, `segwit`, `bitcoin-node` entries.
**Content audit:** Solid, high-completeness history page.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/history/pre-bitcoin-cypherpunks.md

**Changes:** Frontmatter: removed spurious `source:` field; added `sources: []`; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `cypherpunks`, `precursors` (not in allowlist) → `[bitcoin, wiki, history, philosophy]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Pre-Bitcoin: The Cypherpunk Era` H1; removed `*Tags: history, cypherpunks, digital-cash, eCash, Hashcash, Bit-Gold*` italic line; removed 9 `---` horizontal rules. Fixed `Source: [[en/series/genesis-files]]]` triple bracket → `[[en/series/genesis-files|Genesis Files]]`. New wikilinks: `[[en/entities/david-chaum|David Chaum]]` in eCash section; `[[en/entities/adam-back|Adam Back]]`, `[[en/concepts/hashcash|Hashcash]]`, `[[en/concepts/bitcoin-whitepaper|Bitcoin whitepaper]]` in Hashcash section; `[[en/concepts/b-money|b-money]]` in b-money section; `[[en/concepts/bit-gold|Bit Gold]]` in Bit Gold section; `[[en/concepts/blockchain|blockchain]]` in Bit Gold section; `[[en/entities/hal-finney|Hal Finney]]`, `[[en/concepts/rpow|RPOW]]`, `[[en/concepts/double-spend|double-spending]]` in RPOW section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 6 `]]]` triple brackets; converted bare links to description-inside-pipe; added `david-chaum`, `adam-back`, `proof-of-work` entries.
**Content audit:** Solid, high-completeness history page. Table correctly has no wikilinks in cells.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/history/timeline.md

**Changes:** Frontmatter: removed spurious `source:` field; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `timeline`, `events` (not in allowlist) → `[bitcoin, wiki, history]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Bitcoin Timeline` H1; removed `*Tags: history, timeline, events*` italic line; removed 9 `---` horizontal rules. Removed all wikilinks from table cells (hard rule — no wikilinks in table cells): removed 15 links across Pre-Bitcoin, Bitcoin Creation, Macro-Financial, Scaling Debate, and Protocol Upgrades tables. Fixed 4 `]]]` triple brackets in prose ("See..." lines): `[[en/history/pre-bitcoin-cypherpunks|Pre-Bitcoin Cypherpunks]]`, `[[en/series/genesis-files|Genesis Files]]`, `[[en/history/blocksize-war|Blocksize War]]`, `[[en/books/blocksize-war|The Blocksize War (book)]]`. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 6 `]]]` triple brackets; converted bare links to description-inside-pipe; added `segwit` and `taproot` entries.
**Content audit:** Solid, high-completeness timeline. Table-cell link removal is correct per hard rule; key concepts remain linked in prose and Related pages.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/practice/buying.md

**Changes:** Frontmatter: removed spurious `source:` field; reordered to canonical sequence; quoted all scalar fields; removed invalid tags `buying`, `kyc-free` (not in allowlist) → `[bitcoin, wiki, privacy, security]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Buying Bitcoin` H1; removed `*Tags: practice, buying, no-KYC, P2P*` italic line; removed 7 `---` horizontal rules; removed raw/ path from `### Hodl Hodl` heading and `### RoboSats` heading; removed `raw/Practice/buy/newbie-buy.md` inline citation; removed `raw/Theory/economics/dollar-cost-averaging.md` source line (no public URL). Fixed `[[en/concepts/privacy|KYC]]` wrong target → `[[en/concepts/aml|KYC]]`. Fixed `[[en/concepts/security|multisig]]` wrong target → `[[en/concepts/multisig|multisig]]`. Fixed `[[en/concepts/security|self-custody]]` wrong target → `[[en/practice/storage|self-custody]]`. Fixed self-referential `[[en/practice/buying|Hodl Hodl]]` and `[[en/practice/buying|P2P exchange]]` → plain text. Fixed 3 `]]]` triple brackets. New wikilinks: `[[en/concepts/lightning-network|Lightning]]` in RoboSats section. Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 3 `]]]` triple brackets; converted bare links to description-inside-pipe; added `aml`, `multisig`, `lightning-network` entries.
**Content audit:** Solid for medium-completeness practice page. sources: [] intentional — raw/-only content.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/practice/lightning-tools.md

**Changes:** File was already substantially enhanced from prior work — no H1, no tags line, no `---` rules, canonical frontmatter. One fix applied: `[[en/glossary#Private key|keys]]` → `[[en/glossary#private-key|keys]]` (anchor format: capital letter and space → lowercase hyphenated per Obsidian/Quartz standard).
**Content audit:** Solid, medium-completeness practice page. Frontmatter, wikilinks, and body all compliant.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/practice/privacy-practice.md

**Changes:** Frontmatter: removed spurious `source:` field; quoted all scalar fields; reordered to canonical sequence (title → category → quality → sources → synthesized_date → completeness → language → tags → updated → reviewed); removed invalid tags `practice`, `coinjoin` (not in allowlist) → `[bitcoin, wiki, privacy, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Privacy in Practice` H1; removed `*Tags: practice, privacy, CoinJoin, Dojo, GrapheneOS*` italic line; removed 10 `---` horizontal rules; removed `raw/Practice/privacy/grapheneos.md` from `## Step 2` heading; removed `raw/Practice/privacy/dojo/` inline annotation from Dojo entry; removed `raw/Practice/privacy/ronindojo.md` from RoninDojo entry; removed `Source: raw/Theory/privacy/coinjoin.md` line (no public URL); removed `raw/Theory/privacy/bip47-the-ugly-duckling.md` from `## Step 5` heading; removed `freesamourai.md` reference → plain "community channels". Fixed self-referential `[[en/practice/privacy-practice|Dojo]]`, `[[en/practice/privacy-practice|RoninDojo]]`, `[[en/practice/privacy-practice|Whirlpool]]` → plain bold text. Fixed `[[en/concepts/privacy|CoinJoin]]` wrong target → plain text "CoinJoin". Fixed `[[en/concepts/lightning-network]]]` triple bracket → `[[en/concepts/lightning-network|Lightning Network]]`. Fixed `[[en/practice/buying]]]` triple bracket → `[[en/practice/buying|Buying Bitcoin]]`. Fixed `[[en/series/oxt-research|blockchain analysis]]` (second link) → kept first occurrence as link, removed duplicate. New wikilinks: `[[en/concepts/privacy|privacy]]` (Step 1), `[[en/concepts/aml|KYC]]` (Step 1), `[[en/practice/running-a-node|node]]` (Step 3), `[[en/concepts/bip|BIP47]]` (Step 5). Removed `## Related Terms` pipe-list; renamed `## Related Pages` → `## Related pages`; fixed 5 `]]]` triple brackets; rebuilt with 10 description-inside-pipe entries.
**Content audit:** Solid, high-completeness practice page. sources: [] intentional — synthesized from multiple raw/ sources with no single public URL. Samourai Wallet arrest note retained with updated wording.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/practice/running-a-node.md

**Changes:** Frontmatter: removed spurious `source:` field; added `sources: []`; quoted all scalar fields; reordered to canonical sequence; removed invalid tags `practice`, `sovereignty`, `bitcoin-core` (not in allowlist) → `[bitcoin, wiki, node, privacy, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Running a Bitcoin Node` H1; removed `*Tags: practice, node, sovereignty, privacy, Bitcoin-Core, self-verification*` italic line; removed 11 `---` horizontal rules. Fixed 10 `]]]` triple brackets: `[[en/concepts/governance|Bitcoin Governance]]`, `[[en/concepts/privacy|Privacy]]`, `[[en/concepts/bitcoin|Bitcoin]]`, `[[en/practice/storage|Storage & Self-Custody]]`, `[[en/practice/privacy-practice|Privacy in Practice]]` (intro See also), `[[en/history/blocksize-war|The Blocksize War (2015-2017)]]`, `[[en/concepts/governance|Bitcoin Governance]]` (Why Run section), `[[en/practice/privacy-practice|Privacy in Practice]]` (Privacy section), and Related pages. Replaced subsequent `[[en/practice/privacy-practice]]]` in Sparrow/Samourai sections with plain text (already linked above). New wikilinks: `[[en/concepts/bitcoin-node|Bitcoin Node]]` (intro first mention), `[[en/concepts/blockchain|blockchain]]` (intro first mention), `[[en/glossary#hard-fork|hard fork]]` (verbatim from link map — blocksize-war section), `[[en/concepts/bitcoin-core|Bitcoin Core]]` (Software section first mention), `[[en/concepts/lightning-network|Lightning Network]]` (Umbrel section first mention), `[[en/concepts/utxo|UTXO]]` (Disk Requirements section), `[[en/concepts/proof-of-work|proof-of-work]]` (SPV comparison section). Removed `## Related Terms` definitional list. Added `## Sources` section (missing). Renamed `## Related Pages` → `## Related pages`; rebuilt with 10 description-inside-pipe entries.
**Content audit:** Solid, high-completeness practice page. sources: [] intentional — synthesized from multiple raw/ sources. Content covers hardware, software, disk requirements, IBD, wallet connections, Tor, and node type comparison — comprehensive.
**Lint:** 0 issues

---

## [2026-04-14] enhance | wiki-en/practice/storage.md

**Changes:** Frontmatter: removed spurious `source:` field; converted to canonical sequence and quoted all scalar fields; populated `sources:` from referenced `raw/` metadata `url:` slugs (no fabricated URLs); removed invalid tag `practice` (not in allowlist) → `[bitcoin, wiki, security, multisig]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Storage & Self-Custody` H1; removed `*Tags: ...*` italic line; removed all standalone `---` horizontal rules; removed all `raw/...` path mentions; replaced `raw/...` “Source:” line with public 21ideas.org links; fixed wrong wikilinks (`[[en/concepts/security|...]]`) → correct targets from link map (hardware wallet, PSBT, multisig). Removed `## Related Terms` and `## Related Pages`; rebuilt as a single `## Related pages` section with valid `[[en/...]]` links and fixed malformed `]]]` links.
**Content audit:** Solid structure and coverage for a practice overview. Some product-specific claims (e.g., device feature lists) are presented without inline citations; resolving that would require a Mode B update pass (not part of enhance).
**Lint:** Page passes mechanical checks; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/series/bitcoin-astronomy.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `series`, `long-term` (not in allowlist) → `[bitcoin, wiki, philosophy, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Bitcoin Astronomy` H1; removed the italic metadata line (contained `raw/...` path); removed all standalone `---` horizontal rules. Fixed malformed wikilinks (`[[en/philosophy/overview]]]`, `[[en/entities/gigi]]]'s`, `[[en/concepts/...]]]`) and removed the `[[en/philosophy/overview]]` link (not present in the EN link map). Standardized `PoW` link display to `Proof of Work`. Removed `## Related Terms` and `## Related Pages`; rebuilt as a single `## Related pages` section. Converted the bare source URL to a normal markdown link item.
**Content audit:** Solid, medium-completeness series overview; intentionally speculative framing is clear. No Mode B work required.
**Lint:** Page passes mechanical checks; EN layer still has known legacy issues elsewhere.

---
