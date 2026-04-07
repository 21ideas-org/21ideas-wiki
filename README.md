# Bitcoin LLM Wiki — 21ideas

A living, AI-maintained knowledge base for Bitcoin education. Built from **100+ articles** and **10+ foundational books** using [Andrej Karpathy’s LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

- `raw/` — Immutable source material (21ideas original Markdown with frontmatter and links).
- `wiki/` — The synthesized, densely interlinked layer (concepts, entities, terms/glossary, book summaries, series, history, etc.). This is the part that compounds over time.
- Powered by Obsidian (graph view shines here) + LLM agent that ingests, updates, and cross-links everything.

## How to use this repo

1. **Clone & open in Obsidian**  
   ```bash
   git clone https://github.com/21ideas-org/21ideas-wiki.git
   ```

Open the folder as a vault in Obsidian → explore the graph starting from `index.md` or `overview.md`.

2. **Query with AI agents**
Any LLM that can read folders (Claude Code, Cursor, Gemini, local models, etc.) can be pointed at this repo. Instruct it: “Use only the wiki/ folder as source of truth, follow [[wikilinks]], synthesize...”

3. **Fork & extend**
Fork this repo and run your own LLM agent against it. Add new raw sources → let the agent update the wiki. Great for personal Bitcoin research, education projects, or building content.

## Structure
`concepts/` — Core ideas, mechanics, terms (heavily linked to the glossary)
`entities/` — People, projects, events
`books/` — Summaries and syntheses
`series/` — Multi-part educational series
`history/`, `philosophy/`, `practice/` — etc.
`CLAUDE.md` (or `GEMINI.md`) — Rules the agent follows

## Contributing / Building on this
Feel free to open issues or PRs if you spot gaps or want to contribute new syntheses. 
The wiki is designed to be agent-friendly.  
This wiki is a work in progress and will keep evolving as new material is added.  
Built as part of the [21ideas](https://21ideas.org) Bitcoin education project.  

## License

This project is licensed under the [MIT License](LICENSE) — feel free to fork, use, and build upon it.

---

⚡️ Found the project useful? [Zap](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) [Tony](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) a coffee.

