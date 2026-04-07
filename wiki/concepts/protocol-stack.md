---
title: "Bitcoin Protocol Stack"
category: concepts
tags: [bitcoin, wiki, protocol, architecture, layers, lightning]
source: "Synthesized from raw/ sources + glossary"
updated: "2026-04-07"
---

# Bitcoin Protocol Stack

*Tags: protocol, architecture, layers, lightning, script, P2P*

---

Bitcoin is not a single monolithic protocol — it is a layered stack. Each layer builds on the guarantees of the layer below it, trading security and decentralization for speed, scalability, and expressiveness as you move upward. Understanding the stack explains why Bitcoin can be simultaneously slow and uncensorable at the base, and instant and cheap at the application layer.

See also: [[concepts/bitcoin]], [[concepts/utxo]], [[concepts/segwit]], [[concepts/taproot]], [[concepts/lightning-network]], [[concepts/mining]], [[concepts/proof-of-work]]

---

## Layer 0: The Network (P2P Gossip)

The foundation is a peer-to-peer network of approximately 15,000–20,000 publicly reachable nodes (many more exist but do not accept inbound connections).

**What it does:**
- Propagates transactions and blocks across the globe
- Uses a gossip protocol: each node relays new transactions and blocks to its peers, who relay to their peers
- No central server or coordinator; any node can join or leave
- IPv4, IPv6, Tor (onion routing), and I2P are all supported transport layers

**Key properties:**
- **Censorship resistance**: No single entity can block a transaction from propagating globally
- **Redundancy**: Thousands of independent nodes; no single point of failure
- **Privacy**: Tor support hides the originating IP address of transactions

**Tradeoff**: Gossip propagation takes seconds to reach global consensus on which transactions have been seen. This is not a problem at Layer 0 — confirmation happens at Layer 1.

---

## Layer 1: The Base Chain (Blockchain + Consensus + UTXO)

Layer 1 is the settlement layer. It provides Bitcoin's core security guarantees: immutability, scarcity, and final settlement.

**What it does:**
- Organizes transactions into blocks linked by cryptographic hashes (the "blockchain")
- Uses [[concepts/proof-of-work]] (via [[concepts/mining]]) to make block production expensive and rewriting history computationally prohibitive
- Maintains the global [[concepts/utxo|UTXO set]] — the definitive record of who owns what
- Enforces the 21 million coin supply cap and the halving schedule (see [[concepts/scarcity]])
- Full nodes each independently validate every transaction and block; consensus emerges from this distributed validation

**Key protocols:**
- SHA-256 double hash for block hashing
- Nakamoto consensus (longest chain with most accumulated proof-of-work wins)
- Block interval: ~10 minutes
- Block size: ~1–4 MB (weight units after [[concepts/segwit]])

**Tradeoffs:**
- **Security**: Extremely high — rewriting recent history requires controlling >50% of global hash rate
- **Decentralization**: ~15,000+ full nodes; anyone with a laptop and 650GB of disk can participate
- **Throughput**: ~7 transactions/second (base); not designed for high-volume payments
- **Finality**: Probabilistic (more confirmations = more security); 6 confirmations (~1 hour) is conventional for large payments

Layer 1 optimizes for trust minimization and decentralization above all else. Speed and scale are explicitly not its job.

---

## Layer 1.5: Script (Bitcoin's Programming Language)

Between the base chain and the application layer sits Bitcoin Script — a stack-based, intentionally limited programming language that defines spending conditions for each [[concepts/utxo|UTXO]].

**What it does:**
- Every UTXO has a locking script (scriptPubKey) defining how it can be spent
- A spending transaction provides an unlocking script (scriptSig / witness) that satisfies the locking conditions
- Script enables complex conditions: multisig, time locks, hash preimage reveals, and more

**Key upgrades:**
- **[[concepts/segwit]]** (2017): Moved the witness (signature) data out of the transaction body, fixing transaction malleability and enabling the Lightning Network
- **[[concepts/taproot]] / MAST** (2021): Taproot adds Schnorr signatures (enabling MuSig2 key aggregation) and MAST (Merkelized Abstract Syntax Trees), which allows complex multi-path spending conditions to be committed in a single hash. Only the executed spending path is revealed on-chain — unused conditions remain private.

**Tradeoff**: Bitcoin Script is deliberately not Turing-complete. There are no loops, no unbounded execution, no persistent state across transactions. This is intentional: it makes Script analyzable, prevents denial-of-service attacks, and keeps full node validation tractable. Smart contracts requiring richer computation happen on Layer 2 or above.

---

## Layer 2: Lightning Network

[[concepts/lightning-network|Lightning]] is a payment channel network built on top of Layer 1. It enables instant, high-volume, low-fee payments by moving the bulk of transactions off-chain.

