---
title: "Storage & Self-Custody"
category: "practice"
quality: "synthesized"
sources: ["https://21ideas.org/coldcard", "https://21ideas.org/seedsigner", "https://21ideas.org/holodnyj-koshelek-iz-starogo-smartfona", "https://21ideas.org/blue", "https://21ideas.org/multisig-1", "https://21ideas.org/multisig-2", "https://21ideas.org/pgp-verify"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, security, multisig]
updated: "2026-04-07"
reviewed: "2026-04-14"
---

## The Spectrum of Custody

```
LEAST SECURE ←————————————————————————→ MOST SECURE
Exchange   Hot Wallet   Hardware Wallet   Multisig
(custodial) (software)   (single-sig)     (2-of-3+)
```

The right setup depends on the amount you're holding and your threat model. For significant holdings, a [[en/glossary#Hardware wallet|Hardware wallet]] plus [[en/concepts/multisig|multisig]] is a common recommendation.

## Option 1: Software Hot Wallet

For small amounts only (spending money on Lightning, small on-chain amounts).

| Wallet | Platform | Best For |
|--------|----------|---------|
| BlueWallet | iOS/Android | Beginners, Lightning |
| Electrum | Desktop | Advanced users, coin control |

**Warning**: Software wallets are always-online. They are appropriate for "spending money" amounts, not savings.

## Option 2: Hardware Wallet (Single-Sig)

Keeps private keys offline. Significantly better than software wallets for savings.

### Coldcard
- **Best security**: secure element, airgapped (microSD signing), open source firmware
- Supports [[en/glossary#PSBT (Partially Signed Bitcoin Transaction)|PSBT (Partially Signed Bitcoin Transaction)]]
- Advanced features: duress PINs, brick-me PIN, passphrase support
- Learning curve is steep; most powerful option

### SeedSigner
- DIY: Raspberry Pi Zero + camera + display
- **Stateless**: no persistent storage — generates keys from seed words + camera entropy at runtime
- Airgapped (QR codes for signing)
- Very affordable (~$50 in parts)
- Excellent privacy (no serial numbers, no manufacturer account)

### Electrum on Old Phone/Laptop
- Take an old phone, factory reset, install Electrum or Samourai, put in airplane mode permanently
- Functions as a basic airgapped signing device
- Lower security than dedicated hardware wallet but better than nothing

### BlueWallet
- Primary use: watch-only wallet + PSBT coordinator for multisig
- Can sign with hardware wallets via QR
- Good for beginners moving to multisig

## Option 3: Multisig (Recommended for Significant Holdings)

Multisig requires M-of-N keys to spend. Eliminates single point of failure.

**2-of-3 setup** (most common):
- Key 1: [Coldcard](https://21ideas.org/coldcard) (home safe)
- Key 2: [SeedSigner](https://21ideas.org/seedsigner) (different location)
- Key 3: Unchained Capital collaborative custody (or another [[en/glossary#Hardware wallet|Hardware wallet]] with a trusted person)

One key lost → still spendable (use remaining 2)
One key stolen → still secure (thief needs 2 keys)

### Setting Up Multisig

1. Generate each key independently on separate devices
2. Record each seed phrase separately (never together)
3. Create the multisig wallet in Electrum or Sparrow (combining all 3 public keys)
4. Test receiving and spending a small amount before funding

Source: [Multisig — Part I](https://21ideas.org/multisig-1), [Multisig — Part II](https://21ideas.org/multisig-2)

## Seed Phrase Best Practices

- **12 words**: adequate for most users; smaller backup to store
- **24 words**: higher entropy; recommended for large holdings
- **Write on paper**: initial backup only; not durable long-term
- **Metal plates**: fire/water resistant; essential for primary backup
- **Never digital**: no photos, no cloud, no typed copies, no photos
- **Passphrase (25th word)**: strongly recommended for hardware wallets; store separately

## Verifying Your Software

Before using any Bitcoin software, verify the developer's cryptographic signature on the download. See: [Verifying software with PGP](https://21ideas.org/pgp-verify).

## Threat Model

Consider:
- **Loss** (fire, flood, hardware failure): solved by geographic distribution of backups
- **Theft** (seed stolen): solved by passphrase (25th word) + multisig
- **Physical coercion** ($5 wrench attack): solved by multisig with geographically distributed keys (attacker can't get all keys in one location) + small "decoy" wallet with plausible deniability
- **Technical failure** (device breaks): solved by seed backup + multisig redundancy

## Sources

- [What is Coldcard?](https://21ideas.org/coldcard)
- [SeedSigner: offline fortress](https://21ideas.org/seedsigner)
- [Cold wallet from an old smartphone](https://21ideas.org/holodnyj-koshelek-iz-starogo-smartfona)
- [BlueWallet](https://21ideas.org/blue)
- [Multisig — Part I](https://21ideas.org/multisig-1)
- [Multisig — Part II](https://21ideas.org/multisig-2)
- [Verifying software with PGP](https://21ideas.org/pgp-verify)

## Related pages

- [[en/glossary|Glossary]]
- [[en/concepts/security|Security]]
- [[en/concepts/privacy|Privacy]]
- [[en/concepts/utxo|UTXOs (Unspent Transaction Outputs)]]
- [[en/concepts/address-types|Bitcoin Address Types]]
- [[en/concepts/multisig|Multisig (Multisignature)]]
- [[en/practice/buying|Buying Bitcoin]]
- [[en/practice/privacy-practice|Privacy in Practice]]
- [[en/practice/lightning-tools|Lightning Tools]]
- [[en/practice/running-a-node|Running a Bitcoin Node]]
