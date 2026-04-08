---
title: "Glossary"
category: reference
tags: [bitcoin, wiki, reference, glossary, terms]
source: "Synthesized from raw/ sources + glossary"
updated: "2026-04-07"
quality: canonical
sources: ["https://21ideas.org/glossary"]
synthesized_date: "2026-04-07"
completeness: high
---

# Glossary

*Source: `raw/Start/glossary.md` — the master Bitcoin term reference for 21ideas.org. All terms defined in the Russian educational context of the site. Terms with dedicated wiki pages are linked.*

---

## A — Cyrillic

**Адрес (Address)** — A unique string of characters used to receive Bitcoin transactions. Created from a public key via cryptographic hashing. Mainnet addresses start with `1` (P2PKH), `3` (P2SH), or `bc1` (native SegWit / Taproot). See [[concepts/address-types]].

**Алгоритм (Algorithm)** — A sequence of unambiguous instructions used to solve a problem. Bitcoin uses SHA-256 for block hashing and PoW for network security.

**Аппаратный кошелёк (Hardware wallet)** — A physical device designed to store private keys offline. Protects against remote hacking and malware. See [[concepts/security]].

**Атака 51% (51% Attack)** — When a miner or group controls more than 50% of the network's hash rate, enabling double-spend attacks and reorg of recent blocks. Cannot create new coins or steal from other wallets. See [[concepts/proof-of-work]].

**Атака перебором (Brute Force Attack)** — Automated trial-and-error attempt to guess a password or seed. Protected against by BIP39 passphrase and the vast key space of Bitcoin cryptography.

**Атомарные свопы (Atomic swaps)** — Cross-chain or off-chain exchange of one asset for another without custodial intermediaries. Uses HTLCs to ensure both sides of the exchange complete or neither does.

---

## Б — Cyrillic

**Биржа (Exchange)** — A service allowing users to buy, sell, and trade Bitcoin. Centralized exchanges require KYC, linking identity to addresses permanently. See [[practice/buying]], [[concepts/privacy]].

**Биткоин (Bitcoin)** — The first decentralized cryptocurrency, created in 2008 by Satoshi Nakamoto. Protocol/network = Bitcoin (capital B); the monetary unit = bitcoin (lowercase b). Hard cap: 21M BTC. Consensus: Proof of Work. See [[concepts/bitcoin]], [[entities/satoshi-nakamoto]].

**Блок (Block)** — A group of transactions bundled by miners. Average block time: 10 minutes. Transactions with higher fees are included first. Current size limit: ~1MB (base weight) / 4MB (block weight with SegWit).

**Блок-кандидат (Candidate block)** — A temporary block created by a miner for submission to the blockchain, before a valid PoW hash is found.

**Блокчейн (Blockchain)** — A distributed ledger of data consisting of blocks linked in linear sequence. Each block contains: transaction data, hash of the previous block, metadata (timestamp, difficulty). Immutability: altering one block requires recalculating all subsequent blocks. See [[concepts/bitcoin]].

**Бумажный кошелёк (Paper wallet)** — An obsolete (2011-2016) method of storing Bitcoin by printing one private key and address. Has many flaws; not recommended.

---

## В — Cyrillic

**Вознаграждение за блок (Block reward)** — The mechanism by which new bitcoin enters circulation. Consists of: (1) subsidy (new coins) + (2) transaction fees. Subsidy halves every 210,000 blocks. Current (2024): 3.125 BTC. See [[concepts/scarcity]].

**Временнáя метка (Timestamp)** — A digital mark indicating the time of transaction or block creation. Bitcoin timestamps are used for difficulty adjustment and block ordering. See [[concepts/mining]].

---

## Г — Cyrillic

**Генезис-блок (Genesis block)** — Block 0, mined January 3, 2009. Contains the embedded message: *"The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."* The genesis block's coinbase output cannot be spent (protocol quirk). See [[history/timeline]].

**Горячий кошелёк (Hot wallet)** — Any Bitcoin wallet running on an internet-connected device. Higher convenience, lower security vs. cold storage. See [[concepts/security]].

---

## Д — Cyrillic

**Двойная трата / двойное расходование (Double Spend)** — An attempt to spend the same bitcoin twice. Bitcoin solved this for the first time in digital space via the public blockchain + PoW consensus. See [[concepts/bitcoin]], [[concepts/proof-of-work]].

**Дерево хэшей (Merkle Tree)** — A complete binary tree where leaf nodes contain hashes of transaction data and inner nodes contain hashes of their children. The root (Merkle root) is a single hash of all transactions in a block. Named after Ralph Merkle (1979). Enables efficient transaction verification.

