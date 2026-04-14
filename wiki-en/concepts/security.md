---
title: "Security"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/multisig/", "https://21ideas.org/glossary/", "https://21ideas.org/seed-security/", "https://21ideas.org/seed/", "https://21ideas.org/passphrase/", "https://21ideas.org/hwws/", "https://21ideas.org/coldcard/", "https://21ideas.org/seedsigner/"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, security, multisig]
updated: "2026-04-07"
reviewed: "2026-04-14"
---

## The Core Principle

"Not your keys, not your coins." If a third party holds your bitcoin, you have an IOU, not bitcoin. The bankruptcy of FTX, Mt. Gox, Celsius, and others illustrates this. Self-custody is not advanced — it is the point.

## Seed Phrases (BIP39)

A 12- or 24-word seed phrase (mnemonic) is the master key to your bitcoin. All addresses and private keys are derived from this single seed using a deterministic algorithm ([[en/concepts/bip|BIP]]32/44/49/84).

**Critical rules:**
- Never enter your seed online (no photos, no cloud storage, no typing into any website)
- Store offline, physically (metal plate, fireproof safe)
- Store redundant copies in different locations
- The seed is everything — whoever has it, has your bitcoin

Source: [Seed Phrases](https://21ideas.org/seed/), [Seed Security](https://21ideas.org/seed-security/)

## Passphrase (25th Word)

An optional BIP39 extension: add an arbitrary passphrase to your seed. This creates an entirely different wallet tree. Benefits:
- Protection against physical seed discovery (attacker finds your seed words but not the passphrase)
- "Plausible deniability" wallet: keep a small decoy amount on the no-passphrase wallet

**Warning:** Passphrase loss = permanent funds loss. Store separately from the seed words.

Source: [Passphrase Guide](https://21ideas.org/passphrase/)

## Hardware Wallets

Hardware wallets are dedicated signing devices that keep private keys off internet-connected computers. The private key never leaves the device; transactions are signed on the device and broadcast via an airgap or USB.

| Device | Security Model | Notable Feature |
|--------|---------------|-----------------|
| [[en/practice/storage\|Coldcard]] | Airgapped (microSD), secure element | PSBT, advanced [[en/concepts/multisig\|multisig]], open firmware |
| SeedSigner | DIY (RPi Zero + camera), stateless | No persistent storage; generates keys from seed at runtime |
| Foundation Passport | Open source, airgapped | US-made, QR-based signing |
| Trezor | USB, open source | Most accessible; no secure element on older models |
| Ledger | USB, closed source | Largest market share; secure element |
| BitBox02 | USB, open source Swiss | Bitcoin-only edition |

**Recommended:** Coldcard for advanced users; SeedSigner for DIY/open source enthusiasts; Trezor/Foundation Passport for accessibility.

Source: [Hardware Wallets](https://21ideas.org/hwws/), [Coldcard Guide](https://21ideas.org/coldcard/), [SeedSigner Guide](https://21ideas.org/seedsigner/)

## Multisig

[[en/concepts/multisig|Multisig]] (M-of-N) requires M signatures out of N possible keys to spend. Benefits:
- **Eliminates single point of failure**: lose one key → funds still safe
- **Eliminates single point of theft**: steal one key → funds still safe
- **Geographic distribution**: keys can be stored in different locations

Common setups:
- **2-of-3**: most common; one key lost is tolerable; two keys required to spend
- **3-of-5**: higher redundancy, higher complexity

Unchained Capital's model: collaborative custody with 2-of-3 where the user holds 2 keys and Unchained holds 1. The user retains control; Unchained can help recover if one user key is lost.

Source: [Multisig](https://21ideas.org/multisig/)

## Wallets

| Wallet | Type | Platform | Notes |
|--------|------|----------|-------|
| Electrum | Desktop hot + cold | Windows/Mac/Linux | Mature, coin control, connects to own node |
| BlueWallet | Mobile | iOS/Android | Watch-only, PSBT multisig, LN layer |
| Coldcard | Hardware signing device | Airgapped | Best-in-class cold storage |
| SeedSigner | DIY hardware | Airgapped RPi | Stateless, cheapest airgapped option |
| Smartphone cold storage | Repurposed phone | Airgapped phone | Old phone + Electrum in airplane mode |

## PGP (Verifying Software Downloads)

Before running any Bitcoin software, verify the cryptographic signature of the download. PGP (Pretty Good Privacy) allows developers to sign releases; users verify signatures against known public keys. A guide to verifying downloads using GPG command-line tools is available in the [[en/practice/storage|storage practice]] section.

## Physical Security

The weakest link in Bitcoin security is often physical:
- Seed stored in a single location can be lost in a fire or flood
- Seed written on paper can be read by anyone who finds it
- Passphrase stored with seed defeats its purpose

Best practices:
- Metal seed plate (fire/water resistant)
- Seed and passphrase stored separately
- [[en/concepts/multisig|Multisig]] with geographically distributed keys
- Trusted party with one key but not the passphrase (Unchained model)

## Common Attacks

| Attack | Description | Defense |
|--------|-------------|---------|
| Supply chain | Compromised hardware wallet before delivery | Buy direct from manufacturer; verify firmware |
| Seed theft | Physical access to seed storage | Passphrase, geographic distribution |
| Phishing | Fake wallet website | Verify URLs; use hardware wallets |
| $5 wrench | Physical coercion | Geographic key distribution, multisig, decoy wallets |
| Malware | Clipboard hijacking of addresses | Air-gapped signing, hardware wallets |

## Sources

- [Multisig](https://21ideas.org/multisig/)
- [21ideas Glossary](https://21ideas.org/glossary/)
- [Seed Security](https://21ideas.org/seed-security/)
- [Seed Phrases](https://21ideas.org/seed/)
- [Passphrase Guide](https://21ideas.org/passphrase/)
- [Hardware Wallets](https://21ideas.org/hwws/)
- [Coldcard Guide](https://21ideas.org/coldcard/)
- [SeedSigner Guide](https://21ideas.org/seedsigner/)

## Related pages

- [[en/concepts/bitcoin|Bitcoin — what you're securing]]
- [[en/concepts/multisig|Multisig — deep-dive on M-of-N schemes, MuSig2, and PSBT workflow]]
- [[en/concepts/taproot|Taproot — MuSig2 and Schnorr signatures for multisig privacy]]
- [[en/concepts/privacy|Privacy — privacy and security reinforce each other]]
- [[en/practice/storage|Storage — practical cold storage and hardware wallet setup guides]]
- [[en/entities/hal-finney|Hal Finney — PGP pioneer and early Bitcoin security thinker]]
- [[en/entities/cypherpunks|Cypherpunks — the philosophy behind self-custody and privacy]]
