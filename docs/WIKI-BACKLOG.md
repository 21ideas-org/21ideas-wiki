# Wiki backlog

Short-lived scratch list. Promote done items to `log.md` or delete them.

---

## Backlog — new pages

### Concepts (EN/RU as needed)

- [ ] KYC
- [ ] Circular economy
- [ ] P2P
- [ ] Fees
- [ ] Кошелёк (wallet)

### Terms / glossary

- [ ] Script
- [ ] Пластичность транзакций (transaction malleability)
- [ ] Подписи Шнорра (Schnorr signatures)
- [ ] MAST-контракты
- [ ] Key path (Taproot)
- [ ] Дерево Меркла (Merkle tree)
- [ ] SHA-256
- [ ] PSBT
- [ ] Air-gap

---

## Improve existing pages

- [ ] **Proof of work** — expand with PoS contrast + tie-in to difficulty adjustment
- [ ] **Lightning tools** — add more mobile wallets

---

## Fixes / parity

- [ ] **protocol-stack** — EN strong; RU lags (bring RU up to EN)

---

## Structural tasks (from CLAUDE.md rewrite audit — 2026-04-11)

### wiki-en/index.md wikilink conversion
`wiki-en/index.md` uses absolute Markdown paths (`[Bitcoin](wiki-en/concepts/bitcoin.md)`) instead of wikilinks. Convert all entries to `[[en/...]]` style to match `wiki-ru/index.md`.

### wiki-en/ enhancement pass (entire layer)
`wiki-en/` has not been enhanced yet. Known issues across all pages:
- Missing `reviewed:` field in frontmatter
- `source:` singular instead of `sources:` (or missing entirely)
- Unquoted scalar frontmatter fields (`category: concepts` instead of `"concepts"`)
- Non-allowlist tags (e.g. `upgrade`, `schnorr`, `digital-cash`, `soft-fork`)
- `Source: raw/...` citations in body text
- `## Related Terms` sections (should be `## Related pages` with pipe-syntax links)
- Triple-bracket link syntax (`[[en/concepts/segwit]]]`) — stray `]`
- `---` horizontal rules in body
- `#` heading in page body (conflicts with Quartz frontmatter-title rendering)

---

## Coverage gaps — raw/ material with no wiki page (audit 2026-04-11)

### raw/Theory/economics/
- [ ] `comparison-of-monetary-standards.md`
- [ ] `hopf-internet-cycles.md`
- [ ] `jevons-paradox.md`
- [ ] `petrodollar-negative-effects.md`
- [ ] `structural-adjustment.md`
- [ ] `masters-and-slaves-of-money.md`
- [ ] `money-blockchains-and-social-scalability.md`
- [ ] `seven-network-effects-of-bitcoin.md` (→ `topics/network-effects.md` exists in EN; RU version missing)
- [ ] `shelling-out.md`

### raw/Theory/philosophy/
- [ ] `crypto-anarchist-manifesto.md`
- [ ] `bitcoin-universe.md`
- [ ] `dutch-tulip-bubble.md`
- [ ] `everyones-a-scammer.md`
- [ ] `fighting-fake-bitcoin.md`
- [ ] `freedom-of-value.md`
- [ ] `inalienable-property-rights.md`
- [ ] `libertaria-in-cyberspace.md`
- [ ] `most-peaceful-revolution.md`
- [ ] `not-shitcoin.md`
- [ ] `number-zero-and-bitcoin.md`
- [ ] `proof-of-life.md`
- [ ] `bitcoin-meme.md`
- [ ] `bitcoin-is-mycelium.md`
- [ ] `bitcoin-equals-freedom.md`
- [ ] `crypto-bro.md`

### raw/Theory/protocol/
- [ ] `musig2.md` (MuSig2 — only mentioned in multisig pages; no dedicated page)
- [ ] `on-ossification.md`
- [ ] `timestamps.md`
- [ ] `was-satoshi-a-greedy-miner.md`
- [ ] `rgb.md` (RGB protocol — may be out of scope; flag for human decision)
- [ ] `bitcoin-zoloto-2-0.md`
- [ ] `coercion-of-ethereums-difficulty-bomb.md`
- [ ] `proof-of-stake-is-a-scam.md`

### raw/Theory/privacy/
- [ ] `best-practices.md` (privacy best practices)
- [ ] `bip47-the-ugly-duckling.md`
- [ ] `coinjoin.md`
- [ ] `bitcoin-fungibility.md`
- [ ] `no-kyc.md`
- [ ] `freesamourai.md`
- [ ] `bitcoin-becomes-critical.md`

### raw/Theory/lightning/
- [ ] `inbound-liquidity-problem.md`
- [ ] `is-lightning-centralized.md`
- [ ] `lightning-addresses.md`
- [ ] `lightning-privacy.md`
- [ ] `lightning-wallets.md`

### raw/Practice/ (Dojo series)
- [ ] `raw/Practice/privacy/dojo/` — RoninDojo series has no wiki coverage

---

## EN/RU inconsistencies — flagged for human review (audit 2026-04-11)

- **`wiki-en/concepts/taproot.md`** — significantly behind RU version: non-allowlist tags, `raw/...` inline citations, `## Related Terms` section, `source:` singular field, triple-bracket links, `---` in body, `#` heading in body.
- **`wiki-en/index.md` vs `wiki-ru/index.md`** — EN uses absolute Markdown paths; RU uses wikilinks. Structural inconsistency.
- **`wiki-en/` frontmatter generally** — unquoted scalar fields will fail strict Quartz parsing.

---

## Research / fact-check

- [x] Whitepaper contacts (2026-04-12): corrected wording — Adam Back as **one of the few** in private pre-announcement correspondence; removed incorrect EN claim that only Hal Finney was emailed. Pages: `wiki-ru/entities/satoshi-nakamoto.md`, `wiki-ru/entities/adam-back.md`, `wiki-en/entities/satoshi-nakamoto.md`, `wiki-en/entities/adam-back.md`, `wiki-en/series/genesis-files.md`.

---

## Parking lot

Ideas without a clear next step yet:

- (none)
