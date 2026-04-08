---
title: "Lightning Tools"
category: practice
tags: [bitcoin, wiki, practice, lightning, tools]
language: en
source: "Synthesized from raw/ sources + glossary"
updated: "2026-04-07"
quality: synthesized
sources: []
synthesized_date: "2026-04-07"
completeness: medium
---

# Lightning Tools

*Tags: practice, lightning, wallets, apps*

---

## Self-Custodial Wallets

### Phoenix (`raw/Practice/lightning/phoenix.md`)
Made by ACINQ (Lightning developer). The recommended starting point for most users.

- **Self-custodial**: you hold your keys
- **Automatic channel management**: Phoenix opens and manages channels automatically via LSP (Lightning Service Provider)
- **Splicing**: rebalances channels without closing/reopening (reduces on-chain fees)
- **BOLT12**: newer invoice format with privacy improvements
- **Tradeoff**: pays LSP fees for channel opens; not zero-fee

### Mutiny (`raw/Practice/lightning/mutiny.md`)
Web/browser-based Lightning wallet. Runs in the browser but is non-custodial.

- **Self-custodial**: keys in your browser (can back up)
- **LSP for liquidity**: automatically provisions inbound capacity
- **Nostr integration**: wallet address tied to Nostr identity
- **Web-based**: no app store, works on any browser
- **Tradeoff**: browser-based wallets have security tradeoffs; experimental

---

## Self-Hosted / Account Systems

### LNbits (`raw/Practice/lightning/lnbits.md`)
Self-hosted Lightning account system with plugin ecosystem.

- Runs on your own server or a trusted instance
- Plugins: LNURL server, Lightning address, shop plugin, tipjar, NFC payments, Nostr Wallet Connect (NWC)
- Good for: merchant setups, educational Lightning experiments, running wallets for friends/family
- Requires a Lightning node backend (LND, Core Lightning, etc.)

---

## Browser Extensions

### Alby (`raw/Practice/lightning/alby-i-nostr.md`)
Browser extension for Lightning + Nostr.

- **WebLN**: connects web apps to your Lightning wallet
- **Lightning Address**: send to user@domain format
- **Nostr signing**: signs Nostr events in the browser
- **Nostr Wallet Connect (NWC)**: allow web apps to request payments from your wallet
- Works with: LNbits backend, Alby Hub (self-hosted), or cloud service

---

## Bots and Automation

### ZapGram (`raw/Practice/lightning/zapgram.md`)
Telegram bot for Lightning payments.

- Receive/send Lightning payments via Telegram
- Group tipping
- QR code generation
- Good for: communities using Telegram who want Lightning integration

### ZapPlanner (`raw/Practice/lightning/zapplanner.md`)
Tool for recurring Lightning payments.

- Set up recurring payments to any Lightning Address
- "Streaming sats" — scheduled micropayments
- Good for: supporting creators, recurring donations, subscriptions

---

## Liquidity Management

### Lightning Liquidity Guide (`raw/Practice/lightning/lightning-liquidity.md`)
For users running their own Lightning node. Covers:

- **Inbound vs. outbound liquidity**: why you need both
- **Loop In/Out** (submarine swaps): move funds between on-chain and Lightning
- **Lightning Pool**: buy/sell channel capacity
- **Circular rebalancing**: rebalance channels using your own funds
- **Balanced channels**: best practice for routing nodes

---

## Cleaning Bitcoin Through Lightning (`raw/Practice/lightning/ochishchaem-bitcoin-cherez-lajtning.md`)

If you have [[concepts/privacy|KYC]]-tainted on-chain Bitcoin and want to reduce surveillance, you can use [[concepts/lightning-network|Lightning]]:
1. Load KYC Bitcoin into Lightning via a channel open
2. Route payments through Lightning (off-chain, not traceable on the blockchain)
3. Receive fresh [[concepts/utxo|UTXOs]] via submarine swaps back to on-chain

This doesn't achieve the same [[concepts/privacy|privacy]] as [[practice/privacy-practice|Whirlpool]] [[concepts/privacy|CoinJoin]] but reduces the trivial traceability of on-chain spending.

---

## Choosing a Wallet

| Use Case | Recommended Wallet |
|----------|------------------|
| First Lightning wallet | Phoenix |
| Privacy-focused | Phoenix + own node backend |
| Web/Nostr integration | Alby extension |
| Self-hosted infrastructure | LNbits |
| Telegram community | ZapGram |
| Recurring payments | ZapPlanner |
| Running a routing node | Core Lightning / LND + Ride the Lightning |

---

## Sources

*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source article.*

---

## Related Terms

[[glossary|Glossary]] | [[concepts/lightning-network|Lightning Network]] | [[concepts/privacy|privacy]] | [[concepts/utxo|UTXO]] | [[concepts/security|self-custody]] | [[practice/privacy-practice|privacy practice]] | [[practice/storage|cold storage]] | [[practice/buying|buying Bitcoin]]

## Related Pages

- [[concepts/lightning-network]] — how Lightning works
- [[practice/privacy-practice]] — Lightning privacy considerations
- [[practice/storage]] — on-chain storage for larger amounts
