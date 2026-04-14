---
title: "Running a Bitcoin Node"
category: "practice"
quality: "synthesized"
sources: []
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, node, privacy, synthesized]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

Running a full [[en/concepts/bitcoin-node|Bitcoin Node]] means independently downloading, verifying, and storing the complete [[en/concepts/blockchain|blockchain]]. Your node validates every transaction and every block since the genesis block using nothing but the Bitcoin protocol rules — no third party required. It is the deepest form of Bitcoin self-sovereignty: you verify the rules of the system you are trusting.

See also: [[en/concepts/governance|Bitcoin Governance]], [[en/concepts/privacy|Privacy]], [[en/concepts/bitcoin|Bitcoin]], [[en/practice/storage|Storage & Self-Custody]], [[en/practice/privacy-practice|Privacy in Practice]]

## Why Run a Node?

### You Validate Your Own Transactions

When you use a hosted wallet or a light client (SPV wallet) connected to a third-party server, you are trusting that server to tell you the truth about the state of the blockchain. The server could lie about confirmations, show you false balances, or censor your transactions.

A full node validates everything itself: every transaction, every block, every signature, every supply total. When your node says you have a confirmed transaction, you know — without trusting anyone — that the Bitcoin network has accepted it.

### You Enforce Your Own Rules

Bitcoin has no central authority. The protocol rules are enforced collectively by the full nodes on the network. When you run a node, you:

- Reject invalid blocks (including blocks from miners attempting to inflate the supply)
- Reject transactions that violate consensus rules
- Cast a "vote" for the version of Bitcoin you choose to run