**Десктопный кошелёк (Desktop wallet)** — A software wallet on a computer providing full control over private keys. Recommended in combination with hardware wallets. Example: Electrum, Sparrow.

**Детерминированный кошелёк (Deterministic wallet)** — A wallet system deriving all keys from a single seed. Allows easy backup and restoration. Standard: BIP32 (HD wallets). Seeds typically serialized as BIP39 mnemonic phrases. See [[concepts/security]].

**Дефляция (Deflation)** — Increase in purchasing power of money over time, often caused by a limited supply. Bitcoin is deflationary by design (fixed 21M supply + lost keys reduce circulating supply). Distinction: growth deflation (good — productivity) vs. credit deflation (bad — credit contraction). See [[concepts/money]].

**Децентрализация (Decentralization)** — Distribution of power, control, and management among multiple network participants. In Bitcoin: thousands of nodes each hold a full copy of the blockchain; no central authority. See [[concepts/bitcoin]], [[concepts/governance]].

---

## З — Cyrillic

**Задача византийских генералов (Byzantine Generals Problem)** — A cryptological problem of coordination between remote parties where some may be malicious. Satoshi Nakamoto was the first to solve this, via Proof of Work + longest chain rule. Enables trustless consensus in a network with unknown participants.

**Знай своего клиента (KYC — Know Your Customer)** — A financial compliance procedure requiring companies to verify customer identity. Bitcoin exchanges implementing KYC permanently link identity to addresses. See [[concepts/privacy]], [[practice/buying]].

---

## И — Cyrillic

**Инвойс (Lightning Invoice)** — A payment request on the Lightning Network encoded in BOLT 11 format. Contains: amount (optional), recipient node public key, expiry time (usually 1 hour), optional description, sender signature. Presented as QR code or text string. Single-use and time-limited. See [[concepts/lightning-network]].

**Инфляция (Inflation)** — Reduction in money's purchasing power due to increased money supply. Bitcoin's inflation follows a predetermined emission schedule, halving every 4 years. Current (2024): ~<1% annually. Fiat currencies have no hard cap. See [[concepts/money]], [[concepts/scarcity]].

---

## К — Cyrillic

**Кастодиальное хранение (Custodial storage)** — Holding cryptocurrency where a third party controls the private keys. User holds an IOU. Risk: exchange insolvency, hacking, regulatory seizure. "Not your keys, not your coins." See [[concepts/security]].

**Ключ (приватный/публичный) (Private/Public Key)** — Core cryptographic elements. Private key: secret code used to sign transactions; whoever has it controls the funds. Public key: derived from private key; used to create receiving addresses and verify signatures. Loss of private key = permanent loss of funds.

**Комиссия (Fee)** — Payment offered by transaction sender to miners for block inclusion. Expressed in satoshis per byte (sat/B). Higher fee = faster confirmation. If too low, transaction may stay in mempool indefinitely. See [[concepts/utxo]].

**Консенсус Накамото (Nakamoto Consensus)** — The protocol used in Bitcoin to achieve agreement on blockchain state without central authority. Uses Proof of Work + longest chain rule. Nodes always follow the chain with the most accumulated work. See [[concepts/proof-of-work]].

**Коинбэйс (Coinbase transaction)** — A special type of transaction with no inputs, created by miners when a new block is found. Always the first transaction in a block. Pays the block reward (subsidy + fees) to the miner. The Genesis block's coinbase cannot be spent.

**Корректировка сложности (Difficulty adjustment)** — A protocol mechanism that adjusts mining difficulty every 2,016 blocks (~2 weeks) to maintain ~10-minute block times regardless of hash rate changes. See [[concepts/mining]], [[concepts/proof-of-work]].

**Кошелёк (Wallet)** — Software or hardware tool for storing, sending, and receiving Bitcoin. Types: hardware (cold), desktop (hot), mobile (hot), web (hot). The wallet manages keys; it doesn't "hold" bitcoin — the blockchain does. See [[concepts/security]], [[practice/storage]].

**Криптовалюта (Cryptocurrency)** — Digital currency using cryptography for transaction security and verification. Bitcoin is the first. All others (altcoins) are considered shitcoins by the 21ideas.org site perspective. See [[philosophy/overview]].

**Криптография (Cryptography)** — The science of protecting information with mathematical methods. Bitcoin uses: (1) asymmetric cryptography (key pairs) for transaction signing; (2) hash functions (SHA-256) for block IDs.

