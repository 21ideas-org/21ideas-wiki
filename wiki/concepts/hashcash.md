# Hashcash

*Tags: protocol, proof-of-work, cypherpunks, precursor, anti-spam*

---

## What It Is

Hashcash is a [[concepts/proof-of-work|Proof of Work]] algorithm invented by Adam Back in 1997 as an anti-spam mechanism. To send an email, a sender must compute a hash of the email header that starts with N leading zeros — a computation that requires real CPU time but can be verified instantly by the recipient.

The key insight: **unforgeable costliness**. A token that requires real work to produce cannot be counterfeited or inflated. Each email stamp costs a fraction of a second for a human, but becomes catastrophically expensive for spammers sending millions of emails.

Source: [[series/genesis-files]] (Part 2), `raw/Theory/protocol/proof-of-work.md`

---

## The Key Limitation

Hashcash tokens are **single-use and non-transferable**. A Hashcash stamp proves work was done, but it cannot be passed from person to person as money. It has no "ownership" concept — just proof of expenditure.

This was the fundamental limitation separating Hashcash from digital cash. [[entities/hal-finney|Hal Finney]] partially solved this with [[concepts/proof-of-work|RPOW]] (Reusable Proofs of Work) in 2004, but RPOW required a trusted server. [[entities/satoshi-nakamoto|Satoshi Nakamoto]] completed the solution: the Bitcoin blockchain replaces the trusted server with distributed consensus.

---

## Satoshi's Adaptation

Satoshi cited Hashcash directly in the Bitcoin whitepaper. He adapted the mechanism from anti-spam to money:

| Hashcash (1997) | Bitcoin Mining |
|-----------------|----------------|
| Hash email header | Hash block header + nonce |
| N leading zeros required | Difficulty target (leading zeros) |
| One-time proof | Extends blockchain |
| Spent once (anti-spam) | Creates new coins (block reward) |
| No transfer | [[concepts/utxo|UTXO]] model enables transfer |

---

## Why It Matters

Hashcash established the principle that **energy expenditure can create unforgeable digital tokens**. This is the theoretical foundation for Bitcoin's [[concepts/scarcity|scarcity]]: the tokens are valuable precisely because they required real resources to produce — like gold, but in digital form. [[entities/nick-szabo|Nick Szabo]] developed this idea further in his "Shelling Out" and "Bit Gold" work.

---

## Related Terms

[[glossary|Glossary]] | [[concepts/proof-of-work|Proof of Work]] | [[concepts/mining|mining]] | [[concepts/scarcity|scarcity]] | [[entities/satoshi-nakamoto|Satoshi Nakamoto]] | [[entities/hal-finney|Hal Finney]] | [[entities/cypherpunks|cypherpunks]] | [[series/genesis-files|Genesis Files]]

## Related Pages

- [[concepts/proof-of-work]] — the mechanism Hashcash pioneered
- [[entities/cypherpunks]] — the movement that produced Hashcash
- [[series/genesis-files]] — Hashcash as Bitcoin precursor (Part 2)
- [[history/pre-bitcoin-cypherpunks]] — Hashcash in historical context
