---
title: "Privacy"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/privacy/"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, privacy, security]
updated: "2026-04-07"
reviewed: "2026-04-14"
---

## Why Bitcoin Privacy Matters

Bitcoin's ledger is fully public — every transaction is visible to anyone. This is necessary for the consensus mechanism but creates surveillance risks:
- Address clusters can be linked to identities (via [[en/concepts/aml|KYC]] at exchanges, IP addresses, merchant data)
- Once an identity is linked to an address, the entire transaction history becomes deanonymized
- Governments and [[en/series/oxt-research|blockchain analysis]] firms (Chainalysis, Elliptic) actively perform this surveillance
- "Tainted" coins can be blacklisted by exchanges, threatening fungibility

Privacy is not about hiding illegal activity — it is the foundation of financial sovereignty.

## Fungibility Problem

Bitcoin's fungibility is theoretical but practically compromised. If exchanges can blacklist "tainted" coins, then not all bitcoins are equal — which breaks a fundamental property of money. CoinJoin and privacy tools are not luxuries; they restore fungibility.

## KYC vs. No-KYC

**[[en/concepts/aml|KYC]] (Know Your Customer):** exchanges and services that collect identity documents. Problems:
- Permanent data: your identity is permanently linked to your bitcoin addresses
- Data leaks: exchange databases are hacked regularly
- Government coercion: exchanges are compelled to report/freeze funds
- Address surveillance: all future transactions from those addresses are tracked

**No-KYC acquisition:**
- [[en/practice/buying|P2P exchanges]]: Hodl Hodl, RoboSats, Bisq
- ATMs (small amounts, higher fees)
- Mining, earning, accepting payment

## Blockchain Analysis Techniques

*From the [[en/series/oxt-research|OXT Research]] series (Samourai Wallet team):*

**CIOH (Common Input Ownership Heuristic):** If multiple inputs appear in the same transaction, they likely come from the same wallet. This allows clustering addresses into entities.

**Change detection:** When a transaction has two outputs, one is typically change back to the sender. Analysts use value patterns, address reuse, and address types to identify the change output.

**Transaction graph analysis:** Following the flow of coins through multiple hops.

## CoinJoin / Whirlpool

**CoinJoin** merges multiple users' inputs in a single transaction with equal-value outputs, making input-output linking impossible. The equal outputs defeat the CIOH heuristic.

**[[en/practice/privacy-practice|Whirlpool]]** (Samourai Wallet implementation):
- 5 equal-output pools (100k, 1M, 5M, 50M satoshis)
- ZeroLink protocol: fresh UTXOs, no post-mix address reuse
- Pre-mix and post-mix [[en/concepts/utxo|UTXO]] management
- "Toxic change" concept: unequal change from pre-mix stays pre-mix

Note: Samourai Wallet developers (Keonne Rodriguez and William Hill) were arrested by the DOJ in April 2024. The wallet is still functional.

## BIP47 / PayNym

BIP47 introduces reusable payment codes. Alice generates a payment code; Bob generates a derived address for each payment from Alice using ECDH. This eliminates address reuse (a privacy leak) while enabling a recognizable "identity" (PayNym contact). Samourai Wallet implements this as **PayNym contacts**.

## Lightning and Privacy

[[en/concepts/lightning-network|Lightning]] offers better privacy than on-chain (payments are not publicly broadcast) but has issues:
- Public channel graph reveals node topology
- Routing nodes see payment paths they participate in
- Payment probing can map balances

Improvements: private (unannounced) channels, onion routing (already used in Lightning), Blinded Paths (BOLT12).

## Privacy Tools Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Acquisition | RoboSats, Hodl Hodl, Bisq | No-KYC BTC purchase |
| On-chain mixing | Whirlpool (Samourai) | CoinJoin to break history |
| Wallet backend | Dojo / RoninDojo | Self-hosted node so wallet doesn't leak to third-party server |
| Mobile OS | GrapheneOS | Hardened Android, no Google tracking |
| Self-hosted node | [[en/concepts/bitcoin-core|Bitcoin Core]] + Electrs | Verify your own blocks, no reliance on third-party nodes |
| Lightning | Phoenix, Mutiny | Self-custodial LN with LSP handling liquidity |

## Dojo (Self-Hosted Samourai Backend)

Dojo is the node backend for Samourai Wallet. Without it, Samourai's servers see your addresses and transaction history. With Dojo, your wallet connects to your own node — Samourai learns nothing.

**[[en/practice/privacy-practice|RoninDojo]]** = Dojo packaged for x86 hardware with GUI, Whirlpool integration, and Electrum Rust Server.

The Dojo series (7 parts) covers the complete setup — see [[en/practice/privacy-practice|privacy practice guide]].

## GrapheneOS

GrapheneOS is a hardened Android OS for Pixel phones. It removes Google Play Services, sandboxes apps, and hardens the OS against exploitation. Recommended for maximum privacy on mobile Bitcoin/Lightning use.

## Sources

- [Privacy on 21ideas](https://21ideas.org/privacy/)

## Related pages

- [[en/concepts/aml|AML/KYC — how surveillance enters the Bitcoin stack]]
- [[en/concepts/utxo|UTXO — the transaction model privacy tools operate on]]
- [[en/concepts/lightning-network|Lightning Network — off-chain privacy tradeoffs]]
- [[en/concepts/bitcoin-core|Bitcoin Core — self-hosted node for wallet privacy]]
- [[en/concepts/security|Security — seed phrases, hardware wallets, and threat modeling]]
- [[en/series/oxt-research|OXT Research — blockchain analysis techniques explained]]
- [[en/practice/privacy-practice|Privacy practice — practical setup guides for Dojo, Whirlpool, and more]]
- [[en/practice/buying|Buying — no-KYC acquisition methods]]
- [[en/entities/cypherpunks|Cypherpunks — privacy as a core value]]
- [[en/history/blocksize-war|Blocksize War — politics of Bitcoin privacy decisions]]
