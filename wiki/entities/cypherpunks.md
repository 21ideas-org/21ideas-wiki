# Cypherpunks

*Tags: entity, movement, history, privacy, cryptography*

---

## What the Cypherpunks Were

The [[entities/cypherpunks|Cypherpunks]] were a loosely organized movement of cryptographers, programmers, and activists that formed in the early 1990s. Their thesis: cryptography could be used to protect individual [[concepts/privacy|privacy]] and freedom against state surveillance and control — and the best way to advance this was to *write code* rather than lobby politicians.

The mailing list (founded 1992 by Eric Hughes, Timothy May, and John Gilmore) was the primary forum. At peak it had thousands of subscribers including [[entities/satoshi-nakamoto|Satoshi Nakamoto]].

---

## Key Figures

| Person | Contribution |
|--------|-------------|
| Eric Hughes | Cypherpunk Manifesto (1993); mailing list co-founder |
| Timothy May | Crypto Anarchist Manifesto (1988/1992); "Cypherpunks write code" |
| John Gilmore | Co-founder; EFF co-founder |
| Philip Zimmermann | Created PGP (1991); the first mass-market encryption tool |
| David Chaum | eCash/DigiCash; blind signatures; the spiritual godfather |
| Adam Back | [[concepts/hashcash\|Hashcash]] (1997); Blockstream CEO |
| Wei Dai | b-money (1998) |
| Nick Szabo | Bit Gold, smart contracts |
| [[entities/hal-finney\|Hal Finney]] | PGP dev; RPOW; first Bitcoin recipient |
| [[entities/satoshi-nakamoto\|Satoshi Nakamoto]] | Bitcoin (synthesized cypherpunk ideas into working system) |

---

## The Cypherpunks Manifesto (Eric Hughes, 1993)

Key lines:
- "Privacy is necessary for an open society in the electronic age."
- "Privacy is not secrecy. A private matter is something one doesn't want the whole world to know, but a secret matter is something one doesn't want anybody to know. Privacy is the power to selectively reveal oneself to the world."
- "Cypherpunks write code. We know that someone has to write software to defend privacy, and since we can't get privacy unless we all do, we're going to write it."

Source: `raw/Theory/philosophy/cypherpunks-manifesto.md`

---

## The Crypto Anarchist Manifesto (Timothy May, 1988/1992)

Written in 1988, distributed at "Crypto 88" conference, published on the mailing list in 1992. May predicted:
- Cryptography will enable untraceable transactions and communications
- This will fundamentally undermine the state's ability to tax and regulate
- A new form of social order (crypto-anarchy) will emerge — not chaos, but voluntary cryptographic contracts

Bitcoin fulfilled this prediction. May died in 2018 — not long enough to see Bitcoin become a trillion-dollar asset, but long enough to see [[concepts/segwit|SegWit]].

Source: `raw/Theory/philosophy/crypto-anarchist-manifesto.md`

---

## "Libertaria in Cyberspace" (Timothy May, 1992)

Physical libertarian experiments (seasteading, special economic zones) fail because states can use physical force. Cyberspace is structurally different: no territory to invade, no bodies to coerce, cryptography enforces contracts. A libertarian polity in cyberspace is inherently more stable than any physical one.

Source: `raw/Theory/philosophy/libertaria-in-cyberspace.md`

---

## The Progression to Bitcoin

The cypherpunks tried repeatedly to build digital cash:

| Project | Year | Creator | Problem |
|---------|------|---------|---------|
| eCash / DigiCash | 1989 | David Chaum | Required trusted central mint; company went bankrupt |
| [[concepts/hashcash\|Hashcash]] | 1997 | Adam Back | Anti-spam [[concepts/proof-of-work\|PoW]]; non-transferable |
| b-money | 1998 | Wei Dai | Proposed but never implemented |
| Bit Gold | 1998–2005 | Nick Szabo | Required trusted timestamping service |
| RPOW | 2004 | Hal Finney | Transferable PoW tokens but required trusted server |
| **Bitcoin** | **2008** | **[[entities/satoshi-nakamoto\|Satoshi]]** | **Solved all prior problems** |

[[entities/satoshi-nakamoto|Satoshi Nakamoto]] explicitly cited Hashcash (Back) and b-money (Dai) in the whitepaper.

---

## PGP: The First Victory

PGP (Pretty Good Privacy), created by Philip Zimmermann in 1991, was the first practical mass-market encryption tool. Zimmermann was investigated criminally by the US government for exporting cryptography (then regulated as a munition). The case was eventually dropped — a key cypherpunk victory establishing that encryption was speech, not a weapon.

This fight over encryption policy is the direct ancestor of today's debates over Bitcoin and financial privacy.

Source: `raw/Practice/security/pgp.md`

---

## Related Terms

[[glossary|Glossary]] | [[concepts/privacy|privacy]] | [[concepts/proof-of-work|Proof of Work]] | [[concepts/bitcoin|Bitcoin]] | [[entities/satoshi-nakamoto|Satoshi Nakamoto]] | [[entities/hal-finney|Hal Finney]] | [[entities/nick-szabo|Nick Szabo]] | [[history/pre-bitcoin-cypherpunks|pre-Bitcoin era]]

## Related Pages

- [[entities/satoshi-nakamoto]] — the culmination of the movement
- [[entities/hal-finney]] — the bridge from cypherpunks to Bitcoin
- [[entities/nick-szabo]] — Bit Gold and theoretical foundations
- [[series/genesis-files]] — detailed history of each precursor
- [[history/pre-bitcoin-cypherpunks]] — the full prehistory
- [[philosophy/overview]] — cypherpunk ideas in the sources
