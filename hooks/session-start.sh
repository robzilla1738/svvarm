#!/usr/bin/env bash
# svvarm session start — show rainbow banner if project has svvarm initialized.
# Best-effort, never blocking: exits 0 no matter what.

PLUGIN_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Only show banner if this project has svvarm initialized
[ -d ".svvarm" ] || exit 0

# python3 is optional — skip silently if missing
command -v python3 >/dev/null 2>&1 || exit 0

python3 "$PLUGIN_ROOT/skills/svvarm/scripts/ui.py" banner 2>/dev/null || true

exit 0