---

## Л — Cyrillic

**Лайтнинг (Lightning Network)** — A Layer 2 payment protocol built on Bitcoin. Enables near-instant, low-fee micropayments via payment channels. Improves scalability without changing Bitcoin's base rules. See [[concepts/lightning-network]].

---

## М — Cyrillic

**Майнер (Miner)** — A specialized network participant (computer or group of computers) that: (1) bundles pending transactions into blocks; (2) verifies blocks from other miners. Rewarded with block reward (subsidy + transaction fees). See [[concepts/mining]].

**Майнинг (Mining)** — The process of creating new blocks and adding them to the blockchain. Miners use computational power to solve Proof of Work puzzles. Functions: (1) confirm transactions; (2) secure the network; (3) issue new bitcoin. See [[concepts/mining]], [[concepts/proof-of-work]].

**Майнинг-пул (Mining pool)** — A combined mining approach where multiple miners contribute to block creation and share rewards proportionally to contributed hash rate. Reduces variance of individual miner rewards.

**Мемпул (Mempool)** — Temporary storage for unconfirmed transactions. After broadcast, a transaction waits in the mempool until a miner includes it in a block. Higher fee = higher priority. Monitor fees at mempool.space.

**Мобильный кошелек (Mobile wallet)** — A smartphone app for managing Bitcoin. Convenient but less secure than hardware wallets. Best for spending amounts (Lightning or small on-chain). See [[practice/lightning-tools]].

**Мультиподпись (Multisignature / Multisig)** — An address that requires multiple signatures to spend. Example: 2-of-3 multisig requires any 2 of 3 possible signers. Eliminates single point of failure. Used for joint custody, corporate structures, and enhanced security. See [[concepts/security]], [[concepts/taproot]].

---

## Н — Cyrillic

**Невостребованный блок (Orphaned block)** — A block not included in the main chain because the majority of miners built on a competing block. The miner receives no reward; transactions go back to the mempool.

**Нода (Node / Full node)** — A device or program that supports the Bitcoin network by verifying and propagating transactions and blocks. Full nodes enforce all consensus rules independently. The ultimate arbiters of Bitcoin's rules. See [[concepts/governance]].

**Нонс (Nonce — Number only used once)** — A random number field that miners vary when searching for a hash meeting the difficulty target. Mining = iterating through nonces until a valid hash is found. See [[concepts/mining]].

---

## О — Cyrillic

**Обозреватель блоков (Block explorer)** — A tool providing information about transactions and blocks in the Bitcoin network. Example: mempool.space.

**Оффчейн (Off-chain)** — Operations and transactions that occur outside the main blockchain, for scalability. The Lightning Network is the prime example. See [[concepts/lightning-network]].

---

## П — Cyrillic

**Подтверждение (Confirmation)** — The number of blocks added to the chain after the block containing your transaction. 1 confirmation = your transaction is in a block. 6 confirmations is considered safe for large transactions.

**Программное обеспечение с открытым исходным кодом (Open source software)** — Freely distributed software whose code is available for review, modification, and redistribution. Bitcoin Core is open source.

**Премайн (Premine)** — Creation of cryptocurrency tokens before official launch. A red flag indicating founders enrich themselves at users' expense. Example: Ethereum had a premine. Bitcoin had no premine — Satoshi mined alongside others from day one.

**Приватный ключ (Private key)** — A secret cryptographic key used to sign transactions and access wallet funds. Must never be shared. Loss = permanent loss of access to funds. See [[concepts/security]].

**Публичный ключ (Public key)** — The public part of a cryptographic key pair. Used to create receiving addresses and verify transaction signatures. Derived from the private key via one-way elliptic curve function. Cannot be reversed to obtain the private key.

---

## Р — Cyrillic

**Реестр (Ledger)** — A record of identifiers, transactions, timestamps, balances, and other financial accounting data. The Bitcoin network is a unique ledger: decentralized, open, and irreversible.

**Решения второго уровня (Layer 2)** — Technologies built on top of the base layer to improve scalability. Operate off-chain for speed and low cost; settle to the base layer for security. Lightning Network is the prime example. See [[concepts/lightning-network]].

---

## С — Cyrillic

**Сатоши (Satoshi unit)** — The smallest indivisible unit of bitcoin. 1 BTC = 100,000,000 satoshis. Named after Bitcoin's creator. At $100,000/BTC: 1 satoshi = $0.001.

