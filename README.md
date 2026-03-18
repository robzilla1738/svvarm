# svvarm

An opinionated design director for Claude Code. 7 specialist agents. Persistent memory. Zero AI slop.

## Why svvarm instead of separate design skills?

Most Claude Code design skills are single-prompt tools: one skill for color, one for typography, one for layout. They don't talk to each other, they don't remember what you decided last time, and they don't share a creative vision.

svvarm is different:

**Coordinated multi-agent system.** When you say "build me a landing page", svvarm dispatches Color Lead, Typography Lead, Layout Lead, and Content Lead *in parallel* — each reading deep domain-specific knowledge files. A Color Lead focused entirely on OKLCH color theory produces better palettes than a generalist trying to handle color, fonts, and layout in one prompt. Then a CDO (Chief Design Officer) merges their outputs with explicit conflict resolution rules.

**Persistent agent memory.** Every specialist remembers past decisions across sessions. The 5th time Typography Lead runs on your project, it already knows your fonts, your scale, your preferences, and past issues. This is not conversation history — it's structured, per-agent, per-project memory stored as human-readable markdown with optional semantic search via embeddings.

**Anti-slop by design.** svvarm includes a 38-pattern AI design detection system. The Slop Auditor scores your output 0-100 and identifies exactly which patterns make it look AI-generated: purple-to-blue gradients, glassmorphism everywhere, identical card grids, cookie-cutter heroes, Inter as the only font. If an AI would generate it, svvarm flags it and fixes it.

**Unified design token system.** All 7 agents produce output using the same `--color-*`, `--space-*`, `--font-*` token naming convention. Color Lead's `--color-surface` is the same token Layout Lead references in its HTML. No naming mismatches, no broken CSS variable chains.

## Install

```
/plugin marketplace add robzilla1738/svvarm
/plugin install svvarm@svvarm
/reload-plugins
```

That's it. Works immediately.

### Optional: Semantic memory search (recommended)

svvarm's memory system works out of the box with keyword search. For smarter cross-agent memory recall, add an embedding backend:

```bash
brew install ollama && ollama serve && ollama pull bge-m3
```

svvarm auto-detects Ollama. No config needed.

## Requirements

- **Claude Code** v2.1+
- **uv** — `brew install uv` (Python script runner for memory and UI)
- **Ollama** (optional) — enables semantic search across agent memories

## Usage

```
/svvarm init            # New project — guided design brief creation
/svvarm setup           # Existing project — scans codebase, creates context
/svvarm audit           # Full quality review (3 agents in parallel)
/svvarm                 # Open-ended creative conversation with the CDO
/svvarm [anything]      # Natural language — auto-routes to the right specialist
```

### Examples

```
/svvarm build me a landing page       # Full Build: all 7 agents, 5-phase pipeline
/svvarm the fonts feel off            # Typography Lead
/svvarm this looks like AI made it    # Slop Auditor
/svvarm make it bolder                # Layout Lead + Color Lead (parallel)
/svvarm is this accessible            # Production Lead
/svvarm the copy is awkward           # Content Lead
/svvarm polish this                   # Polish Lead
/svvarm is this ready to ship         # Slop Auditor + Polish Lead + Production Lead
```

Just describe what you need. svvarm parses your intent and dispatches the right specialists.

## The team

7 specialist agents, each with dedicated knowledge files:

| Specialist | Knowledge base | What they do |
|------------|---------------|--------------|
| **Color Lead** | `color-mastery.md` (OKLCH theory, gamut mapping, contrast algorithms) | Builds palettes with tinted neutrals, proper contrast ratios, dark mode support |
| **Typography Lead** | `typography-mastery.md` + `font-pairings-db.md` (19 curated pairings) | Font selection, fluid type scales with `clamp()`, weight distribution, loading strategy |
| **Layout Lead** | `layout-mastery.md` + `component-mastery.md` (component recipes) | Every Layout patterns, spacing rhythm, semantic HTML, grid composition |
| **Content Lead** | `ux-writing-mastery.md` | UX copy, marketing text, error messages, voice matching, humanizing AI text |
| **Slop Auditor** | `anti-slop-bible.md` (38 AI convergence patterns) | Scores 0-100, identifies exactly which patterns make output look AI-generated |
| **Polish Lead** | All mastery files | Cross-cutting refinement: alignment, consistency, token usage, detail quality |
| **Production Lead** | All mastery files | Responsive behavior, accessibility (WCAG AA), performance, resilience |

## Full Build pipeline

When you say "build me a landing page", svvarm runs a 5-phase pipeline:

```
Phase 0: CDO writes Creative Brief
         (Vibe, Memorable Thing, Constraint)
              │
Phase 1: ┌────┼────┬────┐
         │    │    │    │    4 agents in parallel
       Color Type Layout Content
         │    │    │    │
         └────┼────┴────┘
              │
Phase 2: CDO assembles page
         (strict merge order, conflict resolution)
              │
Phase 3: ┌────┼────┬────┐
         │    │    │    │    3 agents in parallel
       Slop Polish Production
         │    │    │    │
         └────┼────┴────┘
              │
Phase 4: Save all agent memories
```

**Phase 0** — The CDO writes a 3-sentence Creative Brief before dispatching anyone. Every agent designs toward the same vision.

