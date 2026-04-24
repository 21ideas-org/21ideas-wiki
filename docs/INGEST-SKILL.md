# INGEST-SKILL — Raw Source Ingestion for 21wiki

This skill turns an article URL or pasted content into a properly formatted `raw/` file in the correct subdirectory. It covers one task only: getting source material into `raw/`. Wiki page generation from `raw/` is a separate step — see `docs/WIKI-SKILL.md`.

**Tools required:** Cursor or Claude Code with file-write access to the repo. **Scripts used:** `tools/check_duplicate.py`, `tools/derive_slug.py`, `tools/check_series.py` — see `tools/README.md` for interface reference.

---

## Zero-tolerance rules

These apply before anything else. No exceptions.

1. **Never translate the article body.** The raw/ file preserves the original author's exact words. If the article is in Russian, the file body is in Russian. If in English, English. Translation is out of scope for this skill.
2. **Never fabricate the `url:` field.** Use only the canonical URL provided by the contributor. If no URL is available, leave `url:` empty and warn.
3. **Never modify existing `raw/` files.** If a duplicate is found, stop and report — do not overwrite or merge.
4. **Never summarize or paraphrase** the article body. Clean it, preserve it.
5. **Never ingest the same URL twice.** Run `check_duplicate.py` before writing.
6. **Never add wiki-layer content here.** `raw/` files are source material only — no `[[wikilinks]]`, no `## Related pages`, no Quartz-specific formatting.
7. **Never fetch or reconstruct article body content independently.** The body must come from the contributor's paste only. If no paste has been provided, ask for it — do not proceed.

---

## Input

The contributor provides:

|Field|Required|Notes|
|---|---|---|
|Content (pasted article text, preferably markdown)|**Yes**|Paste the full article text from the title to the last line, including tables, footnotes, and closing notes. Markdown format preferred (e.g. copied from reader mode or a markdown-rendered view).|
|URL|**Yes**|Always required, even when pasting content — cannot be inferred from pasted text reliably.|
|Author|No|Agent infers from article if not provided. If the contributor provided an author name in their prompt, use it as-is — do not override with what the agent infers from the article.|
|Series context|No| Agent detects automatically via `check_series.py`. If the contributor specified series name and part number, use it as-is — do not override. |
| Published | No | Publication date as YYYY-MM-DD. If the contributor supplied it, use it as-is. If not provided and not visible in the article, omit the `date:` field entirely — do not guess. |

If the contributor has not pasted content, ask for it before proceeding. Do not attempt to fetch or reconstruct the article body independently.

---

## Step-by-step execution

### Step 1 — Build source inventory from pasted content

Before writing anything, read the pasted content and produce a structural inventory:

```
Pre-heading content: [YES/NO] — if YES, first sentence: "..."
Headings (in order):
  ## Heading one
    ### Sub-heading
  ## Heading two
  ...
Post-heading content: [YES/NO] — if YES, first sentence: "..."
Tables: [count] — list first-row content of each
Blockquotes: [count] — list first 8 words of each
Approximate word count: [N]
```

This inventory is the ground truth. Every item must appear in the written `raw/` file. Any item missing from the file is a hard stop — do not proceed to wiki ingest.

### Step 2 — Duplicate check (script)

```bash
python3 tools/check_duplicate.py --url "<URL>"
```

- `CLEAR` → proceed
- `DUPLICATE: raw/path/to/file.md` → stop, report the existing file to the contributor, do not proceed
- `SLUG_CONFLICT` → proceed but note the conflict; the filename will need manual adjustment in Step 5

### Step 3 — Classify the source

Read the article content and determine the primary subdirectory using this lookup table. When content spans two categories, pick the primary one and record the secondary in `tags`.

