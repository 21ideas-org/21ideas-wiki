---
name: preview
description: Build and serve the 21wiki locally with Quartz to check how pages actually render before pushing. Use when asked to preview, run, serve, or build the wiki/site locally, to see how a page looks, or to verify rendering quality after editing wiki-en/ or wiki-ru/. Also covers rendering-layer checks that tools/lint.py cannot perform.
---

# Local Quartz preview

`tools/lint.py` checks structure — wikilinks, frontmatter, tags. It cannot tell you how a page **renders**. Some defects only appear once Quartz has processed the Markdown, and they are invisible in the source file. This skill builds the real site locally so those are caught before a push.

## How production works

Know this before touching anything, so the local build stays faithful to it:

1. Push to `main` in this repo touching `wiki-en/**`, `wiki-ru/**`, `raw/**` or `docs/**` fires `.github/workflows/trigger-quartz-deploy.yml`.
2. That dispatches a `wiki-updated` event to `21ideas-org/21ideas-quartz`.
3. That repo's `deploy.yml` checks out this repo and runs:
   ```
   cp -r wiki-content/wiki-en/. content/en/
   cp -r wiki-content/wiki-ru/. content/ru/
   ```
4. Quartz builds `content/` and publishes to `wiki.21ideas.org`.

The `en/` and `ru/` split is why wikilinks use `[[en/...]]` and `[[ru/...]]` prefixes — those map straight onto the deployed URL paths.

## Quick start

```bash
.claude/skills/preview/preview.sh serve    # build + watch + http://localhost:8080
.claude/skills/preview/preview.sh build    # one-shot build, prints warnings, exits
.claude/skills/preview/preview.sh sync     # re-copy wiki content (server picks it up)
.claude/skills/preview/preview.sh clean    # delete the preview tree
```

The script assembles a content tree in a temp directory and points Quartz at it with `-d`. It never writes into the quartz checkout, so `git status` there stays clean.

It locates the quartz checkout automatically (`../quartz`, `../21ideas-quartz`, `~/code/21ideas/quartz`). Override with `QUARTZ_DIR=/path/to/quartz`. Also honours `PORT` and `PREVIEW_DIR`.

**After editing wiki files, run `sync`** — the server watches the preview tree, not `wiki-ru/`, so changes need copying across. Give it a couple of seconds to rebuild.

## What to check

### 1. Build warnings

`build` mode prints them. Two classes matter:

- **`unicodeTextInMathMode`** — a `$` was parsed as LaTeX. See below.
- **Broken links** — Quartz resolves links independently of `tools/lint.py`, so this is a second opinion on the link graph.

A healthy full build currently looks like: `Parsed N Markdown files`, `Emitted M files`, no link warnings. The `punycode` deprecation warning and `couldn't find git repository` are expected noise from building outside a repo.

### 2. Pages actually respond

```bash
for u in ru/concepts/hd-wallets ru/practice/verifying-software; do
  printf "%-40s " "$u"; curl -s -o /dev/null -w "%{http_code}\n" "http://localhost:8080/$u"
done
```

New pages returning 404 usually mean the file landed outside `wiki-en/`/`wiki-ru/`, or `sync` was not re-run.

### 3. Frontmatter `title` became the page title

```bash
curl -s http://localhost:8080/ru/concepts/hd-wallets | grep -o '<title>[^<]*</title>'
```

The body must not open with a `#` heading — Quartz renders the frontmatter `title` as the page heading, so a leading `#` produces a duplicate. `tools/lint.py` catches this, but confirming visually is cheap.

### 4. Wikilinks resolved to real hrefs

```bash
curl -s http://localhost:8080/ru/concepts/hd-wallets | grep -o 'href="[^"]*seed-phrase[^"]*"' | head
```

An unresolved wikilink renders as literal `[[ru/...]]` text in the HTML instead of an `<a>`.

### 5. No stray math spans

```bash
curl -s http://localhost:8080/ru/concepts/passphrase | grep -c katex-html
```

Should be `0`. Any hit means text was swallowed into KaTeX — read the section below.

## The `$` trap

Quartz enables remark-math. **An unescaped `$` opens an inline LaTeX span and the next `$` closes it**, consuming everything between. Currency is the usual trigger.

Real example that shipped before being caught here:

```
те же $77 миллионов превращаются в $750 000
```

rendered as **«те же 77миллионо…»** — the middle of the sentence vanished into KaTeX.

Write currency as `\$77`. `tools/lint.py` now flags any unescaped `$` outside code, so this should not recur — but note the check is deliberately broader than "unpaired `$`": the example above has an *even* number of dollar signs, so an odd-count rule would have missed it.

## Gotchas

**Call `bootstrap-cli.mjs` directly, not `npx quartz`.** The quartz repo declares `bin: {quartz: ./quartz/bootstrap-cli.mjs}`, but since it *is* the package rather than a dependency, `npx quartz` does not resolve it locally — npm silently downloads the published `quartz` package into the npx cache and runs that instead. Different version, possibly different config handling. The script always uses `node ./quartz/bootstrap-cli.mjs`.

**Do not pipe a backgrounded build through `tail` or `head`.** Those buffer until the pipeline ends, so a long-running `--serve` writes nothing to the log and looks hung when it is actually fine. Redirect to a file instead, and check readiness by polling the port:

```bash
until lsof -nP -iTCP:8080 -sTCP:LISTEN >/dev/null 2>&1; do sleep 1; done
```

**Never build into `quartz/content/`.** It would dirty that repo's working tree and mix generated content with checked-in files. The script uses a temp directory for exactly this reason.

**Stop the server when done:**

```bash
kill $(lsof -t -nP -iTCP:8080 -sTCP:LISTEN)
```

## Obsidian as a faster alternative

This repo is also a working Obsidian vault (`.obsidian/` is checked in). For inspecting wikilinks, backlinks and the graph, opening it in Obsidian is quicker than a Quartz build.

What Obsidian will **not** show you: the `$`/KaTeX behaviour, the frontmatter-title rendering, or anything else specific to Quartz's pipeline. Those need a real build.

## After previewing

If the build surfaced a defect, fix it, re-run `sync`, confirm, then append to `docs/log.md` per `CLAUDE.md`. If the defect is a class that `tools/lint.py` could detect mechanically, extending the linter is usually worth more than the one fix — that is how the `$` check came about.