During the [[en/history/blocksize-war|The Blocksize War (2015-2017)]], user-run full nodes were the decisive factor. When miners and major businesses attempted to force through a [[en/glossary#hard-fork|hard fork]] (SegWit2x), the economic nodes — users running their own nodes — rejected it. The miners had to back down. This demonstrated that node operators, not miners, are the ultimate arbiters of Bitcoin's rules. See [[en/concepts/governance|Bitcoin Governance]].

### Privacy: Your Addresses Stay Private

Light wallets query third-party servers (Electrum servers, Blockchain.info, etc.) with your addresses to check balances and transaction history. This means:

- The server learns your complete transaction history and balance
- The server can correlate your addresses, link them to your IP address, and sell or leak that data
- State-level surveillance can compel or compromise these servers

When you connect your wallet (Sparrow, Electrum, BlueWallet) to your own node, your address data never leaves your local network. See [[en/practice/privacy-practice|Privacy in Practice]] for the full privacy stack.

## Hardware Options

Running a node does not require specialized hardware. The main constraint is storage (the full blockchain) and memory (for validation).

### Raspberry Pi 4 (Minimal Setup)

The most popular beginner setup:
- **Hardware**: Raspberry Pi 4 (4GB or 8GB RAM) + 1TB or 2TB SSD (external USB)
- **Cost**: ~$100–150
- **Pros**: Low power (~5W), quiet, can run 24/7, dedicated device
- **Cons**: ARM processor is slower for initial sync; USB SSD is a potential bottleneck

Use a quality SSD (Samsung T7, WD My Passport) — cheap flash drives will corrupt and fail.

### Old Laptop or Desktop

Often the easiest path if you have spare hardware:
- Any machine from the last 10 years with 8GB+ RAM and a spare 1TB+ SSD
- x86/x64 hardware syncs faster than ARM
- Can run Linux alongside another OS partition

### Dedicated Mini PC

Intel NUC, Beelink, or similar mini PCs:
- Faster than Raspberry Pi
- Still low power
- Cost: $150–300 for a complete unit
- This is the recommended option for new dedicated node builds

## Software Options

### Bitcoin Core (Reference Implementation)

[[en/concepts/bitcoin-core|Bitcoin Core]] is the original, most-trusted implementation:
- The reference client that defines the protocol
- Maintained by a globally distributed set of contributors
- Command-line focused, with a GUI available
- Supports full validation, a built-in wallet, and a local Electrum server via ElectrumX add-on

For technical users, Bitcoin Core is the most direct path. For non-technical users, it requires more setup than the turnkey options below.

**Download**: bitcoin.org/en/download

### Umbrel

A consumer-friendly node operating system that installs on Raspberry Pi or Linux:
- Web-based dashboard accessible from your browser
- App store with Bitcoin Core, [[en/concepts/lightning-network|Lightning Network]] (LND), BTCPay Server, Electrs (Electrum server), and more
- One-click installation of most components
- Free and open source

Umbrel is the recommended starting point for users who want a functioning node with minimal technical overhead.

### RaspiBlitz

Open-source node software focused on Lightning integration:
- Runs Bitcoin Core + LND (or CLN) out of the box
- Terminal-based menu system
- Strong community documentation
- Slightly more technical than Umbrel; slightly more control

Preferred by Lightning users who want a full routing node.

### MyNode

Similar to Umbrel in goals; offers both free and premium tiers. Premium tier adds technical support.

## Disk Requirements

The Bitcoin blockchain grows continuously. As of early 2024:

- **Full archival node** (all blocks since genesis): ~650 GB
- **Pruned node**: Can be run in as little as 550 MB (stores only recent [[en/concepts/utxo|UTXO]] set and block headers) — but cannot serve historical blocks to peers
- **Annual growth rate**: ~50–80 GB/year

Recommendation: Start with a 1TB SSD. This gives years of headroom. A 2TB SSD is future-proof.

Pruned mode is acceptable for personal validation but does not contribute to the health of the network — archival nodes serve historical blocks to new nodes syncing for the first time.

## Initial Block Download (IBD)

The first time your node starts, it must download and validate every block from the genesis block (January 3, 2009) to the present. This is called the Initial Block Download.

**Typical times:**
| Hardware | IBD Time |
|----------|----------|
| Raspberry Pi 4 + USB SSD | 3–7 days |
| Modern x86 laptop | 1–3 days |
| Desktop with NVMe SSD | 12–24 hours |

IBD is CPU and I/O intensive. After IBD is complete, the node only processes one new block every ~10 minutes — resource usage drops dramatically.

**Tips for faster IBD:**
- Use a wired ethernet connection (not Wi-Fi)
- Use an NVMe SSD if possible (much faster than USB SSD)
- Keep the machine powered on continuously

## Connecting Your Wallet to Your Node

The primary practical benefit for most users: once your node is running an Electrum server (Electrs or Electrum Personal Server), you can connect your existing wallets to it.

### Sparrow Wallet

Sparrow's server connection settings (File → Preferences → Server) accept:
- **Bitcoin Core RPC**: Direct connection to Bitcoin Core
- **Private Electrum**: Connect to your own Electrs instance
- **Public Electrum**: Third-party server (not recommended; leaks address data)

Connecting Sparrow to your own node eliminates all address data leakage. Sparrow is the recommended desktop wallet for privacy-conscious users (see Privacy in Practice).

### Electrum Wallet

In Electrum, configure the server in Tools → Network → Server. Enter your node's IP address and Electrs port. Electrum requires an Electrum-protocol server (Electrs or Electrum Personal Server) rather than direct Bitcoin Core RPC.

### Mobile Wallets

- **BlueWallet** supports connecting to your own LND node or Electrs server
- **Phoenix** (Lightning) and **Breez** connect to their own servers; for on-chain privacy, use a desktop wallet via your node
- **Samourai Wallet + Dojo**: Dojo is a self-hosted backend for Samourai. It runs alongside Bitcoin Core and provides Samourai's server-side components. This is the recommended setup for Samourai users who want full privacy (see Privacy in Practice).

## Connecting Tor for Additional Privacy

Bitcoin Core can be configured to operate exclusively over the Tor network, hiding your node's IP address from peers:

1. Install Tor on your system
2. In bitcoin.conf: `proxy=127.0.0.1:9050` and `onlynet=onion`
3. Your node will only connect to .onion peers and broadcast transactions through Tor

This prevents your node's IP from being associated with the transactions you broadcast, which is relevant for privacy at the network layer. Umbrel and RaspiBlitz both have one-click Tor integration.

## Full Node vs. Pruned Node vs. SPV

| Type | Validates All Blocks | Serves Historical Data | Disk Usage |
|------|---------------------|----------------------|------------|
| Full archival node | Yes | Yes | ~650 GB+ |
| Pruned full node | Yes | No | ~1–5 GB |
| SPV (light client) | No (headers only) | No | Minimal |

SPV wallets trust the miner with the most [[en/concepts/proof-of-work|proof-of-work]] rather than validating rules themselves. They are convenient but trust-requiring. Full nodes are sovereign.

## Resources

- **bitcoin.org** — Bitcoin Core downloads and documentation
- **raspibolt.org** — Detailed Raspberry Pi node guide
- **getumbrel.com** — Umbrel node software
- **raspiblitz.org** — RaspiBlitz node software
- **en.bitcoin.it/wiki/Running_Bitcoin** — Bitcoin Wiki setup guide

## Sources

*Synthesized from multiple sources in the 21ideas.org raw/ library. No single canonical source article.*

## Related pages

- [[en/concepts/bitcoin-node|Bitcoin Node — what a full node is and how consensus works]]
- [[en/concepts/governance|Bitcoin Governance — why node operators determine Bitcoin's rules]]
- [[en/concepts/privacy|Privacy — the privacy model of Bitcoin]]
- [[en/concepts/bitcoin-core|Bitcoin Core — the reference implementation]]
- [[en/concepts/blockchain|Blockchain — what your node downloads and validates]]
- [[en/practice/privacy-practice|Privacy in Practice — full privacy stack including Sparrow, CoinJoin, Dojo]]
- [[en/practice/storage|Storage & Self-Custody — cold storage and self-custody]]
- [[en/history/blocksize-war|The Blocksize War (2015-2017) — when node operators defeated a miner-led hard fork]]
- [[en/concepts/lightning-network|Lightning Network — Lightning node software runs alongside Bitcoin Core]]
- [[en/glossary|Glossary]]