**Сатоши Накамото (Satoshi Nakamoto)** — The pseudonymous creator of Bitcoin. Published the whitepaper October 31, 2008; launched the network January 3, 2009. Identity unknown. Holds ~1M BTC (never moved). See [[entities/satoshi-nakamoto]].

**Сложность майнинга (Mining difficulty)** — A parameter regulating how hard it is for miners to find new blocks. Recalculates every 2,016 blocks (~2 weeks) to target 10-minute block times. Increases with hash rate growth. See [[concepts/mining]].

**Смарт-контракт (Smart contract)** — A programmable agreement executed automatically when conditions are met. In Bitcoin: constrained (Script language is deliberately limited). Taproot (via MAST) enables more sophisticated conditional contracts. See [[concepts/taproot]].

**Софтфорк (Soft fork)** — A backward-compatible change to consensus rules. Non-upgraded nodes still accept blocks from upgraded nodes. Examples: SegWit (2017), Taproot (2021). See [[concepts/segwit]], [[concepts/taproot]], [[concepts/governance]].

---

## Т — Cyrillic

**Таймчейн (Timechain)** — Satoshi Nakamoto's original term for what is now called "blockchain." Emphasizes the temporal aspect: blocks are linked in chronological sequence with timestamps.

**Тапрут (Taproot)** — Protocol upgrade activated November 14, 2021 (block 709,632). Introduces Schnorr signatures, MAST, and Tapscript. Improves privacy, reduces fees, enables more flexible smart contracts. See [[concepts/taproot]].

**Транзакция (Transaction)** — A transfer of bitcoin between addresses in the blockchain. Contains: inputs (source UTXOs), outputs (destination addresses), and fee (miner payment). Signed with sender's private key. See [[concepts/utxo]].

**Тестовая сеть (Testnet)** — An alternative Bitcoin network for experiments and testing. Testnet BTC has no real value. Addresses start with `m`, `n`, `2`, or `tb1`.

---

## У — Cyrillic

**Узел (Нода / Node)** — A device or program supporting the Bitcoin network by verifying and propagating transactions and blocks. Full nodes = complete, independent validation. See [[concepts/governance]].

---

## Ф — Cyrillic

**Фиат (Fiat)** — Government-issued currency backed by decree, not a physical commodity. No hard supply cap. The fiat system is the main alternative to Bitcoin that the 21ideas.org library critiques. See [[concepts/money]], [[books/fiat-standard]].

**Форк (Fork)** — A process of changing consensus rules that may result in blockchain splits. Hard fork: new chain incompatible with old (e.g., Bitcoin Cash). Soft fork: backward-compatible change (e.g., SegWit, Taproot). See [[concepts/governance]], [[history/blocksize-war]].

---

## Х — Cyrillic

**Халвинг (Halving)** — An event in Bitcoin occurring every ~210,000 blocks (~4 years) that cuts the block subsidy in half. Ensures gradually declining emission toward 21M cap. See [[concepts/scarcity]].

**Хардфорк (Hard fork)** — An extension of consensus rules where previously invalid blocks become valid. Non-upgraded nodes cannot process new-rule blocks. Requires near-universal consensus. Examples: Bitcoin Cash (2017), BSV. See [[concepts/governance]], [[history/blocksize-war]].

**Холодное хранение (Cold storage)** — Storing bitcoin with keys generated and kept offline. Hardware wallets are the most popular cold storage tool. Safest method for long-term holding. See [[concepts/security]], [[practice/storage]].

**Хэш (Hash)** — The output of a hash function that transforms arbitrary-length input into a fixed-length string. Bitcoin uses SHA-256. Properties: unique per input, cannot be reversed, small input changes produce completely different output.

**Хэширование (Hashing)** — The process of transforming arbitrary-length data into a fixed-length output via a hash function. Bitcoin uses SHA-256 twice (SHA-256d) for block hashing. See [[concepts/mining]].

**Хэшрейт (Hash rate)** — A measure of computational power used for mining, expressed in hashes per second (H/s). Higher network hash rate = more security. Growth in hash rate triggers difficulty adjustment. See [[concepts/proof-of-work]].

---

## Ц — Cyrillic

**Целевая сложность (Target difficulty)** — A specific number that a valid block hash must be lower than. Inversely related to difficulty: as target decreases, difficulty increases. Adjusts every 2,016 blocks. See [[concepts/mining]].

---

## Ш — Cyrillic

**Шестнадцатеричная (Hex / Hexadecimal)** — A base-16 number system using digits 0-9 and letters a-f. SHA-256 hashes are expressed as 64 hex characters (256 bits).

