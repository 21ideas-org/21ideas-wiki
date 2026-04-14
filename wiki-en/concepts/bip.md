---
title: "BIP (Bitcoin Improvement Proposal)"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/izobretaem-bitkoin/glava-8", "https://21ideas.org/vojna-za-razmer-bloka/"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, protocol, governance, bip]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## What a BIP is

Changes to [[en/concepts/bitcoin-core|Bitcoin Core]] and the wider ecosystem go through an open process; [[en/books/inventing-bitcoin|*Inventing Bitcoin*]] names **Bitcoin Improvement Proposals (BIPs)** as the pathway for ideas — **reviewed in public**, with code and discussion visible to anyone.

A BIP is a **design document**, not law: [[en/concepts/bitcoin-node|nodes]] choose what software to run; **economic actors** decide what they call "bitcoin."

Source: [Inventing Bitcoin — Ch. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)

## Activation in practice (examples from the blocksize war material)

The sources describe **miner signaling thresholds** (e.g. **95%** of blocks in a difficulty period) used for several [[en/concepts/forks|soft forks]] before [[en/concepts/segwit|SegWit]] — including **BIP 66**, **BIP 65**, and the **BIP 68 / 112 / 113** bundle — and note that **imperfect activations** ([[en/concepts/mining|miners]] signaling without actually enforcing) caused short **chain splits** until the network converged.

**SegWit** activation politics led to **BIP 148** (UASF) — controversial because it risked **consensus divergence** if miners did not cooperate.

Source: [The Blocksize War](https://21ideas.org/vojna-za-razmer-bloka/)

## Relation to forks

[[en/concepts/forks|Soft forks]] are often specified and deployed with BIPs; **hard forks** may also be proposed as implementations (e.g. **BIP 101** / Bitcoin XT era), but require **every participant** to upgrade for a single chain — otherwise two assets emerge.

See [[en/concepts/forks|forks]] and [[en/concepts/governance|governance]].

## Sources

- [Inventing Bitcoin — Ch. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [The Blocksize War (book hub)](https://21ideas.org/vojna-za-razmer-bloka/)

## Related pages

- [[en/concepts/governance|Governance — who accepts proposed rule changes]]
- [[en/concepts/forks|Forks — soft vs hard forks and consensus splits]]
- [[en/history/blocksize-war|Blocksize War — political context of major BIP debates]]
- [[en/concepts/segwit|SegWit — major BIP-activated upgrade (2017)]]
- [[en/concepts/taproot|Taproot — later Schnorr/MAST soft fork bundle (2021)]]
