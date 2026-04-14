---
title: "b-money"
category: "concepts"
quality: "reference"
sources: ["https://21ideas.org/gf/genesis-3", "https://21ideas.org/whitepaper"]
synthesized_date: "2026-04-09"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, history, protocol, security, whitepaper, double-spend]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

**b-money** is Wei Dai’s 1998 proposal for cryptography-based [[en/concepts/money|money]] and [[en/glossary#Smart contract|contracts]] in the [[en/entities/cypherpunks|cypherpunk]] milieu. In the 21ideas framing ([*Genesis Files*, Part III](https://21ideas.org/gf/genesis-3)), it is one of the closest “first drafts” of [[en/concepts/bitcoin|Bitcoin]]’s basic pattern: pseudonymous [[en/glossary#Public key|keys]], signed messages, and a shared [[en/glossary#Ledger|ledger]] — but with critical gaps in practicality and [[en/glossary#Nakamoto Consensus|consensus]].

## What b-money tried to achieve

[Genesis Files, Part III](https://21ideas.org/gf/genesis-3) emphasizes Dai’s motivation: enabling online cooperation ([[en/concepts/money|money]] + [[en/glossary#Smart contract|contracts]]) among pseudonymous participants, resistant to regulation-by-violence.

This goal overlaps with Bitcoin’s later “don’t trust, verify” posture and the attempt to remove [[en/concepts/third-parties|privileged intermediaries]].

## Two designs (version 1 and version 2)

According to [Genesis Files, Part III](https://21ideas.org/gf/genesis-3), Dai described two variants.

### Version 1: everyone keeps the ledger

In the first proposal:

- every participant keeps their own copy of the [[en/glossary#Ledger|ledger]],
- transfers are broadcast as signed messages,
- identities are [[en/glossary#Public key|public keys]] (not legal names).

The source notes why this sounds familiar: it resembles a key intuition behind Bitcoin’s public verification model.

### Version 2: “servers” keep the ledger

Dai’s second version introduces specialized ledger-keeping “servers” connected via a broadcast network. Regular users verify transactions against a subset of servers, and servers post bonds for incentives/penalties.

In 21ideas’ telling, this starts to resemble later ideas where ledger power concentrates, creating new trust and [[en/concepts/governance|governance]] problems.

## What b-money did not solve (per the sources)

The Genesis Files article explains why b-money was not a complete practical system:

- the design assumed network/broadcast properties that did not scale well,
- [[en/concepts/double-spend|double-spend]] prevention and robust consensus were not concretely solved in the first design,
- the “server” model introduces a different trust surface,
- money creation required participants to agree on the “cost” of computations (including [[en/concepts/proof-of-work|Proof of Work]]), a fragile requirement in an adversarial world.

This is why 21ideas treats b-money as conceptually close but not sufficient.

## Why it matters for Bitcoin history

Two connections are highlighted:

- b-money is explicitly cited in the [[en/concepts/bitcoin-whitepaper|Bitcoin whitepaper]] (as emphasized by the [21ideas whitepaper page](https://21ideas.org/whitepaper)).
- it illustrates the pre-Bitcoin design space: many pieces existed, but the robust [[en/concepts/decentralization|decentralized]] double-spend solution was missing.

See [[en/concepts/double-spend|double spend]] and [[en/concepts/byzantine-generals-problem|Byzantine Generals Problem]].

## Sources

- [Genesis Files, Part III: b-money (Wei Dai)](https://21ideas.org/gf/genesis-3)
- [Bitcoin Whitepaper (21ideas page)](https://21ideas.org/whitepaper)

## Related pages

- [[en/concepts/bit-gold|Bit gold — near-miss predecessor in the Genesis Files framing]]
- [[en/concepts/hashcash|Hashcash — the Proof of Work primitive b-money referenced]]
- [[en/concepts/rpow|RPOW — working prototype that still relied on a central server]]
- [[en/concepts/double-spend|Double spend — the problem b-money did not robustly solve]]
- [[en/concepts/bitcoin-whitepaper|Bitcoin whitepaper — cites b-money directly]]
- [[en/series/genesis-files|Genesis Files — the series where 21ideas covers b-money (Part III)]]
- [[en/entities/cypherpunks|Cypherpunks — the milieu in which b-money was proposed]]
