---
title: "Bitcoin Address Types"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/en/bitcoin-address-types/"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, addresses, taproot, segwit]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## Overview

[[en/concepts/bitcoin|Bitcoin]] has evolved through several [[en/glossary#address|address]] types since 2009, each introducing improvements in privacy, fee efficiency, and functionality. The type of address determines how funds are locked and how they can be spent.

Source: [Bitcoin address types (21ideas)](https://21ideas.org/en/bitcoin-address-types/)

## Address Types at a Glance

| Type | Prefix | Encoding | Era | BTC Held (approx.) | Status |
|------|--------|----------|-----|---------------------|--------|
| P2PK | — | Raw pubkey | 2009 | ~1.7M BTC (9%) | Obsolete |
| P2PKH | `1` | Base58 | 2009 | ~8.3M BTC (43%) | Declining |
| P2MS | — | Raw multisig | 2012 | ~43 BTC (0.0002%) | Obsolete |
| P2SH | `3` | Base58 | 2012 | ~4.6M BTC (24%) | Declining |
| P2WPKH | `bc1q` (42) | Bech32 | 2017 | ~3.8M BTC (20%) | Growing |
| P2WSH | `bc1q` (62) | Bech32 | 2017 | ~0.8M BTC (4%) | Growing |
| Nested SegWit | `3` | Base58 | 2017 | (within P2SH) | Transitional |
| P2TR | `bc1p` | Bech32m | 2021 | Growing | Growing |

## P2PK (Pay-to-Public-Key)

The original method [[en/entities/satoshi-nakamoto|Satoshi]] used. Bitcoin is sent directly to a [[en/glossary#public-key|public key]] (not an address). The first Bitcoin [[en/glossary#transaction|transaction]] ever (Satoshi → [[en/entities/hal-finney|Hal Finney]], block 170) used P2PK.

**Problems:** Exposes the full public key; more expensive; less private. No checksum. Now obsolete.

**Interesting:** ~1.7M BTC (~9% of supply) still held in P2PK outputs — mostly Satoshi-era coins.

## P2PKH (Pay-to-Public-Key-Hash) — Legacy

The standard since week 2 of Bitcoin's existence. Instead of paying to a public key, you pay to the *hash* of a public key (the "address"). Addresses start with `1`.

**Improvements over P2PK:** Hashing the key (SHA-256 then RIPEMD-160) adds privacy (key not revealed until spending), reduces data size, adds checksum.

**Status:** Still holds 43% of all mined bitcoin — the most of any type. Declining as users move to SegWit.

## P2MS (Pay-to-Multisig)

An early raw multisig type ([[en/concepts/bip|BIP11]], 2012). Like P2PK, it exposed public keys and was limited to 3-key maximum. Quickly replaced by P2SH for multisig. Essentially obsolete.

## P2SH (Pay-to-Script-Hash) — `3` addresses

Introduced April 2012 ([[en/concepts/bip|BIP16]]). Instead of paying to a key or raw script, you pay to the *hash of a redeem script*. The script's details are revealed only when spending.

**Why important:** Enabled arbitrary spending conditions ([[en/concepts/multisig|multisig]], timelocks, etc.) while keeping the script hidden until spend time. Became the standard for multisig wallets.

**Addresses start with `3`** (BIP13 encoding). Exactly 34 characters. Base58 encoded.

**Also used for Nested SegWit:** When SegWit launched in 2017, many wallets wrapped SegWit outputs inside P2SH for backward compatibility with software that didn't yet recognize `bc1q` addresses.

## P2WPKH (Pay-to-Witness-Public-Key-Hash) — Native SegWit

First native [[en/concepts/segwit|SegWit]] address type, introduced with the SegWit [[en/concepts/forks|soft fork]] (August 2017). The SegWit equivalent of P2PKH.

**Advantages over P2PKH:**
- Witness data (signatures) gets a 75% discount in block weight → lower [[en/glossary#fee|fees]]
- Fixes transaction malleability
- Better for [[en/concepts/lightning-network|Lightning Network]]

**Addresses start with `bc1q`**, 42 characters, Bech32 encoded (no uppercase letters, better error detection).

## P2WSH (Pay-to-Witness-Script-Hash) — Native SegWit Multisig

The SegWit equivalent of P2SH. Used for multisig and complex scripts in native SegWit.

**Differences from P2WPKH:** Uses SHA-256 only (not RIPEMD-160) → longer address (62 chars). Provides additional protection against theoretical birthday attacks on multisig schemes.

**Also starts with `bc1q`** but is 62 characters long.

## Nested SegWit (P2SH-P2WPKH, P2SH-P2WSH)

Not a separate address type — SegWit outputs wrapped inside P2SH for backward compatibility. Uses the `3` prefix. Technically P2SH, but the redeem script contains a SegWit commitment.

**Purpose:** Allowed SegWit fee savings for users whose counterparties didn't yet support native `bc1q` addresses. Now largely superseded by native SegWit and Taproot.

## P2TR (Pay-to-Taproot) — `bc1p` addresses

Introduced with [[en/concepts/taproot|Taproot]] (November 2021, BIP341). The most advanced address type.

**Key features:**
- Schnorr signatures instead of ECDSA
- Key path spending: simple single-signature spend, cheapest and most private
- Script path spending: can satisfy any condition in a [[en/concepts/taproot|MAST]] (Merkle tree of scripts)
- **All P2TR outputs look identical on-chain** — whether a single-sig, a 5-of-7 multisig, a Lightning channel, or a complex contract; this dramatically improves [[en/concepts/privacy|privacy]]

**Addresses start with `bc1p`**, 62 characters, Bech32m encoded.

## Which Address Type to Use?

**For most users today:**
- **Receiving** → P2TR (`bc1p`) if your wallet supports it; otherwise P2WPKH (`bc1q`)
- **Multisig** → P2WSH (`bc1q...`) or P2TR with [[en/concepts/taproot|MuSig2]]
- **Avoid** → P2PKH (`1`) and P2SH (`3`) for new wallets (higher fees, less private)

**Hardware wallets:** [[en/practice/storage|Coldcard]], SeedSigner, Foundation Passport all support P2TR as of 2023+.

## Sources

- [Bitcoin address types (21ideas)](https://21ideas.org/en/bitcoin-address-types/)

## Related pages

- [[en/concepts/segwit|SegWit — P2WPKH and P2WSH address types]]
- [[en/concepts/taproot|Taproot — P2TR, Schnorr, and MuSig2]]
- [[en/concepts/utxo|UTXO — how addresses lock outputs]]
- [[en/concepts/privacy|Privacy — how address types affect on-chain privacy]]
- [[en/concepts/multisig|Multisig — P2SH, P2WSH, and Taproot patterns]]
- [[en/concepts/lightning-network|Lightning Network — uses P2WPKH and P2TR channels]]
- [[en/practice/storage|Hardware wallets and cold storage — address type support by device]]
