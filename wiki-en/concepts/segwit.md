---
title: "SegWit (Segregated Witness)"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/segwit", "https://21ideas.org/vojna-za-razmer-bloka/glava-5/", "https://21ideas.org/vojna-za-razmer-bloka/glava-20/"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, segwit]
updated: "2026-04-07"
reviewed: "2026-04-14"
---

## What It Is

SegWit (Segregated Witness) is a [[en/concepts/forks|soft fork]] protocol upgrade activated on Bitcoin on **August 24, 2017** (block 481,824). It changed the structure of Bitcoin transactions in two key ways:

1. **Separated the witness data** (signatures/unlock scripts) from the rest of the transaction data
2. **Changed how the TXID is calculated** — the TXID now excludes witness data

Source: [SegWit](https://21ideas.org/segwit)

## The Core Change

**Legacy (pre-SegWit) transaction structure:**
```
[input UTXOs + unlock scripts] → [outputs] → TXID hash covers ALL data
```

**SegWit transaction structure:**
```
[input UTXOs] → [outputs] → TXID hash covers only inputs+outputs
[witness data (signatures)] → stored separately
```

The TXID now reflects *what moves* (inputs/outputs) but not *how it's validated* (signatures). This is the "segregated witness" — witness data is separated from the TXID calculation.

## Why It Was Needed

### Problem 1: Transaction Malleability

In legacy transactions, the TXID could be changed by modifying the signature (signatures can have equivalent valid forms). A third party relaying a transaction could alter the TXID before it was confirmed — causing the sender to think the transaction failed when it actually succeeded with a different ID.

**Why this mattered for [[en/concepts/lightning-network|Lightning Network]]:** Lightning's [[en/concepts/lightning-network|payment channel]] design requires knowing the TXID of the funding transaction to build the refund transaction. If the TXID could be changed, the refund transaction would become invalid, making Lightning impossible to build safely.

SegWit fixed malleability: since signatures are excluded from the TXID calculation, changing the signature doesn't change the TXID.

### Problem 2: Block Capacity

SegWit introduced a new "block weight" metric:
- Non-witness data: 4 weight units per byte
- Witness data: 1 weight unit per byte (discounted)
- Block weight limit: 4,000,000 weight units

Since witness data is cheaper, effective block capacity increased from ~1MB to ~2MB for typical transactions (more for SegWit-heavy blocks).

## Address Types Introduced

| Type | Prefix | Description |
|------|--------|-------------|
| P2WPKH | `bc1q` (42 chars) | Native SegWit single-sig; Bech32 encoding |
| P2WSH | `bc1q` (62 chars) | Native SegWit multisig/script; SHA-256 only |
| P2SH-P2WPKH | `3` | "Nested SegWit" — SegWit inside P2SH for backward compatibility |

**Bech32 encoding:** Unlike legacy Base58 addresses, Bech32 has no uppercase letters, includes error detection, and is more compact. Addresses starting with `bc1` are native SegWit. See [[en/concepts/address-types|address types]] for the full comparison.

## The Blocksize War Context

SegWit was the solution to the 2015–2017 scaling debate. Large blockers wanted a [[en/concepts/forks|hard fork]] increasing block size; small blockers (and [[en/concepts/bitcoin-core|Bitcoin Core]] developers) proposed SegWit as a [[en/concepts/forks|soft fork]] that:
- Increased capacity without a hard fork
- Fixed malleability (enabling Lightning)
- Kept full node costs manageable

The UASF (BIP148) forced SegWit activation when miners stalled. SegWit2x (SegWit + 2MB hard fork) was later cancelled. SegWit's activation was a decisive victory for small blockers. See [[en/history/blocksize-war]].

Source: [The Blocksize War — Chapter 5](https://21ideas.org/vojna-za-razmer-bloka/glava-5/), [Chapter 20](https://21ideas.org/vojna-za-razmer-bloka/glava-20/)

## Importance for Lightning Network

SegWit was the prerequisite for the [[en/concepts/lightning-network|Lightning Network]]. Without malleability fixed, Lightning's payment channel design couldn't be safely constructed. Lightning launched and scaled rapidly after SegWit activation in August 2017.

## Sources

- [SegWit](https://21ideas.org/segwit)
- [The Blocksize War — Chapter 5 (SegWit)](https://21ideas.org/vojna-za-razmer-bloka/glava-5/)
- [The Blocksize War — Chapter 20 (SegWit2x)](https://21ideas.org/vojna-za-razmer-bloka/glava-20/)

## Related pages

- [[en/concepts/taproot|Taproot — the next major upgrade, builds on SegWit]]
- [[en/concepts/address-types|Address Types — the bc1 addresses SegWit introduced]]
- [[en/concepts/utxo|UTXO — how SegWit changes UTXO structure]]
- [[en/concepts/lightning-network|Lightning Network — what SegWit made possible]]
- [[en/concepts/forks|Forks — SegWit as a soft fork; UASF user activation]]
- [[en/concepts/bitcoin-core|Bitcoin Core — the implementation that shipped SegWit]]
- [[en/history/blocksize-war|Blocksize War — the political battle over SegWit's activation]]
- [[en/books/blocksize-war|The Blocksize War — book covering the 2015–2017 scaling war]]
