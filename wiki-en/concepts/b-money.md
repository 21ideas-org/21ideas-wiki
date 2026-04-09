---
title: "b-money"
category: concepts
quality: reference
sources:
  - "https://21ideas.org/gf/genesis-3"
  - "https://21ideas.org/whitepaper"
synthesized_date: "2026-04-09"
completeness: high
language: en
tags: [bitcoin, wiki, b-money, history, cypherpunks, digital-cash, proof-of-work]
---

# b-money

**b-money** is Wei Dai’s 1998 proposal for a cryptography-based money and contract system discussed in the cypherpunk milieu. In the 21ideas framing, it is one of the closest “first drafts” of Bitcoin’s basic pattern: pseudonymous keys, signed messages, and a shared ledger — but with critical gaps in practicality and consensus.

## What b-money tried to achieve

Genesis Files Part III emphasizes Dai’s motivation: enabling online cooperation (money + contracts) among pseudonymous participants, resistant to regulation-by-violence.

This goal overlaps with Bitcoin’s later “don’t trust, verify” posture and the attempt to remove privileged intermediaries.

## Two designs (version 1 and version 2)

Per `raw/Theory/history/genesis-files/genesis-3.md`, Dai described two variants.

### Version 1: everyone keeps the ledger

In the first proposal:

- every participant keeps their own copy of the ledger,
- transfers are broadcast as signed messages,
- identities are public keys (not legal names).

The source notes why this sounds familiar: it resembles a key intuition behind Bitcoin’s public verification model.

### Version 2: “servers” keep the ledger

Dai’s second version introduces specialized ledger-keeping “servers” connected via a broadcast network. Regular users verify transactions against a subset of servers, and servers post bonds for incentives/penalties.

In 21ideas’ telling, this starts to resemble later ideas where ledger power concentrates, creating new trust and governance problems.

## What b-money did not solve (per the sources)

The Genesis Files article explains why b-money was not a complete practical system:

- the design assumed network/broadcast properties that did not scale well,
- double-spend prevention and robust consensus were not concretely solved in the first design,
- the “server” model introduces a different trust surface,
- money creation required participants to agree on the “cost” of computations, a fragile requirement in an adversarial world.

This is why 21ideas treats b-money as conceptually close but not sufficient.

## Why it matters for Bitcoin history

Two connections are highlighted:

- b-money is explicitly cited in the Bitcoin whitepaper (as emphasized by the 21ideas whitepaper page).
- it illustrates the pre-Bitcoin design space: many pieces existed, but the robust decentralized double-spend solution was missing.

See [[en/concepts/double-spend]] and [[en/concepts/byzantine-generals-problem]].

---

## Sources

- [Genesis Files, Part III: b-money (Wei Dai)](https://21ideas.org/gf/genesis-3)
- [Bitcoin Whitepaper (21ideas page)](https://21ideas.org/whitepaper)

---

## Related Terms

[[en/glossary|Glossary]] | [[en/entities/cypherpunks|cypherpunks]] | [[en/concepts/double-spend|double spend]] | [[en/concepts/proof-of-work|Proof of Work]] | [[en/concepts/decentralization|decentralization]] | [[en/concepts/third-parties|third parties]]

## Related Pages

- [[en/concepts/bit-gold]] — another near-miss predecessor in the Genesis Files framing
- [[en/concepts/rpow]] — a working prototype that still relied on a central server
- [[en/concepts/double-spend]] — the problem b-money did not robustly solve
- [[en/concepts/bitcoin-whitepaper]] — whitepaper context and citations
