---
title: "Scott Aaronson's Quantum Computing AMA"
author: "Scott Aaronson"
url: "https://stacker.news/items/1477913/"
source_domain: "stacker.news"
category: "theory/security"
language: "en"
tags: [quantum-computing, cryptography, bitcoin, ecdsa, secp256k1, shor, grover, post-quantum-cryptography]
---

_Distilled from Scott Aaronson's AMA (quantum computing theorist, UT Austin)_

---

## The Big Misconception

**Quantum computers do not "try all answers in parallel."**

This is the most pervasive and damaging misconception. The intuition of a machine that splits into a thousand copies of itself and races down every path simultaneously is simply wrong — and it leads to completely wrong expectations about what QCs are useful for.

The actual mechanism is **interference among amplitudes**. Quantum mechanics replaces ordinary probabilities with complex numbers called _amplitudes_. Unlike probabilities, which can only add, amplitudes can cancel each other out — like waves. Every quantum algorithm is an attempt to _choreograph_ this interference so that:

- Wrong answers cancel each other out (their amplitudes interfere destructively)
- The right answer reinforces itself (its amplitude interferes constructively)

This is an extraordinarily specific hammer. It doesn't work on arbitrary problems — only on problems with the right mathematical structure to exploit interference.

[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477510) to `@StillStackinAfterAllTheseYears` 

> _"quantum speedup is an incredibly special phenomenon that hinges on the way quantum mechanics changes the rules of probability themselves"_

---

## What Quantum Computers Actually Speed Up

Genuine, world-changing quantum speedups are known for only a narrow set of problem classes:

### 1. Simulating Quantum Mechanics Itself

The original and most natural application — proposed by Richard Feynman in 1981. Quantum systems are exponentially hard to simulate on classical computers. A quantum computer is, in a sense, the native hardware for the job.

**Why it matters:** Better simulations of quantum chemistry and materials science could enable:

- New drug discovery
- Better solar cells and batteries
- High-temperature superconductors
- Simulations relevant to high-energy physics and cosmology

This is Aaronson's personal #1 application. He considers it the _born purpose_ of quantum computing.

[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477531) to `@Scoresby`

> _"Simulating quantum mechanics is the big one, frankly"_

### 2. Breaking Public-Key Cryptography

Peter Shor's 1994 discovery: a quantum algorithm that can factor large integers (and solve discrete logarithm problems) in polynomial time — exponentially faster than any known classical algorithm.

**What this breaks:**

- RSA
- Diffie-Hellman key exchange
- Elliptic curve cryptography (including secp256k1, used by Bitcoin)

**What this does NOT break:** Symmetric cryptography like AES — see below.

[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477552) to `@jimmysong` (fault tolerance question)

> _"Bitcoin now looks vulnerable to systems with only ~30,000 physical qubits"_

### 3. Grover's Algorithm (Quadratic Speedup for Search)

Grover's algorithm solves a surprisingly general problem: searching through _n_ items for a desired one. It achieves a **quadratic** speedup — turning an _n_-step search into a √n-step search.

**Important nuance:** Quadratic is useful but not revolutionary. It doesn't break AES; it just halves the effective key length. AES-128 becomes roughly equivalent to AES-64 under Grover — the fix is simply to use AES-256. It's a manageable engineering response, not a catastrophic break.

[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477560) to `@SimpleStacker`

> _"the speedup is 'merely' quadratic"_

---

## What Quantum Computers Probably Won't Speed Up

- **Training LLMs / machine learning:** No known quantum algorithm provides meaningful speedup here. Quantum AI articles are, in Aaronson's words, full of "enormous amounts of misrepresentation and hype" — typically failing to compare against the best available classical solutions.
- **General optimization:** Not a solved case. The "QC will revolutionize optimization" claim is unsupported by known algorithms.
- **Everyday computing:** Email, apps, browsing, games — no quantum speedup applies. There is no reason to ever want a quantum computer at home.


