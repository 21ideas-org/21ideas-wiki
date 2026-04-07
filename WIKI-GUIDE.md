# 21ideas Bitcoin Wiki — Living Knowledge Base

**A synthesized, densely interlinked, AI-assisted knowledge base for Bitcoin education.**

Built from **100+ articles + 10 foundational books** curated on [21ideas.org](https://21ideas.org), using Andrej Karpathy’s [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

This is not another static archive. It is a living knowledge system that compounds over time: new material is ingested, synthesized, and connected to the existing structure, making the whole wiki progressively more useful.

## What has been accomplished so far (April 2026)

The wiki is now in a solid, usable state after the initial build phase:

- **Total wiki files**: 54 pages with consistent structure
- **Core sections**:
  - `concepts/` — Core ideas, mechanics, and a fully integrated glossary
  - `entities/` — Key individuals and projects
  - `books/` — Syntheses and cross-references for all 10 books
  - `series/` — Coverage of major multi-part educational series
  - `history/`, `philosophy/`, `practice/` — Timelines, philosophical themes, and practical guides
- **Glossary integration** — Important Bitcoin terms have dedicated pages with definitions, context from multiple sources, and extensive backlinks
- **Dense internal linking** — Approximately 400–450 wikilinks connecting concepts across the vault
- **Consistent YAML frontmatter** on every page (compatible with Obsidian, Dataview, and Quartz)
- **Clean separation**: `raw/` contains immutable original sources, `wiki/` contains the synthesized and interlinked layer
- **Obsidian-ready** — Graph view reveals rich connections with major hubs such as Bitcoin, mining, UTXO, and glossary terms

The result is a high-density, queryable knowledge artifact grounded in the 21ideas.org library.

## What you can use the 21ideas Bitcoin Wiki for

### For readers and learners
- Explore Bitcoin concepts from first principles through interconnected pages
- Trace how ideas have evolved across books, articles, and series over 15+ years
- Discover unexpected connections via the graph view
- Browse the upcoming public website at **wiki.21ideas.org**

### For content creators and educators
- Generate Telegram threads and social media posts that combine current events with solid fundamentals
- Draft deeper blog posts and articles more efficiently
- Create lesson plans, comparison tables, or educational sequences
- Maintain a reliable reference that reduces repetition of earlier material

### For developers and researchers
- Fork the repository and run your own LLM agent against it
- Query the synthesized wiki with Claude, Cursor, Gemini, or local models
- Build tools or applications on top of the structured knowledge layer

### Practical examples
1. Open `index.md` in Obsidian and follow links from any concept page.
2. Query an LLM with access to the `wiki/` folder:  
   > “Using only the wiki/ folder, compare different views on Lightning Network scaling across sources.”
3. Generate content:  
   > “Create a Telegram post on the Cantillon Effect using only content from the wiki/.”
4. Combine with fresh news:  
   > “Take the news article below and write a blog post that supplements it with relevant explanations from the wiki/ folder.”

## How to use it right now

### Option A — Local Obsidian (recommended)
1. `git clone https://github.com/21ideas-org/21ideas-wiki.git`
2. Open the folder as a vault in Obsidian
3. Start exploring from `index.md` or `overview.md`
4. Enjoy the graph view

### Option B — Query with AI agents
- Point Claude Code, Cursor, Gemini CLI, or any folder-aware LLM at the vault
- Use a grounding prompt such as:  
  > “You are assisting with the 21ideas Bitcoin Wiki. Use **only** the wiki/ folder as your source of truth. Follow [[wikilinks]] and cite relevant pages.”

High-quality outputs can be saved back into the `wiki/` folder so the knowledge continues to grow.

### Option C — Public website (coming soon)
- Planned at **wiki.21ideas.org**
- Clean, searchable interface with graph support
- Multilingual support (English + Russian)
- Simple AI chatbot for natural-language questions

## Technical notes

- `raw/` — Immutable source of truth (do not edit directly)
- `wiki/` — AI-assisted synthesis layer (the agent helps maintain this)
- `CLAUDE.md` — Defines the rules and workflow the agent follows
- All changes are tracked in Git

## Contributing

The wiki is intentionally agent-friendly. Ways to contribute:
1. Open an issue suggesting new raw sources or areas that need expansion
2. Fork the repo, add material to `raw/`, run the agent, and open a pull request

Every addition helps strengthen the shared knowledge base.

---

**Built as part of the [21ideas Bitcoin education project](https://21ideas.org).**

Happy learning,  
— [Tony](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7)

---

⚡️ Found this useful? [Zap me a coffee](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7)  