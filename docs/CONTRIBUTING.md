# Contributing to 21wiki

Thank you for your interest in improving 21wiki — a bilingual Bitcoin education resource built from [21ideas.org](https://21ideas.org) source material.

This guide explains exactly how to contribute, at whatever level of involvement you have time for.

---

## Three ways to contribute

### Track 1 — Suggest (no code, no AI required)

The lowest-friction contribution. Use GitHub Issues to:

- **Suggest a missing topic** — something you'd like to see covered that isn't yet in the wiki
- **Report an error** — factual mistake, broken link, or outdated information
- **Request a language parity fix** — a topic exists in one language layer but not the other

Use the issue templates in the repo. A maintainer will triage and queue it.

---

### Track 2 — Add a source file (intermediate)

The wiki is grounded in immutable source files in `raw/`. If you have a 21ideas.org article or a relevant primary Bitcoin source (a BIP, a research paper, a Satoshi writing) that isn't in the repo yet, you can add it.

**Source acceptance policy:**
- Only material from **21ideas.org** is accepted without explicit maintainer approval.
- Primary Bitcoin sources (BIPs, Bitcoin-only material, Satoshi writings) may be accepted case-by-case — open an issue first.
- No third-party blog posts, exchange content, or altcoin material.
- `raw/` files are **immutable once added** — they are source of truth, never edited.

**How to add a source file:**

1. Fork the repo and create a branch.
2. Place the markdown file in the correct `raw/` subtree:

   ```
   raw/Books/           ← book chapters
   raw/Theory/
     economics/         ← monetary theory, Bitcoin economics
     protocol/          ← technical protocol (UTXOs, SegWit, Taproot, etc.)
     philosophy/        ← culture, manifestos, cypherpunk thought
     history/           ← Genesis Files, Silk Road, etc.
     privacy/           ← privacy tools, CoinJoin, AML
     security/          ← seeds, hardware wallets, MuSig2
     lightning/         ← Lightning Network theory
     future/            ← long-horizon scenarios
   raw/Practice/
     hodl/ lightning/ privacy/ buy/ security/ interact/
   raw/Start/           ← intro guides
   ```

3. If the source has a canonical 21ideas.org URL, add it as metadata in the file's frontmatter (field: `url`). This is what the wiki uses to populate `sources:` — **never fabricate URLs**.
4. Open a PR with just the `raw/` addition. A maintainer will handle the wiki synthesis, or you can continue with Track 3.

---

### Track 3 — Generate wiki pages with AI (advanced)

This is the full contributor path: fork the repo, run an AI coding agent locally against the full vault, generate wiki pages for both language layers, verify with the lint tool, and open a PR.

**Why local + agent, not a chat window?**
The agent needs to read `CLAUDE.md`, `docs/PAGE-ENHANCEMENT-STANDARD.md`, existing index files, and the target `raw/` source simultaneously — and then write files directly into the right paths. Pasting content into a web chat session produces worse output: the agent can't verify wikilink targets, can't run lint, and can't write files atomically. A local agent session with the full repo in context is the only reliable way to produce clean contributions.

**Supported tools:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli). Any agent that can read a directory tree and write files works.

**Before you start — read these two files in the repo:**
- `CLAUDE.md` (repo root) — the non-negotiable rules for every wiki page
- `docs/PAGE-ENHANCEMENT-STANDARD.md` — the full single-page polish checklist

**The short version of the rules:**
- Every page needs complete YAML frontmatter (see schema below)
- Tags must come from the strict allowlist in `CLAUDE.md` — never invent tags
- Internal links use `[[en/...]]` in `wiki-en/` and `[[ru/...]]` in `wiki-ru/` — no bare links, no `[[wiki-en/...]]` prefixes
- **Never fabricate 21ideas.org URLs** — if no URL exists in the source's metadata, set `sources: []`
- No `#` heading in the page body (Quartz renders frontmatter `title` as the heading)
- No `---` horizontal rules in the body
- `wiki-en/` and `wiki-ru/` are **independent syntheses** from the same source — not translations of each other
- Every page must end with `reviewed: "YYYY-MM-DD"` as the **last** frontmatter field

---

## AI-assisted contribution workflow

### What you need

- Git and Python 3 installed locally
- One of: Claude Code, Cursor, or Gemini CLI
- A fork of this repo, cloned locally

### Step 1 — Fork and clone

