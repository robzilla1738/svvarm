#!/bin/sh
# svvarm installer — copies or symlinks the skill folder into a tool's skills directory.
#
#   ./install.sh <claude|codex|cursor|opencode|all> [--global|--project] [--copy|--link] [--uninstall]
#
# Defaults: --global (cursor is project-only), --link.
# --link  : symlink the skill folder (stays in sync with this repo)
# --copy  : copy the skill folder (install-and-forget; re-run to update)

set -e

SRC="$(cd "$(dirname "$0")" && pwd)/skills/svvarm"
TOOL=""
SCOPE="global"
METHOD="link"
UNINSTALL=0

usage() {
  echo "Usage: ./install.sh <claude|codex|cursor|opencode|all> [--global|--project] [--copy|--link] [--uninstall]"
  exit 1
}

for arg in "$@"; do
  case "$arg" in
    claude|codex|cursor|opencode|all) TOOL="$arg" ;;
    --global)    SCOPE="global" ;;
    --project)   SCOPE="project" ;;
    --copy)      METHOD="copy" ;;
    --link)      METHOD="link" ;;
    --uninstall) UNINSTALL=1 ;;
    -h|--help)   usage ;;
    *) echo "Unknown argument: $arg"; usage ;;
  esac
done

[ -n "$TOOL" ] || usage
[ -d "$SRC" ] || { echo "Error: skill source not found at $SRC"; exit 1; }

target_for() {
  case "$1" in
    claude)
      if [ "$SCOPE" = "global" ]; then echo "$HOME/.claude/skills/svvarm"
      else echo "$(pwd)/.claude/skills/svvarm"; fi ;;
    codex)
      if [ "$SCOPE" = "global" ]; then echo "$HOME/.codex/skills/svvarm"
      else echo "$(pwd)/.codex/skills/svvarm"; fi ;;
    opencode)
      if [ "$SCOPE" = "global" ]; then echo "$HOME/.config/opencode/skills/svvarm"
      else echo "$(pwd)/.opencode/skills/svvarm"; fi ;;
    cursor)
      if [ "$SCOPE" = "global" ]; then echo "$HOME/.cursor/skills/svvarm"
      else echo "$(pwd)/.cursor/skills/svvarm"; fi ;;
  esac
}

install_one() {
  tool="$1"
  target="$(target_for "$tool")"

  if [ "$UNINSTALL" = 1 ]; then
    if [ -L "$target" ] || [ -d "$target" ]; then
      rm -rf "$target"
      echo "✓ $tool: removed $target"
    else
      echo "- $tool: nothing installed at $target"
    fi
    return 0
  fi

  # Idempotency: already linked to this source?
  if [ -L "$target" ] && [ "$(readlink "$target")" = "$SRC" ]; then
    echo "- $tool: already linked at $target"
    return 0
  fi

  mkdir -p "$(dirname "$target")"
  rm -rf "$target"

  if [ "$METHOD" = "link" ]; then
    ln -s "$SRC" "$target"
    echo "✓ $tool: linked $target -> $SRC"
  else
    cp -R "$SRC" "$target"
    echo "✓ $tool: copied to $target"
  fi
}

if [ "$TOOL" = "all" ]; then
  status=0
  for t in claude codex opencode cursor; do
    install_one "$t" || status=1
  done
else
  install_one "$TOOL"
  status=$?
fi

if [ "$UNINSTALL" = 0 ]; then
  if command -v python3 >/dev/null 2>&1; then
    echo "- python3 found: terminal banner enabled"
  else
    echo "- python3 not found: banner will be skipped (everything else works)"
  fi
fi

exit $status
