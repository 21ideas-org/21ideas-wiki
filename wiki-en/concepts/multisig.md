---
title: "Multisig (Multisignature)"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/multisig/", "https://21ideas.org/glossary/"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, security, multisig, taproot]
updated: "2026-04-07"
reviewed: "2026-04-14"
---

Multisig (multisignature) is a Bitcoin security architecture in which spending a [[en/concepts/utxo|UTXO]] requires multiple cryptographic signatures rather than one. The threshold is expressed as M-of-N: M signatures required out of N total keys. This eliminates the single point of failure inherent in standard single-key custody.

## The Problem: Single-Key as Single Point of Failure

Standard Bitcoin ownership is single-signature: one private key controls one or more addresses. This means:

- **Loss** of the key = loss of funds permanently
- **Theft** of the key = loss of funds permanently
- **Coercion** (wrench attack) = loss of funds instantly

A single seed phrase stored in one location gives an attacker exactly one target to acquire. Self-custody is excellent, but single-sig self-custody trades counterparty risk for a concentrated personal risk.

## M-of-N Schemes

The M-of-N threshold defines how many co-signers must participate to authorize a spend:

| Scheme | Keys Required | Keys Held | Typical Use |
|--------|--------------|-----------|-------------|
| 1-of-2 | 1 of 2 | 2 | Shared access (two people, either can spend) |
| 2-of-2 | 2 of 2 | 2 | Both parties must sign (joint control) |
| 2-of-3 | 2 of 3 | 3 | Most common personal setup; lose one key and still recover |
| 3-of-5 | 3 of 5 | 5 | Institutional; high-value holdings |
| 5-of-7 | 5 of 7 | 7 | Exchange cold storage; quorum-based custody |

The **2-of-3** setup is the sweet spot for individuals: one key can be lost or stolen without losing funds, but an attacker who steals one key still cannot spend. This is the setup recommended in the [[en/practice/storage|storage guide]].

## Geographic vs. Vendor Distribution

Two distinct axes of key distribution reinforce each other:

**Geographic distribution** places keys at physically separate locations — for example, one key at home, one in a safe deposit box, one with a trusted family member or legal entity in another jurisdiction. An attacker must physically access multiple locations simultaneously.

**Vendor distribution** uses different hardware wallet brands for each key — for example, Coldcard, Trezor, and Jade. This protects against:
- A supply-chain attack on a single manufacturer
- A firmware vulnerability affecting one device family
- A regulatory action against a single company

Combining both axes creates a robust setup: a 2-of-3 where each key is a different hardware wallet brand stored in a different location.

## Address Types for Multisig

Multisig can be encoded in several Bitcoin [[en/concepts/address-types|address types]], each with different privacy and cost tradeoffs:

**P2SH (Pay-to-Script-Hash)** — Legacy multisig format. The redeem script (listing all N public keys and the threshold) is revealed when spending. This leaks the multisig structure on-chain.

**P2WSH (Pay-to-Witness-Script-Hash)** — Native SegWit multisig. Script moved into the witness (lower fees via [[en/concepts/segwit|SegWit]]). Still reveals the multisig structure when spending.

**P2TR + MuSig2 (Taproot multisig)** — The modern standard. Using [[en/concepts/taproot|Taproot]] and the MuSig2 key-aggregation protocol, N-of-N multisig participants can combine their keys into a single aggregated public key that is indistinguishable from a single-sig key on-chain. The N-of-N structure is invisible to blockchain observers. This provides significant privacy benefits and reduces fees further.

## MuSig2 and Taproot: N-of-N Looks Like Single-Sig

[[en/concepts/taproot|Taproot]] introduced Schnorr signatures, which are linearly aggregatable — multiple signatures can be combined into one. The MuSig2 protocol exploits this:

1. Each participant generates a nonce and a partial signature
2. The partial signatures are combined into a single Schnorr signature
3. The transaction looks identical to a standard single-sig P2TR spend

