# Mining

*Tags: mining, SHA256, PoW, hash-rate, difficulty, nonce, ASIC*

---

## What Mining Is

Bitcoin mining is the process of:
1. Collecting pending transactions from the mempool into a candidate block
2. Finding a valid Proof of Work hash for that block
3. Broadcasting the valid block to the network
4. Receiving the block reward (new bitcoin subsidy + transaction fees)

Mining simultaneously: confirms transactions, secures the network, and issues new bitcoin on a predetermined schedule.

Source: `raw/Theory/protocol/mining-walkthrough.md` (Arman The Parman / Bitcoin Magazine), `raw/Books/izobretaem-bitkoin/glava-4.md`

---

## SHA-256: The Hash Function

Bitcoin uses the **SHA-256** (Secure Hash Algorithm, 256-bit) hash function. Properties:

- **Fixed output size:** Any input → always a 256-bit (64 hex character) output
- **Deterministic:** Same input always produces the same output
- **Avalanche effect:** Tiny input change → completely different output
- **One-way:** Cannot reverse a hash to find its input
- **Collision resistant:** No two different inputs produce the same output (in practice)

Bitcoin actually applies SHA-256 *twice* (SHA-256d) for block hashing.

Example: SHA-256("1") = `6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b`

---

## The Nonce and the Mining Process

A block header contains:
- Previous block hash
- Merkle root of transactions
- Timestamp
- Difficulty target
- **Nonce** (a 32-bit number that miners vary)

**The mining loop:**
1. Construct a candidate block
2. Hash the block header with SHA-256d
3. Check if the hash is below the difficulty target (starts with enough zeros)
4. If not: increment the nonce and try again
5. If yes: broadcast the valid block and collect the reward

A valid hash looks like:
```
00000000000000000002fca...
```
The required number of leading zeros is determined by the difficulty target.

**How many attempts?** At Bitcoin's current difficulty, miners must try trillions of nonces per second before finding a valid hash. This is intentional — it makes finding a block expensive and finding a fake history impossibly expensive.

---

## Difficulty Adjustment

Every **2,016 blocks** (~2 weeks), all nodes independently recalculate the difficulty target:

```
new_target = old_target × (actual_time / 1,209,600 seconds)
```

Where 1,209,600 seconds = 2 weeks (the ideal time for 2,016 blocks at 10 minutes each).

**If blocks came fast** (miners joined): target decreases → harder to find valid hashes → slower blocks.
**If blocks came slow** (miners left): target increases → easier to find valid hashes → faster blocks.

The adjustment always seeks the ~10-minute average. This makes Bitcoin's block schedule remarkably stable despite massive swings in hash rate (e.g., the 2021 China mining ban cut global hash rate by ~50% overnight — difficulty adjusted down within 2 weeks and hash rate recovered).

---

## Hash Rate

Hash rate = number of SHA-256d hashes a miner (or the network) can perform per second.

| Unit | Hashes/second |
|------|--------------|
| 1 TH/s (terahash) | 10¹² |
| 1 EH/s (exahash) | 10¹⁸ |

Bitcoin network hash rate as of 2024: ~500–700 EH/s. A single modern ASIC miner produces ~100–200 TH/s.

---

## ASIC Miners

**ASIC (Application-Specific Integrated Circuit):** Chips designed exclusively to compute SHA-256 hashes. Far more efficient than CPUs or GPUs for this task.

Key ASICs:
- Antminer S19 XP: ~140 TH/s, ~3,000W
- Whatsminer M50S: ~126 TH/s, ~3,276W

ASICs made GPU mining obsolete for Bitcoin around 2013. The specialization of ASICs is a deliberate feature: ASICs require significant capital investment and cannot be easily repurposed, raising the cost of a 51% attack.

---

## Mining Pools

Solo mining at current difficulty would take an individual miner thousands of years to find a block. Mining pools combine hash rate and share rewards proportionally. Pools smooth income variance but introduce some centralization concerns.

**Top pools by hash rate share (approximate, varies):** Foundry USA, AntPool, ViaBTC, F2Pool.

Pool centralization is watched carefully — if any pool approaches 50% of hash rate, the community notices and miners shift voluntarily.

---

## The Block Reward

Block reward = **block subsidy + transaction fees**.

| Halving epoch | Subsidy |
|---------------|---------|
| 2009-2012 | 50 BTC |
| 2012-2016 | 25 BTC |
| 2016-2020 | 12.5 BTC |
| 2020-2024 | 6.25 BTC |
| 2024-2028 | 3.125 BTC |

After the subsidy reaches zero (~2140), miners are compensated entirely by transaction fees. The sources argue this is sufficient for network security — as Bitcoin adoption grows, fee revenue will increase even as the subsidy drops. See [[concepts/scarcity]].

---

## Energy and Environment

Bitcoin mining consumes significant energy — this is intentional (PoW security requires cost). Key arguments from the sources:

1. **Stranded energy:** Mining is location-independent, so miners move to wherever energy is cheapest — often excess renewable energy that would otherwise be curtailed
2. **Comparison:** Fiat monetary system (banks, central banks, mints, military for petrodollar) consumes far more energy
3. **Jevons Paradox:** Energy efficiency improvements tend to increase total energy consumption — not unique to Bitcoin
4. **Incentive for renewables:** Bitcoin miners create demand for cheap, stranded renewable energy, potentially accelerating renewable deployment

Source: `raw/Theory/economics/bitcoin-is-not-harmful-for-the-environment.md`, [[series/gradually-then-suddenly]] Part 4.

---

## Related Pages

- [[concepts/proof-of-work]] — the underlying mechanism
- [[concepts/scarcity]] — mining as the issuance mechanism
- [[concepts/bitcoin]] — the system mining secures
- [[glossary]] — ASIC, nonce, hash rate, mining pool, block reward defined
