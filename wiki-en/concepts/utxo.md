---
title: "UTXOs (Unspent Transaction Outputs)"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/protocol/utxo-1/", "https://21ideas.org/protocol/utxo-2/", "https://21ideas.org/protocol/utxo-3/"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, utxo]
updated: "2026-04-07"
reviewed: "2026-04-14"
---

## What a UTXO Is

Bitcoin has no accounts and no balances in the traditional sense. Instead, the ledger tracks **Unspent Transaction Outputs (UTXOs)** — discrete chunks of bitcoin that have been created by a transaction output and not yet spent.

Your "balance" is simply the sum of all UTXOs that your private keys can spend.

Source: [UTXO — Part 1](https://21ideas.org/protocol/utxo-1/)

## How Transactions Work

**Inputs** consume existing UTXOs; **outputs** create new UTXOs.

Example: Alice has a 0.5 BTC UTXO and wants to send 0.3 BTC to Bob.
1. Alice creates a transaction with her 0.5 BTC UTXO as input
2. Output 1: 0.3 BTC → Bob's address
3. Output 2: 0.19999 BTC → Alice's change address (she gets back the remainder, minus fee)
4. The 0.5 BTC UTXO is consumed; two new UTXOs (0.3 and 0.19999) are created

The UTXO set = all currently unspent outputs. Every [[en/concepts/bitcoin-node|full node]] maintains this set to validate new transactions.

Source: [UTXO — Part 2](https://21ideas.org/protocol/utxo-2/)

## Why UTXOs Matter for Privacy

The UTXO model has important privacy implications:

**Address reuse is bad:** If Alice always uses the same address, analysts can track all her UTXOs together.

**Change addresses:** The change output going back to Alice reveals which of the two outputs is "hers" to analysts — defeating some [[en/concepts/privacy|privacy]].

**CIOH (Common Input Ownership Heuristic):** Multiple inputs in one transaction likely come from the same wallet — allowing address clustering. See [[en/series/oxt-research|blockchain analysis]] for how this is exploited.

**UTXO management:** Thoughtfully combining (or not combining) UTXOs affects [[en/concepts/privacy|privacy]]. Poor UTXO management can link previously separate coin histories.

See [[en/concepts/privacy|privacy countermeasures]] for how to address these risks.

## Coin Control

Coin control is the ability to manually select which UTXOs to use as inputs in a transaction. Important for:
- Avoiding mixing [[en/concepts/aml|KYC]] and no-KYC coins (which reveals the no-KYC address to the KYC cluster)
- Preserving [[en/concepts/privacy|privacy]] by not combining outputs from unrelated origins
- Managing UTXO sizes (avoid dust)

Wallets with coin control: Electrum, Sparrow Wallet, Samourai.

## UTXO Set and Full Node Validation

Every Bitcoin [[en/concepts/bitcoin-node|full node]] maintains the complete UTXO set (~5–6 GB as of 2024). When validating a new transaction, the node checks:
- The input UTXOs exist in the UTXO set
- The signatures are valid for those UTXOs
- The total output ≤ total input (no new coins created)

This is Bitcoin's trustless validation — no need to trust anyone, the math checks out.

Source: [UTXO — Part 3](https://21ideas.org/protocol/utxo-3/)

## Lightning Channels as UTXOs

A Lightning channel is a single 2-of-2 [[en/concepts/multisig|multisig]] UTXO on-chain. The entire channel balance lives in one UTXO; off-chain commitment transactions determine the split between parties. Closing a channel creates one or two UTXOs (one per party).

This is why [[en/concepts/lightning-network|Lightning]] is efficient: thousands of off-chain payments settle to a single on-chain UTXO pair.

## Sources

- [UTXO — Part 1](https://21ideas.org/protocol/utxo-1/)
- [UTXO — Part 2](https://21ideas.org/protocol/utxo-2/)
- [UTXO — Part 3](https://21ideas.org/protocol/utxo-3/)

## Related pages

- [[en/concepts/bitcoin|Bitcoin — the system built on UTXOs]]
- [[en/concepts/privacy|Privacy — UTXO management and privacy countermeasures]]
- [[en/concepts/lightning-network|Lightning Network — channels are single on-chain UTXOs]]
- [[en/concepts/multisig|Multisig — Lightning channels use 2-of-2 multisig UTXOs]]
- [[en/concepts/segwit|SegWit — changes how UTXOs store witness data]]
- [[en/concepts/address-types|Address Types — address types link to UTXO spending conditions]]
- [[en/concepts/bitcoin-node|Bitcoin Node — full nodes maintain the complete UTXO set]]
- [[en/series/oxt-research|OXT Research — blockchain analysis using UTXO heuristics]]
