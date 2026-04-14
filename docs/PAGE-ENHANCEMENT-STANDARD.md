> **⚠ Superseded.** This document has been replaced by `docs/ENHANCE-SKILL.md`.
> It is kept here for historical reference only. Use `ENHANCE-SKILL.md` for all
> new enhancement work.

# Page Enhancement Standard — 21ideas Bitcoin Wiki

> Superseded by docs/ENHANCE-SKILL.md — kept for historical reference.

This document defines the exact rules and prompt used to polish individual pages in the wiki.

## How to use
When asking Cursor (or any agent) to improve a page, paste the **Full Reusable Prompt** below and specify the page path.

## Full Reusable Prompt for Cursor

```markdown
You are editing a single page in the 21ideas Bitcoin Wiki.

**Page to edit:** [INSERT FULL PATH HERE, e.g. wiki-ru/concepts/aml.md]

**Reference style examples:**
- RU: `wiki-ru/concepts/address-types.md` — balanced wikilinks, pipe-syntax nav section (`## Дополнительные материалы`), no redundant "terms" sections.
- RU: `wiki-ru/concepts/bitcoin-node.md` — reader-facing provenance: paragraphs tie to 21ideas.org via normal markdown links, not `raw/...` paths in the body.
- EN: `wiki-en/` pages have not yet been enhanced — treat this run as the first enhancement pass. A well-formed EN page must match the same structural rules as the RU reference pages, with `[[en/...]]` links, `## Related pages`, and `## Sources` at the bottom.

**Task 0 — Pre-edit mechanical scan (wiki-en pages only)**

Before touching content, scan the page for these known EN legacy antipatterns and fix them all mechanically:

- `source:` (singular, unquoted) → rename to `sources:` and convert value to inline array: `sources: ["https://..."]`
- `sources:` as block YAML list (with `  - url` lines) → collapse to inline array: `sources: ["url1", "url2"]`
- `*Tags: ...*` italic tag line at the top of the body → remove entirely
- `# Title` heading at the top of the body → remove (Quartz renders the frontmatter `title` as the page heading)
- `---` horizontal rules in the body → remove all of them; separate sections with `##` headings and blank lines
- Inline `raw/...` citations (e.g. `` `raw/Practice/...` `` or `Source: raw/...`) → remove or replace with a 21ideas.org URL if one exists in `sources:`
- `## Related Terms` section → rename to `## Related pages` and convert to pipe-syntax wikilinks
- Triple-bracket links `[[en/concepts/foo]]]` → strip the extra `]` to get `[[en/concepts/foo]]`
- Any `[[wiki-en/...]]` or `[[wiki-ru/...]]` prefixes → fix to `[[en/...]]` or `[[ru/...]]`
- Missing `reviewed:` field → add `reviewed: "YYYY-MM-DD"` as the **last** frontmatter field
- Unquoted scalar frontmatter fields → add double quotes to all scalar values
- Frontmatter field order wrong → reorder to the canonical sequence (see Task 1)

**Tasks (apply all of them):**

1. **Frontmatter Standardization**
   Ensure the frontmatter follows this exact field order and includes all required fields:

   **String quoting (Quartz / GitHub Pages):** Use **double-quoted** YAML strings for every scalar text field (`title`, `category`, `quality`, `language`, `completeness`, `synthesized_date`, `updated`, `reviewed`). This avoids edge cases with colons, parentheses, or Unicode in titles and keeps parsing consistent across Obsidian, Quartz, and static generators. `tags` stays a flow sequence of bare identifiers: `tags: [bitcoin, wiki, concept]` (see CLAUDE.md Tags Policy). Each URL in `sources` must be a quoted string inside an inline array.

   **Canonical field order (enforce strictly):**
   `title` → `category` → `quality` → `sources` → `synthesized_date` → `completeness` → `language` → `tags` → `updated` (optional) → `reviewed` (required, always last)

   **Last frontmatter field:** The **final** key in every enhanced page's frontmatter **must** be **`reviewed: "YYYY-MM-DD"`** — the date of the last maintainer review pass. If `updated` is present, order is `tags` → `updated` → `reviewed`.

   ```yaml
   ---
   title: "Page title"
   category: "concepts"         # one of: concepts | entities | books | series | history | philosophy | practice | topics
   quality: "reference"         # one of: canonical | reference | synthesized | stub
   sources: ["https://21ideas.org/..."]   # or [] only if no URL exists in raw/; never fabricate sources
   synthesized_date: "2026-04-XX"
   completeness: "high"         # one of: high | medium | low
   language: "en"               # "en" for wiki-en/ pages; "ru" for wiki-ru/ pages
   tags: [bitcoin, wiki, concept, protocol]   # STRICT allowlist: CLAUDE.md (never invent tags)
   updated: "2026-04-XX"        # optional — last edit in this workflow
   reviewed: "2026-04-XX"       # required — MUST be the last field before the closing ---
   ---
   ```

   Tag selection guide (choose 1–3 in addition to `bitcoin` + `wiki`, total 3–8 tags):
   - If it's a **core protocol/mechanism** page: prefer `concept`, `protocol` (+ `security` / `privacy` / `scaling` when central)
   - If it's **historical context / precursors**: prefer `concept`, `history` (+ `protocol` if mechanism-heavy)
   - If it's an **entity** page: prefer `entity` (plus 0–2 of `history`, `philosophy`, `economics`, etc. when central)
   - If it's a glossary/reference index: use `glossary` (only when the page is actually a glossary)