**Phase 1** — Color, Typography, Layout, and Content Leads run in parallel. Each reads only their domain knowledge, producing focused, expert-level output.

**Phase 2** — The CDO merges all outputs in a strict order (spacing tokens → color tokens → typography tokens → HTML skeleton → copy → interaction). Conflict resolution rules determine who wins when agents disagree.

**Phase 3** — Three quality agents audit the assembled page in parallel. The Slop Auditor checks for AI patterns, Polish Lead checks alignment and consistency, Production Lead checks responsive behavior and accessibility. If issues are found, specific remediation rules guide the fixes.

**Phase 4** — Every agent's decisions are saved to per-project memory for future sessions.

## Agent memory system

This is the feature that makes svvarm get better over time. Each specialist has persistent, per-project memory.

```
your-project/
└── .svvarm/
    ├── context.md           # Design brief (source of truth)
    ├── decisions.md         # Cross-agent decision log
    └── memory/              # Per-agent memories
        ├── color-lead.md    # "Chose warm neutrals, user rejected cool grays twice"
        ├── typography-lead.md   # "Using Instrument Sans + Newsreader, 1.25 ratio"
        ├── layout-lead.md   # "User prefers asymmetric layouts, no card grids"
        └── ...
```

**How it works:**
- Before dispatching an agent, the CDO reads that agent's memory file and includes it in the prompt
- The agent sees all its past decisions, user preferences, and established patterns
- After the agent returns, new decisions are appended to its memory
- Cross-agent context is available too — Typography Lead can see what Color Lead decided

**What gets remembered:**
- Design decisions and the reasoning behind them
- User preferences learned from corrections ("rejected cool grays twice")
- Established patterns ("4pt spacing base, 1.25 type ratio")
- Issues to watch ("card grid tendency — push for varied layouts")

**Semantic search (with Ollama/OpenAI/llama.cpp):**
Memories are chunked, embedded, and indexed in ChromaDB. When the CDO recalls an agent, it can semantically search across all agent memories for relevant context — not just the agent's own file.

**Keyword fallback (no setup needed):**
Without an embedding backend, memory still works. Save, read, and recall all use the markdown files directly. Search falls back to keyword matching.

**Git-friendly:** Memory files are plain markdown — readable, diffable, committable. The vector index (`.svvarm/.chromadb/`) is a derived cache that rebuilds automatically. Add it to `.gitignore`.

## Style guides

5 complete style guides with specific OKLCH colors, font pairings, spacing tokens, and motion rules:

| Style | Vibe | Best for |
|-------|------|----------|
| **Dark Premium** | Sleek, cinematic, high-end | Creative tools, premium SaaS |
| **Minimal Refined** | Ruthless restraint, precision | SaaS, productivity, dashboards |
| **Brutalist Raw** | Raw, structural, anti-decoration | Portfolios, editorial, dev tools |
| **Organic Warm** | Natural, tactile, handmade | Wellness, food, artisan brands |
| **Playful Bold** | Vibrant, energetic, personality-forward | Consumer apps, gaming, creative |

You can also describe your own direction ("moody and cinematic", "clean but not boring") and svvarm will adapt.

## Knowledge library

11 deep reference files the specialists consult:

- **anti-slop-bible.md** — 38 AI design convergence patterns with detection + fixes
- **typography-mastery.md** — Type scales, fluid `clamp()` formulas, dark mode typography
- **color-mastery.md** — OKLCH color theory, gamut mapping, P3 wide-gamut, accessibility
- **layout-mastery.md** — Every Layout primitives, CUBE CSS, spacing rhythm systems
- **component-mastery.md** — Token-based component recipes (buttons, cards, inputs, nav, modals)
- **font-pairings-db.md** — 19 curated font pairings organized by aesthetic
- **ux-writing-mastery.md** — Microcopy, error messages, empty states, voice frameworks
- **interaction-mastery.md** — Hover states, focus management, scroll-driven effects
- **motion-mastery.md** — Easing curves, duration scales, reduced-motion support
- **icon-mastery.md** — Icon systems, sizing, alignment, library recommendations
- **case-studies.md** — Design analysis of Linear, Stripe, Vercel, Apple, Nothing

## Configuration

### Embedding backends

Configure in `~/.svvarm/config.json` (global) or `.svvarm/config.json` (per-project override):

| Backend | Setup | Notes |
|---------|-------|-------|
| **Ollama** (recommended) | `brew install ollama && ollama serve && ollama pull bge-m3` | Free, local, auto-detected |
| **OpenAI** | Set `OPENAI_API_KEY` env var, set `"backend": "openai"` in config | Uses text-embedding-3-small |
| **llama.cpp** | Best quality with LCO-Embedding-Omni-3B model | See setup below |
| **None** | No setup needed | Keyword search fallback, still fully functional |

<details>
<summary>llama.cpp setup (best quality)</summary>

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

Control which Claude model the specialist agents use. Add to `.svvarm/config.json` in your project:

```json
{
  "agent_model": "sonnet"
}
```

| Model | Tradeoff |
|-------|----------|
| `"opus"` | Highest quality output, slower, costs more |
| `"sonnet"` | Fast and capable, good default |
| `"haiku"` | Lightweight, good for copy editing |
| *(omit)* | Inherits parent model |

## License

MIT
