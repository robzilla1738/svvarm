# svvarm

A design director for Claude Code. Deep expertise files, a comprehensive knowledge library, and a deep hatred for AI-looking output.

## The problem

You ask Claude to build a landing page. It gives you Inter font, a purple gradient, three identical cards, and centered everything. It looks like every other AI-generated site on the internet.

svvarm fixes that.

## How it works

When you say "build me a landing page", svvarm reads its full design knowledge directly — color theory, typography systems, layout composition, content strategy, and 38 anti-slop patterns — all in the same context window. Every design decision is cross-referenced: the color palette works with the typography, the layout supports the content, and the whole thing gets self-audited for AI patterns before you see it.

No agent dispatching. No multi-phase pipelines. Just deep expertise applied coherently in one pass.

## Install

```
/plugin marketplace add robzilla1738/svvarm
/plugin install svvarm@svvarm
/reload-plugins
```

## Usage

```
/svvarm init                              # New project — answers 6 questions, creates design brief
/svvarm setup                             # Existing project — scans your code first
/svvarm audit                             # Full quality review
/svvarm [anything]                        # Just describe what you need
```

Some things you can say:

```
/svvarm build me a landing page           # Full build — reads all expertise + knowledge
/svvarm the fonts feel off                # Reads typography expertise + knowledge
/svvarm this looks like AI made it        # Slop audit with scoring
/svvarm the copy is awkward               # Content expertise — kills AI-sounding text
/svvarm is this ready to ship             # Slop + production + polish checks
```

## Expertise

7 deep expertise files guide design decisions:

| Expertise | What it covers |
|-----------|---------------|
| **Color Lead** | OKLCH palettes, tinted neutrals, proper contrast, dark mode architecture |
| **Typography Lead** | Font selection from 19 curated pairings, fluid type scales, weight distribution |
| **Layout Lead** | Page composition, spacing rhythm, semantic HTML, responsive systems |
| **Content Lead** | Landing copy, UX writing, error messages, voice matching. Kills AI-sounding text |
| **Slop Auditor** | Scores output 0-100 for AI patterns. 38 specific detection patterns |
| **Polish Lead** | Cross-cutting refinement. Alignment, consistency, token usage, details |
| **Production Lead** | Responsive behavior, WCAG AA accessibility, performance, resilience |

## Knowledge library

13 reference files with deep domain knowledge:

- **anti-slop-bible.md** — 38 AI design convergence patterns with detection and fixes
- **typography-mastery.md** — Type scales, fluid `clamp()`, dark mode typography
- **color-mastery.md** — OKLCH color theory, gamut mapping, P3 wide-gamut, accessibility
- **layout-mastery.md** — Layout primitives, spacing rhythm, responsive systems
- **component-mastery.md** — Token-based component recipes (buttons, cards, inputs, nav, modals)
- **font-pairings-db.md** — 19 curated pairings organized by aesthetic
- **ux-writing-mastery.md** — Microcopy, error messages, empty states, voice frameworks
- **interaction-mastery.md** — Hover states, focus management, scroll-driven effects
- **motion-mastery.md** — Easing curves, duration scales, reduced-motion support
- **icon-mastery.md** — Icon systems, sizing, alignment, library selection
- **case-studies.md** — Design teardowns of Linear, Stripe, Vercel, Apple, Nothing
- **design-gallery.md** — Reference design patterns
- **creative-arsenal.md** — Creative direction patterns with dial affinity tags

## Style direction

No presets. Describe what you want in your own words: "moody and cinematic", "clean but not boring", "dark and premium", "bright and playful". Everything is derived from your description.

## Memory

Simple markdown files. Readable, diffable, committable.

```
your-project/
└── .svvarm/
    ├── context.md              # Design brief
    └── decisions.md            # Decision log
```

## Requirements

- **Claude Code** v2.1+
- **uv** — `brew install uv` (for the rainbow banner)

## License

MIT
