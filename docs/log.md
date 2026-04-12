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