This is a significant privacy and efficiency improvement. However, MuSig2 requires all N participants to be online during signing, making it best suited for N-of-N (all keys required) schemes. M-of-N with M < N can use Taproot's script path via MAST, but this reveals the script structure if the script path is used.

## PSBT Workflow

Partially Signed Bitcoin Transactions (PSBT, BIP 174) are the standard protocol for coordinating multi-device signing:

1. **Transaction construction**: A coordinator (Sparrow Wallet, Nunchuk, Unchained dashboard) creates an unsigned transaction and serializes it as a PSBT
2. **Distribution**: The PSBT file is transferred to each required signer (via USB, QR code, SD card, or encrypted network)
3. **Partial signing**: Each hardware wallet reviews the transaction details and adds its partial signature to the PSBT
4. **Combination**: Once M signatures are collected, the coordinator combines them into a fully signed transaction
5. **Broadcast**: The completed transaction is broadcast to the Bitcoin network

Air-gapped devices (like Coldcard in fully air-gapped mode) pass PSBTs via microSD card, never touching a networked computer.

## Collaborative Custody Platforms

For users who want institutional-grade multisig without managing all keys themselves, collaborative custody platforms hold one key in a quorum while the user holds the remaining keys:

**Unchained Capital** — 2-of-3 multisig where Unchained holds one key, the user holds two. Unchained can never spend unilaterally; the user can recover without Unchained using their two keys. Offers loans against bitcoin collateral.

**Nunchuk** — Mobile-first multisig coordinator. Users can invite co-signers and manage keys across multiple devices. Supports both personal and collaborative setups.

**Sparrow Wallet** — Desktop wallet with full multisig support. Can coordinate signing with multiple hardware wallets, display PSBT workflow, and connect to the user's own node for privacy (see [[en/practice/privacy-practice|privacy practice guide]]).

**Casa** — Consumer-focused 2-of-3 and 3-of-5 multisig. Casa holds a recovery key. Emphasizes user experience over technical transparency.

## Trade-offs and Considerations

Multisig increases security but also increases operational complexity:

- **Inheritance**: Heirs must know the quorum threshold, have access to M keys, and understand the PSBT workflow. Proper documentation is essential.
- **Signing friction**: Every spend requires M hardware wallets and coordination. Not suitable for spending wallets; best for long-term cold storage.
- **Backup complexity**: The redeem script (or output descriptor) must be backed up alongside each key. Losing the script means losing the ability to reconstruct the addresses even if you have the keys.
- **Output descriptors**: Modern wallets (Sparrow, Nunchuk) encode the full multisig configuration in an output descriptor string — this must be backed up like a seed phrase.

## Comparison: Single-Sig vs. Multisig

| Property | Single-Sig | Multisig 2-of-3 |
|----------|------------|-----------------|
| Setup complexity | Low | Medium-High |
| Single point of failure | Yes | No |
| Key loss survivability | None | Lose 1 of 3 |
| Coercion resistance | Low | Higher (keys in multiple locations) |
| Fee overhead | None | Higher (larger scripts, more data) |
| Privacy (P2TR + MuSig2) | High | High (N-of-N) |
| Best use case | Spending wallet | Cold storage, large holdings |

## Sources

- [Multisig](https://21ideas.org/multisig/)
- [21ideas Glossary](https://21ideas.org/glossary/)

## Related pages

- [[en/concepts/security|Security — broader threat modeling including hardware wallets and seed phrases]]
- [[en/concepts/taproot|Taproot — Schnorr signatures and the MuSig2 foundation]]
- [[en/concepts/segwit|SegWit — reduces fees for multisig transactions]]
- [[en/concepts/address-types|Address types — P2SH, P2WSH, P2TR formats]]
- [[en/concepts/utxo|UTXO — the model underlying all Bitcoin transactions]]
- [[en/practice/storage|Storage — practical guide to cold storage and multisig setups]]
- [[en/practice/privacy-practice|Privacy practice — connecting to your own node for signing privacy]]