|Content type|Subdirectory|
|---|---|
|Bitcoin monetary theory, economics, Austrian school, inflation, deflation, monetary history|`raw/Theory/economics/`|
|Protocol mechanics: UTXO, opcodes, addresses, upgrades, SegWit, Taproot, mining, difficulty|`raw/Theory/protocol/`|
|Philosophy, culture, manifestos, cypherpunk thought, sovereignty|`raw/Theory/philosophy/`|
|History: events, legal cases, exchange histories, regulatory milestones|`raw/Theory/history/`|
|Biographical / entity-focused articles (people, organizations)|`raw/Theory/entities/`|
|Privacy tools, techniques, chain analysis, CoinJoin, KYC|`raw/Theory/privacy/`|
|Security: key management, custody, hardware wallets, seed phrases|`raw/Theory/security/`|
|Lightning Network — theory, how it works, channel mechanics|`raw/Theory/lightning/`|
|Long-horizon scenarios, hyperbitcoinization, future speculation|`raw/Theory/future/`|
|Book chapters|`raw/Books/<book-name>/`|
|Practical guides — self-custody, cold storage, hardware setup|`raw/Practice/hodl/`|
|Practical guides — Lightning wallets, nodes, liquidity|`raw/Practice/lightning/`|
|Practical guides — privacy tools in practice, Tor, CoinJoin workflows|`raw/Practice/privacy/`|
|Practical guides — buying Bitcoin, P2P exchanges|`raw/Practice/buy/`|
|Practical guides — operational security, passphrase, multisig setup|`raw/Practice/security/`|
|Practical guides — interacting with Bitcoin ecosystem, explorers, nodes|`raw/Practice/interact/`|
|Introductory content, onboarding guides, glossary source material|`raw/Start/`|

**Ambiguous cases:** If genuinely unclear between two categories, prefer `Theory/` over `Practice/` for conceptual articles, and `protocol/` over `economics/` for articles that explain a mechanism (even if they discuss economic implications).

### Step 4 — Derive the filename (script)

```bash
python3 tools/derive_slug.py "<URL>"
```

Use the output as the filename base. Append `.md`.

**Exceptions — use a manual filename when:**
- The article is a book chapter → use `chapter-N-book-name.md` with a shortened book name if applicable 
- The script returns an empty slug (non-ASCII path segment) → derive from the article title manually: lowercase, hyphenated, ASCII only
- A `SLUG_CONFLICT` was reported in Step 2 → append `-2` or a disambiguating word

Run the duplicate check again with the slug and subdir to confirm no path conflict before writing:

```bash
python3 tools/check_duplicate.py --url "<URL>" --slug "<slug>" --subdir "<Theory/protocol>"
```

### Step 5 — Clean the content

**Strip all of the following** from the pasted or fetched content:

- Site header, navigation bar, breadcrumbs
- Footer (links, copyright, social icons)
- "Related articles" / "You might also like" blocks
- Subscription prompts, newsletter signup forms
- Cookie consent banners
- Comment sections
- Social sharing buttons
- Any repeated site chrome that is not part of the article itself

**Preserve exactly:**

- Article title (keep as `# Title` at the top of the body — raw/ files are not Quartz pages, so a `#` heading is fine here)
- All body sections, headings, and subheadings
- Blockquotes, code blocks, tables, footnotes
- Images references (keep alt text, drop src if it's a CDN path that won't resolve; note `[image: description]` instead)
- The author's original formatting and paragraph structure
- All original hyperlinks in the body (these are source material)

**VERBATIM RULE:** The body of the `raw/` file must be a character-level faithful copy of the pasted content after chrome removal. Do not rewrite sentences. Do not compress or merge paragraphs. Do not omit sections that seem redundant or off-topic — curation happens at the wiki layer, not during `raw/` ingest. The only permitted changes are: stripping site chrome (as listed above), converting HTML entities to Unicode, and normalizing heading levels if inconsistent.

**Normalization:**

- Convert HTML entities to proper Unicode characters (`&amp;` → `&`, etc.)
- Normalize heading levels if the article uses inconsistent jumps (e.g. `##` directly to `####`) — but do not change the author's intended hierarchy
- Preserve original language throughout — do not translate any word, phrase, heading, or caption

### Step 6 — Build the frontmatter

```yaml
---
title: "<Article title — exact, from the article's h1>"
author: "<Original author name>"
url: "<Canonical URL as provided by contributor — verbatim>"
source_domain: "<domain only, e.g. 21ideas.org>"
category: "<e.g. theory/protocol>"
language: "<en, ru, fr, etc. — the article's original language>"
tags: [descriptive, free-form, tags]
date: "<YYYY-MM-DD publication date if known, else omit>"
---
```

**Field notes:**

