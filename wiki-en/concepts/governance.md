---
title: "Bitcoin Governance"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/kto-kontroliruet-bitkoin-kor/", "https://21ideas.org/upravlenie-bitcoin/"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, governance, protocol, bip]
updated: "2026-04-07"
reviewed: "2026-04-14"
---

## No One Controls Bitcoin

Bitcoin has no CEO, no board, no company, no foundation with authority over the protocol. Changes require broad consensus across multiple independent groups, each with veto power:

| Group | Role | Veto Power |
|-------|------|-----------|
| **[[en/concepts/bitcoin-node\|Full nodes]]** | Enforce consensus rules; reject invalid blocks | Yes — simply don't upgrade |
| **[[en/concepts/mining\|Miners]]** | Produce blocks; signal readiness for soft forks | Yes — can refuse to mine upgraded blocks |
| **Developers** | Write [[en/concepts/bitcoin-core\|Bitcoin Core]] code; propose [[en/concepts/bip\|BIPs]] | No unilateral power; anyone can fork Core |
| **Users/HODLers** | Choose which chain/software to use | Strongest veto — economic majority determines chain value |
| **Exchanges/Businesses** | Indicate which chain they'll support | Economic signal only |

Source: [Who Controls Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/) (Jameson Lopp), [Bitcoin Governance](https://21ideas.org/upravlenie-bitcoin/) (Pierre Rochard)

## Bitcoin Improvement Proposals (BIPs)

Changes are proposed as [[en/concepts/bip|BIP]]s (Bitcoin Improvement Proposals) — public documents specifying technical changes. Anyone can write a BIP. Adoption requires:
1. Developer review and refinement
2. Implementation in [[en/concepts/bitcoin-core|Bitcoin Core]]
3. Miner signaling (for soft forks) or node adoption
4. Actual upgrade by full nodes

Examples:
- BIP39: seed phrase standard
- BIP141: SegWit (soft fork, 2017)
- BIP340-342: Taproot (soft fork, 2021)
- BIP47: PayNym payment codes

## Soft Forks vs. Hard Forks

**[[en/concepts/forks|Soft fork]]:** New rules are backward-compatible. Non-upgraded nodes still accept blocks from upgraded nodes. [[en/concepts/segwit|SegWit]] and [[en/concepts/taproot|Taproot]] were soft forks.

**[[en/concepts/forks|Hard fork]]:** New rules break backward compatibility. The chain splits unless all nodes upgrade simultaneously. Hard forks require near-universal consensus — practically impossible in Bitcoin without extraordinary circumstances.

The [[en/history/blocksize-war|blocksize war]] (2015–2017) was largely a dispute over whether to implement a hard fork for larger blocks. Small blockers won; SegWit (soft fork) was the solution. See [[en/history/blocksize-war]].

## User-Activated Soft Fork (UASF)

BIP148 (UASF) was a remarkable demonstration of user power. In 2017, when miners were stalling [[en/concepts/segwit|SegWit]] activation, a coalition of [[en/concepts/bitcoin-node|full node]] operators announced they would enforce SegWit rules starting August 1, 2017 — regardless of miner signaling. The economic threat of miners being on a chain that the economic majority rejected forced miner capitulation.

This established a key precedent: **full nodes (not miners) are the ultimate arbiters of Bitcoin's rules.**

Source: [[en/history/blocksize-war]], [[en/books/blocksize-war|The Blocksize War]]

## Bitcoin Core Is Not Bitcoin

[[en/concepts/bitcoin-core|Bitcoin Core]] is the most widely used implementation, but it is not Bitcoin. Anyone can run an alternative implementation (Bitcoin Knots, btcd) or fork Core. The rules of Bitcoin are what all nodes agree to run — not what any single implementation says.

Jameson Lopp: "Bitcoin Core contributors have zero control over the Bitcoin network. They can only propose changes; users decide whether to adopt them."

Source: [Who Controls Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/)

## The 21M Cap Is Non-Negotiable

The 21 million supply cap is the most sacred rule. Changing it would require convincing every bitcoin holder that they benefit from inflation — which is economically incoherent for anyone who holds BTC as a store of value. It has never been seriously proposed and has never changed.

## Sources

- [Who Controls Bitcoin Core?](https://21ideas.org/kto-kontroliruet-bitkoin-kor/) — Jameson Lopp
- [Bitcoin Governance](https://21ideas.org/upravlenie-bitcoin/) — Pierre Rochard

## Related pages

- [[en/concepts/bitcoin|Bitcoin — the system governed this way]]
- [[en/concepts/scarcity|21M cap — the most important rule]]
- [[en/concepts/forks|Forks explained]]
- [[en/history/blocksize-war|Blocksize War — the greatest governance test]]
- [[en/practice/running-a-node|Running a node — how you personally enforce the rules you believe in]]
- [[en/entities/satoshi-nakamoto|Satoshi Nakamoto — the governance problem he solved by disappearing]]
- [[en/books/blocksize-war|The Blocksize War — book on the 2015–2017 governance crisis]]