[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477515) to `@k00b` (`@Space_Child67`'s question about LLMs)

> _"articles you'll find on 'quantum AI' tend to contain ENORMOUS amounts of misrepresentation and hype"_

---

## The Bitcoin / Cryptography Threat — Unpacked

### What's actually at risk

Bitcoin's elliptic curve signature scheme (secp256k1 / ECDSA) is directly vulnerable to Shor's algorithm. A sufficiently powerful quantum computer could derive a private key from an exposed public key.

### How far away is this?

As of the AMA, a recent advance reduced the estimated overhead for fault-tolerant quantum factoring such that Bitcoin becomes vulnerable with approximately **~30,000 physical qubits** — significantly fewer than earlier estimates. However, today's best machines are nowhere near fault-tolerant at that scale. What remains is engineering, not science — but that's a meaningful distinction: it means there are no known fundamental blockers, only hard problems of execution.

### Symmetric crypto (AES) is a different story

AES is not broken by quantum computers the way RSA and elliptic curve are. Grover's algorithm provides only a quadratic speedup. The fix — doubling key length to AES-256 — is straightforward and already standardized.

[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477482) to `@0xbitcoiner`

> _"we could just switch to AES256 and have as much security as before"_

### Post-quantum cryptography

Lattice-based cryptographic schemes (the leading candidates for post-quantum standards) have now been "battle-tested" for roughly 25 years — not drastically less than RSA/elliptic curve's ~50 years. The "no proofs" concern applies equally to all practical cryptography: _no_ cryptosystem in common use has a formal security proof. They all rest on unproven hardness conjectures (at minimum, P ≠ NP).

[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477559) to `@Lobotomite`

> _"lattice problems have been battle tested for ~25 years"_

---

## Hardware Realities

### Multiple physical platforms exist

The leading qubit technologies — superconducting qubits, trapped ions, and neutral atoms — are different in important ways, but Aaronson treats them as differences in _prefactors_, not fundamental scaling differences. Fault-tolerance should ultimately work in all of them.

**Key tradeoff:** Superconducting qubits are fast but fixed in a 2D grid. Trapped-ion and neutral-atom qubits are ~1000x slower at gate operations but can be physically moved — enabling flexible, all-to-all connectivity. This is a major practical advantage for the latter.

### Fault tolerance is no longer the theoretical blocker

After 30 years of engineering, sub-threshold error rates have been demonstrated in trapped ions, neutral atoms, and superconducting qubits. The skeptics' prediction — that correlated errors would prevent fault-tolerance from working — has been empirically falsified. The remaining work is scaling up, which is an engineering challenge, not a scientific unknown. Aaronson compares the current state to nuclear weapons development circa 1942.

[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477489) to `@k00b` (`@south_korea_ln` 2 question about qubit platforms)

> _"superconducting qubits are fixed in place on a 2D grid, whereas with trapped-ion and neutral atom qubits you can pick them up and move them around"_

---

## Speedup Classes — A Quick Map

|Problem|Speedup Type|Example|
|---|---|---|
|Periodic function / factoring|Exponential|Shor's algorithm|
|Unstructured search|Quadratic|Grover's algorithm|
|Quantum simulation|Exponential|Feynman's original vision|
|Parity of n bits|None (factor of 2 at most)|Proven lower bound|
|LLM training / general ML|Unknown / likely none|Active research, heavy hype|

---

## Calibration: When to Be Skeptical

- Any claim that QC will "revolutionize" machine learning, logistics, or finance without citing a specific quantum algorithm that outperforms the best classical solution → **likely hype**
- Any claim that symmetric encryption (AES) is "broken" by quantum computers → **wrong**
- Any claim that fault-tolerance is an unsolved theoretical problem → **outdated** (it's an engineering problem now)
- Any claim that all qubit platforms are equally viable or equally limited → **oversimplified**
- Any article on "quantum AI" that doesn't compare against best classical baselines → **almost certainly misleading**

---

## If Quantum Computing Turned Out To Be Impossible...

This would be _more_ scientifically significant than if it works. It would imply that quantum mechanics itself is wrong or incomplete — the biggest revolution in physics in a century. The conservative, boring position is that QC is possible and will eventually break current public-key cryptography. If QC fails, something far stranger is true about the universe.

---

## Tools for Hands-On Exploration

For those who want to experiment: **Qiskit**, **PennyLane**, and **Q#** are the main platforms. Try them and use whichever feels most natural — there's no strong theoretical reason to prefer one over another for learning purposes.

[Reply](https://stacker.news/items/1477467/r/Tony?commentId=1477516) to `@k00b` (`@south_korea_ln` 5 question)

> _"try Qiskit, Pennylane, Q#"_

---

_Note: A few questions in the AMA went unanswered (power requirements for a cryptographically relevant QC; quantum money practicality; specific engineering milestones that would compress the Bitcoin threat timeline). These remain open based on this source._