```bash
git clone https://github.com/YOUR-USERNAME/21ideas-wiki.git
cd 21ideas-wiki
git checkout -b contribute/[slug]
```

Open the repo in your agent of choice:
- **Claude Code:** `claude` from the repo root
- **Cursor:** `cursor .`
- **Gemini CLI:** `gemini` from the repo root

The agent will load `CLAUDE.md` automatically (it's in the repo root). In Cursor, `CLAUDE.md` is picked up as project rules.

### Step 2 — Identify the source

Pick an unprocessed file from `raw/` — check `docs/WIKI-BACKLOG.md` for a curated list of gaps. Note the file path (e.g. `raw/Theory/protocol/musig2.md`) and any `url:` field in its frontmatter. That URL is what goes into `sources:`. If there's no `url:` field, `sources: []` — never fabricate one.

### Step 3 — Run the ingest prompt

With your agent session open at the repo root, use this prompt:

```
Read CLAUDE.md and docs/PAGE-ENHANCEMENT-STANDARD.md in full first.

Then ingest raw/[PATH TO FILE] into both wiki layers:
- wiki-en/[CATEGORY]/[SLUG].md
- wiki-ru/[CATEGORY]/[SLUG].md

Rules:
- Both pages are INDEPENDENT syntheses from the same raw/ source — not translations of each other
- Use only the url: field from the source file's frontmatter to populate sources: — if none exists, set sources: []
- Never fabricate 21ideas.org URLs
- Verify all [[en/...]] and [[ru/...]] wikilink targets exist before adding them
- Follow the full frontmatter schema and tag allowlist from CLAUDE.md
- After writing both files, update wiki-en/index.md and wiki-ru/index.md
- Run: python3 tools/lint.py --layer both
- Report the lint result and list any wikilinks you couldn't verify
```

The agent reads the source file, checks existing pages for valid link targets, writes both wiki files, updates the indexes, and runs lint — all in one session. Review the diff before committing.

### Step 4 — Review the output

Check the diff carefully:

- [ ] No fabricated 21ideas.org URLs — if unsure, search [21ideas.org](https://21ideas.org) to confirm the URL resolves
- [ ] All `[[en/...]]` targets exist as files in `wiki-en/`
- [ ] All `[[ru/...]]` targets exist as files in `wiki-ru/`
- [ ] Tags are all on the allowlist (defined in `CLAUDE.md`)
- [ ] `reviewed:` is the last frontmatter field in both files
- [ ] No `#` heading in body, no `---` in body, no `raw/...` citations
- [ ] Lint passes: `python3 tools/lint.py --layer both` reports 0 issues

If lint reports issues, ask the agent to fix them before committing.

### Step 5 — Open a PR

```bash
git add wiki-en/[CATEGORY]/[SLUG].md wiki-ru/[CATEGORY]/[SLUG].md wiki-en/index.md wiki-ru/index.md
git commit -m "ingest: [slug] (both layers)"
git push origin contribute/[slug]
```

Open a PR against `main`. Title format: `ingest: [slug] (both layers)` or `enhance: wiki-ru/[path]`.

Include in the PR description:
- Which `raw/` file(s) the page is grounded in
- Whether both layers are covered, or one is missing and why
- The lint result (paste the `tools/lint.py` output)

---

## Frontmatter quick reference

```yaml
---
title: "MuSig2"
category: "concepts"
quality: "synthesized"
sources: ["https://21ideas.org/musig2"]
synthesized_date: "2026-04-12"
completeness: "high"
language: "en"
tags: [bitcoin, wiki, concept, protocol, multisig]
reviewed: "2026-04-12"
---
```

Full schema and all rules: `CLAUDE.md`.

---

## What makes a good contribution

**Do:**
- Ground every claim in the `raw/` source material
- Add wikilinks to related concepts that already exist
- Keep the tone educational and precise — the same voice as the rest of the wiki
- Cover both language layers when possible

**Don't:**
- Invent 21ideas.org URLs
- Add tags not on the allowlist
- Treat the Russian page as a translation of the English page (or vice versa)

---

## Questions?

Open a GitHub Issue with the label `question` or join 21ideas contributors [Telegram chat](https://t.me/+DVlyZlInKfBkY2M0).

---

## Support

⚡️ Found the project useful? [Zap](https://zapmeacoffee.com/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) [Tony](https://njump.me/npub10awzknjg5r5lajnr53438ndcyjylgqsrnrtq5grs495v42qc6awsj45ys7) a coffee.