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

## [2026-04-14] enhance | wiki-en/practice/storage.md (follow-up)

**Changes:** Updated glossary wikilinks to match the regenerated link map format (heading-text fragments): `[[en/glossary#Hardware wallet|Hardware wallet]]` and `[[en/glossary#PSBT (Partially Signed Bitcoin Transaction)|PSBT (Partially Signed Bitcoin Transaction)]]`. Removed a non-verbatim PSBT label variant.
**Lint:** Page not flagged in EN lint report; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/concepts/* (glossary anchor update)

**Changes:** Converted slug-style glossary fragments to heading-text fragments (per regenerated `docs/link-map-en.md`) in `wiki-en/concepts/aml.md`, `wiki-en/concepts/address-types.md`, `wiki-en/concepts/b-money.md`. Examples: `#kyc-know-your-customer` → `#KYC — Know Your Customer`, `#public-key` → `#Public key`, `#smart-contract` → `#Smart contract`, `#nakamoto-consensus` → `#Nakamoto Consensus`.
**Lint:** Files not flagged in EN lint report; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/topics/bitcoin-dissidents.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `human-rights`, `activism` (not in allowlist) → `[bitcoin, wiki, philosophy, censorship-resistance, privacy]`; added `reviewed: "2026-04-14"` as last field. Body: removed `# Bitcoin for Dissidents` H1; removed `*Tags: ...*` italic line; removed all standalone `---` horizontal rules; removed `raw/...` reference line and replaced with the public source link. Removed self-referential links in the overview. Removed wikilinks inside the table (hard rule). Removed `## Related Terms` and `## Related Pages`; rebuilt as a single `## Related pages` section with valid, map-backed links and fixed malformed `]]]` links.
**Content audit:** Solid, high-level synthesis with concrete case studies. No Mode B work required.
**Lint:** Page not flagged in EN lint report; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/topics/network-effects.md

**Changes:** Frontmatter: reordered to canonical sequence; quoted all scalar fields; removed invalid tags `adoption`, `network-effects` (not in allowlist) → `[bitcoin, wiki, economics, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed H1 and the italic `*Tags:*` line; removed all standalone `---` horizontal rules; replaced `raw/...` citation with the public 21ideas.org source link; fixed malformed `]]]` links; removed `## Related Terms` and `## Related Pages`; rebuilt as a single `## Related pages` section with valid, link-map-backed links.
**Content audit:** Solid, high-completeness topic page; no Mode B update required.
**Lint:** Page not flagged in EN lint report; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/history/timeline.md

**Changes:** Body: removed `raw/` mention from `## Sources` (EN enhance rule); added link-map-backed `[[en/...]]` references outside tables for key precursors (Hashcash, b-money, Bit Gold, RPOW) and the whitepaper. No changes inside tables (hard rule).
**Content audit:** Likely needs a Mode B fact/citation pass for some precise claims (e.g., “MuSig2 2023+”, fine-grained scaling debate details, and strong wording like “exposed as fraud”) because the page has `sources: []` and currently provides no canonical URLs.
**Lint:** Ran `python3 tools/lint.py --layer en --write-report`; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/series/discovering-bitcoin.md

**Changes:** Frontmatter: standardized canonical field order; quoted scalar values; replaced off-allowlist tags (`series`, `zucco`) with allowlist tags `[bitcoin, wiki, economics, philosophy, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed H1, removed `raw/...` metadata line, removed standalone `---` rules, removed `## Related Terms` and legacy `## Related Pages` (and fixed malformed `]]]` links) → rebuilt a single `## Related pages` list with link-map-backed targets. Wikilinks: fixed wrong targets (`Multisig`, `HTLC`) using `docs/link-map-en.md`; removed a non-map-backed “Time preference” wikilink.
**Content audit:** Solid series overview; factual claims are high-level and do not depend on missing raw/ URLs beyond the canonical series URL in `sources:`.
**Lint:** Ran `python3 tools/lint.py --layer en --write-report`; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/series/genesis-files.md

**Changes:** Frontmatter: standardized canonical field order; quoted scalar values; replaced off-allowlist tags (`series`, `cypherpunks`) with allowlist tags `[bitcoin, wiki, history, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed H1, removed `raw/...` metadata line, removed standalone `---` rules, removed `## Related Terms` and legacy `## Related Pages` (and fixed malformed `]]]` links) → rebuilt a single `## Related pages` list with link-map-backed targets. Wikilinks: converted Part 3–5 system names to map-backed page links (`b-money`, `Bit Gold`, `RPOW`); fixed `Proof-of-work` label to `Proof of Work`; added `David Chaum` and `Hal Finney` entity links in headings (outside tables).
**Content audit:** Solid series overview with concrete system summaries; the “private email” paragraph is already cautiously worded.
**Lint:** Ran `python3 tools/lint.py --layer en --write-report`; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/series/gradually-then-suddenly.md

**Changes:** Frontmatter: standardized canonical field order; quoted scalar values; replaced off-allowlist tags (`series`, `parker-lewis`) with allowlist tags `[bitcoin, wiki, economics, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed H1, removed `raw/...` metadata line, removed standalone `---` rules, removed `## Related Terms` and legacy `## Related Pages` (and fixed malformed `]]]` links) → rebuilt a single `## Related pages` list with link-map-backed targets and consistent labels.
**Content audit:** Solid high-level series summary; the Part 16 note is preserved as-is.
**Lint:** Ran `python3 tools/lint.py --layer en --write-report`; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/series/oxt-research.md

**Changes:** Frontmatter: standardized canonical field order; quoted scalar values; replaced off-allowlist tags (`series`, `blockchain-analysis`) with allowlist tags `[bitcoin, wiki, privacy, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed H1, removed `raw/...` metadata line, removed standalone `---` rules, removed a self-referential “blockchain analysis” wikilink and an internal “Source files” line; fixed malformed `[[en/practice/privacy-practice]]].` link; removed `## Related Terms` and legacy `## Related Pages` (and fixed malformed `]]]` links) → rebuilt a single `## Related pages` list with link-map-backed targets. Avoided adding non-map-backed links for CoinJoin/Whirlpool/Dojo.
**Content audit:** Solid, high-completeness series summary; Samourai arrest note preserved as-is.
**Lint:** Ran `python3 tools/lint.py --layer en --write-report`; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/series/silk-road.md

**Changes:** Frontmatter: standardized canonical field order; quoted scalar values; replaced off-allowlist tags (`series`, `adoption`) with allowlist tags `[bitcoin, wiki, history, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed H1, removed `raw/...` metadata line, removed standalone `---` rules, removed `raw/...` source line in the Ulbricht essay section; fixed malformed `[[en/concepts/privacy]]]` links; removed `## Related Terms` and legacy `## Related Pages` (and fixed malformed `]]]` links) → rebuilt a single `## Related pages` list with link-map-backed targets.
**Content audit:** Kept all substantive claims unchanged; this pass was mechanical/style compliance only.
**Lint:** Ran `python3 tools/lint.py --layer en --write-report`; EN layer still has known legacy issues elsewhere.

---

## [2026-04-14] enhance | wiki-en/series/what-i-learned-from-bitcoin.md

**Changes:** Frontmatter: standardized canonical field order; quoted scalar values; replaced off-allowlist tags (`series`, `gigi`) with allowlist tags `[bitcoin, wiki, philosophy, synthesized]`; added `reviewed: "2026-04-14"` as last field. Body: removed H1, removed `raw/` mentions (including “raw/ library” phrasing and `Source: raw/...` lines), removed standalone `---` rules; fixed malformed `]]]` links; corrected `Philosophy Overview` link label; replaced incorrect “full node” link with the map-backed glossary entry `[[en/glossary#Node / Full node|Node / Full node]]`; removed legacy `## Related Terms` / `## Related Pages` → rebuilt a single `## Related pages` list with link-map-backed targets.
**Content audit:** Kept substantive content unchanged; this pass was mechanical/style compliance only.
**Lint:** Ran `python3 tools/lint.py --layer en --write-report`; EN layer still has known legacy issues elsewhere.

---

## [2026-04-24] process | tighten raw/ ingest — paste-first + verbatim rule

Changes: INGEST-SKILL.md (paste-first flow, verbatim rule, inventory check, new zero-tolerance rule 7); CONTRIBUTING.md (contributor prompt template updated — Content field first, URL second, copy instructions and JS-pages note added); WIKI-GUIDE.md (prompt pattern updated); README.md (ingest step 1 note added).

---

---

## [2026-04-24] process | clarify source URL policy in CLAUDE.md

Changes: CLAUDE.md — three lines updated to replace "21ideas.org URLs" with "canonical source URL from the raw/ file's url: field". The rule was never 21ideas.org-only; other accepted domains (nakamotoinstitute.org, bitcoin.org, etc.) are valid. No behaviour change — wording only.

---

---

## [2026-04-24] lint | fix wiki-ru/ issues + lint tool improvements

wiki-ru/ flagged rows: 7 → 0.
Changes:
- tools/lint.py: added META_FILES exemption (contribute.md, support.md) — skips missing_keys, missing_reviewed, bad_tags, raw_in_body for meta/utility pages in both layers. Added code-fence-aware raw_in_body check (skips lines inside ``` blocks for all other files).
- wiki-ru/contribute.md: updated ingest prompt template to paste-first (Content field added as first required field, URL second); added JS-rendered pages note.
Lint: python3 tools/lint.py --layer both --write-report; wiki-ru/ 0 issues; wiki-en/ 23 (pre-existing, unrelated to this pass).

---

## [2026-04-24] ingest | quantum-computing-ama (both layers)

**Raw source:** raw/Theory/security/quantum-computing-ama.md
**URL in raw/:** https://stacker.news/items/1477913/
**Created:** wiki-en/topics/quantum-computing-ama.md, wiki-ru/topics/quantum-computing-ama.md
**Indexes:** wiki-en/index.md (Topics); wiki-ru/index.md (Topics — replaced missing `scott-aaronson-quantum-ama-distilled` with `quantum-computing-ama`)
**Wikilinks:** EN — [[en/concepts/security|Security]], [[en/glossary#Cryptography|Cryptography]], [[en/glossary#Encryption|Encryption]]; RU — [[ru/concepts/security|Безопасность и самостоятельное хранение]], [[ru/glossary#Криптография|Криптография]], [[ru/glossary#Шифрование|Шифрование]]
**Content audit:** No gaps noted (page is a faithful synthesis of the raw distillation).
**Lint:** Ran `python3 tools/lint.py --layer both --write-report`; wiki-ru/ 0 issues; wiki-en/ has pre-existing legacy issues elsewhere.

---

## [2026-04-24] enhance | wiki-ru/topics/quantum-computing-ama.md

**Changes:** Added link-map-backed glossary links for private/public key terms; made the PQC section two sentences (no substantive change).
**Content audit:** Solid — no gaps found requiring Mode B.
**Lint:** Ran `python3 tools/lint.py --layer ru --write-report`; 0 issues.

---

## [2026-08-01] ingest | entropy, seed-phrase, passphrase, hardware-wallets (RU only)

**Context:** Post-incident cluster for the COLDCARD RNG story. The gap audit found ~9000 words of unused `raw/` material (`hwws.md`, `passphrase.md`, `seed.md`, `seed-security.md`) and zero RU coverage of "where does a key come from".

**Layers:** RU only — deliberate. EN counterparts deferred to a separate Mode A pass and recorded in `docs/lint-report.md` under Suggested follow-ups per the gap-handling rule.

**Raw sources used (no external fetching, no new raw/ files):**
- raw/Theory/protocol/bitcoins-eternal-struggle.md — url: vechnaja-borba
- raw/Theory/security/passphrase.md — url: passphrase
- raw/Theory/security/seed.md — url: seed
- raw/Theory/security/seed-security.md — url: seed-security
- raw/Theory/security/hwws.md — url: hwws
- raw/Theory/security/what-is-multisig.md — url: multisig
- raw/Practice/hodl/coldcard.md — url: coldcard
- raw/Practice/hodl/seedsigner.md — url: seedsigner
- raw/Books/izobretaem-bitkoin/glava-3.md, glava-7.md

**Created:**
- wiki-ru/concepts/entropy.md — entropy as a measure, bits and 2^N, why a key cannot be guessed, "a hash does not create entropy", device RNG vs user-supplied entropy, Diceware, cost-of-brute-force method
- wiki-ru/concepts/seed-phrase.md — BIP-32/BIP-39 origin, 2048-word list, seed-to-address chain, 12 vs 24, checksum, compatibility, XFP, storage models, BIP-85, SSSS
- wiki-ru/concepts/passphrase.md — three generation methods, Diceware 6^5/6^4, $-denominated attack cost, Moore's law, trade-offs, passphrase vs multisig
- wiki-ru/concepts/hardware-wallets.md — threat model: RNG, secure element, open source, vendor survival, supply chain, duress mechanisms, air gap, wireless, Bitcoin-only firmware, 8-step checklist

**Updated (Mode B):**
- wiki-ru/concepts/multisig.md — new section "Чего мультиподпись не защищает": 1-of-n / n-of-n quorum limits, independence of key failures (geographic + provenance), wallet configuration as part of the backup, device/seed co-location, complexity as a threat. `sources:` extended with seed-security, seed, hwws.
- wiki-ru/glossary.md — added Генератор случайных чисел (ГСЧ), Контрольная сумма (Checksum), Парольная фраза (Passphrase), Энтропия, BIP-32, BIP-39, SHA-256. Extended Атака перебором with the "nominal vs actual entropy" caveat. Merged the duplicate `### Узел (Нода)` into `### Нода (Узел)` (SPV detail preserved; the removed anchor had no inbound links) and removed the duplicate `### UTXO` under `## U` (the `## У` entry `### UTXO (Unspent Transaction Output)` is the one actually linked).
- wiki-ru/index.md — 4 new rows in the Concepts table; multisig description updated.

**Content audit — gaps recorded on-page under «Пробелы» (not written, not invented):**
- TRNG vs PRNG/CSPRNG: absent from all `raw/` material. Pages state only "the generator inside a closed box cannot be verified".
- Derivation paths (BIP-44/49/84/86): the term appears in `raw/` but is nowhere explained.
- BIP-39 internals: entropy-to-word bit accounting, checksum computation, PBKDF2-HMAC-SHA512.
- Reproducible builds: zero mentions across the whole corpus.
- Device diversity in a multisig quorum: no `raw/` source states it directly. Written as a derived consequence of two grounded claims — "keys must be stored in geographically separate locations so several cannot be compromised at once" (multisig) and "a hardware manufacturer can always make a mistake that compromises your funds" (seed) — and framed as such rather than as reported fact. The July 2026 COLDCARD incident is **not** cited anywhere: `raw/` has no such source yet.

**Not done (blocked):** the incident page itself (`topics/coldcard-rng-incident`) and `practice/dice-seed`. Both require ingesting the "Сид на костях" guide into `raw/` first via docs/INGEST-SKILL.md.

**Lint:** `python3 tools/build_link_map.py`; `python3 tools/lint.py --layer ru --write-report` → wiki-ru/ 91 pages, 0 issues. Parity checked: all 4 new slugs RU_ONLY.

---

## [2026-08-01] ingest | dice-seed → raw/ + coldcard-rng-incident, dice-seed (RU)

### Part 1 — raw/ ingest (docs/INGEST-SKILL.md)

**Created:** raw/Practice/security/dice-seed.md
**Source:** local 21ideas.org content repo, content.ru/docs/Practice/security/dice-seed.md — provided by the maintainer, not fetched
**URL in raw/:** dice-seed → https://21ideas.org/dice-seed/
**Title:** "Создаём ключ, не доверяя генератору" (h1: "Сид на костях: как создать ключ, не доверяя генератору")
**Classification:** Practice/security — "practical guides, operational security" per the Step 3 lookup table
**Checks:** check_duplicate.py CLEAR · derive_slug.py → dice-seed · check_series.py NO_SERIES
**Verbatim:** `diff` against source = identical. Original Hugo frontmatter preserved, matching the convention of every other raw/ file (pgp.md, seed.md, coldcard.md).
**Inventory verified:** 22 headings · 2 tables · 4 blockquotes · 6 code blocks · pre-heading content present · 3637 words — all present in file.

### Part 2 — wiki ingest (Mode A, RU only)

**Created:**
- wiki-ru/topics/coldcard-rng-incident.md — what happened (594.48 BTC, 1324 UTXO, three-block window), the `#ifndef` root cause and why review missed it, entropy loss table (Coinkite ~40/~72 bits vs Block's 2^40.7 / <2^73.3 upper bounds), affected/fixed firmware versions, why a firmware update does not fix an existing seed, the invisible-failure lesson, what actually saved people (Add Dice Rolls; multisig only half-true), five threat-model conclusions
- wiki-ru/practice/dice-seed.md — the procedure: 2.585 bits per roll, 50/99 thresholds, rolls → SHA-256 → BIP-39, offline environment, the iancoleman `Dice` mode trap, the red-warning explanation (1.67 vs 3 vs 2.585 bits/roll), three cross-checks, transfer + XFP verification, cleanup, alternatives (coin, on-device dice, hybrid, multisig), who should skip this, what never to do

**Updated (Mode B) — this source closes previously logged gaps:**
- concepts/entropy.md — TRNG vs software-fallback distinction now grounded (was an open gap); new subsection "Сколько бросков нужно" with the 2.585-bit figure and 50/99 table; «Пробелы» narrowed to reproducible builds and TRNG internals
- concepts/seed-phrase.md — new section "Сколько бит в сид-фразе" with the exact 128+4 / 256+8 accounting (was an open gap); checksum section rewritten to state that the last word carries it; «Пробелы» narrowed — `m/84'/0'/0'/0/0` is now at least identified as the native-SegWit default, path anatomy still missing
- concepts/multisig.md — the device-diversity claim was written on 2026-08-01 as a *derived consequence* because no raw/ source stated it; it is now grounded directly by the Block engineers' quote from this article and rewritten as reported fact with the quote inline
- concepts/hardware-wallets.md — RNG section and "Само существование производителя" now cite the incident as a concrete precedent alongside the Ledger 2023 case
- glossary.md — Генератор случайных чисел entry extended with the TRNG/software distinction
- index.md — rows added to Practice and Topics tables

**Content audit — remaining gaps (recorded on-page and in lint-report.md):**
- Derivation paths: `m/84'/0'/0'/0/0` appears but path anatomy and BIP-44/49/84/86 roles remain unexplained anywhere in raw/. Now the highest-value remaining gap.
- BIP-39 internals: checksum computation, PBKDF2-HMAC-SHA512 mnemonic-to-seed.
- Reproducible builds: still zero mentions in raw/.
- TRNG internals: covered at the level of failure consequences, not construction.

**External URLs:** the article body links to CoinDesk, blog.coinkite.com, engineering.block.xyz and others. None were fetched, and none were carried into `sources:` or body citations — only the canonical https://21ideas.org/dice-seed/ is reader-facing, per CLAUDE.md. Organizations (Coinkite, Block, AnchorWatch, LLFOURN) are named in prose without links.

**Layers:** RU only. EN counterparts for all six new slugs flagged in docs/lint-report.md → Suggested follow-ups.

**Lint:** `python3 tools/build_link_map.py`; `python3 tools/lint.py --layer ru --write-report` → wiki-ru/ 93 pages, 0 issues. Parity: both new slugs RU_ONLY.

---

## [2026-08-01] ingest | Mastering Bitcoin ch05 + BIP-44/49/84/86 → raw/ + hd-wallets (RU)

### Part 1 — raw/ ingest (docs/INGEST-SKILL.md)

**Created:**
- raw/Books/mastering-bitcoin/chapter-5-wallets.md — url: github.com/bitcoinbook/bitcoinbook/blob/develop/ch05_wallets.adoc — CC BY-SA 4.0 — 10,613 words
- raw/Theory/protocol/bip-44.md — url: github.com/bitcoin/bips/blob/master/bip-0044.mediawiki — license not stated in document
- raw/Theory/protocol/bip-49.md — bip-0049.mediawiki — Public domain
- raw/Theory/protocol/bip-84.md — bip-0084.mediawiki — CC0-1.0
- raw/Theory/protocol/bip-86.md — bip-0086.mediawiki — BSD-2-Clause

**Source acquisition:** the maintainer ran `curl` themselves into the session scratchpad and supplied the paths. Per INGEST-SKILL rule 7 and the CLAUDE.md no-fetch rule, the agent did not retrieve any URL.

**Classification:** book chapter → `Books/<book-name>/` with the `chapter-N-<name>.md` exception; BIP specifications → `Theory/protocol/` per the Quick-reference table.

**Format handling — deviation from the usual raw/ shape, recorded deliberately.** These are the first non-Markdown and first English sources in `raw/`. Conversion was done with throwaway scripts in the scratchpad (`clean_adoc.py`, `clean_bip.py`) rather than by hand, so prose stays character-identical. Transformations applied:
- AsciiDoc: removed O'Reilly index macros `((("...")))` (invisible build tooling, treated as chrome), `[[anchors]]`, `[role=...]` hints and `//` editorial comments; normalized `=`-headings to `#`; converted `----` literal blocks to fenced code; converted the `++++` HTML passthrough blocks (9 tables, several `<p>`, one `<ol start="7">`) to Markdown, preserving every cell; rendered the MathML equation as `K + (123 × G) == (k + 123) × G`; replaced `image::` with `[image: alt]`.
- MediaWiki: `==X==` → `## X`, `<pre>` → fenced code, `{| … |}` tables → Markdown tables, `<code>/<tt>` → backticks.
- **`[[link|text]]` was flattened to plain text or Markdown links in all five files.** This is not cosmetic: `raw/` sits inside the Obsidian vault, where `[[...]]` would render as broken wikilinks. Verified: 0 occurrences of `[[` remain in the ingested files.
- The BIP preamble blocks were re-spliced verbatim from the originals after an early pass stripped author `<email>` addresses along with HTML tags.

### Part 2 — wiki ingest (Mode A, RU only)

**Created:** wiki-ru/concepts/hd-wallets.md — why HD wallets exist (per-key backup, ~32 bytes each), root seed → HMAC-SHA512 → master key + chain code, the CKD function and the 512-bit split, extended keys (xprv/xpub), public child key derivation and the key-tweak arithmetic, hardened derivation and the leaked-chain-code attack it prevents, index ranges 0…2^31−1 vs 2^31…2^32−1, path notation (`m` vs `M`, right-to-left ancestry), the five BIP-44 levels one by one, the `purpose'` table 44/49/84/86, extended-key prefixes with version bytes, why a wallet looks "empty", account discovery and the gap limit of 20, implicit vs explicit paths and descriptors, what a seed phrase cannot restore, and the entropy-sufficiency argument (128-bit security strength).

**Judgment call recorded:** the `purpose'` table lists **mainnet** paths (`m/49'/0'/0'` etc.), composed from BIP-49/84/86 (`purpose'` only) plus BIP-44 (`coin_type'` = `0'` for Bitcoin). Mastering Bitcoin's implicit-paths table shows `m/49'/1'/0'` for BIP-49 — a testnet path, matching that BIP's testnet-only test vectors. The discrepancy is called out in the page body rather than silently smoothed over.

**Updated (Mode B) — these sources closed previously logged gaps:**
- concepts/seed-phrase.md — replaced the two-row bit table with the full BIP-39 table (128/160/192/224/256); added the 11-bit arithmetic and the note that 12/24 are not the only valid lengths; added a new section "Как мнемоника превращается в сид" with all nine BIP-39 steps, the `"mnemonic"` salt, 2048 rounds of HMAC-SHA512, and why key-stretching helps only partially; «Пробелы» narrowed to wordlist design and SeedQR
- concepts/passphrase.md — «Пробелы» rewritten: the PBKDF2-salt mechanic is now covered and cross-linked; open question narrowed to how BIP-39 alternatives authenticate the passphrase
- concepts/address-types.md — new section "Тип адреса и путь деривации" with the purpose ↔ prefix table and the deliberate-incompatibility rationale
- concepts/bip.md — was the thinnest page in the layer (264 words, entirely governance). Added "Стандарты кошельков" separating compatibility BIPs from consensus BIPs, with a table of BIP-32/39/43/44/49/84/86/174/380-389
- glossary.md — added Дескриптор выходного скрипта, Путь деривации, Расширенный ключ (xpub/xprv); expanded Детерминированный кошелёк with the tree structure and the "seed alone is not enough" caveat
- index.md — hd-wallets added to the Concepts table

**Content audit — remaining gaps (on-page and in lint-report.md):** reproducible builds; how the master fingerprint (XFP) is computed; normative address encoding (BIP-141/173/341); TRNG internals; BIP-39 wordlist design.

**Licensing note for the maintainer:** Mastering Bitcoin is CC BY-SA 4.0, so Russian text synthesized from it inherits share-alike. Attribution is in `sources:` and in the Sources section of every derived page. The four BIPs are permissive (PD / CC0 / BSD-2) except BIP-44, which states no license in the document itself.

**Layers:** RU only. EN counterpart for `concepts/hd-wallets` flagged in docs/lint-report.md alongside the other six RU-only slugs.

**Lint:** `python3 tools/build_link_map.py`; `python3 tools/lint.py --layer ru --write-report` → wiki-ru/ 94 pages, 0 issues. Parity: `concepts/hd-wallets` RU_ONLY.

---

## [2026-08-02] ingest | BIP-32/39/43/174 + Bitcoin Core build docs → raw/ + verifying-software (RU)

### Part 1 — raw/ ingest (docs/INGEST-SKILL.md)

**Created:**
- raw/Theory/protocol/bip-32.md — Hierarchical Deterministic Wallets (Pieter Wuille) — BSD-2-Clause — 3,460 words
- raw/Theory/protocol/bip-39.md — Mnemonic code for generating deterministic keys — MIT — 1,112 words
- raw/Theory/protocol/bip-43.md — Purpose Field for Deterministic Wallets — no license stated — 395 words
- raw/Theory/protocol/bip-174.md — Partially Signed Bitcoin Transaction Format — BSD-2-Clause — 6,049 words
- raw/Practice/security/reproducible-builds-guix.md — contrib/guix/README.md from bitcoin/bitcoin — MIT
- raw/Practice/security/bitcoin-core-release-process.md — doc/release-process.md from bitcoin/bitcoin — MIT

**Source acquisition:** maintainer ran `curl` (all six returned 200) into the session scratchpad and supplied the paths. Agent retrieved no URL, per INGEST-SKILL rule 7 and the CLAUDE.md no-fetch rule.

**Classification:** BIP specifications → `Theory/protocol/` per the Quick-reference table. The two Bitcoin Core documents → `Practice/security/` (operational security / verification); neither is a perfect fit for the lookup table, and this was a judgment call.

**Format handling:** BIPs converted with the same `clean_bip.py` used on 2026-08-01 (mediawiki headings, `<pre>` → fenced code, `{|` tables → Markdown, `[[link|text]]` flattened so the Obsidian vault does not render broken wikilinks — verified 0 occurrences of `[[`). Preamble blocks re-spliced verbatim to preserve author email addresses. The two Bitcoin Core files are already Markdown and were copied **verbatim** with only frontmatter prepended.

**check_series.py:** reports `SERIES_DETECTED` for `raw/Theory/protocol/bip-32.md` — base `bip`, parts 32/39/43/44/49/84/86/174, and suggests a hub file. **Recorded as a false positive:** BIP numbers are identifiers, not sequence positions, and the "missing parts 33…173" list is meaningless. No `series:`/`part:` frontmatter added. Reported here per the skill's instruction to report and not branch.

### Part 2 — wiki ingest (Mode A, RU only)

**Created:** wiki-ru/practice/verifying-software.md — the three questions verification answers (integrity / authorship / correspondence to source) and one tool each; PGP vs GPG terminology; why the signature covers `SHA256SUMS` rather than the binary and why both verification steps are mandatory; console procedure (`gpg --recv-keys`, `gpg --verify`, `sha256sum` / `shasum -a 256`); the caveat that a valid signature proves only which key signed, not whose key it is, plus Web of Trust and `gpg --edit-key trust`; reproducible builds — bit-for-bit determinism, `SOURCE_DATE_EPOCH`, the `guix.sigs` attestation repo, `guix-attest` / `guix-verify`, publication only after six or more builders match, noncodesigned vs all SHA256SUMS; what this buys the reader (a quorum, not a single signature); the substitutes trade-off; a five-step checklist.

**Updated (Mode B) — these sources closed previously logged gaps:**
- concepts/hd-wallets.md — new section "Отпечаток ключа (XFP)": HASH160 of the serialized public key, first 32 bits = fingerprint, the spec's own warning that collisions are possible and software must handle them, plus the 78-byte serialization layout and the 111-character Base58 result. Master key generation now cites the `"Bitcoin seed"` HMAC key and the 128–512 bit range. Hardened derivation now quotes BIP-32's explicit non-property (parent xpub + non-hardened child private key ⇒ parent extended private key). BIP-43's motivation added, plus the historical note that `m/0'/*` was taken by BIP-32 itself. Sources extended with BIP-32 and BIP-43. **The XFP gap logged on 2026-08-01 is now closed.**
- concepts/seed-phrase.md — wordlist section rewritten from the spec: the three design criteria, UTF-8 NFKD, and the standard's own strong discouragement of non-English wordlists. Added "Признанные недостатки" from the Shortcomings section (seed depends on wordlist, one-way conversion, short checksum missing ~1-in-256 errors, no versioning) and the spec's framing of plausible deniability. Sources extended with BIP-39.
- concepts/hardware-wallets.md — verification checklist item now links to the new page; «Пробелы» narrowed to TRNG internals and firmware reproducibility
- concepts/entropy.md — «Пробелы» narrowed; reproducible builds now cross-linked rather than listed as missing
- glossary.md — added Отпечаток кошелька (XFP / Master Fingerprint) and PSBT. **The PSBT anchor gap — the term was used in two RU pages with no glossary entry, while the EN glossary had one — is now closed.**
- index.md — verifying-software added to the Practice table

**Content audit — remaining gaps (on-page and in lint-report.md):** address encoding (BIP-141/173/350/341); secp256k1 arithmetic; TRNG internals; BIP-39 wordlist provenance; firmware reproducibility for hardware wallets; `contrib/verify-binaries`.

**Layers:** RU only. EN counterpart for `practice/verifying-software` flagged in docs/lint-report.md alongside the other seven RU-only slugs.

**Lint:** `python3 tools/build_link_map.py`; `python3 tools/lint.py --layer ru --write-report` → wiki-ru/ 95 pages, 0 issues.

---

## [2026-08-02] fix | escape currency `$` that KaTeX was parsing as math

**Found by:** local Quartz preview (`node ./quartz/bootstrap-cli.mjs build --serve`), not by `tools/lint.py`.

**Problem:** Quartz enables remark-math. Two unescaped `$` on the same line open and close an inline math span, so text between them was swallowed into KaTeX and rendered garbled. Visible example on `wiki-ru/concepts/passphrase.md`: "те же $77 миллионов превращаются в $750 000" rendered as "те же 77миллионо…". The build also emitted dozens of `unicodeTextInMathMode` warnings for Cyrillic characters.

**Fixed:** escaped `$` before a digit as `\$` outside code fences.
- wiki-ru: passphrase.md (5), entropy.md (2), history/timeline.md (2), practice/storage.md (2) — the last two pre-existing
- wiki-en: glossary.md (2), series/silk-road.md (3), concepts/security.md (1), history/timeline.md (1), practice/storage.md (2), practice/running-a-node.md (2), topics/bitcoin-dissidents.md (3) — all pre-existing

**Verified:** rebuilt; the paragraph renders correctly and `katex-html` no longer appears on the page. Build: 175 files parsed, 234 emitted, no broken-link warnings.

**Follow-up worth considering:** `tools/lint.py` cannot catch this — it is a rendering-layer issue, not a wikilink or frontmatter issue. A check for an even number of unescaped `$` per line (outside fences) would be cheap to add.

---

## [2026-08-02] tooling | add unescaped-`$` check to tools/lint.py

**Why:** the KaTeX bug fixed earlier today was found by the local Quartz preview, not by lint. Adding a mechanical check so it cannot recur.

**Design note — deliberately broader than "unpaired `$`".** The obvious rule (flag an odd number of `$` per line) would **not** have caught the bug that motivated it: `те же $77 миллионов превращаются в $750 000` has exactly two dollar signs — an even, "paired" count — and that pair is precisely what opened and closed the math span. The check therefore flags **any** unescaped `$` outside code, since this vault contains no legitimate LaTeX. If real math is ever added, this check needs revisiting.

**Implementation:**
- `unescaped_dollars(body)` — skips fenced blocks and inline code spans (`INLINE_CODE_RE`), matches `(?<!\\)\$`, returns (line, count, snippet) per offending line.
- Reported line numbers are offset back to file coordinates, since `split_frontmatter()` returns only the body slice. Verified against `sed -n '75p'`.
- New result key `unescaped_dollar`; new column in the report Summary table; new row in Detail; new line in stdout output. Counts toward `--strict` (exit 1) via the existing `count_issues()`.

**Tested:**
1. Clean tree → `wiki-ru` 0 rows, `wiki-en` 0 rows for this check.
2. Regression: reintroduced the bug in `wiki-ru/concepts/passphrase.md` → caught, 1 row at the correct line 75, `--strict` exits 1.
3. Rolled back → clean again.

**Docs updated:** `tools/lint.py` module docstring now lists all checks; `CLAUDE.md` → Lint section adds the check to the script's list and to the mechanical auto-fix checklist with the reason (Quartz enables remark-math).

**Baseline note:** a `--layer both` run shows 23 pre-existing flagged rows in `wiki-en/` (bad links, broken targets, `raw/` in body, body `---`/`#`). Unrelated to this change — that layer has not had an enhance pass.

---

## [2026-08-02] tooling | add .claude/skills/preview — local Quartz build and render checks

**Why:** the KaTeX/`$` defect was invisible in source and invisible to `tools/lint.py`; only a real Quartz build surfaced it. Capturing the build procedure and the render-level checks so future sessions do not have to rediscover the pipeline.

**Added:**
- `.claude/skills/preview/SKILL.md` — how the production pipeline works (push → repository_dispatch → `cp -r wiki-ru/. content/ru/` → build), what to check after a build, the `$`/remark-math trap, and the gotchas below
- `.claude/skills/preview/preview.sh` — `serve` | `build` | `sync` | `clean`

**Design decisions:**
- Content is assembled into a temp tree and passed with `-d`; the quartz checkout is never written to, so its `git status` stays clean.
- Calls `node ./quartz/bootstrap-cli.mjs` directly. `npx quartz` does **not** resolve the local checkout (quartz *is* the package, not a dependency) — npm silently downloads the published package into the npx cache and runs that instead.
- `QUARTZ_DIR` is honoured or fails; it is never silently fallen back from. An early version fell through to auto-discovery when the override was wrong, which hid the mistake.
- Auto-discovery order: `../quartz`, `../21ideas-quartz`, `~/code/21ideas/quartz`.

**Documented gotchas (each hit during this session):**
- Do not pipe a backgrounded `--serve` through `tail`/`head` — they buffer until the pipeline ends, so the log looks empty while the server is actually fine. Poll the port instead.
- The server watches the preview tree, not `wiki-ru/` — re-run `sync` after edits.
- Never build into `quartz/content/`.

**Tested:** build; serve (port opens, `/`, `/ru/concepts/hd-wallets`, `/ru/practice/verifying-software` all 200, `katex-html` count 0); sync round-trip; clean; invalid `QUARTZ_DIR` → exit 1 with a clear message; explicit valid `QUARTZ_DIR`; auto-discovery; invalid mode → usage, exit 2; `bash -n` clean.

**CLAUDE.md updated:** skill added to the Directory Map, plus a "Rendering checks" note in the Lint section pointing at it and stating that `lint.py` validates structure, not output.

---

## [2026-08-02] remove | wiki-ru/practice/dice-seed
**Layers:** RU
**Removed:** `wiki-ru/practice/dice-seed.md` — the page was a step-by-step how-to guide, not encyclopedic wiki material. Maintainer decision.
**Reference cleanup:** dropped the `[[ru/practice/dice-seed]]` row from `wiki-ru/index.md`; removed the nav-section link from `concepts/entropy`, `concepts/hardware-wallets`, `concepts/seed-phrase`, `concepts/hd-wallets`, `practice/verifying-software`, `topics/coldcard-rng-incident`; removed the two in-prose pointers (`practice/verifying-software`, `topics/coldcard-rng-incident`).
**Kept:** `https://21ideas.org/dice-seed/` remains in `sources:` on pages that genuinely synthesized from it — `raw/Practice/security/dice-seed.md` is untouched and still the citable origin.
**Lint:** `--layer ru` clean, 94 pages, 0 flagged rows. Link map regenerated.
---

## [2026-08-02] rules | CLAUDE.md — Primary-Source Test
**Change:** `sources:` and body citations may now use a primary-source URL that appears **verbatim in the body of a raw/ file**, not only the raw/ `url:` field. Three conditions required: verbatim in raw/, primary (vendor docs about the vendor's own product, vendor advisory about its own defect, project repo/license, protocol or standards document), and load-bearing for a technical claim.
**Explicitly excluded:** news outlets and crypto press, aggregators, social media, community trackers, unaffiliated blogs, and third-party commentary about a vendor. A vendor documenting its own product is primary; a vendor commenting on a competitor is not.
**Also added:** when a raw/ file is older than the facts it reports, do not restate its volatile figures as current — prefer mechanism, affected versions and vendor documentation over headline numbers.
**No-fetch rule unchanged:** a URL is citable because it appears in `raw/`, never because it was read.
---

## [2026-08-02] enhance | wiki-ru/concepts/hardware-wallets.md
Changes:
- **RNG section reframed.** Replaced the "DIY entropy exists on some models" framing with the operative axis: is there any randomness source outside the manufacturer's silicon, and can the result be reproduced independently. Three groups described generically (all-internal / user entropy addable or substitutable / device does not generate at all), deliberately without naming vendors in the all-internal group — the page states a **class of failure**, not an accusation. Added the mix-vs-replace distinction (insuring the result vs making it reproducible). Dropped the "~40 bits on one generation" figure: it understated scope and is a volatile number per the new CLAUDE.md rule.
- **Openness section corrected.** Removed the false binary claim ("у COLDCARD открыты обе"). Replaced with three independent questions — firmware and its licence, board schematics, secure-element code — plus the point that answers do not coincide and must be checked per vendor. Added "readable is not the same as read correctly".
- **Vendor-failure taxonomy.** "Прецедентов два" replaced by four categories distinguished by what can be done afterwards: unintentional code defect, product decision changing the security model, hardware defect not fixable by update, supply-chain tampering — each with the corresponding response.
- **De-centred COLDCARD as exhibit.** Reseller-avoidance paragraph and tamper-evident packaging bullet rewritten as general mechanisms with Coinkite/COLDCARD as one illustration rather than the subject.
**New sources (Primary-Source Test):** `coldcard.com/docs/master-seed/`, `github.com/coldcard/firmware`, `github.com/Coldcard/firmware/tree/master/hardware`, `github.com/SeedSigner/seedsigner`, `github.com/Foundation-Devices`, `ledger.com/academy/security/our-custom-operating-system-bolos` — all verbatim in `raw/Theory/security/hwws.md` or `raw/Practice/security/dice-seed.md`, all vendor/project primary. No secondary source used; reseller and third-party comparison links present in raw/ were excluded.
**Deliberately not asserted** (not supported by `raw/`): COLDCARD's exact licence terms, Block's ≤32-bit estimate, dice-roll enforcement behaviour in hybrid mode.
**Lint:** `--layer ru` clean, 94 pages, 0 flagged rows.
---

## [2026-08-02] enhance | wiki-ru/concepts/hardware-wallets.md — editorial callout
Changes: added an editorial notice at the top of the page using an Obsidian/Quartz callout (`> [!warning] Позиция редакции`) — the first callout used anywhere in the vault. It states that the page was reworked after the July 2026 COLDCARD RNG incident, that the vendor's devices should not be trusted pending an independent audit report, and that COLDCARD appears on the page as an engineering example rather than a purchase recommendation — the page recommends no device at all.
**Rendering:** verified by local Quartz build (v4.5.2, `callouts: true` by default) — emits `<blockquote class="callout warning">` with its own icon, no emoji needed; the inner wikilink resolves. Callout types available: note, abstract, info, todo, tip, success, question, warning, failure, danger, bug, example, quote.
**Note:** this is an explicit maintainer editorial position, marked as such in the block's title, not a claim sourced from `raw/`.
**Lint:** `--layer ru` clean, 94 pages, 0 flagged rows.
---

## [2026-08-02] enhance | wiki-ru/concepts/hardware-wallets.md — PSBT cross-links
Changes: the air-gap section previously named "BIP-174: частично подписанные транзакции (PSBT)" as bare text. Now linked to three existing targets — `[[ru/concepts/bip]]` (BIP-174 listed in its table), the glossary entry `[[ru/glossary#PSBT (Partially Signed Bitcoin Transaction)]]`, and the workflow section `[[ru/concepts/multisig#PSBT — Partially Signed Bitcoin Transaction]]`. Added a sentence tying the air-gap and multisig uses of the same format together.
**Source added:** `https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki` (BSD-2-Clause) — the `url:` field of `raw/Theory/protocol/bip-174.md`, load-bearing for the claim that BIP-174 defines the PSBT format. Same treatment as BIP-39 on `concepts/seed-phrase`.
**Rendering verified:** local Quartz build resolves all three; anchor ids confirmed present in the emitted HTML (`psbt-partially-signed-bitcoin-transaction` in glossary, `psbt--partially-signed-bitcoin-transaction` in multisig — the double hyphen comes from the em dash in that heading).
**Still unlinked elsewhere (follow-up):** PSBT is mentioned as plain text in `concepts/multisig` (lead), `concepts/security:66` and `practice/storage`; `concepts/bip` has no per-BIP anchors, only a table.
**Lint:** `--layer ru --strict-links` clean, exit 0.
---

## [2026-08-02] enhance | wiki-ru/concepts/security.md — rebuilt as a hub
**Why:** 20 inbound links from 15 pages, listed as step 4 of the reading path in `overview.md` — the vault already treated this page as the security hub, but it was written as a standalone survey (April, `quality: reference`, never enhanced) and duplicated four pages at lower quality with no links out to any of them.
Changes:
- **Removed the `### Coldcard` section** ("один из наиболее безопасных аппаратных кошельков" + "Открытый исходный код прошивки" — the same over-simplification corrected on `hardware-wallets` earlier today). No device model is named or recommended anywhere on the page now.
- **Replaced the «Уровни безопасности» ladder.** The old table indexed protection by amount held ("Средний | Аппаратный кошелёк (Coldcard, Trezor) | Основные сбережения"), which tells the reader that one named device closes their main savings. New table is indexed by **threat**, names no vendors, and ends on the point the ladder omitted: the qualitative jump is a quorum of devices from **different** manufacturers on different codebases, not a pricier device — the last row is the only threat a single device cannot close by construction.
- **Four duplicated sections folded** into one paragraph + link each (hardware wallets → `concepts/hardware-wallets`, seed phrase → `concepts/seed-phrase`, multisig → `concepts/multisig`, passphrase → `concepts/passphrase`).
- **Added the page's own territory** from `raw/Theory/security/how-to-hold-private-keys.md`, previously unused: bearer-asset framing, the security/convenience spectrum, the two sizing questions (share of capital, access frequency), hot vs cold, and the source's own warning against over-complicating a scheme until you lock yourself out.
- **Added the missing half of seed security:** the seed has two vulnerable moments, creation and storage; the page previously covered only storage. Creation links to `concepts/entropy`.
- **Passphrase corrected:** previously sold only the decoy-wallet upside; now states that any passphrase including a typo yields a valid wallet, and that fingerprint verification is required before funding.
- **Navigation fixed:** hardware-wallets, seed-phrase, entropy, passphrase added to the closing nav — none were linked before.
- `quality` `reference` → `synthesized`; `updated`/`reviewed` → 2026-08-02.
**No editorial callout added** — after the rework the page discusses no specific device, so there is nothing to warn about.
**Verification:** `--layer ru --strict-links` clean, exit 0. Local Quartz build resolves all 18 links; all nine glossary anchor ids confirmed present in the emitted `glossary.html`.
---

## [2026-08-02] enhance | wiki-ru/concepts/security.md — link pass
Changes: linked «приватный ключ» → `[[ru/glossary#Приватный ключ]]` and «публичные ключи» → `[[ru/glossary#Публичный ключ]]` in the bearer-asset section; linked FTX to `https://21ideas.org/posts/krah-ftx/` and added it to `sources:` and the Источники list.
⚠️ **Provenance note:** `https://21ideas.org/posts/krah-ftx/` does **not** appear in any `raw/` file — it was supplied directly by the maintainer. It is therefore not covered by the Primary-Source Test in CLAUDE.md, which recognises only (a) a raw/ `url:` field and (b) a primary URL verbatim in a raw/ body. The rule exists to prevent agents fabricating URLs; a maintainer-supplied URL on the wiki's own anchor domain is not that case, but the gap should be closed — either by ingesting the article into `raw/` or by adding an explicit maintainer-supplied clause to the rule.
**Verification:** `--layer ru --strict-links` clean; rendered page resolves both glossary anchors (`приватный-ключ`, `публичный-ключ` — both ids confirmed in `glossary.html`) and the external FTX link.
---

## [2026-08-02] enhance | wiki-ru/practice/storage.md
Changes:
- **Removed the purchase instruction.** Step 2 of «С чего начать» read «При накоплении от ~\$1000 — купите **Coldcard** или соберите **SeedSigner**» — a named-vendor buy order tied to a round threshold. Replaced with an approach-based step: the threshold is personal ("how much would it hurt to lose"), and device choice routes to `concepts/hardware-wallets` rather than being made for the reader.
- **Superlatives removed.** «Самый безопасный аппаратный кошелёк» and «Рекомендован для опытных пользователей и крупных сумм» (COLDCARD) replaced with factual capability lines plus an explicit caveat pointing at the RNG incident. SeedSigner's «Оптимальный баланс» reworded; added the substantive point that it has no key generator of its own.
- **Editorial callout added** at the top, matching `concepts/hardware-wallets` — the page is purchase-adjacent and names devices.
- **Level 3 (multisig)** no longer indexed by amount alone; added that protection comes from key *independence*, and a quorum built from one manufacturer's devices does not protect against that manufacturer's defect.
- **Seed creation gap closed:** the four seed rules covered storage only; added the second vulnerable moment (creation) with links to `concepts/entropy` and `concepts/seed-phrase`.
- **Passphrase section** renamed to Russian and given the missing warning: any passphrase including a typo yields a valid wallet; verify the fingerprint before funding.
- **Common mistakes** extended with the post-incident scam vector (sites offering to "check your wallet for a vulnerability") and unverified software installs.
- Nav extended with hardware-wallets, seed-phrase, entropy, passphrase, verifying-software; `quality` → `synthesized`; dates bumped.
**Verification:** `--layer ru` clean, 0 flagged rows. Rendered page confirms the callout, the removal of «Самый безопасный»/«купите», and that the escaped `~\$500` still renders as text (not a LaTeX span).
---

## [2026-08-02] enhance | wiki-en/concepts/security.md
First substantive pass on this page since April; the EN layer has no counterparts to the new RU pages, so everything is fixed in place with no outbound links to non-existent targets.
Changes:
- **Removed «Recommended: Coldcard for advanced users; SeedSigner for DIY…; Trezor/Foundation Passport for accessibility»** — the bluntest device recommendation in the repository. Replaced with an explicit statement that the wiki does not rank devices, plus the point that "open source" is three separate questions (firmware licence, schematics, secure-element code) that rarely have the same answer.
- **«Best-in-class cold storage»** (Coldcard row of the wallet table) replaced with a factual description referring to the trust caveats.
- **Comparison table corrected:** "open firmware" → "published firmware source"; Ledger "closed source" → "closed operating system"; SeedSigner row now states it has no key generator of its own.
- **New subsection "What you are trusting"** — the page previously had no notion of the RNG trust point at all. Covers the three things taken on faith, the comparison axis (entropy outside the vendor's silicon + replay verifiability), and the July 2026 incident framed as a **class of failure** rather than a verdict on one vendor, including why a secure element is irrelevant to it.
- **Editorial callout** added at the top, mirroring the RU position.
- **Seed creation gap closed** in the Seed Phrases section (rules covered storage only).
- **Multisig:** added that independence, not key count, is what protects — a single-vendor quorum falls the way one key would.
- **Common Attacks table:** phishing row extended to cover fake "vulnerability checkers"; new row for weak key generation.
- `quality` `reference` → `synthesized`; `sources` and Sources list gain `https://21ideas.org/dice-seed/`; dates bumped.
**Verification:** `--layer en` reports **no findings for this file** (the 23 flagged rows in wiki-en/ are pre-existing issues on other unenhanced pages). Rendered page confirms the callout and the removal of both recommendation strings.
---

## [2026-08-02] enhance | wiki-ru/topics/coldcard-rng-incident.md — on-chain figures refreshed
**Why:** the page carried the day-two figures from `raw/Practice/security/dice-seed.md` (594.48 BTC, ~$38M, "примерно пятьсот адресов", 1324 UTXO in a three-block window, 562 BTC consolidated to three addresses). Those were an early partial estimate of the first wave and understated the incident by more than half.
Changes:
- **`## Что произошло` replaced by `## Ончейн-картина`,** carrying maintainer-supplied figures as of 2026-08-02: three waves, **4 585 addresses, 1 367,05 BTC** (Galaxy Research breakdown), consolidated into **eight thief hoards totalling 1 159,55 BTC**, none of them spent — itemised in a table (562.02 · 398.48 · 89.62 · 45.90 · 32.45 · 30.18 · 0.61 · 0.33).
- **Arithmetic discrepancy stated explicitly:** the eight listed balances sum to 1 159,59, four hundredths above the stated 1 159,55. That is exactly within rounding of eight two-decimal balances (8 × 0.005), and the page says so rather than leaving a reader who adds the column to suspect an error.
- **The two totals are distinguished** instead of being conflated: 1 367,05 BTC is what left victims' wallets, 1 159,55 BTC is what sits in the known hoards; no publicly reconciled balance exists between them. No explanation for the ~207 BTC gap was invented.
- **Dated-snapshot callout** (`> [!info] Данные на 2 августа 2026 года`) added above the figures, stating that estimates were revised several times during the incident and the thief's funds may move at any time — so the page does not have to be re-edited on every change and the reader can judge currency. First use of the `info` callout type in the vault.
- Dollar figures dropped entirely — they age fastest and add nothing to the argument.
- Attribution split into `## Кто разбирал` (AnchorWatch / Galaxy Research / Coinkite / Block / LLFOURN), named in prose without links, as before.
- `выводы` section: "ценой в 594 биткоина" → "ценой более чем в тысячу биткоинов". `wiki-ru/index.md` row description no longer cites 594 BTC.
**Provenance:** the on-chain figures and the Galaxy Research attribution were supplied directly by the maintainer; they are not in `raw/`, and no URL was fabricated for them — organisations are named in prose only, matching the page's existing convention. Same open gap as the FTX link (see 2026-08-02 link-pass entry): the Primary-Source Test has no clause for maintainer-supplied data.
**Verification:** `--layer ru --strict-links` clean, 0 flagged rows. Rendered page shows the info callout and all three figures; no occurrence of "594" remains anywhere in `wiki-ru/` or `wiki-en/`.
---

## [2026-08-02] enhance | wiki-ru/concepts/seed-phrase.md — «12 или 24 слова»
Changes: the section closed on "компромисс, который каждый решает сам", presenting the choice as a neutral coin flip. Replaced with the argument for why the margin matters in practice:
- word count sets the **capacity** of the encoding, not the guarantee that it is filled with real randomness (ties back to the existing rule further down the page);
- a real entropy source is almost always slightly below ideal — an unbalanced die, rounded edges, a limp throw — so a nominal 256 bits can land at, say, 230, while the phrase looks identical from outside;
- 230 bits still exceeds a flawless 12-word seed's 128 bits by a factor on the order of 10³⁰, so 24 words on imperfect dice beat 12 words on perfect ones;
- conclusion: do not economise on the effort — one-off inconvenience buys a permanent reserve.
**Honesty caveat added:** the argument holds for imperfection, not gross bias. A die that systematically lands on one face is a different problem, and phrase length does not fix it — without this the reasoning would over-promise (entropy per roll would have to halve, to ~1.29 bits, for 99 rolls to fall to 128 bits).
**Provenance:** the SeedSigner guide citation is unchanged and still carries the "24 words are more reliable but more work to back up" claim. The numerical illustration is derived arithmetic from figures already established on this page and on `concepts/entropy` (2.585 bits per fair roll, 128/256-bit levels, hashing adds no entropy) — presented as an example ("скажем, 230"), not as a measured value, so it does not imply anyone benchmarked biased dice.
**Verification:** `--layer ru --strict-links` clean; rendered page shows the new text and the superscript 10³⁰.
---
