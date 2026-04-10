# Page Enhancement Standard — 21ideas Bitcoin Wiki

This document defines the exact rules and prompt used to polish individual pages in the wiki.

## How to use
When asking Cursor (or any agent) to improve a page, paste the **Full Reusable Prompt** below and specify the page path.

## Full Reusable Prompt for Cursor

```markdown
You are editing a single page in the 21ideas Bitcoin Wiki.

**Page to edit:** [INSERT FULL PATH HERE, e.g. wiki-ru/concepts/aml.md]

**Reference style examples:**
- `ru/concepts/address-types.md` — balanced wikilinks, structure, `## Дополнительные материалы` (pipe syntax `[[link|descriptive text]]`), no redundant “terms” sections.
- `ru/concepts/bitcoin-node.md` — **reader-facing provenance**: paragraphs tie to original posts on 21ideas.org via normal markdown links (e.g. chapter titles or the practice article), not `raw/...` file paths in the body.

**Tasks (apply all of them):**

1. **Frontmatter Standardization**
   Ensure the frontmatter follows this exact order and includes all required fields:

   **String quoting (Quartz / GitHub Pages):** Use **double-quoted** YAML strings for every scalar text field (`title`, `category`, `quality`, `language`, `completeness`, `synthesized_date`, and optional `reviewed` / `updated`). This avoids edge cases with colons, parentheses, or Unicode in titles and keeps parsing consistent across Obsidian, Quartz, and static generators. `tags` stay a flow sequence of bare identifiers: `tags: [bitcoin, wiki, concept]` (see CLAUDE.md Tags Policy). Each URL in `sources` must be a quoted string.

   ```yaml
   ---
   title: "Page title"
   category: "concepts"   # one of: concepts | entities | books | series | history | philosophy | practice | topics
   quality: "reference"    # one of: canonical | reference | synthesized | stub
   sources: ["https://21ideas.org/..."]   # or [] only if no URL exists in raw/; never fabricate sources
   synthesized_date: "2026-04-XX"
   completeness: "high"  # one of: high | medium | low
   language: "ru"        # or "en" for wiki-en/
   tags: [bitcoin, wiki, concept, protocol]   # STRICT allowlist: CLAUDE.md (never invent tags)
   # optional workflow fields, also quoted when present:
   # reviewed: "2026-04-10"
   # updated: "2026-04-10"
   ---
   ```

   Tag selection guide (choose 1–3 in addition to `bitcoin` + `wiki`, total 3–8 tags):
   - If it’s a **core protocol/mechanism** page: prefer `concept`, `protocol` (+ `security` / `privacy` / `scaling` when central)
   - If it’s **historical context / precursors**: prefer `concept`, `history` (+ `protocol` if mechanism-heavy)
   - If it’s an **entity** page: prefer `entity` (plus 0–2 of `history`, `philosophy`, `economics`, etc. when central)
   - If it’s a glossary/reference index: use `glossary` (only when the page is actually a glossary)

2. **Wikilinking**
   Wikilinking quality is a primary deliverable of this workflow. Be deliberately thorough: scan the entire page end-to-end and do not miss obvious opportunities to add a relevant wikilink to key terms, core concepts, and named entities (people, orgs, protocols). Add links sparingly (first meaningful mention), but never leave important nouns unlinked simply because they “feel obvious”.

   Before adding any link, verify that the target page (or glossary heading) actually exists. Never create links to missing pages or anchors.

   Add relevant wikilinks using a two-pass sweep:

   Pass A — Concept backbone (must do):
   - Link the primary subject when first introduced
   - Link named people/orgs to existing entity pages (e.g. `[[ru/entities/adam-back|Адам Бэк]]`)
   - Link the “spine concepts” that carry the page’s meaning (examples: proof-of-work, ledger/реестр, публичный ключ, double spend, forks, consensus)
   - Link explicitly mentioned related systems/pages when they exist (examples: b-money, Hashcash, RPOW, SegWit, Taproot)

   Pass B — Glossary sweep (must do):
   - Prefer linking to an existing dedicated page when it exists (even if a glossary heading also exists)
   - Use `ru/glossary` on `wiki-ru/` and `en/glossary` on `wiki-en/` pages anchors for high-value primitives when no dedicated page exists
   - IMPORTANT: before adding any `[[ru/glossary#...]]` link, verify the exact heading exists in `wiki-ru/glossary.md`
     - Example (correct pattern): `[[ru/glossary#Знай своего клиента (KYC)|KYC]]`
     - Do NOT assume short anchors like `#KYC` exist.
   - Glossary sweep checklist (mechanical; link when the term appears on the page and the heading exists):
     - `[[ru/glossary#Нода (Узел)|узел / нода]]`
     - `[[ru/glossary#Майнер|майнер]]`
     - `[[ru/glossary#Ключ (приватный / публичный)|ключ (приватный/публичный)]]`
     - `[[ru/glossary#Криптография|криптография]]`
     - `[[ru/glossary#Консенсус Накамото|консенсус (Накамото)]]`
     - `[[ru/glossary#Реестр (Ledger)|реестр (ledger)]]`
     - `[[ru/glossary#Транзакция|транзакция]]`
     - `[[ru/glossary#Комиссия (Transaction Fee)|комиссия]]`

   General rules:
   - Never create a link to a page or anchor that does not currently exist.
   - Follow the balanced style from address-types.md: link a term the first meaningful time it appears.
   - Do not repeat the same link multiple times on one page unless the context is significantly different.
   - Mechanical link hygiene is allowed and expected: fix malformed links (e.g. `[[...||text]]`), wrong prefixes, or obvious broken wikilink syntax.

