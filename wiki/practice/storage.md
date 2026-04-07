# Storage & Self-Custody

*Tags: practice, storage, cold-storage, hardware-wallet, multisig*

---

## The Spectrum of Custody

```
LEAST SECURE ←————————————————————————→ MOST SECURE
Exchange   Hot Wallet   Hardware Wallet   Multisig
(custodial) (software)   (single-sig)     (2-of-3+)
```

The right setup depends on the amount you're holding and your threat model. For significant holdings, hardware wallet + multisig is the recommendation.

---

## Option 1: Software Hot Wallet

For small amounts only (spending money on Lightning, small on-chain amounts).

| Wallet | Platform | Best For |
|--------|----------|---------|
| BlueWallet | iOS/Android | Beginners, Lightning |
| Electrum | Desktop | Advanced users, coin control |

**Warning**: Software wallets are always-online. They are appropriate for "spending money" amounts, not savings.

---

## Option 2: Hardware Wallet (Single-Sig)

Keeps private keys offline. Significantly better than software wallets for savings.

### Coldcard (`raw/Practice/hodl/coldcard.md`)
- **Best security**: secure element, airgapped (microSD signing), open source firmware
- Supports PSBT (Partially Signed Bitcoin Transactions)
- Advanced features: duress PINs, brick-me PIN, passphrase support
- Learning curve is steep; most powerful option

### SeedSigner (`raw/Practice/hodl/seedsigner.md`)
- DIY: Raspberry Pi Zero + camera + display
- **Stateless**: no persistent storage — generates keys from seed words + camera entropy at runtime
- Airgapped (QR codes for signing)
- Very affordable (~$50 in parts)
- Excellent privacy (no serial numbers, no manufacturer account)

### Electrum on Old Phone/Laptop (`raw/Practice/hodl/smartphone-cold-storage.md`)
- Take an old phone, factory reset, install Electrum or Samourai, put in airplane mode permanently
- Functions as a basic airgapped signing device
- Lower security than dedicated hardware wallet but better than nothing

### BlueWallet (`raw/Practice/hodl/blue.md`)
- Primary use: watch-only wallet + PSBT coordinator for multisig
- Can sign with hardware wallets via QR
- Good for beginners moving to multisig

---

## Option 3: Multisig (Recommended for Significant Holdings)

Multisig requires M-of-N keys to spend. Eliminates single point of failure.

**2-of-3 setup** (most common):
- Key 1: Coldcard (home safe)
- Key 2: SeedSigner (different location)
- Key 3: Unchained Capital collaborative custody (or another hardware wallet with a trusted person)

One key lost → still spendable (use remaining 2)
One key stolen → still secure (thief needs 2 keys)

### Setting Up Multisig

1. Generate each key independently on separate devices
2. Record each seed phrase separately (never together)
3. Create the multisig wallet in Electrum or Sparrow (combining all 3 public keys)
4. Test receiving and spending a small amount before funding

Source: `raw/Theory/security/multisig-1.md`, `raw/Theory/security/multisig-2.md`

---

## Seed Phrase Best Practices

- **12 words** (BIP39): adequate for most users; smaller backup to store
- **24 words**: higher entropy; recommended for large holdings
- **Write on paper**: initial backup only; not durable long-term
- **Metal plates**: fire/water resistant; essential for primary backup
- **Never digital**: no photos, no cloud, no typed copies, no photos
- **Passphrase (25th word)**: strongly recommended for hardware wallets; store separately

---

## Verifying Your Software

Before using any Bitcoin software, verify the developer's cryptographic signature on the download. The `raw/Practice/security/pgp.md` guide covers GPG verification step-by-step.

---

## Threat Model

Consider:
- **Loss** (fire, flood, hardware failure): solved by geographic distribution of backups
- **Theft** (seed stolen): solved by passphrase (25th word) + multisig
- **Physical coercion** ($5 wrench attack): solved by multisig with geographically distributed keys (attacker can't get all keys in one location) + small "decoy" wallet with plausible deniability
- **Technical failure** (device breaks): solved by seed backup + multisig redundancy

---

## Related Pages

- [[concepts/security]] — detailed security concepts
- [[concepts/privacy]] — privacy in storage
- [[practice/buying]] — where bitcoin comes from before storage
- [[practice/lightning-tools]] — for spending/Lightning amounts