2. **Wikilinking**
   Wikilinking quality is a primary deliverable of this workflow. Be deliberately thorough: scan the entire page end-to-end and do not miss obvious opportunities to add a relevant wikilink to key terms, core concepts, and named entities (people, orgs, protocols). Add links sparingly (first meaningful mention), but never leave important nouns unlinked simply because they "feel obvious".

   Before adding any link, verify that the target page (or glossary heading) actually exists. Never create links to missing pages or anchors.

   Add relevant wikilinks using a two-pass sweep:

   Pass A — Concept backbone (must do):
   - Link the primary subject when first introduced
   - Link named people/orgs to existing entity pages
     - EN example: `[[en/entities/adam-back|Adam Back]]`
     - RU example: `[[ru/entities/adam-back|Адам Бэк]]`
   - Link the "spine concepts" that carry the page's meaning (examples: proof-of-work, double spend, forks, consensus, ledger)
   - Link explicitly mentioned related systems/pages when they exist (examples: b-money, Hashcash, RPOW, SegWit, Taproot)

   Pass B — Glossary sweep (must do):
   - Prefer linking to an existing dedicated concept or entity page when it exists (even if a glossary heading also exists)
   - Use glossary anchors only when no dedicated page exists for a term

   **For wiki-ru/ pages — verify exact heading in `wiki-ru/glossary.md` before linking:**
   - IMPORTANT: never assume short anchors like `#KYC` exist; always check the real heading
   - Example (correct pattern): `[[ru/glossary#Знай своего клиента (KYC)|KYC]]`
   - Glossary sweep checklist (link when the term appears on the page and the heading exists):
     - `[[ru/glossary#Нода (Узел)|узел / нода]]`
     - `[[ru/glossary#Майнер|майнер]]`
     - `[[ru/glossary#Ключ (приватный / публичный)|ключ (приватный/публичный)]]`
     - `[[ru/glossary#Криптография|криптография]]`
     - `[[ru/glossary#Консенсус Накамото|консенсус (Накамото)]]`
     - `[[ru/glossary#Реестр (Ledger)|реестр (ledger)]]`
     - `[[ru/glossary#Транзакция|транзакция]]`
     - `[[ru/glossary#Комиссия (Transaction Fee)|комиссия]]`

   **For wiki-en/ pages — verify exact heading in `wiki-en/glossary.md` before linking:**
   - IMPORTANT: The EN glossary uses `### **Term**` (bold inside heading). Markdown anchors are generated from the full heading text, lowercased, with spaces as hyphens and special characters stripped. Always read `wiki-en/glossary.md` to confirm the exact anchor before using it. Do NOT guess.
   - Glossary sweep checklist (link when the term appears and the heading exists; prefer dedicated pages):
     - node → prefer `[[en/concepts/bitcoin-node|node]]` (dedicated page exists)
     - miner → prefer `[[en/concepts/mining|miner]]` (dedicated page exists)
     - transaction → `[[en/glossary#transaction|transaction]]` if no dedicated page
     - private/public key → `[[en/glossary#key-private--public|key]]` — verify exact anchor first
     - consensus → prefer `[[en/concepts/governance|consensus]]` or verify `[[en/glossary#consensus|consensus]]`
     - ledger → `[[en/glossary#ledger|ledger]]` — verify anchor
     - transaction fee → `[[en/glossary#transaction-fee|fee]]` — verify anchor
     - UTXO → prefer `[[en/concepts/utxo|UTXO]]` (dedicated page exists)

   General rules:
   - Never create a link to a page or anchor that does not currently exist.
   - Link a term the first meaningful time it appears; do not repeat the same link on one page unless context is significantly different.
   - Mechanical link hygiene is allowed and expected: fix malformed links (e.g. `[[...||text]]`, `]]]` triple brackets), wrong prefixes, or broken wikilink syntax.