3. **Section Handling**
   - Completely remove any “terms” section if it exists (examples: `## Термины`, `## Terms`, `## Related Terms`, `## Связанные термины`).
   - Keep exactly one top-level heading (`# ...`) in the page body for SEO. Do not start the page body with `## ...`.
   - Ensure there is a single bottom navigation section named:
     - For `wiki-ru/`: `## Дополнительные материалы`
     - For `wiki-en/`: `## Related pages`
   - Convert that section to clean pipe links, preserving the meaning of the existing descriptions:
     - `- [[link|Descriptive text]]`

4. **Language-specific linking**
   - In wiki-en/ pages: use `[[en/...]]` links
   - In wiki-ru/ pages: use `[[ru/...]]` links
   - NEVER use `[[wiki-ru/...]]` / `[[wiki-en/...]]` prefixes. Those are invalid in this vault and must be removed/fixed.

5. **Reader-facing sources (no `raw/` paths in the page body)**
   - Do **not** place per-paragraph provenance like `` `raw/...` `` or “Источник: raw/…” in wiki pages meant for readers (Obsidian publish / Quartz). Those paths are not clickable for most readers and duplicate what already belongs in workflow metadata.
   - **While editing**, agents still ground claims in `raw/` per `CLAUDE.md`; that is author workflow, not the reader-facing citation layer.
   - Avoid third-party links. Use reader-facing links **only** to `https://21ideas.org/...`.
   - Prefer linking sources directly in the paragraph text where it fits naturally and does not require you to infer extra claims.
   - If inline linking would be awkward, add a short `Основа:` line immediately after the paragraph that used those sources (maximum 1–2 such lines per page):
     - `Основа: [название](https://21ideas.org/...)`.
   - Every `https://21ideas.org/...` URL cited inline must already appear in YAML `sources:` and in the bottom `## Источники` / `## Sources` list (deduplicated). Never fabricate URLs.
   - If no public 21ideas URL exists for a claim, keep `sources: []` or the project’s agreed fallback note in frontmatter only; do not invent a pretty link.

   Markdown tables:
   - Keep existing table formatting unless it is actually broken. Do not “reformat to satisfy a linter” if it changes readability or semantics.

**Important constraints:**
- Do not change the **substantive** wording, headings, tables, or meaning — except where task (5) asks to **replace** `raw/...` citations with `https://21ideas.org/...` links (or add such links) without altering claims.
- Keep the tone educational, precise, and consistent with the rest of the wiki.

After editing, output:
- The full updated Markdown content of the page.
- A short summary of changes: which wikilinks were added, tags updated, frontmatter standardized, sections modified, and (if applicable) how reader-facing `21ideas.org` citations replaced or complement `raw/` mentions.

Pre-flight checklist (must pass before you finish):
- No `raw/...` citations in the page body (replace with reader-facing 21ideas.org links, or remove).
- No `[[wiki-ru/...]]` or `[[wiki-en/...]]` links anywhere.
- For wiki-ru pages: all internal links start with `[[ru/...]]`; for wiki-en pages: `[[en/...]]`.
- Every 21ideas URL used inline is included in YAML `sources:` and in the bottom `## Источники` / `## Sources` list (deduplicated).
- Wikilinking passes completed: backbone sweep + glossary sweep; no obvious missed links for key terms/concepts/entities.

Work only on this one page.
```