---
title: "BIP (Bitcoin Improvement Proposal)"
category: concepts
tags: [bitcoin, wiki, protocol, governance, upgrades]
language: en
quality: reference
sources:
  - "https://21ideas.org/izobretaem-bitkoin/glava-8"
  - "https://21ideas.org/vojna-za-razmer-bloka/"
synthesized_date: "2026-04-09"
completeness: high
---

# BIP (Bitcoin Improvement Proposal)

*Tags: standards process, soft fork activation*

---

## What a BIP is

Changes to **Bitcoin Core** and the wider ecosystem go through an open process; *Inventing Bitcoin* names **Bitcoin Improvement Proposals (BIPs)** as the pathway for ideas — **reviewed in public**, with code and discussion visible to anyone.

A BIP is a **design document**, not law: **nodes choose** what software to run; **economic actors** decide what they call “bitcoin.”

Source: `raw/Books/izobretaem-bitkoin/glava-8.md`

---

## Activation in practice (examples from the blocksize war material)

The sources describe **miner signaling thresholds** (e.g. **95%** of blocks in a difficulty period) used for several soft forks before **SegWit** — including **BIP 66**, **BIP 65**, and the **BIP 68 / 112 / 113** bundle — and note that **imperfect activations** (miners signaling without actually enforcing) caused short **chain splits** until the network converged.

**SegWit** activation politics led to **BIP 148** (UASF) as a user-driven pressure mechanism — controversial because it risked **consensus divergence** if miners did not cooperate.

Sources: `raw/Books/vojna-za-razmer-bloka/glava-5.md`, `raw/Books/vojna-za-razmer-bloka/glava-17.md`

---

## Relation to forks

**Soft forks** are often specified and deployed with BIPs; **hard forks** may also be proposed as implementations (e.g. **BIP 101** / Bitcoin XT era), but require **every participant** to upgrade for a single chain — otherwise two assets emerge.

See [[en/concepts/forks]] and [[en/concepts/governance]].

---

## Sources

- [Inventing Bitcoin — Ch. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [The Blocksize War (book hub)](https://21ideas.org/vojna-za-razmer-bloka/)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/concepts/governance|governance]] | [[en/concepts/forks|forks]] | [[en/concepts/segwit|SegWit]] | [[en/concepts/taproot|Taproot]]

## Related Pages

- [[en/concepts/governance]] — who accepts rule changes
- [[en/concepts/forks]] — soft vs hard forks
- [[en/history/blocksize-war]] — political context of BIP debates
- [[en/concepts/segwit]] — major BIP-era upgrade
- [[en/concepts/taproot]] — later soft fork bundle