- `title` — copy from the article's `<h1>` or page title exactly. Do not rewrite or translate.
- `author` — original author of the content, not a translator or republisher. For 21ideas articles that are adaptations, use the original author's name if credited; otherwise use `"21ideas"`.
- `url` — use the URL exactly as the contributor provided it. Do not reconstruct, normalize, or guess. If the contributor did not provide a URL and fetch failed, set `url: ""` and add a comment line `# url unknown — verify before wiki ingest`.
- `source_domain` — the bare domain, no protocol or path. Used for provenance classification downstream.
- `category` — the subdirectory path relative to `raw/`, lowercase, forward slashes. E.g. `theory/protocol`, `practice/hodl`, `books/fiat-standard`.
- `language` — the language the article is written in, not the language the wiki page will be written in. `en` or `ru` for the vast majority of cases.
- `tags` — free-form descriptive tags for this raw file. These are NOT the wiki allowlist tags. Use whatever is useful for search and classification. Examples: `[taproot, schnorr, protocol-upgrade, bip340]`
- `date` — publication date if visible on the article. Omit the field entirely if unknown rather than guessing.
- `series` and `part` — add only if Step 7 confirms a series. See below.

### Step 7 — Series check (script)

Write the file first (Step 8), then run:

```bash
python3 tools/check_series.py raw/<subdir>/<filename>.md
```

- `NO_SERIES` → nothing to do
- `SERIES_DETECTED` → include the full output block in your verification report to the contributor (see Step 9). Do not block or branch — just report. If confirmed as a series, add `series:` and `part:` to the frontmatter as a follow-up edit.

### Step 8 — Write the file

Write the cleaned content with the frontmatter to the target path:

```
raw/<Subdirectory>/<slug>.md
```

The file structure is:

```
---
<frontmatter>
---

# Article Title

<cleaned article body — verbatim, original language>
```

Do not add anything after the body. No wiki navigation, no wikilinks, no `## Sources` section — those belong in wiki pages, not raw/ files.

### Step 9 — Verification report

Output this block after writing the file. Do not skip it.

```
✓ Created: raw/<subdir>/<slug>.md
  Title:    <article title>
  Author:   <author>
  URL:      <url>
  Language: <en|ru>
  Category: <category>
  Subdir:   raw/<subdir>/
  Slug:     <slug>

  Duplicate check: CLEAR
  Slug conflict:   <CLEAR or note>

  Section & content inventory:
    [PRE-HEADING]  in source: YES/NO → in file: [x]/[ ]
    [## Heading]   blocks in source: N → in file: N  [x]/[ ]
    ... (one row per heading)
    [POST-HEADING] in source: YES/NO → in file: [x]/[ ]
    Tables: source N / file N  [x]/[ ]
    Blockquotes: source N / file N  [x]/[ ]

  Any [ ] item is a blocking issue — rewrite the file before proceeding.

  <If SERIES_DETECTED — paste full check_series.py output here>

Next step:
  To generate wiki pages from this file, run the wiki ingest workflow:
  → See CLAUDE.md "Ingest" section, or docs/WIKI-SKILL.md
  → File path to use: raw/<subdir>/<slug>.md
```

If `url:` is empty or unverified, add a warning line:

```
  ⚠ url: field is empty — verify the canonical URL before running wiki ingest.
    Without it, wiki pages will have sources: [] and no reader-facing citation.
```

---

## Quick reference — common classification calls

These come up often enough to be worth stating explicitly:

- **"What is X?" explanatory articles** → `Theory/` in the relevant subcategory
- **"How to do X" step-by-step guides** → `Practice/` in the relevant subcategory
- **Person profiles, obituaries, interviews** → `Theory/entities/`
- **BIP specifications** → `Theory/protocol/`
- **Legal cases, regulatory events** → `Theory/history/`
- **Academic papers on Bitcoin cryptography** → `Theory/protocol/` or `Theory/security/`
- **"Bitcoin vs X" comparison articles** → classify by the primary Bitcoin concept being explained (usually `Theory/economics/` or `Theory/protocol/`)
- **Newsletter issues (Bitcoin Optech, etc.)** — ingest individual topic sections as separate files, not the full newsletter

---

## What this skill does NOT do

- Does not generate `wiki-en/` or `wiki-ru/` pages — that is the wiki ingest workflow in `CLAUDE.md`
- Does not enforce source acceptance policy — that is `CONTRIBUTING.md` and PR review
- Does not translate content — ever
- Does not summarize or condense the article
- Does not update `docs/log.md` — the maintainer logs raw/ additions manually or as part of the subsequent wiki ingest step