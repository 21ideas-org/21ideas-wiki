---
title: "Contribute to 21wiki"
category: "meta"
language: "en"
---

21wiki is open to contributions. There are three ways to help — pick the one that fits your time and technical comfort.

## Track 1 — Suggest (no code required)

The simplest contribution. Open a GitHub Issue to:

- **Suggest a missing topic** — something you'd like to see covered
- **Report an error** — factual mistake, broken link, or outdated information
- **Request a language parity fix** — a topic exists in English but not Russian, or vice versa

[Open an issue](https://github.com/21ideas-org/21ideas-wiki/issues/new/choose)

## Track 2 — Add a source file

The wiki is built from immutable source files in `raw/` — anchored in [21ideas.org](https://21ideas.org) and other **Bitcoin-only** sources. If you have material that will benefit the wiki, you can add it to the source library.

Source acceptance rules (full list: [docs/CONTRIBUTING.md](https://github.com/21ideas-org/21ideas-wiki/blob/main/docs/CONTRIBUTING.md)):
- **21ideas.org**, **primary Bitcoin sources** (BIPs, Satoshi writings, whitepaper, official protocol docs), and **reputable Bitcoin-only educational** content from established authors and publications are accepted.
- Sources that need a decision (e.g. academic papers, non-English primaries outside 21ideas.org) — open an issue before adding.
- **Not accepted for the main repo:** exchange content, altcoin or multi-coin material, price speculation, or third-party blogs without a clear Bitcoin-only editorial focus.

**Using the ingest skill (recommended):** open Cursor or Claude Code in the repo root and run:

```
Use docs/INGEST-SKILL.md to add the following article to raw/.

URL:       <paste the full URL here>
Author:    <author's name — omit if unsure>
Published: <YYYY-MM-DD — omit if unknown>
Series:    <series name and part number if applicable — omit if not a series>
Notes:     <anything unusual — omit if nothing to flag>
```

URL is always required. Everything else improves results but is optional. The agent handles subdirectory placement, duplicate checking, and frontmatter — you don't need to know the `raw/` structure.

Once you've added a source file, a maintainer will handle wiki synthesis — or continue to Track 3.

## Track 3 — Generate wiki pages with AI

The full contributor path: fork the repo, use an AI coding agent (Claude Code, Cursor, or Gemini CLI) locally against the full vault, generate pages for both language layers, verify with the lint tool, and open a PR.

This track requires a local setup. **The full workflow, rules, and agent prompt are in the contributing guide on GitHub:**

[docs/CONTRIBUTING.md](https://github.com/21ideas-org/21ideas-wiki/blob/main/docs/CONTRIBUTING.md)

## Questions?

Open a GitHub Issue with the label `question` or join 21ideas contributors [Telegram chat](https://t.me/+DVlyZlInKfBkY2M0).

## Related pages

- [Support 21wiki](./support)
- [21ideas.org](https://21ideas.org)