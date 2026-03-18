# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
svvarm terminal UI — rainbow effects, spinners, banners.
Outputs to stderr so it shows live in Claude Code terminal.
"""

import math
import sys
import time
import threading
from typing import Optional

IS_TTY = sys.stderr.isatty()

# ─── Rainbow Colors ───────────────────────────────────────────

def rainbow_color(i: int, total: int) -> str:
    """Generate a true-color ANSI code cycling through the rainbow."""
    hue = (i / max(total, 1)) * 360
    c = 1.0
    x = 1.0 - abs((hue / 60) % 2 - 1)
    if hue < 60:
        r, g, b = c, x, 0
    elif hue < 120:
        r, g, b = x, c, 0
    elif hue < 180:
        r, g, b = 0, c, x
    elif hue < 240:
        r, g, b = 0, x, c
    elif hue < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    return f"\033[38;2;{int(r*255)};{int(g*255)};{int(b*255)}m"

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"

# ─── Rainbow Text ─────────────────────────────────────────────

def rainbow_text(text: str, offset: int = 0) -> str:
    """Apply rainbow colors to each character."""
    result = []
    visible_idx = 0
    for char in text:
        if char in (' ', '\n', '\t'):
            result.append(char)
        else:
            color = rainbow_color((visible_idx + offset) % 80, 80)
            result.append(f"{color}{char}")
            visible_idx += 1
    result.append(RESET)
    return "".join(result)

def rainbow_line(text: str, offset: int = 0) -> str:
    """Apply a single rainbow gradient across a line."""
    chars = list(text)
    result = []
    idx = 0
    for c in chars:
        if c in (' ', '\n'):
            result.append(c)
        else:
            result.append(f"{rainbow_color((idx + offset) % len(chars), len(chars))}{c}")
            idx += 1
    result.append(RESET)
    return "".join(result)

# ─── Animated Rainbow Banner ──────────────────────────────────

BANNER_TAGLINE = "beautiful first · safe never"
WAVE_UP = "▁▂▃▅▆▇▆▅▃▂▁"
WAVE_DOWN = "▇▆▅▃▂▁▂▃▅▆▇"
BANNER_NAME = "S  V  V  A  R  M"

# Fixed colors for the banner letters: red, orange, yellow, green, blue, purple
BANNER_COLORS = [
    "\033[38;2;255;59;48m",    # red
    "\033[38;2;255;149;0m",    # orange
    "\033[38;2;255;204;0m",    # yellow
    "\033[38;2;52;199;89m",    # green
    "\033[38;2;0;122;255m",    # blue
    "\033[38;2;175;82;222m",   # purple
]

def _banner_text(text: str) -> str:
    """Each visible character in the banner gets a fixed color: R O Y G B P."""
    visible_idx = 0
    result = []
    for char in text:
        if char == ' ':
            result.append(' ')
        else:
            result.append(f"{BANNER_COLORS[visible_idx % len(BANNER_COLORS)]}{char}")
            visible_idx += 1
    result.append(RESET)
    return "".join(result)

def _full_rainbow_text(text: str, offset: int = 0) -> str:
    """Each character gets evenly spaced across the full rainbow spectrum."""
    visible = [c for c in text if c != ' ']
    total = len(visible)
    if total == 0:
        return text
    result = []
    idx = 0
    for char in text:
        if char == ' ':
            result.append(' ')
        else:
            result.append(f"{rainbow_color((idx + offset) % total, total)}{char}")
            idx += 1
    result.append(RESET)
    return "".join(result)

def show_banner(animate: bool = True, size: str | None = None):
    """Show the svvarm rainbow banner with spectrum wave."""
    wave_top = WAVE_UP * 3
    wave_bot = WAVE_DOWN * 3
    w = len(wave_top)
    name_pad = " " * ((w - len(BANNER_NAME)) // 2)
    tag_pad = " " * ((w - len(BANNER_TAGLINE)) // 2)
    indent = "  "
    sys.stderr.write("\n")
    sys.stderr.write(indent + _full_rainbow_text(wave_top) + "\n")
    sys.stderr.write("\n")
    sys.stderr.write(indent + name_pad + BOLD + _banner_text(BANNER_NAME) + "\n")
    sys.stderr.write(indent + tag_pad + DIM + BANNER_TAGLINE + RESET + "\n")
    sys.stderr.write("\n")
    sys.stderr.write(indent + _full_rainbow_text(wave_bot, offset=len(wave_bot) // 2) + "\n")
    sys.stderr.write("\n")
    sys.stderr.flush()

# ─── Spinner ──────────────────────────────────────────────────

SPINNER_FRAMES = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']

class Spinner:
    """Animated spinner with rainbow colors."""

    def __init__(self, message: str = "Working"):
        self.message = message
        self.running = False
        self.thread: Optional[threading.Thread] = None
        self.frame_idx = 0

    def _spin(self):
        while self.running:
            frame = SPINNER_FRAMES[self.frame_idx % len(SPINNER_FRAMES)]
            color = rainbow_color(self.frame_idx % 40, 40)
            sys.stderr.write(f"\r{color}{frame}{RESET} {self.message}  ")
            sys.stderr.flush()
            self.frame_idx += 1
            time.sleep(0.08)

    def start(self):
        self.running = True
        if IS_TTY:
            self.thread = threading.Thread(target=self._spin, daemon=True)
            self.thread.start()
        else:
            sys.stderr.write(f"⏳ {self.message}\n")
            sys.stderr.flush()

    def update(self, message: str):
        self.message = message
        if not IS_TTY:
            sys.stderr.write(f"⏳ {message}\n")
            sys.stderr.flush()

    def stop(self, final: str = ""):
        self.running = False
        if self.thread:
            self.thread.join(timeout=0.2)
        if IS_TTY:
            sys.stderr.write("\r" + " " * 80 + "\r")
        if final:
            sys.stderr.write(f"✓ {final}\n")
        sys.stderr.flush()

# ─── Phase Indicators ─────────────────────────────────────────

PHASE_COLORS = {
    "slop":       "\033[38;2;255;80;80m",
    "typography": "\033[38;2;180;120;255m",
    "color":      "\033[38;2;80;200;255m",
    "layout":     "\033[38;2;255;180;50m",
    "polish":     "\033[38;2;120;220;120m",
    "production": "\033[38;2;255;150;200m",
    "content":    "\033[38;2;200;200;100m",
    "cdo":        "\033[38;2;255;255;255m",
}

def phase(name: str, message: str):
    """Print a phase indicator with color."""
    color = PHASE_COLORS.get(name, RESET)
    sys.stderr.write(f"{color}▸{RESET} {message}\n")
    sys.stderr.flush()

def success(message: str):
    sys.stderr.write(f"\033[38;2;120;220;120m✓{RESET} {message}\n")
    sys.stderr.flush()

def warn(message: str):
    sys.stderr.write(f"\033[38;2;255;180;50m⚠{RESET} {message}\n")
    sys.stderr.flush()

def error(message: str):
    sys.stderr.write(f"\033[38;2;255;80;80m✗{RESET} {message}\n")
    sys.stderr.flush()

# ─── Progress Bar ─────────────────────────────────────────────

def progress_bar(current: int, total: int, width: int = 30, label: str = "") -> str:
    """Rainbow progress bar."""
    filled = int(width * current / max(total, 1))
    bar = ""
    for i in range(width):
        if i < filled:
            bar += f"{rainbow_color(i, width)}█"
        else:
            bar += f"{DIM}░"
    pct = int(100 * current / max(total, 1))
    return f"{bar}{RESET} {pct}% {label}"

def show_progress(current: int, total: int, label: str = ""):
    """Display a rainbow progress bar to stderr."""
    bar = progress_bar(current, total, label=label)
    if IS_TTY:
        sys.stderr.write(f"\r{bar}  ")
    else:
        sys.stderr.write(f"{bar}\n")
    sys.stderr.flush()

# ─── Step Indicator ───────────────────────────────────────────

def step(current: int, total: int, message: str):
    """Show step progress with rainbow number."""
    color = rainbow_color(current * 10, total * 10)
    dots = "".join(
        f"{rainbow_color(i * 10, total * 10)}{'▸' if i < current else '▹'}"
        for i in range(total)
    )
    sys.stderr.write(f"{color}[{current}/{total}]{RESET} {dots}{RESET} {message}\n")
    sys.stderr.flush()

# ─── CLI ──────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="svvarm UI utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("banner", help="Show rainbow banner")

    step_cmd = subparsers.add_parser("step", help="Show step progress")
    step_cmd.add_argument("current", type=int, help="Current step number")
    step_cmd.add_argument("total", type=int, help="Total steps")
    step_cmd.add_argument("message", help="Step description")

    phase_cmd = subparsers.add_parser("phase", help="Show phase indicator")
    phase_cmd.add_argument("name", help="Phase name")
    phase_cmd.add_argument("message", help="Phase message")

    ok_cmd = subparsers.add_parser("ok", help="Show success message")
    ok_cmd.add_argument("message", help="Success message")

    subparsers.add_parser("test", help="Run full UI demo")

    args = parser.parse_args()

    if args.command == "banner":
        show_banner()

    elif args.command == "step":
        step(args.current, args.total, args.message)

    elif args.command == "phase":
        phase(args.name, args.message)

    elif args.command == "ok":
        success(args.message)

    elif args.command == "test":
        show_banner()
        time.sleep(0.3)

        step(1, 6, "What are we building?")
        time.sleep(0.3)
        step(2, 6, "Tech stack?")
        time.sleep(0.3)
        step(3, 6, "Who's it for?")
        time.sleep(0.3)
        step(4, 6, "Pick a style direction")
        time.sleep(0.3)
        step(5, 6, "Design references?")
        time.sleep(0.3)
        step(6, 6, "Anything else?")
        time.sleep(0.3)

        print()
        phase("slop", "Sending to Slop Auditor...")
        time.sleep(0.2)
        phase("typography", "Sending to Typography Lead...")
        time.sleep(0.2)
        phase("color", "Sending to Color Lead...")
        time.sleep(0.2)

        print()
        for i in range(11):
            show_progress(i, 10, "Indexing memories")
            time.sleep(0.1)
        print()

        success("Design system initialized")
        warn("No style direction set yet")
        error("Slop score: 72 — needs redesign")
