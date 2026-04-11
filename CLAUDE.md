# 21ideas Bitcoin Wiki — Agent Rules

A bilingual (EN + RU) Bitcoin education wiki built from immutable source files in `raw/` — all from 21ideas.org, a Russian-language Bitcoin education site (~308 files). Content is grounded in `raw/` material only. Agents write and maintain `wiki-en/` and `wiki-ru/`; humans curate `raw/`. The wiki is read in Obsidian and published via Quartz.

---

## What Agents Must NOT Do

- **Never fabricate 21ideas.org URLs.** If no URL exists in `raw/` metadata, set `sources: []`.
- **Never invent tags** outside the allowlist below.
- **Never write bare wikilinks** (`[[taproot]]`, `[[concepts/taproot]]`) — always use `[[en/...]]` or `[[ru/...]]` prefixes.
- **Never use `[[wiki-ru/...]]` or `[[wiki-en/...]]` prefixes** — they are invalid in this vault.
- **Never modify `raw/` files.**
- **Never cite `raw/...` paths in page body text** — only 21ideas.org URLs are reader-facing.
- **Never treat `wiki-ru/` as a translation of `wiki-en/`.** Both are independent syntheses from the same sources.
- **Never use `---` horizontal rules in the page body.** Only YAML frontmatter delimiters are permitted.
- **Never open the page body with a `#` heading.** Quartz uses the frontmatter `title` field as the page title. Start the body directly with `##` sections.

---

## Frontmatter Schema

Every wiki page requires all fields below. Use **double-quoted** strings for every scalar field; `tags` is an unquoted flow list; `sources` is an inline array of quoted strings.

```yaml
---
title: "Page title"
category: "concepts"        # concepts | entities | books | series | history | philosophy | practice | topics
quality: "reference"        # canonical | reference | synthesized | stub
sources: ["https://21ideas.org/..."]  # real URLs only; [] if none exist in raw/ metadata
synthesized_date: "2026-04-XX"
completeness: "high"        # high | medium | low
language: "ru"              # en | ru
tags: [bitcoin, wiki, concept, protocol]
updated: "2026-04-XX"       # optional: date of last edit pass
reviewed: "2026-04-XX"      # required on enhanced pages; MUST be the last frontmatter field
---
```

**Field order enforced:** `tags` → `updated` (optional) → `reviewed` (last, required on enhanced pages).

---

## Tags — Strict Allowlist

Every page must include **at least** `bitcoin` and `wiki`. Total: 3–8 tags. Lowercase, hyphenated only.

**Core (always):** `bitcoin`, `wiki`

**Category (pick relevant):** `concept`, `entity`, `glossary`, `protocol`, `economics`, `history`, `philosophy`, `security`, `privacy`, `governance`, `scaling`, `mining`

**Page type (when applicable):** `synthesized`, `reference`, `stub`

**Specific (when relevant):** `utxo`, `lightning`, `bip`, `node`, `fork`, `censorship-resistance`, `decentralization`, `double-spend`, `difficulty-adjustment`, `third-party`, `whitepaper`, `aml`, `addresses`, `multisig`, `taproot`, `segwit`

---

## Wikilink Discipline — CRITICAL

| Layer | Required prefix | Example |
|---|---|---|
| `wiki-en/` | `[[en/...]]` | `[[en/concepts/taproot\|Taproot]]` |
| `wiki-ru/` | `[[ru/...]]` | `[[ru/concepts/taproot\|Taproot]]` |

- Bare links (`[[taproot]]`) and `[[wiki-ru/...]]` / `[[wiki-en/...]]` are always wrong.
- Before adding any link, verify the target page exists. Never link to a missing page or anchor.
- For glossary anchors: verify the exact heading in `glossary.md` before linking (e.g. `[[ru/glossary#Нода (Узел)|нода]]`).

---

## Style & Sources

