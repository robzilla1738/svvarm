# svvarm

A design director for Claude Code. 7 specialist agents, persistent memory, and a deep hatred for AI-looking output.

## The problem

You ask Claude to build a landing page. It gives you Inter font, a purple gradient, three identical cards, and centered everything. It looks like every other AI-generated site on the internet.

svvarm fixes that.

## How it works

When you say "build me a landing page", svvarm doesn't just generate code. It dispatches a team:

- **Color Lead** picks a palette using OKLCH color theory, not Tailwind defaults
- **Typography Lead** selects fonts from 19 curated pairings and builds a fluid type scale
- **Layout Lead** composes the page with real spatial hierarchy, not uniform padding everywhere
- **Content Lead** writes copy that sounds like a person, not a press release

They run in parallel. Then a CDO merges their work, resolves conflicts, and assembles the page. After that, three more agents audit the result for AI patterns, accessibility issues, and polish.

Every agent reads deep domain knowledge. Color Lead knows OKLCH gamut mapping. Typography Lead knows `clamp()` formulas for fluid scaling. The Slop Auditor knows 38 specific patterns that make designs look AI-generated, and it scores your output 0-100.

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
/svvarm audit                             # Quality review (3 agents in parallel)
/svvarm [anything]                        # Just describe what you need
```

Some things you can say:

```
/svvarm build me a landing page           # Full pipeline — all 7 agents
/svvarm the fonts feel off                # Typography Lead
/svvarm this looks like AI made it        # Slop Auditor
/svvarm the copy is awkward               # Content Lead
/svvarm is this ready to ship             # Slop Auditor + Polish Lead + Production Lead
```

## The team

| Agent | What they actually do |
|-------|---------------------|
| **Color Lead** | Builds palettes with tinted neutrals, proper contrast, dark mode. Reads `color-mastery.md` (OKLCH theory, gamut mapping, P3 wide-gamut) |
| **Typography Lead** | Font selection, fluid type scales, weight distribution. Reads `typography-mastery.md` + `font-pairings-db.md` (19 pairings) |
| **Layout Lead** | Page composition, spacing rhythm, semantic HTML, grids. Reads `layout-mastery.md` + `component-mastery.md` |
| **Content Lead** | Landing copy, UX writing, error messages, voice matching. Kills AI-sounding text. Reads `ux-writing-mastery.md` |
| **Slop Auditor** | Scores output 0-100 for AI patterns. Purple gradients, glassmorphism, identical cards — it catches all of it. Reads `anti-slop-bible.md` (38 patterns) |
| **Polish Lead** | Cross-cutting refinement. Alignment, consistency, token usage, details |
| **Production Lead** | Responsive behavior, WCAG AA accessibility, performance, resilience |

## Full build pipeline

```
Phase 0: Creative Brief (vibe, memorable thing, constraint)
              │
Phase 1: ┌────┼────┬────┐
       Color Type Layout Content    ← 4 agents in parallel
         └────┼────┴────┘
              │
Phase 2: CDO assembles page (strict merge order, conflict resolution)
              │
Phase 3: ┌────┼────┬────┐
       Slop Polish Production       ← 3 agents in parallel
         └────┼────┴────┘
              │
Phase 4: Save all agent memories
```

## Memory

Every agent remembers what it decided. The 5th time Typography Lead runs on your project, it already knows your fonts, your scale, and that you rejected cool grays twice.

```
your-project/
└── .svvarm/
    ├── context.md              # Design brief
    ├── decisions.md            # Decision log
    └── memory/
        ├── color-lead.md       # "Chose warm neutrals, user rejected cool grays twice"
        ├── typography-lead.md  # "Using Instrument Sans + Newsreader, 1.25 ratio"
        └── ...
```

Plain markdown. Readable, diffable, committable. Works out of the box with keyword search. Add an embedding backend for semantic search across all agent memories:

```bash
# Recommended — free, local, auto-detected
brew install ollama && ollama serve && ollama pull bge-m3
```

## Style direction

No presets. Describe what you want in your own words: "moody and cinematic", "clean but not boring", "dark and premium", "bright and playful". The agents derive everything from your description.

## Knowledge library

11 reference files the agents consult:

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

## Configuration

### Embedding backends

| Backend | Setup | Notes |
|---------|-------|-------|
| **Ollama** | `brew install ollama && ollama serve && ollama pull bge-m3` | Free, local, auto-detected |
| **OpenAI** | Set `OPENAI_API_KEY`, set `"backend": "openai"` in config | text-embedding-3-small |
| **llama.cpp** | Best quality with LCO-Embedding-Omni-3B | See below |
| **None** | Nothing to do | Keyword fallback, fully functional |

<details>
<summary>llama.cpp setup</summary>

```bash
brew install llama.cpp
mkdir -p ~/.svvarm/models && cd ~/.svvarm/models
huggingface-cli download marksverdhei/LCO-Embedding-Omni-3B-GGUF \
  LCO-Embedding-Omni-3B-Q8_0.gguf --local-dir .
llama-server -m LCO-Embedding-Omni-3B-Q8_0.gguf \
  --embedding --pooling last --port 8384 -ngl 99
```
</details>

### Agent model

Control which Claude model the agents use. In `.svvarm/config.json`:

```json
{
  "agent_model": "sonnet"
}
```

`"opus"` for max quality, `"sonnet"` for speed, `"haiku"` for lightweight tasks. Omit to inherit the parent model.

## Requirements

- **Claude Code** v2.1+
- **uv** — `brew install uv`
- **Ollama** (optional) — semantic memory search

## License

MIT
