---
title: "The Blocksize War (2015-2017)"
category: "history"
quality: "synthesized"
sources: ["https://21ideas.org/vojna-za-razmer-bloka/"]
synthesized_date: "2026-04-07"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, history, governance]
updated: "2026-04-14"
reviewed: "2026-04-14"
---

## Overview

The **Blocksize War** was a two-year conflict (2015–2017) over how to scale Bitcoin. Large blockers ([[en/concepts/mining|miners]], some businesses) wanted to increase the base block size limit (1MB) via a [[en/concepts/forks|hard fork]]. Small blockers (developers, [[en/concepts/bitcoin-node|full node]] operators, most users) preferred a [[en/concepts/forks|soft fork]] ([[en/concepts/segwit|SegWit]]) and Layer 2 scaling ([[en/concepts/lightning-network|Lightning]]). Small blockers won decisively.

Source: [[en/books/blocksize-war|The Blocksize War]] (Jonathan Bier's authoritative account)

## The Core Dispute

**Large blockers argued:**
- Bitcoin must scale on-chain to serve as peer-to-peer cash
- 1MB blocks create fee pressure that will make small transactions uneconomic
- Hard fork is technically straightforward; miners support it
- Bitcoin Core developers are blocking necessary upgrades

**Small blockers argued:**
- Increasing block size increases full node costs, reducing [[en/concepts/decentralization|decentralization]]
- A hard fork requires unanimous agreement — far too risky
- SegWit (soft fork) increases effective capacity while fixing transaction malleability
- Lightning Network handles small payments; base layer settles large/final transactions
- Miners don't have the right to change consensus rules unilaterally

## Key Events

**2015:**
- Scaling Bitcoin conferences (Montreal) organized to find solutions
- Bitcoin XT proposed by Mike Hearn and Gavin Andresen: 8MB hard fork
- XT gains modest support then fades

**Feb 2016 — Hong Kong Roundtable:**
- Secret meeting of miners and developers
- Miners agree to support SegWit if developers commit to 2MB hard fork after
- Agreement collapses — developers did not consider it binding

**Apr 2016 — Bitcoin Classic:**
- 2MB hard fork client; gains exchange/miner support briefly
- Nodes crash when hit with large blocks from test
- Movement collapses

**Apr 2017 — ASICBoost:**
- Bitmain's mining hardware had a covert optimization (ASICBoost) incompatible with SegWit
- This explained why Bitmain was blocking SegWit despite agreeing to it in principle
- Exposed by Gregory Maxwell

**May 2017 — New York Agreement (NYA):**
- Barry Silbert organizes meeting of 58 companies (exchanges, miners)
- Agreement: activate SegWit + commit to 2MB hard fork (SegWit2x) within 6 months
- No major Bitcoin Core developers sign

**Aug 1, 2017 — Two forks:**
- **UASF ([[en/concepts/bip|BIP]]148) activates**: [[en/concepts/bitcoin-node|full node]] operators enforce [[en/concepts/segwit|SegWit]] rules; miners capitulate
- **Bitcoin Cash launches**: Roger Ver and Jihan Wu create 8MB hard fork chain; market immediately assigns it ~10% of Bitcoin's value (it fell further over time)

**Aug 24, 2017:** SegWit officially activates on Bitcoin mainnet.

**Nov 2017:** SegWit2x cancelled due to massive community opposition. Email to signatories reads: "Our goal has always been a smooth upgrade for Bitcoin. Although we strongly believe in the need for a larger blocksize, there is something we believe is even more important: keeping the community together."

## What the War Proved

1. **Full nodes are supreme**: miners cannot change consensus rules without full node adoption
2. **Economic majority matters**: exchanges and businesses that followed SegWit determined the "real Bitcoin"
3. **UASF works**: users can force protocol changes by threatening to reject non-compliant miners
4. **Hard forks are nearly impossible**: even with 58 major companies and major miners, SegWit2x failed
5. **Bitcoin Cash is an alt**: the hard fork chain was immediately valued far below Bitcoin, confirming the market's preference

## Craig Wright

During the conflict, Craig Wright claimed to be [[en/entities/satoshi-nakamoto|Satoshi Nakamoto]] and threw his support behind large blockers. His claims were comprehensively disproven — he could not produce a valid signature from known Satoshi addresses. He later sued various Bitcoin community members for defamation (litigation ongoing). His involvement damaged the large-blocker cause by association.

## Legacy

The blocksize war established the template for [[en/concepts/governance|Bitcoin governance]]: changes require genuine consensus, [[en/concepts/forks|soft forks]] are strongly preferred over [[en/concepts/forks|hard forks]], and [[en/concepts/bitcoin-node|full nodes]] (not miners) are the ultimate arbiters of Bitcoin's rules. The [[en/concepts/segwit|SegWit]] activation also enabled the [[en/concepts/lightning-network|Lightning Network]], which launched shortly after.

## Sources

- [The Blocksize War (21ideas)](https://21ideas.org/vojna-za-razmer-bloka/)

## Related pages

- [[en/books/blocksize-war|The Blocksize War (book) — Jonathan Bier's definitive account]]
- [[en/concepts/governance|Bitcoin Governance — lessons this conflict established]]
- [[en/concepts/forks|Forks — hard fork vs. soft fork distinction at the heart of the dispute]]
- [[en/concepts/segwit|SegWit — the soft fork that resolved the war]]
- [[en/concepts/bitcoin-node|Bitcoin Node — full nodes as the ultimate rule arbiters]]
- [[en/concepts/lightning-network|Lightning Network — what SegWit enabled]]
- [[en/entities/satoshi-nakamoto|Satoshi Nakamoto — his absence from the conflict was notable]]
- [[en/history/timeline|Bitcoin Timeline — chronological context]]
