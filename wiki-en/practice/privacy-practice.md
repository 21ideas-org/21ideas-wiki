---
title: "Privacy in Practice"
category: "practice"
quality: "synthesized"
sources: []
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, privacy, synthesized]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## The Privacy Stack

Privacy is not one tool — it is a stack of practices at every layer. A privacy failure at any layer can undo gains at other layers.

```
Layer               Tool                    What it protects
─────────────────────────────────────────────────────────────
Acquisition         RoboSats / Hodl Hodl    No-KYC BTC
OS / Device         GrapheneOS              Mobile tracking
Wallet backend      Dojo / RoninDojo        Address discovery
On-chain mixing     Whirlpool (Samourai)    Transaction history
UTXO management     Coin control            Cross-contamination
Payments            Lightning               Small payment privacy
Identity            PayNym / BIP47          Address reuse
```

## Step 1: Start No-KYC

The easiest [[en/concepts/privacy|privacy]] improvement is never creating the link between identity and Bitcoin address in the first place. See [[en/practice/buying|Buying Bitcoin]] for no-[[en/concepts/aml|KYC]] options.

If you already have KYC Bitcoin, the next steps are more important.

## Step 2: GrapheneOS

Before worrying about Bitcoin-specific privacy, your phone is the biggest tracking device you own. GrapheneOS is a hardened Android OS for Pixel phones:

- Removes Google Play Services (replaced with sandboxed Google Play if needed)
- Hardens the OS against exploitation
- Per-app network and sensor permissions
- Strong compartmentalization between apps

Setup: flash GrapheneOS on a supported Pixel phone. The guide covers the full process.

## Step 3: Self-Hosted Node (Dojo / RoninDojo)

When your wallet queries a third-party server for your balance and transaction history, that server learns all your addresses. Solution: run your own [[en/practice/running-a-node|node]] and connect your wallet to it.

**Dojo**: Samourai Wallet's node backend. Series of 7 guides covering complete setup on x86 hardware.

**RoninDojo**: Dojo packaged for easier deployment. Includes:
- Dojo (full node + indexer)
- Electrum Rust Server (for other wallets)
- Whirlpool GUI (for CoinJoin)
- Whirlpool CLI (for automated mixing)

After setup, point your Samourai Wallet to your Dojo. Now the only server that knows your addresses is your own.

## Step 4: Whirlpool CoinJoin

CoinJoin mixes your [[en/concepts/utxo|UTXOs]] with other users', breaking the transaction history link. Whirlpool (Samourai Wallet) is the implementation covered in this library.

**The process:**
1. Move funds into Samourai Wallet (connected to your Dojo)
2. Enter a Whirlpool pool (100k / 1M / 5M / 50M sats)
3. Your UTXOs are split into equal-value outputs and mixed with other participants
4. Post-mix UTXOs have no traceable history back to pre-mix

**Key concepts:**
- **Toxic change**: the unequal leftover from pool entry stays in "pre-mix" — treat it as unclean
- **Remixing**: post-mix UTXOs participate in additional free mixes over time (more mixes = better privacy)
- **Spending post-mix**: use post-mix UTXOs separately; don't combine with pre-mix

*Note: Samourai Wallet developers were arrested by the DOJ in April 2024. The wallet is still functional; the backend servers are being maintained by the community.*

## Step 5: PayNym / BIP47

Address reuse is a privacy leak: if you always receive to the same address, anyone can see your full incoming transaction history. PayNym ([[en/concepts/bip|BIP47]]) solves this:

- You publish a "payment code" (a kind of Bitcoin identity)
- Senders derive unique one-time addresses from your payment code using ECDH
- Each sender gets their own private address space
- No one else can link your incoming transactions

Setup: Samourai Wallet supports PayNym natively.

## Step 6: Coin Control

Manual selection of which UTXOs to use in transactions. Prevents:
- Mixing KYC and no-KYC coins (which links the no-KYC address to your KYC identity)
- Creating large combined UTXOs that reveal all coin sources

Best wallets for coin control: Sparrow Wallet, Electrum, Samourai Wallet.

## The OXT Research Series

The [[en/series/oxt-research|OXT Research]] series (4 parts) explains blockchain analysis from the attacker's perspective, so you can understand what you're defending against:

1. **Fundamentals of blockchain analysis**: what analysts do, what data they use
2. **Key concepts**: CIOH (Common Input Ownership Heuristic), change detection methods
3. **Defenses**: how CoinJoin and good UTXO hygiene defeat analysis
4. **Practical application**: how to analyze your own transaction history

Understanding the attacker's view is essential for meaningful [[en/concepts/privacy|privacy]].

## Lightning Privacy

[[en/concepts/lightning-network|Lightning Network]] payments are better for privacy than on-chain (payments aren't broadcast publicly), but have their own issues. Key: use private (unannounced) channels where possible, and prefer Phoenix/Mutiny (which handle routing intelligently). See [[en/practice/lightning-tools|Lightning Tools]] for wallet options.

## Sources

*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source article.*

## Related pages

- [[en/concepts/privacy|Privacy — the theory and why it matters]]
- [[en/concepts/utxo|UTXOs — UTXO management and coin control]]
- [[en/concepts/aml|AML/KYC — why no-KYC acquisition matters]]
- [[en/practice/buying|Buying Bitcoin — no-KYC acquisition options]]
- [[en/practice/running-a-node|Running a Node — connect your wallet backend to your own node]]
- [[en/practice/lightning-tools|Lightning Tools — Lightning wallets for payment privacy]]
- [[en/series/oxt-research|OXT Research — blockchain analysis from the attacker's perspective]]
- [[en/entities/cypherpunks|Cypherpunks — why privacy matters philosophically]]
- [[en/concepts/bitcoin-node|Bitcoin Node — full node self-sovereignty]]
- [[en/glossary|Glossary]]
