# Bitcoin Wiki — User Guide

A guide to using the 21ideas Bitcoin Wiki — 54 pages synthesized from 308 Russian-language source articles.

## What this wiki is

This is a synthesized English-language knowledge base built from the 21ideas.org source library — a Russian Bitcoin education platform covering philosophy, economics, technical protocol, history, and practical self-custody. It is not a mirror or translation of the source material. A language model agent read the Russian sources, extracted key concepts, and compiled a structured set of interlinked wiki pages — integrating content across sources, flagging contradictions, and building up a layered synthesis. The wiki is maintained by Claude Code and grows richer each time a new source is ingested or a question is explored.

## What you can use the 21ideas Bitcoin Wiki for

- **Learning Bitcoin** — Start at [[wiki/concepts/bitcoin]] → [[wiki/concepts/money]] → [[wiki/concepts/proof-of-work]] for a complete conceptual foundation
- **Looking up terms** — [[wiki/glossary]] covers ~100 terms with wikilinks to concept pages
- **Finding the right book** — [[wiki/books/]] pages summarize all 8 books with quality and best-for ratings
- **Following a learning path** — [[wiki/series/gradually-then-suddenly]] (Parker Lewis) for economics; [[wiki/series/genesis-files]] for history; [[wiki/series/oxt-research]] for privacy
- **Checking original sources** — Every page lists its `sources:` in frontmatter and a `## Sources` section linking back to 21ideas.org original articles
- **Obsidian graph exploration** — Open in Obsidian and use Graph View to see how concepts interconnect

### Real example of the wiki in action

The [[wiki/concepts/cantillon-effect]] page shows what synthesis looks like in practice. It draws from two sources that approach the same concept differently — Saifedean Ammous's *The Fiat Standard* (structural/economic framing) and Robert Breedlove's *Masters and Slaves of Money* (philosophical/moral framing) — reconciles them, flags where emphasis differs, and arrives at a single synthesized conclusion: Bitcoin is Cantillon-resistant because PoW makes money creation open and competitive rather than politically concentrated. See the `## Example of synthesis` section on that page for a live demonstration.

## How the wiki is structured

The wiki lives in the `wiki/` directory with the following layout:

- `wiki/concepts/` — Core Bitcoin concepts: bitcoin, money, proof-of-work, scarcity, mining, lightning-network, privacy, security, utxo, governance, segwit, taproot, address-types, multisig, hashcash, cantillon-effect, protocol-stack
- `wiki/entities/` — Key people: Satoshi Nakamoto, Hal Finney, Nick Szabo, Gigi, Parker Lewis, Saifedean Ammous, and the Cypherpunks movement
- `wiki/books/` — Summaries of 8 foundational books: *Inventing Bitcoin*, *The Fiat Standard*, *The Bullish Case for Bitcoin*, *Sovereignty Through Mathematics*, *The Blocksize War*, *The Sovereign Individual*, *The Price of Tomorrow*, *21 Ways*
- `wiki/series/` — Article series: Gradually Then Suddenly, Genesis Files, Discovering Bitcoin, Bitcoin Astronomy, Silk Road, OXT Research, What I Learned From Bitcoin
- `wiki/history/` — Historical narrative: pre-Bitcoin cypherpunk era, the Blocksize War, and a full timeline
- `wiki/philosophy/` — 17 philosophical themes extracted and synthesized across the source library
- `wiki/practice/` — Practical guides: buying, storage/self-custody, Lightning tools, privacy practice, running a node
- `wiki/topics/` — Thematic deep-dives: Bitcoin for dissidents, Bitcoin's seven network effects
- `wiki/glossary.md` — A-Z term reference (~100 terms) drawn from the 21ideas.org glossary
- `wiki/overview.md` — Big-picture synthesis of the entire knowledge base
- `wiki/index.md` — Navigation index linking all 54 pages

## Frontmatter fields

Each page has YAML frontmatter that Obsidian's Dataview plugin can query:
- `title` — human-readable page title
- `category` — page type (concepts, entities, books, series, history, philosophy, practice, topics)
- `tags` — topic tags; always include `bitcoin` and `wiki`
- `quality` — canonical | reference | synthesized | stub
- `completeness` — high | medium | low
- `sources` — list of original 21ideas.org URLs (empty array if no single source)
- `synthesized_date` — date this synthesis was created

### Example Dataview query
To list all high-completeness concept pages:
```dataview
TABLE title, quality, completeness
FROM "wiki/concepts"
WHERE completeness = "high"
SORT title ASC
```

## Source material

All 308 source files are in `raw/`. They are immutable — the wiki is built from them but never modifies them. Source language: Russian. Wiki synthesis: English.

## Maintenance

This wiki is maintained by Claude Code (Anthropic). To add a new source: drop the markdown file in `raw/`, then ask Claude to ingest it. To run a lint pass: ask Claude to check for orphan pages, broken links, and stale content.

*Last updated: 2026-04-07. Contains 54 wiki pages.*
