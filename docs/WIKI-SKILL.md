# WIKI-SKILL — Wiki Page Generation for 21ideas Bitcoin Wiki

Covers two operations on `raw/` files that already exist:

- **Mode A — Ingest:** no wiki page exists yet → create both `wiki-en/` and `wiki-ru/` pages
- **Mode B — Update:** wiki page exists, `raw/` source changed or new `raw/` files added → revise without losing good content

For getting source material into `raw/`, see `docs/INGEST-SKILL.md`.
For polishing existing pages (frontmatter, body style, link hygiene), see `docs/ENHANCE-SKILL.md`.

---

## Zero-Tolerance Rules

1. **Never fabricate `sources:` URLs.** Use only the URL from the `raw/` file's `url:` field verbatim. If none exists, set `sources: []` and flag it in the log.
2. **Never treat one layer as a translation of the other.** Return to `raw/` independently for each language. If the source is in Russian, `wiki-en/` is an English synthesis from that Russian source — not a translation of `wiki-ru/`.
3. **Never link to pages or glossary anchors that do not exist.** The link map is the ground truth.
4. **Never modify `raw/` files.**
5. **Never use `raw/...` paths in the page body.** Reader-facing citations use `https://21ideas.org/...` only.
6. **Never open the body with a `#` heading. Never use `---` in the body.**

---

## Before Writing: Three Script Checks

Run these before touching any wiki file.

```bash
# 1. Check parity — does a page exist in both layers?
python3 tools/check_parity.py <category/slug>

# 2. Regenerate link maps if any pages were added since the last run
python3 tools/build_link_map.py

# 3. Read the link maps — these are your wikilink ground truth
docs/link-map-en.md
docs/link-map-ru.md
```

The link maps list every valid wikilink target in the vault. Scan them against your draft content before writing. Do not invent targets.

---

## Wikilinking (applies to both modes, both layers)

Wikilinks are a primary deliverable — not optional polish. A page without meaningful wikilinks is incomplete.

**Resolution rule (from the link map header):**
- First mention of a term → dedicated page entry
- Meaningful second mention in a *different* `##` section where the term is being defined or explained → `[glossary]` entry
- All other repetitions → no link

**Two passes, every page:**

Pass A — Concept backbone: primary subject on first introduction; named people and organizations; spine concepts the page depends on; explicitly mentioned protocol upgrades or systems.

Pass B — Glossary sweep: scan the link map for remaining terms that appear in the draft and have a `[glossary]` entry. Apply only where the term is substantively used, not in passing.

**Hard rules:**
- `wiki-en/` pages: `[[en/...]]` prefixes only
- `wiki-ru/` pages: `[[ru/...]]` prefixes only
- No bare links, no `[[wiki-en/...]]` or `[[wiki-ru/...]]` prefixes
- No wikilinks inside markdown table cells — link the term in surrounding prose instead

---

## Content Quality Audit

Answer before writing any section. If you cannot answer a question, do not write that section yet.

1. **Coverage** — What claims or mechanisms exist in `raw/` that the page does not cover? List them or state "none."
2. **Thin sections** — Would any `##` section have fewer than two substantive sentences? Expand or fold it.
3. **Unsupported claims** — Can every factual assertion be traced to `raw/` or an existing wiki page? Flag anything that cannot.
4. **Concept completeness** — Does the page explain the concept (mechanism, significance, implications), or only name it?

---

## Mode A — Ingest

### Steps

**1. Orient**
Read the `raw/` source in full. Note the `url:` field (your only permitted `sources:` value), the source language, and the target category. Confirm target paths:
```
wiki-en/<category>/<slug>.md
wiki-ru/<category>/<slug>.md
```

**2. Run script checks** (see above)

**3. Run content quality audit** against the `raw/` source

**4. Write `wiki-en/` page**
Synthesize from `raw/` directly into English. Apply full frontmatter schema (canonical field order, double-quoted scalars, `reviewed:` last). Apply Pass A and Pass B wikilinks. Close with `## Sources` then `## Related pages`.

**5. Write `wiki-ru/` page**
Return to `raw/`. Synthesize independently into Russian — do not derive from the English page just written. Apply `[[ru/...]]` links. Close with `## Источники` then `## Дополнительные материалы`.

**6. Update index files**
Add entries to `wiki-en/index.md` and `wiki-ru/index.md` in the correct category table.

**7. Lint and log**
```bash
python3 tools/lint.py --layer both --write-report
```
Fix any issues before writing the log. Append to `docs/log.md`:
```
## [YYYY-MM-DD] ingest | <slug> (both layers)
**Raw source:** raw/<subdir>/<slug>.md
**URL in raw/:** <url or "none — sources: []">
**Created:** wiki-en/<category>/<slug>.md, wiki-ru/<category>/<slug>.md
**Wikilinks:** <key links added per layer>
**Content audit:** <gaps found or "none">
**Lint:** 0 issues
```

### Definition of done
- [ ] Both pages exist with complete, valid frontmatter
- [ ] `sources:` from `raw/` `url:` only; if `[]`, flagged in log and sources section
- [ ] Pass A and Pass B applied to both pages; all targets verified via link map
- [ ] Content quality audit passed; no unsupported claims
- [ ] Both `index.md` files updated
- [ ] `python3 tools/lint.py --layer both` → 0 issues
- [ ] `docs/log.md` appended

---

## Mode B — Update

### Steps

**1. Read before writing**
Read the current wiki page(s) and the updated `raw/` source(s) in full. Write an explicit delta statement before touching any file:

```
Delta — wiki-en/concepts/segwit.md
Raw/ change: new section on v0 vs v1 addresses added
Wiki impact: expand "Address types" section; new link [[en/concepts/taproot]]
Unchanged: "Malleability fix", "Block weight" — preserve as-is
```

If you cannot write the delta statement, you do not understand the change well enough to proceed.

**2. Run script checks** (see above)

**3. Run content quality audit** scoped to changed sections only

**4. Apply changes**
Rewrite only delta-affected sections. Preserve all existing good content. Update `updated:` field; keep `reviewed:` last. If `raw/` introduced a new URL, add it to `sources:` and the sources section — never remove an existing valid URL.

**5. Apply wikilinks** to new or changed content only (Pass A and Pass B)

**6. Lint and log**
```bash
python3 tools/lint.py --layer both --write-report
```
Append to `docs/log.md`:
```
## [YYYY-MM-DD] update | <page path(s)>
**Raw/ change:** <what changed in raw/>
**Wiki changes:** <sections changed, links added>
**Layers:** both
**Content audit:** <clean or gaps noted>
**Lint:** 0 issues
```

### Definition of done
- [ ] Delta statement written before any edits
- [ ] Only delta-affected sections rewritten; existing content preserved
- [ ] Pass A and Pass B applied to changed sections; targets verified via link map
- [ ] `updated:` reflects today; `reviewed:` is last frontmatter field
- [ ] `sources:` updated if `raw/` introduced a new URL (never fabricated)
- [ ] `python3 tools/lint.py --layer both` → 0 issues
- [ ] `docs/log.md` appended with delta description

---

## What This Skill Does Not Do

- Add source material to `raw/` → `docs/INGEST-SKILL.md`
- Polish existing pages (frontmatter, body style, link hygiene) → `docs/ENHANCE-SKILL.md`
- Make Bitcoin accuracy judgments — claims are grounded in `raw/` only; accuracy review is human
- Link to pages that do not exist — missing targets belong in `docs/WIKI-BACKLOG.md`