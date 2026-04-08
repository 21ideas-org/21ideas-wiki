---
title: "Privacy"
category: concepts
tags: [bitcoin, wiki, privacy, security, coinjoin]
language: en
updated: "2026-04-07"
quality: reference
sources: [https://21ideas.org/privacy/]
synthesized_date: "2026-04-07"
completeness: high
---

# Privacy

*Tags: privacy, coinjoin, surveillance, fungibility, on-chain*

---

## Why Bitcoin Privacy Matters

Bitcoin's ledger is fully public — every transaction is visible to anyone. This is necessary for the consensus mechanism but creates surveillance risks:
- Address clusters can be linked to identities (via [[en/concepts/privacy|KYC]] at exchanges, IP addresses, merchant data)
- Once an identity is linked to an address, the entire transaction history becomes deanonymized
- Governments and [[en/series/oxt-research|blockchain analysis]] firms (Chainalysis, Elliptic) actively perform this surveillance
- "Tainted" coins can be blacklisted by exchanges, threatening fungibility

Privacy is not about hiding illegal activity — it is the foundation of financial sovereignty.

Source: `raw/Theory/privacy/`, `raw/Theory/privacy/oxt/`, `raw/Theory/philosophy/cypherpunks-manifesto.md`

---

## Fungibility Problem

Bitcoin's fungibility is theoretical but practically compromised. If exchanges can blacklist "tainted" coins, then not all bitcoins are equal — which breaks a fundamental property of money. CoinJoin and privacy tools are not luxuries; they restore fungibility.

Source: `raw/Theory/privacy/bitcoin-fungibility.md`

---

## KYC vs. No-KYC

**KYC (Know Your Customer):** exchanges and services that collect identity documents. Problems:
- Permanent data: your identity is permanently linked to your bitcoin addresses
- Data leaks: exchange databases are hacked regularly
- Government coercion: exchanges are compelled to report/freeze funds
- Address surveillance: all future transactions from those addresses are tracked

**No-KYC acquisition:**
- [[en/practice/buying|P2P exchange]]s: [[en/practice/buying|Hodl Hodl]], RoboSats, Bisq
- ATMs (small amounts, higher fees)
- Mining, earning, accepting payment

Source: `raw/Theory/privacy/no-kyc.md`

---

## Blockchain Analysis Techniques

*From the OXT Research series (Samourai Wallet team):*

**CIOH (Common Input Ownership Heuristic):** If multiple inputs appear in the same transaction, they likely come from the same wallet. This allows clustering addresses into entities.

**Change detection:** When a transaction has two outputs, one is typically change back to the sender. Analysts use value patterns, address reuse, and address types to identify the change output.

**Transaction graph analysis:** Following the flow of coins through multiple hops.

Source: `raw/Theory/privacy/oxt/`

---

## CoinJoin / Whirlpool

[[en/concepts/privacy|CoinJoin]] merges multiple users' inputs in a single transaction with equal-value outputs, making input-output linking impossible. The equal outputs defeat the CIOH heuristic.

**[[en/practice/privacy-practice|Whirlpool]]** (Samourai Wallet implementation):
- 5 equal-output pools (100k, 1M, 5M, 50M satoshis)
- ZeroLink protocol: fresh UTXOs, no post-mix address reuse
- Pre-mix and post-mix UTXO management
- "Toxic change" concept: unequal change from pre-mix stays pre-mix

Note: Samourai Wallet developers (Keonne Rodriguez and William Hill) were arrested by the DOJ in April 2024. The wallet is still functional. See `raw/Theory/privacy/freesamourai.md`.

Source: `raw/Theory/privacy/coinjoin.md`

---

## BIP47 / PayNym

BIP47 introduces reusable payment codes. Alice generates a payment code; Bob generates a derived address for each payment from Alice using ECDH. This eliminates address reuse (a privacy leak) while enabling a recognizable "identity" (PayNym contact). Samourai Wallet implements this as **PayNym contacts**.

Source: `raw/Theory/privacy/bip47-the-ugly-duckling.md`

---

## Lightning and Privacy

Lightning offers better privacy than on-chain (payments are not publicly broadcast) but has issues:
- Public channel graph reveals node topology
- Routing nodes see payment paths they participate in
- Payment probing can map balances

Improvements: private (unannounced) channels, onion routing (already used in Lightning), Blinded Paths (BOLT12).

Source: `raw/Theory/lightning/lightning-privacy.md`

---

## Privacy Tools Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Acquisition | RoboSats, Hodl Hodl, Bisq | No-KYC BTC purchase |
| On-chain mixing | Whirlpool (Samourai) | CoinJoin to break history |
| Wallet backend | Dojo / RoninDojo | Self-hosted node so wallet doesn't leak to third-party server |
| Mobile OS | GrapheneOS | Hardened Android, no Google tracking |
| Self-hosted node | Bitcoin Core + Electrs | Verify your own blocks, no reliance on third-party nodes |
| Lightning | Phoenix, Mutiny | Self-custodial LN with LSP handling liquidity |

---

## Dojo (Self-Hosted Samourai Backend)

Dojo is the node backend for Samourai Wallet. Without it, Samourai's servers see your addresses and transaction history. With Dojo, your wallet connects to your own node — Samourai learns nothing.

**[[en/practice/privacy-practice|RoninDojo]]** = [[en/practice/privacy-practice|Dojo]] packaged for x86 hardware with GUI, Whirlpool integration, and Electrum Rust Server.

The Dojo series (7 parts, `raw/Practice/privacy/dojo/`) covers the complete setup.

Source: `raw/Practice/privacy/ronindojo.md`, `raw/Practice/privacy/dojo/`

---

## GrapheneOS

GrapheneOS is a hardened Android OS for Pixel phones. It removes Google Play Services, sandboxes apps, and hardens the OS against exploitation. Recommended for maximum privacy on mobile Bitcoin/Lightning use.

Source: `raw/Practice/privacy/grapheneos.md`

---

## Sources

*Synthesized from multiple sources in the `/raw/privacy` directory https://21ideas.org/privacy/. No single canonical source article.*

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/bitcoin|Bitcoin]] | [[en/concepts/utxo|UTXO]] | [[en/concepts/security|self-custody]] | [[en/concepts/lightning-network|Lightning Network]] | [[en/series/oxt-research|blockchain analysis]] | [[en/practice/privacy-practice|privacy practice]] | [[en/entities/cypherpunks|cypherpunks]] | [[en/practice/buying|no-KYC buying]]

## Related Pages

- [[en/concepts/bitcoin]]] — the public ledger
- [[en/concepts/lightning-network]]] — Lightning privacy
- [[en/entities/cypherpunks]]] — privacy as core value
- [[en/practice/privacy-practice]]] — practical setup guides
- [[en/history/blocksize-war]]] — politics of Bitcoin privacy decisions