**What it does:**
- Two parties open a payment channel by locking bitcoin in a 2-of-2 multisig UTXO on-chain
- They can then exchange an unlimited number of off-chain payment updates, each cryptographically signed
- HTLCs (Hashed Time-Lock Contracts) route payments across multiple channels without trust
- Either party can close the channel at any time, settling the final balance on-chain

**Key properties:**
- **Speed**: Payments settle in milliseconds (no waiting for block confirmation)
- **Cost**: Near-zero fees (fractions of a satoshi)
- **Privacy**: Payments are not recorded on-chain; routing nodes see only adjacent hops
- **Capacity**: Theoretically unlimited transactions/second; constrained only by liquidity and routing topology

**Tradeoffs:**
- Both parties must be online (or have a watchtower) to detect and respond to cheating
- Inbound liquidity must be pre-provisioned; you can only receive up to the inbound capacity of your channels
- Routing failures occur when no path with sufficient liquidity exists between sender and receiver
- Not suited for large payments relative to channel capacity; optimized for frequent small payments

**Standards**: BOLT (Basis of Lightning Technology) — the specification suite. Major implementations: LND (Go), CLN (C), Eclair (Scala), LDK (Rust library).

---

## Layer 3: Applications

The application layer abstracts away the complexity of the layers below. Most users interact with Bitcoin exclusively through Layer 3.

**What it does:**
- **Wallets**: Key management, address derivation, PSBT construction, hardware wallet integration (Sparrow, Nunchuk, BlueWallet, Phoenix, Muun)
- **Exchanges**: On/off ramps between fiat and bitcoin (custodial and non-custodial)
- **BTCPay Server**: Self-hosted, open-source payment processor; accepts on-chain and Lightning payments without a third party
- **LNbits**: Layer on top of Lightning for point-of-sale apps, vouchers, wallets-within-wallets
- **Nostr**: Decentralized social protocol with native Lightning payment integration (zaps)
- **Mining pools**: Coordinate hashing work across many miners, distribute block rewards proportionally

**Tradeoffs:**
- Applications can be custodial or non-custodial; custodial apps trade self-sovereignty for convenience
- The diversity of applications means different security assumptions apply at each product layer

---

## Why Layering Is the Right Architecture

Bitcoin's critics frequently attack the base layer for being slow (7 TPS) or expensive (high on-chain fees during congestion). This misunderstands the design intentionally.

**The base layer's job is to be the hardest money to censor and the hardest to fake settlement on.** Every byte on Layer 1 is validated by every full node on Earth, permanently. This is maximally expensive to produce. You cannot have unlimited throughput and that level of security simultaneously.

**Upper layers trade some trust for scale.** Lightning requires watching for cheating (trust in your own availability, or a watchtower). Applications may require trusting a server. But these trust assumptions are bounded, recoverable, and opt-in — and the base layer always provides the final backstop.

This mirrors other successful layered systems:
- TCP/IP (reliable transport) → HTTP (documents) → TLS (security) → Web applications
- Physical cash (base settlement) → Commercial bank credit → Card networks → Payment apps

The correct analogy for Lightning is not "Bitcoin is slow, but Lightning is fast." It is: Layer 1 is the clearinghouse; Lightning is the payment rail. You do not pay your grocery bill by moving gold bars between vaults. You settle the underlying gold obligation periodically and run a credit layer on top.

---

## Stack Summary Table

| Layer | Name | Speed | Trust | Scale |
|-------|------|-------|-------|-------|
| 0 | P2P Network | Seconds (propagation) | Trustless | Global |
| 1 | Base Chain | ~10 min/block | Trustless | ~7 TPS |
| 1.5 | Script/Taproot | Same as L1 | Trustless | Same as L1 |
| 2 | Lightning | Milliseconds | Near-trustless | Millions TPS |
| 3 | Applications | Varies | Varies | Unlimited |

---

## Related Terms

- **HTLC** (Hashed Time-Lock Contract) — Lightning's atomic routing primitive
- **BOLT** (Basis of Lightning Technology) — Lightning protocol specifications
- **MAST** (Merkelized Abstract Syntax Trees) — Taproot script efficiency mechanism
- **Witness** — Transaction data moved off the main block body by SegWit
- **Gossip protocol** — P2P message propagation mechanism

---

## Related Pages

- [[concepts/bitcoin]] — foundational overview
- [[concepts/utxo]] — the UTXO accounting model at Layer 1
- [[concepts/segwit]] — the 2017 upgrade enabling Lightning
- [[concepts/taproot]] — Schnorr and MAST at Layer 1.5
- [[concepts/lightning-network]] — detailed Lightning coverage
- [[concepts/mining]] — Layer 1 consensus mechanism
- [[concepts/proof-of-work]] — the security primitive underlying Layer 1
