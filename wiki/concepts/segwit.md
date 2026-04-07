# SegWit (Segregated Witness)

*Tags: protocol, upgrade, soft-fork, 2017, transaction-malleability, lightning*

---

## What It Is

SegWit (Segregated Witness) is a soft fork protocol upgrade activated on Bitcoin on **August 24, 2017** (block 481,824). It changed the structure of Bitcoin transactions in two key ways:

1. **Separated the witness data** (signatures/unlock scripts) from the rest of the transaction data
2. **Changed how the Transaction ID (TXID) is calculated** — the TXID now excludes witness data

Source: `raw/Theory/protocol/segwit.md` (translation of Greg Walker / learnmeabitcoin.com)

---

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

---

## Why It Was Needed

### Problem 1: Transaction Malleability

In legacy transactions, the TXID could be changed by modifying the signature (signatures can have equivalent valid forms). A third party relaying a transaction could alter the TXID before it was confirmed — causing the sender to think the transaction failed when it actually succeeded with a different ID.

**Why this mattered for Lightning:** Lightning Network's payment channel design requires knowing the TXID of the funding transaction to build the refund transaction. If the TXID could be changed, the refund transaction would become invalid, making Lightning impossible to build safely.

SegWit fixed malleability: since signatures are excluded from the TXID calculation, changing the signature doesn't change the TXID.

### Problem 2: Block Capacity

SegWit introduced a new "block weight" metric:
- Non-witness data: 4 weight units per byte
- Witness data: 1 weight unit per byte (discounted)
- Block weight limit: 4,000,000 weight units

Since witness data is cheaper, effective block capacity increased from ~1MB to ~2MB for typical transactions (more for SegWit-heavy blocks).

---

## Address Types Introduced

| Type | Prefix | Description |
|------|--------|-------------|
| P2WPKH | `bc1q` (42 chars) | Native SegWit single-sig; Bech32 encoding |
| P2WSH | `bc1q` (62 chars) | Native SegWit multisig/script; SHA-256 only |
| P2SH-P2WPKH | `3` | "Nested SegWit" — SegWit inside P2SH for backward compatibility |

**Bech32 encoding:** Unlike legacy Base58 addresses, Bech32 has no uppercase letters, includes error detection, and is more compact. Addresses starting with `bc1` are native SegWit.

---

## The Blocksize War Context

SegWit was the solution to the 2015-2017 scaling debate. Large blockers wanted a hard fork increasing block size; small blockers (and Bitcoin Core developers) proposed SegWit as a soft fork that:
- Increased capacity without a hard fork
- Fixed malleability (enabling Lightning)
- Kept full node costs manageable

The UASF (BIP148) forced SegWit activation when miners stalled. SegWit2x (SegWit + 2MB hard fork) was later cancelled. SegWit's activation was a decisive victory for small blockers. See [[history/blocksize-war]].

---

## Importance for Lightning Network

SegWit was the prerequisite for the Lightning Network. Without malleability fixed, Lightning's payment channel design couldn't be safely constructed. Lightning launched and scaled rapidly after SegWit activation in August 2017. See [[concepts/lightning-network]].

---

## Related Pages

- [[concepts/taproot]] — the next major upgrade (builds on SegWit)
- [[concepts/address-types]] — address types SegWit introduced
- [[concepts/utxo]] — SegWit changes how UTXOs are structured
- [[concepts/lightning-network]] — what SegWit enabled
- [[history/blocksize-war]] — the political context of SegWit's activation
- [[concepts/governance]] — UASF demonstrated user power