- **Tone:** Clear, precise, neutral but firm on Bitcoin's monetary sovereignty and censorship resistance.
- **No `#` heading in the page body.** Quartz renders the frontmatter `title` as the page heading. Start the body with `##` sections.
- **Sources section:** Every page must end with `## Sources` (wiki-en) or `## Источники` (wiki-ru) listing all 21ideas.org URLs used.
- **Inline citations:** Use 21ideas.org URLs in text or as `Основа: [title](https://21ideas.org/...)` after paragraphs. No `raw/...` paths.
- **Closing nav section:** Every page ends with `## Related pages` (EN) or `## Дополнительные материалы` (RU) using pipe-syntax wikilinks: `- [[ru/concepts/segwit|SegWit]]`.
- **Remove `## Related Terms` sections** wherever found; replace with pipe-syntax wikilinks in the closing nav section.
- **Trust marker:** Set `quality: "synthesized"` for synthesis pages. Flag remaining gaps explicitly.

---

## Directory Map

```
raw/                        ← IMMUTABLE source of truth — never edit
  Books/                    ← Book chapters (one subfolder per book)
  Theory/
    economics/              ← Money, Cantillon, deflation, GTS series, Discovering Bitcoin
    protocol/               ← UTXO, Taproot, SegWit, difficulty, governance
    philosophy/             ← Culture, manifestos, What I Learned From Bitcoin
    history/                ← Genesis Files, Silk Road
    privacy/                ← AML, CoinJoin, OXT (oxt/ subfolder)
    security/               ← Seeds, passphrase, MuSig2
    lightning/              ← Lightning theory
    future/                 ← Bitcoin Astronomy and long-horizon scenarios
  Practice/
    hodl/ lightning/ privacy/ buy/ security/ interact/
  Start/                    ← Intro guides and glossary source

wiki-en/                    ← English wiki (synthesized from raw/)
  concepts/ entities/ books/ series/ history/ philosophy/ practice/ topics/
  index.md  overview.md  glossary.md

wiki-ru/                    ← Russian wiki (independent synthesis from raw/)
  concepts/ entities/ books/ series/ history/ philosophy/ practice/ topics/
  index.md  overview.md  glossary.md

docs/
  log.md                    ← Append-only operations log; update after every operation
  lint-report.md            ← Current lint pass results; overwrite on each lint run
  PAGE-ENHANCEMENT-STANDARD.md  ← Full single-page enhancement prompt + checklist
  WIKI-GUIDE.md             ← Human-facing guide
  WIKI-BACKLOG.md           ← Short-lived backlog

tools/
  lint.py                   ← Mechanical lint (wikilinks, frontmatter shape, tags); stdlib only
```

---

## Recurring Operations

### Ingest (new raw/ source → wiki pages)

1. Read the new `raw/` file(s). Do not modify them.
2. Check `wiki-en/index.md` and `wiki-ru/index.md` for pages to create or update.
3. Write pages independently for each layer from the same `raw/` sources.
4. Apply full frontmatter schema; populate `sources:` with real 21ideas.org URLs from raw/ metadata.
5. Verify all wikilinks use the correct layer prefix.
6. Update `wiki-en/index.md` and `wiki-ru/index.md`.
7. Append to `docs/log.md`:
   ```
   ## [YYYY-MM-DD] ingest | <title or batch name>
   **Layers:** Both | EN | RU
   **Created/Updated:** list of slugs
   **Lint:** brief result
   ---
   ```

### Enhance (single page)

Read `docs/PAGE-ENHANCEMENT-STANDARD.md` in full before starting. After applying the standard:

1. Confirm `reviewed: "YYYY-MM-DD"` is the **last** frontmatter field.
2. Confirm: no `---` in body, no `#` heading in body, no `raw/...` in body, no `[[wiki-ru/...]]` / `[[wiki-en/...]]` prefixes.
3. Do not update `index.md` unless the title or category changed.
4. Append to `docs/log.md`:
   ```
   ## [YYYY-MM-DD] enhance | <page path>
   Changes: <wikilinks added, frontmatter fixed, sections modified>
   ---
   ```

### Lint (full bilingual pass)

Run a complete pass across **both** `wiki-en/` and `wiki-ru/` in one session.

**Standardized runner (preferred):** from the repo root,

```bash
python3 tools/lint.py --layer both          # stdout summary; both trees
python3 tools/lint.py --layer ru            # targeted: wiki-ru/ only
python3 tools/lint.py --layer en            # targeted: wiki-en/ only
python3 tools/lint.py --layer both --write-report   # also overwrite docs/lint-report.md
python3 tools/lint.py --strict              # exit 1 if any mechanical issue exists (CI / gates)
python3 tools/lint.py --strict-links        # exit 1 only on wrong wikilink prefix or broken target
```

