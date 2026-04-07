# Bitcoin Governance

*Tags: governance, decentralization, protocol, consensus*

---

## No One Controls Bitcoin

Bitcoin has no CEO, no board, no company, no foundation with authority over the protocol. Changes require broad consensus across multiple independent groups, each with veto power:

| Group | Role | Veto Power |
|-------|------|-----------|
| **Full nodes** | Enforce consensus rules; reject invalid blocks | Yes — simply don't upgrade |
| **Miners** | Produce blocks; signal readiness for soft forks | Yes — can refuse to mine upgraded blocks |
| **Developers** | Write Bitcoin Core code; propose changes (BIPs) | No unilateral power; anyone can fork Core |
| **Users/HODLers** | Choose which chain/software to use | Strongest veto — economic majority determines chain value |
| **Exchanges/Businesses** | Indicate which chain they'll support | Economic signal only |

Source: `raw/Theory/protocol/bitcoin-governance.md` (Pierre Rochard), `raw/Theory/protocol/who-controls-bitcoin-core.md` (Jameson Lopp)

---

## Bitcoin Improvement Proposals (BIPs)

Changes are proposed as BIPs (Bitcoin Improvement Proposals) — public documents specifying technical changes. Anyone can write a BIP. Adoption requires:
1. Developer review and refinement
2. Implementation in Bitcoin Core
3. Miner signaling (for soft forks) or node adoption
4. Actual upgrade by full nodes

Examples:
- BIP39: seed phrase standard
- BIP141: SegWit (soft fork, 2017)
- BIP340-342: Taproot (soft fork, 2021)
- BIP47: PayNym payment codes

---

## Soft Forks vs. Hard Forks

**Soft fork:** New rules are backward-compatible. Non-upgraded nodes still accept blocks from upgraded nodes. SegWit and Taproot were soft forks.

**Hard fork:** New rules break backward compatibility. The chain splits unless all nodes upgrade simultaneously. Hard forks require near-universal consensus — practically impossible in Bitcoin without extraordinary circumstances.

The blocksize war (2015-2017) was largely a dispute over whether to implement a hard fork for larger blocks. Small blockers won; SegWit (soft fork) was the solution. See [[history/blocksize-war]].

---

## User-Activated Soft Fork (UASF)

BIP148 (UASF) was a remarkable demonstration of user power. In 2017, when miners were stalling SegWit activation, a coalition of full node operators announced they would enforce SegWit rules starting August 1, 2017 — regardless of miner signaling. The economic threat of miners being on a chain that the economic majority rejected forced miner capitulation.

This established a key precedent: **full nodes (not miners) are the ultimate arbiters of Bitcoin's rules.**

Source: [[history/blocksize-war]], `raw/Books/vojna-za-razmer-bloka/`

---

## Bitcoin Core Is Not Bitcoin

Bitcoin Core is the most widely used implementation, but it is not Bitcoin. Anyone can run an alternative implementation (Bitcoin Knots, btcd) or fork Core. The rules of Bitcoin are what all nodes agree to run — not what any single implementation says.

Jameson Lopp: "Bitcoin Core contributors have zero control over the Bitcoin network. They can only propose changes; users decide whether to adopt them."

---

## The 21M Cap Is Non-Negotiable

The 21 million supply cap is the most sacred rule. Changing it would require convincing every bitcoin holder that they benefit from inflation — which is economically incoherent for anyone who holds BTC as a store of value. It has never been seriously proposed and has never changed.

Source: `raw/Theory/protocol/21-million-is-non-negotiable.md`

---

## Related Pages

- [[concepts/bitcoin]] — the system governed this way
- [[concepts/scarcity]] — the most important rule
- [[history/blocksize-war]] — the greatest governance test
- [[entities/satoshi-nakamoto]] — the governance problem he solved by disappearing
