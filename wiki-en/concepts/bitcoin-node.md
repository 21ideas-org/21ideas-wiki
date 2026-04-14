---
title: "Bitcoin Node"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/practice/bitcoin-node/", "https://21ideas.org/izobretaem-bitkoin/glava-8", "https://21ideas.org/izobretaem-bitkoin/glava-2"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, node, privacy, decentralization]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## What a Bitcoin node is

A **Bitcoin node** is a computer running Bitcoin software that participates in the peer-to-peer network: it relays transactions and blocks, keeps itself in sync, and (for full nodes) verifies that everything follows Bitcoin's [[en/concepts/governance|consensus rules]].

## Two key roles: relay and rules enforcement

The practice article distinguishes what nodes do in the system:

- **Networking:** nodes broadcast and relay transactions / blocks so the system converges.
- **Validation:** full nodes download blocks and verify every transaction against consensus rules. Invalid blocks are rejected automatically.

This is why nodes matter politically: running your own node is framed as the practical form of "don't trust, verify."

## Full nodes vs light clients (SPV)

The same source contrasts:

- **Full node:** verifies everything; holds the chain; enforces rules locally.
- **Light / SPV client:** can verify inclusion but does not validate the full history; cheaper to run but weaker trust model.

## How nodes remove third parties

[[en/books/inventing-bitcoin|*Inventing Bitcoin*]] frames legacy systems as centralized ledgers ("banks are just ledgers"). A node is the way individuals can hold a copy of the ledger and verify reality without outsourcing trust to [[en/concepts/third-parties|third parties]] such as explorers, custodians, or payment processors.

Source: [Inventing Bitcoin — Ch. 2](https://21ideas.org/izobretaem-bitkoin/glava-2)

## Nodes, Bitcoin Core, and rule changes

*Inventing Bitcoin* explains that many implementations exist; the most common is [[en/concepts/bitcoin-core|Bitcoin Core]]. But nodes are the actual enforcement layer: [[en/concepts/mining|miners]] produce blocks, while nodes decide whether those blocks are valid under the rules they run.

See [[en/concepts/bitcoin-core|Bitcoin Core]] and [[en/concepts/governance|governance]].

## Sources

- [Why you should run your own Bitcoin node](https://21ideas.org/practice/bitcoin-node/)
- [Inventing Bitcoin — Ch. 8](https://21ideas.org/izobretaem-bitkoin/glava-8)
- [Inventing Bitcoin — Ch. 2](https://21ideas.org/izobretaem-bitkoin/glava-2)

## Related pages

- [[en/concepts/bitcoin-core|Bitcoin Core — the most common node implementation]]
- [[en/concepts/governance|Governance — who sets rules in practice]]
- [[en/concepts/third-parties|Third parties — why outsourcing validation introduces TTP risk]]
- [[en/concepts/censorship-resistance|Censorship resistance — why distributed nodes matter]]
- [[en/concepts/decentralization|Decentralization — nodes as the enforcement layer of distributed consensus]]
- [[en/practice/running-a-node|Running a node — hands-on guidance for running your own node]]