The script implements the **mechanical** checks below (wikilink prefix, broken `[[en/...]]` / `[[ru/...]]` targets, block `sources:`, standalone `---` and `#` in body, `raw/` in body, required frontmatter keys, `reviewed`, tags vs allowlist). It does **not** check orphans, `index.md` coverage, or EN/RU content parity — those remain human review. **Keep `ALLOW_TAGS` in `tools/lint.py` in sync** with the **Tags — Strict Allowlist** section below when the allowlist changes.

**Note:** `wiki-en/` is not yet fully enhanced; a full `--layer both` run will report many EN issues until that layer is brought up to the same standard as `wiki-ru/`.

**Scope vs `docs/lint-report.md`:** `--write-report` overwrites the **single** report file. Match `--layer` to the task: use `--layer ru` for RU-only work, `--layer both` when you want one bilingual snapshot. The `_Last pass: … (scope)_` line records which layers were scanned.

**Report language:** `docs/lint-report.md` MUST be **English** (headings, table column labels, section titles, suggested follow-ups). File paths stay as in the repo; when citing snippets from vault pages (e.g. a Russian `title` or heading), quote them **verbatim** inside English prose.

**Mechanical checks — auto-fix allowed:**
- [ ] All pages have every required frontmatter field
- [ ] All `wiki-ru/` links use `[[ru/...]]`; all `wiki-en/` links use `[[en/...]]`
- [ ] No `[[wiki-ru/...]]` or `[[wiki-en/...]]` anywhere
- [ ] No tags outside the allowlist
- [ ] All scalar frontmatter fields are double-quoted strings
- [ ] `sources:` is an inline array (`sources: ["..."]`), not block YAML

**Content checks — flag for human review only:**
- [ ] Orphan pages (no incoming wikilinks)
- [ ] Pages missing from their layer's `index.md`
- [ ] `sources: []` pages — intentional?
- [ ] Significant EN/RU content divergence for the same slug
- [ ] `raw/...` paths in body text
- [ ] `---` horizontal rules in body
- [ ] `#` headings in body (should not exist — Quartz uses frontmatter title)
- [ ] `## Related Terms` sections (should be `## Related pages` / `## Дополнительные материалы`)

**Output (agents):**
1. Prefer running the tool with `--write-report` so the report stays consistent:
   ```bash
   python3 tools/lint.py --layer ru --write-report      # targeted RU
   python3 tools/lint.py --layer both --write-report    # full bilingual snapshot
   ```
2. Overwrite `docs/lint-report.md` with **English** prose (the script output is already English; if you hand-edit or supplement the file, keep the same language rule).
3. Append to `docs/log.md`:
   ```
   ## [YYYY-MM-DD] lint | Full bilingual pass (or: targeted — <scope>)
   Auto-fixed: <list>
   Flagged for review: <list>
   ---
   ```

### Query / Research

1. Read the relevant layer's `index.md` first to find candidate pages.
2. Drill into relevant pages; synthesize an answer with citations to 21ideas.org URLs.
3. **File the answer back as a wiki page** if it synthesizes across 3+ pages, compares concepts, or fills a documented gap. Apply full frontmatter; update index; append log entry.
4. If it is a one-off chat answer, no log entry needed.

---

## Bilingual Parity Rules

- `wiki-en/` and `wiki-ru/` are **independent syntheses** — not translations of each other.
- **Parity means:** same slug exists in both layers and core facts/conclusions are conceptually aligned.
- **Current state:** `wiki-ru/concepts/` and `wiki-ru/entities/` are enhanced. `wiki-en/` has not been enhanced yet — expect missing `reviewed:`, old-style frontmatter, `raw/...` body citations, and `## Related Terms` sections.
- **Gap handling:** If a slug exists in one layer only, flag it in `docs/lint-report.md` under "Suggested follow-ups". Create the missing page during the next ingest or lint pass.
- **Do not assume** either layer is authoritative — both must be independently grounded in `raw/`.