**Шифрование (Encryption)** — The process of converting data into an encrypted format inaccessible to outsiders. Bitcoin uses asymmetric encryption (ECDSA / Schnorr) for transaction signing.

**Шифропанк (Cypherpunk)** — A digital technology activist who strongly supports cryptographic solutions for social and political goals. The cypherpunk movement directly produced Bitcoin. See [[entities/cypherpunks]].

---

## Щ — Cyrillic

**Щиткоин (Shitcoin)** — Any cryptocurrency other than Bitcoin. The 21ideas.org position: all altcoins reintroduce trusted parties, centralization, or inflation; no altcoin use case is improved by using an alternative blockchain instead of Bitcoin. See [[philosophy/overview]].

---

## Э — Cyrillic

**Эмиссия (Issuance/Emission)** — The process of releasing new monetary units into circulation. Bitcoin's issuance is via mining with a predetermined halving schedule. Total cap: 21M BTC. Last bitcoin mined ~2140.

**Эскроу (Escrow)** — A contractual arrangement where a third party holds funds until conditions are met. In Bitcoin: implemented natively via multisig addresses (e.g., Hodl Hodl uses 2-of-3 multisig escrow for P2P trades). See [[practice/buying]].

---

## Latin Terms

**AML (Anti-Money Laundering)** — International rules ostensibly aimed at preventing money laundering. The site takes a critical view: AML policies are often used to serve narrow interests rather than prevent crime. Often paired with KYC.

**ASIC (Application-Specific Integrated Circuit)** — Specialized chips designed for a single task. In Bitcoin: ASICs perform SHA-256 hashing far more efficiently than CPUs or GPUs. Examples: Antminer S19, Whatsminer M30S. See [[concepts/mining]].

**BIP (Bitcoin Improvement Proposal)** — A formal document proposing changes to the Bitcoin protocol. Anyone can write a BIP. Major BIPs: BIP32 (HD wallets), BIP39 (mnemonics), BIP141 (SegWit), BIP340-342 (Taproot). See [[concepts/governance]].

**BOLT (Basis of Lightning Technology)** — The specification documents for the Lightning Network protocol. BOLT 11 defines the Lightning invoice format. See [[concepts/lightning-network]].

**HTLC (Hash Time Lock Contract)** — A conditional payment contract using a cryptographic hash and a time lock. Enables trustless multi-hop routing in Lightning: payment succeeds if the recipient reveals a preimage within the time limit; otherwise it refunds automatically. See [[concepts/lightning-network]].

**KYC (Know Your Customer)** — See Знай своего клиента above. See [[concepts/privacy]], [[practice/buying]].

**P2P (Peer-to-Peer)** — Direct communication or exchange between participants without intermediaries. Bitcoin is a P2P electronic cash system by design.

**PoW (Proof of Work)** — See [[concepts/proof-of-work]].

**PSBT (Partially Signed Bitcoin Transaction)** — A standard (BIP174) for passing unsigned/partially signed transactions between wallets and signing devices. Enables hardware wallet signing workflows and multisig coordination. See [[concepts/security]].

**TXID (Transaction ID)** — A unique identifier for a transaction, derived by hashing the transaction data. In SegWit transactions, the TXID excludes witness data (fixing malleability). See [[concepts/segwit]].

**UTXO (Unspent Transaction Output)** — See [[concepts/utxo]].

---

## Address Types Quick Reference

| Type | Prefix | Era | Notes |
|------|--------|-----|-------|
| P2PK | — | 2009 | Obsolete; pay to public key directly |
| P2PKH | `1` | 2009 | Legacy; still 43% of supply |
| P2MS | — | 2012 | Obsolete raw multisig |
| P2SH | `3` | 2012 | Script hash; used for multisig and nested SegWit |
| P2WPKH | `bc1q` (42 chars) | 2017 | Native SegWit single-sig |
| P2WSH | `bc1q` (62 chars) | 2017 | Native SegWit script/multisig |
| P2TR | `bc1p` | 2021 | Taproot; Schnorr; all scripts look identical |

See [[concepts/address-types]] for full details.

---

## Sources

- [Original article on 21ideas.org](https://21ideas.org/glossary)

---

## Related Pages

- [[concepts/bitcoin]] — Bitcoin fundamentals
- [[concepts/address-types]] — full address type guide
- [[concepts/utxo]] — UTXO model
- [[concepts/lightning-network]] — Lightning terminology
- [[concepts/security]] — self-custody terms
- [[index]] — full wiki navigation
