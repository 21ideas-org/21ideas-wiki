---
title: "AML (Anti-Money Laundering) in Bitcoin"
category: concepts
quality: reference
sources: []
synthesized_date: "2026-04-09"
completeness: high
language: en
tags: [bitcoin, wiki, aml, kyc, privacy, fungibility, censorship, third-parties, surveillance]
---

# AML (Anti-Money Laundering) in Bitcoin

In the 21ideas sources, “AML” (anti-money laundering) around Bitcoin is framed less as a neutral compliance topic and more as a **third-party risk + surveillance pipeline**: it pushes users into KYC, funds chain-analysis firms, and enables custodians to block or confiscate under vague “risk score” narratives.

This page summarizes that framing from `raw/Theory/privacy/aml.md`.

## What AML means in practice (per the source)

The source describes AML as a bundle of procedures (often paired with **KYC**) justified as fighting money laundering. In practice, it shows up for Bitcoin users primarily through:

- Exchange deposit screening
- “Risk scoring” of addresses/UTXOs by private analytics firms
- Account freezes and demands for personal documents

This links directly to the broader problem of [[en/concepts/third-parties|trusted third parties]]: if your money lives behind an account, you can be censored.

## “Dirty bitcoins” as a narrative

The article argues that “dirty bitcoins” is largely a narrative built to sell paid checks and normalize surveillance, while:

- Different chain-analysis companies can disagree substantially.
- Methods are not transparent or independently auditable.
- “Cleanliness” thresholds are set privately by custodians and can change.

The practical implication is that “buying an AML check” is buying **someone’s opinion** about risk — not a guarantee.

## Why this is dangerous for Bitcoin users

The source highlights several harms:

- **Custodial censorship**: centralized services can freeze deposits and demand KYC.
- **Privacy loss**: AML checks encourage users to disclose sensitive data and transaction history.
- **Fungibility erosion**: “taint” narratives split money into “acceptable” vs “unacceptable” coins.

These concerns connect to:

- [[en/concepts/privacy]] — privacy as a requirement for freedom, not a luxury
- [[en/concepts/censorship-resistance]] — censorship shifts to chokepoints (custodians)
- [[en/concepts/third-parties]] — intermediaries as security holes

## Defensive posture suggested by the source

The article’s practical conclusion is to avoid the AML/KYC trap by:

- avoiding services that use these procedures when possible,
- using P2P / circular economy paths,
- treating AML scoring as non-objective and not a legitimate basis for “freezing” funds.

---

## Sources

- *No canonical 21ideas.org URL was present in the raw file metadata for this article in the repository.*
- Source used for synthesis: `raw/Theory/privacy/aml.md`

---

## Related Terms

[[en/glossary|Glossary]] | KYC | [[en/concepts/privacy|privacy]] | [[en/concepts/security|security]] | [[en/concepts/third-parties|third parties]] | [[en/concepts/censorship-resistance|censorship resistance]]

## Related Pages

- [[en/concepts/third-parties]] — why custodians become censorable chokepoints
- [[en/concepts/privacy]] — why chain surveillance undermines freedom and safety
- [[en/concepts/security]] — operational safety: custody choices and threat models
