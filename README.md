# svvarm

A design director for your coding agent. Deep design expertise, a two-tier reference library, and a deep hatred for AI-looking output. Works with **Claude Code, Codex CLI, opencode, and Cursor**.

> **Canonical home:** svvarm is developed in [roberts-skills](https://github.com/robzilla1738/roberts-skills) (`plugins/svvarm/`), where it's also installable as `svvarm@roberts-skills`. This repo mirrors the skill for the standalone plugin-marketplace install below.

## The problem

You ask an AI to build a landing page. It gives you Inter font, a purple gradient, three identical cards, and centered everything. It looks like every other AI-generated site on the internet.

svvarm fixes that.

## How it works

svvarm is a single portable skill (the standard `SKILL.md` format) with a two-tier reference library:

- **The digest** (`references/core.md`) — one compiled file with every domain's essential rules: 38 anti-slop patterns, color/typography/layout/copy/interaction/production rules, a font shortlist, and a self-audit gate. Full builds read this one file — fast, and everything stays in one context window so decisions are coherent.
- **Eleven deep references** — per-domain files with full evaluation rubrics and exhaustive knowledge (color, typography, font pairings, layout, content, slop, polish, interaction, motion, icons, inspiration). Focused tasks load only the file they need; full builds pull at most 2-3 when a decision demands depth.

No agent dispatching. No multi-phase pipelines. Just deep expertise applied coherently in one pass.

## Install

### Claude Code (plugin)

```
/plugin marketplace add robzilla1738/svvarm
/plugin install svvarm@svvarm
/reload-plugins
```

### Any tool (skill install)

```bash
git clone https://github.com/robzilla1738/svvarm
cd svvarm

./install.sh claude              # → ~/.claude/skills/svvarm
./install.sh codex               # → ~/.codex/skills/svvarm
./install.sh opencode            # → ~/.config/opencode/skills/svvarm
./install.sh cursor              # → ~/.cursor/skills/svvarm
./install.sh all                 # all of the above
```

Flags: `--project` installs into the current project instead of globally · `--copy` copies instead of symlinking (install-and-forget) · `--uninstall` removes cleanly.

> opencode also reads `.claude/skills/` directly, so a Claude Code project install covers opencode too.

## Usage

```
/svvarm init                              # New project — answers 6 questions, creates design brief
/svvarm setup                             # Existing project — scans your code first
/svvarm audit                             # Full quality review
/svvarm [anything]                        # Just describe what you need
```

In tools without slash commands, just ask naturally — "use svvarm to review this page" — and the skill activates.

Some things you can say:

```
/svvarm build me a landing page           # Full build — reads the core digest
/svvarm the fonts feel off                # Reads typography deep file
/svvarm this looks like AI made it        # Slop audit with scoring
/svvarm the copy is awkward               # Content expertise — kills AI-sounding text
/svvarm is this ready to ship             # Slop + production + polish checks
```

## Reference library

| File | What it covers |
|------|---------------|
| **core.md** | The digest — everything below, compressed. Full builds read only this. |
| **color.md** | OKLCH palettes, tinted neutrals, contrast, dark mode architecture |
| **typography.md** | Type systems, fluid scales, weight discipline, dark mode type |
| **font-pairings.md** | 19 curated pairings with sources, imports, and cautions |
| **layout.md** | Composition, spacing scale, layout primitives, semantic HTML, component recipes |
| **content.md** | Landing copy, UX writing, the humanizer — kills AI-sounding text |
| **slop.md** | The Anti-Slop Bible: 38 patterns with detection, fixes, and 0-100 scoring |
| **polish.md** | 6-pass refinement: alignment, consistency, tokens, surfaces, motion restraint |
| **interaction.md** | Production hardening: a11y, responsive, 8-state components, forms, focus |
| **motion.md** | Easing curves, duration rules, scroll choreography, reduced motion |
| **icons.md** | Library selection, sizing, stroke matching, icon accessibility |
| **inspiration.md** | Case studies, design gallery anatomy, advanced pattern catalog |

## Style direction

No presets. Describe what you want in your own words: "moody and cinematic", "clean but not boring", "dark and premium", "bright and playful". Everything is derived from your description.

## Memory

Simple markdown files in your project. Readable, diffable, committable.

```
your-project/
└── .svvarm/
    ├── context.md              # Design brief
    └── decisions.md            # Decision log
```

## Requirements

- Claude Code, Codex CLI, opencode, or Cursor
- `python3` — optional, only for the rainbow terminal banner; everything works without it

## What changed in 2.0

- Portable: standard skill format, runs in all four tools — paths resolve relative to the skill folder, no plugin-only env vars
- Two-tier library: full builds read one ~5K-token digest instead of 20 files (~78K tokens) — dramatically faster with the same opinions
- 7 expertise + 13 knowledge files merged into 12 deduped references (the old `agents/` and `knowledge/` directories are gone)
- `uv` dependency dropped — the banner runs on plain `python3`, and is always optional

## License

MIT
