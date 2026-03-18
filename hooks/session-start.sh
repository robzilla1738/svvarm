#!/usr/bin/env bash
# svvarm session start — show rainbow banner if project has svvarm initialized

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Only show banner if this project has svvarm initialized
[ -d ".svvarm" ] || exit 0

# Show the rainbow banner
uv run "$SCRIPT_DIR/scripts/ui.py" banner 2>&1

exit 0
