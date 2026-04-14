---
title: "Lightning Tools"
category: "practice"
quality: "synthesized"
sources: ["https://21ideas.org/practice/lightning", "https://21ideas.org/phoenix", "https://21ideas.org/mutiny", "https://21ideas.org/lnbits", "https://21ideas.org/alby-i-nostr", "https://21ideas.org/zapplanner", "https://21ideas.org/zapgram", "https://21ideas.org/ochishchaem-bitcoin-cherez-lajtning", "https://21ideas.org/likvidnost-v-lajtning"]
synthesized_date: "2026-04-07"
completeness: "medium"
language: "en"
tags: [bitcoin, wiki, lightning, privacy, security, multisig, concept, synthesized]
updated: "2026-04-11"
reviewed: "2026-04-11"
---

## Introduction

Practical tools for [[en/concepts/lightning-network|Lightning Network]] on [[en/concepts/bitcoin|Bitcoin]]: wallets, extensions, automation, and liquidity. The guides below map to the [Lightning practice section](https://21ideas.org/practice/lightning) on 21ideas.org.

## Self-Custodial Wallets

### Phoenix

Made by ACINQ (Lightning developer). The recommended starting point for most users. Guide: [Phoenix wallet](https://21ideas.org/phoenix).

- **Self-custodial**: you hold your [[en/glossary#private key|keys]]
- **Automatic channel management**: Phoenix opens and manages channels automatically via LSP (Lightning Service Provider)
- **Splicing**: rebalances channels without closing/reopening (reduces on-chain fees)
- **BOLT12**: newer invoice format with privacy improvements (see [[en/concepts/bip|BIPs]])
- **Tradeoff**: pays LSP fees for channel opens; not zero-fee

### Mutiny

Web/browser-based Lightning wallet. Runs in the browser but is non-custodial. Guide: [Mutiny wallet](https://21ideas.org/mutiny).

- **Self-custodial**: keys in your browser (can back up)
- **LSP for liquidity**: automatically provisions inbound capacity
- **Nostr integration**: wallet address tied to Nostr identity
- **Web-based**: no app store, works on any browser
- **Tradeoff**: browser-based wallets have [[en/concepts/security|security]] tradeoffs; experimental

## Self-Hosted / Account Systems

### LNbits

Self-hosted Lightning account system with plugin ecosystem. Guide: [LNbits](https://21ideas.org/lnbits).

- Runs on your own server or a trusted instance
- Plugins: LNURL server, Lightning address, shop plugin, tipjar, NFC payments, Nostr Wallet Connect (NWC)
- Good for: merchant setups, educational Lightning experiments, running wallets for friends/family
- Requires a Lightning node backend (LND, Core Lightning, etc.); see [[en/practice/running-a-node|running a node]]

## Browser Extensions

### Alby

Browser extension for Lightning + Nostr. Guide: [Alby and Nostr](https://21ideas.org/alby-i-nostr).

- **WebLN**: connects web apps to your Lightning wallet
- **Lightning Address**: send to user@domain format
- **Nostr signing**: signs Nostr events in the browser
- **Nostr Wallet Connect (NWC)**: allow web apps to request payments from your wallet
- Works with: LNbits backend, Alby Hub (self-hosted), or cloud service

## Bots and Automation

### ZapGram

Telegram bot for Lightning payments. Guide: [ZapGram](https://21ideas.org/zapgram).

- Receive/send Lightning payments via Telegram
- Group tipping
- QR code generation
- Good for: communities using Telegram who want Lightning integration

### ZapPlanner

Tool for recurring Lightning payments. Guide: [Lightning subscriptions (ZapPlanner)](https://21ideas.org/zapplanner).

- Set up recurring payments to any Lightning Address
- "Streaming sats" — scheduled micropayments
- Good for: supporting creators, recurring donations, subscriptions

## Liquidity Management

### Lightning Liquidity Guide

For users running their own Lightning node. Guide: [Lightning liquidity management](https://21ideas.org/likvidnost-v-lajtning). Covers:

- **Inbound vs. outbound liquidity**: why you need both
- **Loop In/Out** (submarine swaps): move funds between on-chain and Lightning
- **Lightning Pool**: buy/sell channel capacity
- **Circular rebalancing**: rebalance channels using your own funds
- **Balanced channels**: best practice for routing nodes

## Cleaning Bitcoin Through Lightning

If you have [[en/concepts/aml|KYC]]-tainted on-chain Bitcoin and want to reduce surveillance, you can use Lightning ([guide](https://21ideas.org/ochishchaem-bitcoin-cherez-lajtning)):

1. Load KYC Bitcoin into Lightning via a channel open
2. Route payments through Lightning (off-chain, not traceable on the blockchain)
3. Receive fresh [[en/concepts/utxo|UTXOs]] via submarine swaps back to on-chain

This doesn't achieve the same [[en/concepts/privacy|privacy]] as a [[en/practice/privacy-practice|Whirlpool-style CoinJoin]], but reduces the trivial traceability of on-chain spending.

## Choosing a Wallet

| Use Case | Recommended Wallet |
| -------- | ------------------ |
| First Lightning wallet | Phoenix |
| Privacy-focused | Phoenix + own node backend |
| Web/Nostr integration | Alby extension |
| Self-hosted infrastructure | LNbits |
| Telegram community | ZapGram |
| Recurring payments | ZapPlanner |
| Running a routing node | Core Lightning / LND + Ride the Lightning |

## Sources

- [Lightning practice (index)](https://21ideas.org/practice/lightning)
- [Phoenix wallet](https://21ideas.org/phoenix)
- [Mutiny wallet](https://21ideas.org/mutiny)
- [LNbits](https://21ideas.org/lnbits)
- [Alby and Nostr](https://21ideas.org/alby-i-nostr)
- [ZapPlanner — Lightning subscriptions](https://21ideas.org/zapplanner)
- [ZapGram](https://21ideas.org/zapgram)
- [Cleaning bitcoin through Lightning](https://21ideas.org/ochishchaem-bitcoin-cherez-lajtning)
- [Lightning liquidity management](https://21ideas.org/likvidnost-v-lajtning)

## Related pages

- [[en/concepts/lightning-network|How Lightning works]]
- [[en/concepts/bip|Bitcoin Improvement Proposals (BIPs)]]
- [[en/practice/running-a-node|Running a Bitcoin / Lightning node]]
- [[en/practice/privacy-practice|Privacy practice (CoinJoin, operational hygiene)]]
- [[en/practice/storage|Cold storage for larger on-chain amounts]]
- [[en/practice/buying|Buying Bitcoin]]
- [[en/concepts/security|Security and self-custody]]
- [[en/concepts/privacy|Privacy in Bitcoin]]
- [[en/concepts/multisig|Multisig]]
- [[en/glossary|Glossary]]
