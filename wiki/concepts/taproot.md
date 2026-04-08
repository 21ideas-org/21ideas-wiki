---
title: "Taproot"
category: concepts
tags: [bitcoin, wiki, protocol, upgrade, taproot, schnorr]
language: en
source: "Synthesized from raw/ sources + glossary"
updated: "2026-04-07"
quality: reference
sources: ["https://21ideas.org/taproot", "https://21ideas.org/glossary/"]
synthesized_date: "2026-04-07"
completeness: high
---

# Taproot

*Tags: protocol, upgrade, soft-fork, 2021, Schnorr, privacy, smart-contracts*

---

## What It Is

Taproot is a soft fork protocol upgrade activated on Bitcoin on **November 14, 2021** (block 709,632). It consists of three BIPs implemented together:

- **BIP 340** — Schnorr Signatures
- **BIP 341** — Taproot (the MAST + P2TR output type)
- **BIP 342** — Tapscript (updated scripting language)

Together they introduce new, more efficient, flexible, and private ways to send bitcoin.

Source: `raw/Theory/protocol/taproot.md`, `raw/Start/glossary.md`

---

## Schnorr Signatures (BIP 340)

Bitcoin previously used **ECDSA** (Elliptic Curve Digital Signature Algorithm) for signing transactions. Taproot adds **[[concepts/taproot|Schnorr]] signatures**, which are:

**More efficient:**
- 32-byte public keys vs. 33-byte ECDSA
- 65-byte signatures vs. 71-72-byte ECDSA
- Smaller size → lower fees

**Key aggregation ([[concepts/taproot|MuSig2]]):**
- Multiple signers can aggregate their public keys and signatures into a single key/signature that looks identical to a single-sig transaction on-chain
- 3-of-5 [[concepts/security|multisig]] looks like a simple payment → massive privacy improvement + fee reduction
- See [[concepts/security]] (multisig section)

**Linear:** Schnorr signatures are linear, enabling more efficient batch verification and protocol composition.

---

## Taproot / MAST (BIP 341)

Taproot introduces the **[[concepts/address-types|P2TR]] (Pay-to-Taproot)** output type and integrates **[[concepts/taproot|MAST]] (Merklized Abstract Syntax Trees)**.

**How P2TR works:**
1. Funds are sent to a single public key `Q`
2. `Q` is actually an aggregation of: a "key path" public key `P` + the Merkle root of many possible "script paths"
3. To spend, the sender can either:
   - Sign with key `P` (simple payment — most private path)
   - Reveal and satisfy any script in the Merkle tree (complex conditions)

**Privacy benefit:** When spending via the key path, a complex multisig, a time-locked contract, or a Lightning channel closure all look *identical* on-chain — a single signature from a single key. Chain analysis heuristics (which depend on distinguishing multisig from single-sig) break down.

**Flexibility:** Conditions (e.g., "3-of-5 OR timelock after 6 months OR 2-of-2 emergency") are encoded in the Merkle tree; only the executed condition is revealed on-chain.

---

## Tapscript (BIP 342)

An update to Bitcoin's scripting language to:
- Support Schnorr signature verification
- Support Taproot spending paths
- Enable future upgrades via new OP codes without hard forks (using `OP_SUCCESS`)

Tapscript is designed for maximum future extensibility.

---

## Practical Impacts

| Area | Before Taproot | After Taproot |
|------|----------------|---------------|
| Multisig on-chain appearance | Reveals N-of-M structure | Looks like single-sig (via MuSig) |
| Complex script spending | Reveals all script branches | Only reveals executed branch |
| Lightning channel closes | Often distinguishable | Look like normal spends |
| Multisig fees | Pay for all keys/sigs | Pay for one aggregated sig |
| Smart contract privacy | Script visible on-chain | Hidden in Merkle tree |

---

## Address Type

**P2TR addresses** start with `bc1p` and use Bech32m encoding (a slightly improved Bech32 variant). They are 62 characters long.

Taproot adoption has been growing since 2022, accelerating with hardware wallet support.

---

## Relationship to SegWit

Taproot builds on [[concepts/segwit|SegWit]]'s foundation:
- Uses SegWit's [[concepts/segwit|block weight]] system for cheaper witness data
- Required SegWit's [[concepts/segwit|malleability]] fix (same principle extended further)
- [[concepts/address-types|P2TR]] is a native SegWit v1 output type

---

## MuSig2

MuSig2 (standardized 2023+) is the Schnorr multi-party key aggregation protocol enabled by Taproot. N-of-N participants cooperatively generate a single key and signature — indistinguishable from a regular single-sig on-chain. See [[concepts/security]].

---

## Sources

- [Original article on 21ideas.org](https://21ideas.org/taproot)

---

## Related Terms

[[glossary|Glossary]] | [[concepts/segwit|SegWit]] | [[concepts/address-types|address types]] | [[concepts/security|multisig]] | [[concepts/privacy|privacy]] | [[concepts/lightning-network|Lightning Network]] | [[concepts/governance|soft fork]] | [[concepts/utxo|UTXO]]

## Related Pages

- [[concepts/segwit]] — the prerequisite upgrade
- [[concepts/address-types]] — P2TR address type
- [[concepts/security]] — multisig using Schnorr/MuSig2
- [[concepts/privacy]] — Taproot's privacy improvements
- [[concepts/lightning-network]] — Lightning channels benefit from Taproot
- [[glossary]] — Taproot, Schnorr, MuSig2 defined
