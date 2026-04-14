# `tools/` — ingest helpers (stdlib-only)

Run commands from the **repository root**. Python **3.9+**.

## `check_duplicate.py`

**Purpose:** Before adding a new `raw/` file, check for an existing `url:` match or a conflicting on-disk path.

**Inputs / flags**

- `--url` (required) — canonical URL or site path to compare to every `url:` in `raw/**/*.md` (normalized: case-insensitive path; trailing `/` ignored; `http(s)` uses path only).
- `--slug` (optional) — proposed filename **without** `.md`.
- `--subdir` (optional) — target folder under `raw/`, e.g. `Theory/protocol` (with `--slug`, checks `raw/<subdir>/<slug>.md`; without it, `raw/<slug>.md`).

**Stdout (one line):** `CLEAR`, `DUPLICATE: raw/...`, or `SLUG_CONFLICT: raw/...`.

**Exit codes:** `0` — clear; `1` — duplicate URL or `raw/` missing (`ERROR:` on stderr); `2` — `SLUG_CONFLICT:`.

**Examples**

```bash
python3 tools/check_duplicate.py --url "https://21ideas.org/taproot"
python3 tools/check_duplicate.py --url "https://21ideas.org/foo" --slug my-article --subdir "Theory/protocol"
```

## `derive_slug.py`

**Purpose:** Turn a single article URL into a normalized filename slug (last path segment).

**Input:** one positional **URL**.

**Stdout:** the slug (one line). **Stderr + exit `1`:** if the slug is empty after normalization, prints a short warning and still prints an empty line on stdout.

**Examples**

```bash
python3 tools/derive_slug.py "https://21ideas.org/theory/protocol/musig2/"
```

## `check_series.py`

**Purpose:** See if a `raw/` article looks like part of a numbered series and which parts exist next to it.

**Input:** one positional path to a **`.md` file under `raw/`**.

**Stdout**

- `NO_SERIES` — no series signal; **exit `0`**.
- Or a multi-line report starting with **`SERIES_DETECTED`**, then `Base:`, `This part:`, `Parts found in raw/:`, a `Possibly missing` line, `Suggested hub file:`, and `Signals:` — **exit `0`**.

**Exit `1`** — path is not a file or not under `raw/` (`ERROR:` on stderr).

**Example**

```bash
python3 tools/check_series.py raw/Theory/economics/gradually-then-suddenly/03-bitcoin-is-not-too-volatile.md
```
