---
title: "Quantum computing and Bitcoin security (Scott Aaronson AMA)"
category: "topics"
quality: "synthesized"
sources: ["https://stacker.news/items/1477913/"]
synthesized_date: "2026-04-24"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, security, synthesized]
reviewed: "2026-04-24"
---

This page distills Scott Aaronson’s AMA on what quantum computers can and can’t do, and what that implies for Bitcoin’s cryptography and long-run security posture.

## The big misconception: “quantum tries all answers in parallel”

Quantum computers don’t “branch into many universes and try everything.” The core mechanism is **interference among amplitudes**: quantum algorithms are designed so that wrong answers’ amplitudes cancel out while the right answer’s amplitude is reinforced. This can yield dramatic speedups, but only for problems with very specific mathematical structure.

## What quantum computers actually speed up

The AMA highlights a narrow set of problem classes where quantum speedups are known and meaningful:

- **Simulating quantum systems**: a “native hardware” advantage for chemistry / materials simulation.
- **Breaking public-key cryptography**: Shor’s algorithm can factor integers and solve discrete log in polynomial time, breaking RSA / Diffie-Hellman / elliptic-curve schemes.
- **Unstructured search**: Grover’s algorithm gives a quadratic speedup (useful but not “magic”).

## What quantum computers probably won’t speed up (despite hype)

Aaronson is skeptical of broad claims like “quantum will revolutionize machine learning” or “quantum will revolutionize optimization” absent a specific algorithm that beats the best classical approach. He also treats “quantum AI” discourse as often hype-heavy and misrepresentative.

## The Bitcoin / cryptography threat — what’s actually at risk

Bitcoin’s signature scheme (ECDSA on secp256k1) is the central public-key component discussed. In the AMA framing:

- A sufficiently capable quantum computer could, in principle, recover a private key from an exposed public key (via Shor-type discrete-log attacks).
- The “distance” to that capability is primarily engineering (fault-tolerant scale), not a known scientific impossibility.

## Symmetric crypto (AES) is different

Grover’s algorithm yields only a quadratic speedup against symmetric primitives. The AMA’s practical takeaway is that this is an engineering problem with a standard mitigation: increase key sizes (e.g., AES-256).

## Post-quantum cryptography (PQC)

The AMA notes that leading PQC candidates (notably lattice-based families) have been studied for decades and are “battle-tested” relative to their age, with the general caveat that practical cryptography rests on unproven hardness assumptions.

## Hardware realities and fault tolerance

Multiple qubit platforms exist (superconducting, trapped ions, neutral atoms) with different tradeoffs. The AMA emphasizes that fault tolerance is no longer the main theoretical blocker; scaling remains the hard engineering challenge.

## Calibration: when to be skeptical

Signals the AMA treats as red flags:

- Claims of quantum “revolutionizing” fields without naming an algorithm that beats the best classical baseline
- Claims that AES is “broken” (rather than “effective security is reduced; increase key size”)
- Claims that fault tolerance is still an unsolved theoretical problem (as opposed to engineering scale-up)

## Sources

- https://stacker.news/items/1477913/

## Related pages

- [[en/concepts/bitcoin|Bitcoin]]
- [[en/concepts/security|Security]]
- [[en/glossary#Cryptography|Cryptography]]
- [[en/glossary#Encryption|Encryption]]
