# Lightning Network

*Tags: layer-2, payments, scalability, lightning*

---

## What It Is

The Lightning Network (LN) is a Layer 2 payment protocol built on top of Bitcoin. It enables near-instant, low-fee micropayments without recording every transaction on the blockchain. Two parties open a payment channel by locking BTC in a multisig UTXO on-chain; they can then exchange unlimited signed commitment transactions off-chain; they settle to the blockchain only when closing the channel.

Multi-hop routing uses **HTLC (Hash Time Lock Contracts)** to enable payments between parties who don't share a direct channel, without either party needing to trust the intermediary routers.

Sources: `raw/Theory/lightning/`, `raw/Practice/lightning/`

---

## Why It Exists

Bitcoin's base layer processes ~7 transactions per second. Global payment volume (Visa, etc.) is tens of thousands per second. The base layer is intentionally slow and expensive — it prioritizes security and decentralization over throughput. Lightning adds throughput at a higher layer without changing Bitcoin's base rules.

SegWit (2017) was the prerequisite: it fixed transaction malleability, which was required for Lightning's commitment transaction scheme to work. Lightning was designed alongside SegWit.

---

## How Payment Channels Work

1. Alice and Bob create a 2-of-2 multisig address and both sign a funding transaction (on-chain)
2. They exchange signed "commitment transactions" — each reflects the current channel balance
3. Any payment between them updates the commitment; old commitments are invalidated by sharing private revocation keys
4. Either party can broadcast their latest commitment to settle on-chain at any time
5. Cheating (broadcasting an old commitment) is punished: the other party can sweep all channel funds using a revocation key

---

## Routing and HTLC

When Alice wants to pay Carol through Bob:
1. Carol generates a hash of a random secret (the **payment hash**)
2. Alice sends Bob an HTLC: "Pay Carol 1000 sats if you reveal the preimage of this hash within 24 hours"
3. Bob forwards it to Carol; Carol reveals the preimage, receives funds; Bob learns the preimage, receives his share from Alice

If routing fails, HTLCs expire and funds return — no loss.

---

## Inbound Liquidity Problem

A new Lightning node has no inbound capacity — it can send payments but not receive them. Solutions:
- Loop In (submarine swaps): convert on-chain BTC to inbound capacity
- Lightning Pool (Lightning Labs): buy channels from routing nodes
- Receive a channel from another node (social/marketplace)
- Phoenix Wallet (ACINQ) handles this automatically via splicing

Source: `raw/Theory/lightning/inbound-liquidity-problem.md`

---

## Centralization Concerns

Critics argue Lightning hubs create a centralized hub-and-spoke topology. The sources counter:
- Anyone can be a routing node; there is no permission required
- The routing topology is market-driven; the best routes attract flow
- Lightning does not change Bitcoin's base-layer properties
- Centralized hubs, if they emerge, are still censorship-resistant at the base layer

Source: `raw/Theory/lightning/is-lightning-centralized.md`

---

## Lightning Privacy

Lightning offers better privacy than on-chain (payments are not publicly broadcast), but has its own issues:
- The channel graph is partially public (announcing channels reveals node topology)
- Routing nodes learn sender/receiver information for payments they route
- Payment probes can map the network and infer balances

Using private (unannounced) channels and routing-node-aware wallets (Phoenix, Mutiny) improves privacy.

Source: `raw/Theory/lightning/lightning-privacy.md`

---

## Key Tools and Wallets

| Tool | Type | Key Feature |
|------|------|-------------|
| Phoenix | Self-custodial mobile | ACINQ LSP, automatic channel management, splicing, BOLT12 |
| Mutiny | Web/browser wallet | LSP liquidity, Nostr integration |
| LNbits | Self-hosted account system | Plugins: shop, tipjar, Lightning address, LNURL |
| Alby | Browser extension | WebLN, Nostr signing, Lightning Address, NWC |
| ZapGram | Telegram bot | Lightning tips via Telegram |
| ZapPlanner | Scheduling tool | Recurring Lightning payments |

See [[practice/lightning-tools]] for setup guides.

---

## Value-for-Value

Lightning enables a new model for creator monetization: value-for-value. Instead of platforms taking a cut (YouTube, Spotify), listeners/readers pay creators directly via Lightning micropayments — "streaming sats." The Nostr protocol + Alby browser extension makes this seamless. Podcasting 2.0 uses this model.

Source: `raw/Theory/philosophy/freedom-of-value.md`

---

## Related Pages

- [[concepts/bitcoin]] — the base layer
- [[concepts/utxo]] — channels are UTXOs
- [[concepts/privacy]] — Lightning privacy considerations
- [[practice/lightning-tools]] — practical tools
- [[entities/gigi]] — value-for-value philosophy
