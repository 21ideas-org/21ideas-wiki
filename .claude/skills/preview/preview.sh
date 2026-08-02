#!/usr/bin/env bash
# Build the 21wiki locally with Quartz, mirroring the production deploy pipeline.
#
#   preview.sh serve   # build + watch + serve on :8080 (default)
#   preview.sh build   # one-shot build, print warnings, exit
#   preview.sh sync    # re-copy wiki content into the preview tree (triggers rebuild)
#   preview.sh clean   # remove the preview tree
#
# Env overrides:
#   QUARTZ_DIR   path to the quartz checkout (default: ../quartz relative to repo)
#   PREVIEW_DIR  where the assembled content tree lives
#   PORT         serve port (default 8080)

set -euo pipefail

WIKI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
PREVIEW_DIR="${PREVIEW_DIR:-${TMPDIR:-/tmp}/21wiki-preview}"
OUT_DIR="${PREVIEW_DIR%/}-out"
PORT="${PORT:-8080}"
MODE="${1:-serve}"

is_quartz() { [[ -f "$1/quartz/bootstrap-cli.mjs" ]]; }

# An explicit QUARTZ_DIR is honoured or fails — never silently fallen back from.
if [[ -n "${QUARTZ_DIR:-}" ]]; then
  if ! is_quartz "$QUARTZ_DIR"; then
    echo "ERROR: QUARTZ_DIR=$QUARTZ_DIR has no quartz/bootstrap-cli.mjs" >&2
    exit 1
  fi
  QUARTZ="$(cd "$QUARTZ_DIR" && pwd)"
else
  QUARTZ=""
  for c in "$WIKI_ROOT/../quartz" "$WIKI_ROOT/../21ideas-quartz" "$HOME/code/21ideas/quartz"; do
    if is_quartz "$c"; then QUARTZ="$(cd "$c" && pwd)"; break; fi
  done
  if [[ -z "$QUARTZ" ]]; then
    {
      echo "ERROR: quartz checkout not found (needs quartz/bootstrap-cli.mjs)."
      echo "  Looked in: ../quartz, ../21ideas-quartz, ~/code/21ideas/quartz"
      echo "  Set QUARTZ_DIR=/path/to/quartz to override."
    } >&2
    exit 1
  fi
fi

sync_content() {
  # Mirrors .github/workflows/deploy.yml in the quartz repo:
  #   cp -r wiki-content/wiki-en/. content/en/
  #   cp -r wiki-content/wiki-ru/. content/ru/
  # Quartz-repo files at the content root (index.md, robots.txt, llms.txt) are
  # part of the site, not the wiki, so they are seeded from the quartz checkout.
  mkdir -p "$PREVIEW_DIR"
  cp -R "$QUARTZ/content/." "$PREVIEW_DIR/" 2>/dev/null || true
  mkdir -p "$PREVIEW_DIR/en" "$PREVIEW_DIR/ru"
  cp -R "$WIKI_ROOT/wiki-en/." "$PREVIEW_DIR/en/"
  cp -R "$WIKI_ROOT/wiki-ru/." "$PREVIEW_DIR/ru/"
  echo "synced → $PREVIEW_DIR  (en: $(find "$PREVIEW_DIR/en" -name '*.md' | wc -l | tr -d ' '), ru: $(find "$PREVIEW_DIR/ru" -name '*.md' | wc -l | tr -d ' ') md files)"
}

case "$MODE" in
  clean)
    rm -rf "$PREVIEW_DIR" "$OUT_DIR"
    echo "removed $PREVIEW_DIR and $OUT_DIR"
    ;;
  sync)
    sync_content
    ;;
  build)
    sync_content
    cd "$QUARTZ"
    # Call bootstrap-cli directly: `npx quartz` resolves to the npm-published
    # package from the npx cache, not this checkout's config.
    node ./quartz/bootstrap-cli.mjs build -d "$PREVIEW_DIR" -o "$OUT_DIR"
    ;;
  serve)
    sync_content
    cd "$QUARTZ"
    echo "serving http://localhost:$PORT  (content: $PREVIEW_DIR)"
    node ./quartz/bootstrap-cli.mjs build --serve --port "$PORT" -d "$PREVIEW_DIR" -o "$OUT_DIR"
    ;;
  *)
    echo "usage: preview.sh [serve|build|sync|clean]" >&2
    exit 2
    ;;
esac
