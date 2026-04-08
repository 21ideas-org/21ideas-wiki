---
title: "OXT Research: Understanding Bitcoin Privacy"
category: series
tags: [bitcoin, wiki, series, privacy, blockchain-analysis]
updated: "2026-04-07"
quality: synthesized
sources: ["https://21ideas.org/privacy/oxt-1", "https://21ideas.org/privacy/oxt-2", "https://21ideas.org/privacy/oxt-3", "https://21ideas.org/privacy/oxt-4"]
synthesized_date: "2026-04-07"
completeness: high
---

# OXT Research: Understanding Bitcoin Privacy

*Authors: Samourai Wallet team (TDevD and others) | Parts: 4 | Source: `raw/Theory/privacy/oxt/` | Tags: series, privacy, blockchain-analysis, chain-surveillance*

---

## Overview

A 4-part series written by the developers of Samourai Wallet explaining [[series/oxt-research|blockchain analysis]] from the attacker's perspective — so that Bitcoin users can understand and defeat it. Also available as a video playlist.

The series represents the deepest treatment of Bitcoin privacy in the 21ideas.org library. Understanding the attacker's view is the foundation of meaningful privacy practice.

> "The reality of Bitcoin privacy... is somewhere between complete anonymity and complete traceability." — Part 1

Source files: `oxt-1.md` through `oxt-4.md`

---

## Part 1: Blockchain Analysis and Transaction Privacy

**Core claim:** Bitcoin is *not anonymous* — it is *pseudonymous*. The common belief in 2011 that Bitcoin offered "anonymous payments" was dangerous and incorrect. Blockchain data is permanent; surveillance capabilities in 2011 were minimal but have since become sophisticated law enforcement tools.

**What blockchain analysis is:**
- Examination of the public transaction graph to identify patterns, link addresses, and attribute transactions to real-world entities
- Used by: law enforcement, chain analysis firms (Chainalysis, Elliptic), exchanges (for compliance), governments
- Enables: linking KYC-exchange withdrawals to subsequent transactions, identifying when coins from different sources are combined, building probabilistic identity clusters

**Key insight from Part 1:** The blockchain is *forever*. Surveillance capabilities are *increasing*. Privacy choices made today affect the interpretability of past and future transactions.

---

## Part 2: Key Concepts of Chain Analysis

### CIOH (Common Input Ownership Heuristic)

The most powerful [[series/oxt-research|blockchain analysis]] heuristic: **if multiple [[concepts/utxo|UTXO]]s appear in the same transaction, they likely come from the same wallet.**

Why: to spend multiple UTXOs, you must provide signatures for each — which requires controlling all the corresponding private keys. Standard wallets only have one user's keys.

**Consequence:** An analyst seeing UTXOs A, B, C combined in one transaction infers A, B, C belong to the same entity. If A was identified (via KYC or other means), B and C are now also identified — even if they came from separate, previously unlinked sources.

**[[concepts/privacy|CoinJoin]] defeats CIOH:** When 5 users combine inputs in a single transaction with equal outputs, the CIOH cannot determine which input belongs to which user.

### Change Detection

When a transaction has two outputs and one is a round number while the other is an odd change amount, analysts infer which is change and which is payment. Additional heuristics:
- Address type consistency (change often returns to same address type as input)
- Address reuse (if you've received to an address before, a second output to that address is likely change)
- Round number bias

**Defense:** Use equal-output CoinJoin (Whirlpool), avoid address reuse, use coin control.

### Transaction Graph Analysis

Following the flow of funds through multiple hops. Even after N transactions, if coin history can be traced back to an identified source, the current UTXO is "tainted."

---

## Part 3: Defenses Against Chain Analysis

The third part provides the practical defensive toolkit:

**[[concepts/privacy|CoinJoin]] ([[practice/privacy-practice|Whirlpool]]):**
- Equal-output transactions break CIOH and make input-output linking impossible
- 5 parties in, 5 equal outputs out → analyst cannot determine which input paid which output
- "Toxic change" concept: the unequal pre-mix change retains prior history; treat separately from post-mix coins

**Address reuse avoidance:**
- Using a fresh address for each receive breaks the clustering analysts rely on
- BIP47 / PayNym provides a reusable "identity" that generates unique per-sender addresses (ECDH-derived)

**UTXO management / coin control:**
- Manually selecting which UTXOs to spend prevents accidentally mixing KYC and no-KYC coins
- Cross-contamination: combining a KYC UTXO with a no-KYC UTXO in one transaction links them permanently via CIOH

**Running your own node:**
- Wallet queries to third-party servers reveal your address set
- Connect to your own Dojo/Electrum server to eliminate this leak

---

## Part 4: Applying Chain Analysis Concepts to Improve Privacy

The final part is practical: applying the attack model to real transaction histories to identify and remediate privacy leaks.

**Steps:**
1. Analyze your own transaction history using OXT.me (the block explorer by Samourai)
2. Identify: address reuse, CIOH violations (UTXOs you combined), timing correlations
3. Remediate: use Whirlpool to break history on coins you want to protect
4. Plan future: coin control, fresh addresses, no-KYC acquisition going forward

**The OXT.me Tool:** A blockchain visualization and analysis tool built by the Samourai team. Allows transaction graph visualization, entity clustering, and privacy scoring of your own transactions.

---

## Significance

This series establishes that:
1. Bitcoin privacy is not free — it requires deliberate action
2. The tools to compromise privacy are widely deployed and improving
3. The tools to protect privacy (CoinJoin, coin control, self-hosted nodes, BIP47) are available but require effort
4. Past transactions are permanent — remediation is possible but not retroactive

The OXT Research series is the analytical foundation for the privacy practice guides in [[practice/privacy-practice]].

*Note: Samourai Wallet developers (Keonne Rodriguez and William Hill) were arrested by the DOJ in April 2024. The OXT research and Whirlpool tools remain, though the ecosystem is under pressure.*

---

## Sources

- [Part 1 — Blockchain Analysis and Transaction Privacy](https://21ideas.org/privacy/oxt-1)
- [Part 2 — Key Concepts of Chain Analysis](https://21ideas.org/privacy/oxt-2)
- [Part 3 — Defenses Against Chain Analysis](https://21ideas.org/privacy/oxt-3)
- [Part 4 — Applying Chain Analysis Concepts](https://21ideas.org/privacy/oxt-4)

---

## Related Terms

[[glossary|Glossary]] | [[concepts/privacy|privacy]] | [[concepts/utxo|UTXO]] | [[practice/privacy-practice|privacy practice]] | [[practice/buying|no-KYC buying]] | [[entities/cypherpunks|cypherpunks]] | [[concepts/bitcoin|Bitcoin]]

## Related Pages

- [[concepts/privacy]] — the privacy concept page
- [[practice/privacy-practice]] — practical implementation
- [[concepts/utxo]] — UTXO management for privacy
- [[entities/cypherpunks]] — why privacy matters
