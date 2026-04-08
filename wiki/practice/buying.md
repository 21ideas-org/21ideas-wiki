---
title: "Buying Bitcoin"
category: practice
tags: [bitcoin, wiki, practice, buying, kyc-free]
language: en
source: "Synthesized from raw/ sources + glossary"
updated: "2026-04-07"
quality: synthesized
sources: []
synthesized_date: "2026-04-07"
completeness: medium
---

# Buying Bitcoin

*Tags: practice, buying, no-KYC, P2P*

---

## The KYC Problem

Most Bitcoin exchanges require [[concepts/privacy|KYC]] (Know Your Customer) — passport, ID, sometimes bank statements. The problem: this permanently links your identity to your Bitcoin addresses. Exchange databases get hacked. Governments compel exchanges to report or freeze funds. Once linked, every transaction from those addresses is tracked.

For maximum financial sovereignty, buy no-KYC. See [[concepts/privacy]] for the full argument.

---

## No-KYC Options

### [[practice/buying|Hodl Hodl]] (`raw/Practice/buy/hodl-hodl.md`)
[[practice/buying|P2P exchange]] (non-custodial). Buyer and seller agree on terms; funds are locked in a 2-of-3 [[concepts/security|multisig]] contract (buyer + seller + Hodl Hodl). No ID required. Accepts many payment methods (bank transfer, cash, gift cards).

- **Pros**: No ID, non-custodial escrow, many payment methods, reasonable fees
- **Cons**: Requires trust in counterparty (mitigated by reputation system), slower than centralized exchange
- **Best for**: Moderate amounts, recurring buys, privacy-conscious users

### RoboSats (`raw/Practice/buy/robosats.md`)
Lightning-native P2P exchange. Uses "robot identities" (generated from seed) — completely anonymous. Operates over Tor. Settlement via Lightning.

- **Pros**: Very fast (Lightning settlement), highest privacy (Tor + robot identities), no accounts
- **Cons**: Lightning-only; requires Lightning wallet; smaller liquidity than Hodl Hodl
- **Best for**: Small-to-medium amounts, maximum privacy, Lightning-native users

### Bisq
Decentralized desktop exchange. Fully P2P, no central server. Many payment methods.

- **Pros**: Completely decentralized, no central point of failure, no accounts
- **Cons**: Desktop app required, lower liquidity, slower UX, learning curve
- **Best for**: Technical users, moderate amounts

### Bitcoin ATMs
Physical machines accepting cash → Bitcoin. No account required (for small amounts).

- **Pros**: Physical cash, instant, anonymous for small amounts
- **Cons**: High fees (3-8%+), limited locations, ID may be required above certain limits
- **Best for**: Very small amounts, one-time purchases, cash on hand

---

## Beginner Guide (for new buyers)

The site's beginner guide (`raw/Practice/buy/newbie-buy.md`) walks through the full flow from zero:
1. Get a Bitcoin wallet first (see [[practice/storage]])
2. Choose a P2P exchange based on your country/payment method
3. Create an offer or take an existing one
4. Receive BTC into your own wallet (not exchange wallet)
5. Move to cold storage if amount is significant

---

## Dollar Cost Averaging (DCA)

DCA = buying a fixed fiat amount at regular intervals (weekly, monthly) regardless of price. The argument for DCA:
- Eliminates timing decisions (removes emotion)
- Averages your cost basis over multiple price levels
- Consistent with "stack sats" strategy for long-term holders

Source: `raw/Theory/economics/dollar-cost-averaging.md`

---

## After Buying: Self-Custody

The most important step after buying: move your bitcoin to a wallet you control. An exchange balance is not Bitcoin — it is an IOU. See [[practice/storage]] for [[concepts/security|self-custody]] options.

---

## Sources

*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source article.*

---

## Related Terms

[[glossary|Glossary]] | [[concepts/privacy|privacy]] | [[concepts/security|self-custody]] | [[concepts/utxo|UTXO]] | [[practice/storage|cold storage]] | [[practice/privacy-practice|privacy practice]] | [[practice/lightning-tools|Lightning tools]] | [[series/oxt-research|blockchain analysis]]

## Related Pages

- [[concepts/privacy]] — why no-KYC matters
- [[practice/storage]] — where to put your bitcoin after buying
- [[practice/lightning-tools]] — Lightning wallets for RoboSats and Phoenix
