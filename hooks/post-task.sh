#!/usr/bin/env bash
# svvarm post-task hook — re-index memory files after work
# Runs async after each Claude response. Silent unless error.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SVVARM_DIR=".svvarm"

# Only run if this project has svvarm initialized
[ -d "$SVVARM_DIR" ] || exit 0

# Only run if memory directory has files
[ -d "$SVVARM_DIR/memory" ] || exit 0
ls "$SVVARM_DIR/memory"/*.md >/dev/null 2>&1 || exit 0

# Re-index memory files for semantic search (non-fatal)
uv run "$SCRIPT_DIR/scripts/memory.py" index --project-dir . 2>/dev/null || true

exit 0