3. **Section Handling**
   - Completely remove any "terms" section if it exists (examples: `## Термины`, `## Terms`, `## Related Terms`, `## Связанные термины`).
   - Do **not** add a `#` heading to the page body. Quartz uses the frontmatter `title` field as the page heading. Start the body directly with `##` sections. If a `# Title` heading already exists in the page, remove it.
   - Do **not** use Markdown **horizontal rules** (`---` alone on a line) in the **page body**. The only `---` allowed is the YAML frontmatter delimiter at the very top of the file. In the body, `---` renders as an `<hr>` and adds noise in Obsidian/Quartz; separate blocks with `##` headings and blank lines instead.
   - Ensure there is a single bottom navigation section named:
     - For `wiki-en/`: `## Related pages`
     - For `wiki-ru/`: `## Дополнительные материалы`
   - Convert that section to clean pipe links, preserving the meaning of the existing descriptions:
     - `- [[en/concepts/foo|Descriptive text]]` (EN) or `- [[ru/concepts/foo|Описание]]` (RU)

4. **Language-specific linking**
   - In wiki-en/ pages: use `[[en/...]]` links only
   - In wiki-ru/ pages: use `[[ru/...]]` links only
   - NEVER use `[[wiki-ru/...]]` / `[[wiki-en/...]]` prefixes. Those are invalid in this vault and must be removed/fixed.

5. **Reader-facing sources (no `raw/` paths in the page body)**
   - Do **not** place per-paragraph provenance like `` `raw/...` `` or "Source: raw/…" in wiki pages meant for readers (Obsidian publish / Quartz). Those paths are not clickable for most readers and duplicate what already belongs in workflow metadata.
   - **While editing**, agents still ground claims in `raw/` per `CLAUDE.md`; that is author workflow, not the reader-facing citation layer.
   - Avoid third-party links. Use reader-facing links **only** to `https://21ideas.org/...`.
   - Prefer linking sources directly in the paragraph text where it fits naturally and does not require you to infer extra claims.
   - If inline linking would be awkward, add a short provenance line immediately after the paragraph that used those sources (maximum 1–2 such lines per page):
     - EN pages: `Source: [title](https://21ideas.org/...)`
     - RU pages: `Основа: [название](https://21ideas.org/...)`
   - Every `https://21ideas.org/...` URL cited inline must already appear in YAML `sources:` and in the bottom sources section (deduplicated). Never fabricate URLs.
   - If no public 21ideas URL exists for a claim, keep `sources: []` in frontmatter only; do not invent a pretty link.
   - The bottom sources section must be named:
     - EN pages: `## Sources`
     - RU pages: `## Источники`

   Markdown tables:
   - Keep existing table formatting unless it is actually broken. Do not "reformat to satisfy a linter" if it changes readability or semantics.

**Important constraints:**
- Do not change the **substantive** wording, headings, tables, or meaning — except where task (5) asks to **replace** `raw/...` citations with `https://21ideas.org/...` links (or add such links) without altering claims.
- Keep the tone educational, precise, and consistent with the rest of the wiki.

After editing, output:
- The full updated Markdown content of the page.
- A short summary of changes: which wikilinks were added, tags updated, frontmatter standardized, sections modified, legacy antipatterns fixed, and (if applicable) how reader-facing `21ideas.org` citations replaced or complement `raw/` mentions.

Pre-flight checklist (must pass before you finish):
- Frontmatter ends with **`reviewed: "YYYY-MM-DD"`** as the **last** field (after `updated` if present).
- Frontmatter fields are in canonical order: `title → category → quality → sources → synthesized_date → completeness → language → tags → updated? → reviewed`.
- All scalar frontmatter fields are double-quoted strings; `tags` is a bare flow sequence; `sources` is an inline array of quoted strings.
- No `source:` (singular) field anywhere — it must be `sources: [...]`.
- No `*Tags: ...*` italic tag line in the body.
- No `#` heading anywhere in the page body (Quartz uses frontmatter `title`; body starts with `##`).
- No standalone `---` horizontal rules anywhere in the page body (YAML opening/closing frontmatter excepted).
- No `raw/...` citations in the page body (replace with reader-facing 21ideas.org links, or remove).
- No `[[wiki-ru/...]]` or `[[wiki-en/...]]` links anywhere.
- No `]]]` triple-bracket links anywhere.
- For wiki-en pages: all internal links start with `[[en/...]]`; for wiki-ru pages: `[[ru/...]]`.
- Bottom nav section is `## Related pages` (EN) or `## Дополнительные материалы` (RU) — not `## Related Terms` or any other variant.
- Bottom sources section is `## Sources` (EN) or `## Источники` (RU).
- Every 21ideas URL used inline is included in YAML `sources:` and in the bottom sources section (deduplicated).
- Wikilinking passes completed: backbone sweep + glossary sweep; no obvious missed links for key terms/concepts/entities.

Work only on this one page.
```
