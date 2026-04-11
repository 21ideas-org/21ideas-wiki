# Lint report — 21ideas Bitcoin Wiki

_Last pass: 2026-04-09 (targeted: Batch 3 only)_

## Summary

| Check | wiki-en (10 new pages) | wiki-ru (10 new pages) |
|--------|------------------------|------------------------|
| Required frontmatter (`title`, `category`, `quality`, `sources`, `synthesized_date`, `completeness`, `language`) | OK | OK |
| Internal wikilinks: `[[en/...]]` vs `[[ru/...]]` | OK | OK |
| Broken wikilinks to non-existent targets | None found | None found |

## Pages in this pass

| Slug | EN | RU |
|------|----|----|
| bitcoin-whitepaper | `wiki-en/concepts/bitcoin-whitepaper.md` | `wiki-ru/concepts/bitcoin-whitepaper.md` |
| aml | `wiki-en/concepts/aml.md` | `wiki-ru/concepts/aml.md` |
| b-money | `wiki-en/concepts/b-money.md` | `wiki-ru/concepts/b-money.md` |
| bit-gold | `wiki-en/concepts/bit-gold.md` | `wiki-ru/concepts/bit-gold.md` |
| rpow | `wiki-en/concepts/rpow.md` | `wiki-ru/concepts/rpow.md` |
| adam-back | `wiki-en/entities/adam-back.md` | `wiki-ru/entities/adam-back.md` |
| tim-may | `wiki-en/entities/tim-may.md` | `wiki-ru/entities/tim-may.md` |
| eric-hughes | `wiki-en/entities/eric-hughes.md` | `wiki-ru/entities/eric-hughes.md` |
| david-chaum | `wiki-en/entities/david-chaum.md` | `wiki-ru/entities/david-chaum.md` |
| phil-zimmermann | `wiki-en/entities/phil-zimmermann.md` | `wiki-ru/entities/phil-zimmermann.md` |

## Suggested follow-ups (not auto-fixed)

- **Orphans:** New pages are linked from indexes and from each other; older hub pages may mention these concepts/entities without wikilinks — optional improvement for graph density.
- **AML source URL:** `raw/Theory/privacy/aml.md` does not include a canonical 21ideas.org URL in its metadata in this repo snapshot; the wiki pages note this and use `sources: []`.
- **Full-repo lint:** This report covers **only** the Batch 3 new pairs; a whole-vault pass was not run.
