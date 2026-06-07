# Core — The svvarm Digest

This single file is enough to design a complete, svvarm-quality page or feature. It compresses every domain — color, typography, layout, content, slop detection, interaction, motion, production — into one read. For a full build, read THIS file, not the deep references.

## When to Pull a Deep File

Pull at most 2-3 deep files per build, and only when a trigger fires:

| Trigger | Deep file |
|---------|-----------|
| Picking final fonts (need sources, fallbacks, import snippets, all 19 pairings) | `font-pairings.md` |
| Hand-computing full 9-11 step OKLCH primitive scales | `color.md` |
| Direction needs real-brand reference points or ambitious pattern vocabulary | `inspiration.md` |
| Heavy interactive surfaces: multi-step forms, overlays, keyboard navigation | `interaction.md` |
| MOTION dial ≥ 7: scroll choreography, view transitions, stagger budgets | `motion.md` |
| Detailed slop audit with evidence format and worked scoring | `slop.md` |
| Component code recipes, layout primitives, grid architecture | `layout.md` |
| Deep type-system work: OpenType, variable fonts, loading strategy | `typography.md` |
| Full UX-copy pass: empty states, validation messages, microcopy tables | `content.md` |
| Icon system decisions: library choice, sizing tables, a11y patterns | `icons.md` |
| Final polish pass: 6-pass refinement, token extraction, distill mode | `polish.md` |

For **focused tasks** (the user asked about one domain), skip this digest and read that domain's deep file directly — see the Reference File Index in SKILL.md.

---

## Core Design Principles

Non-negotiables. Every project, every style.

1. **Beautiful first, safe never** — The goal is a page someone would screenshot and share. A clean page that avoids all risk is forgettable. Push for visual craft: rich color, dramatic typography, purposeful motion, layouts with rhythm.
2. **Intentionality over decoration** — Every element earns its place by adding beauty, delight, or emphasis. A gradient that sets a mood earns its place. A floating orb does not.
3. **Hierarchy through multiple dimensions** — Size + weight + color + space. Never size alone.
4. **The "one memorable thing" test** — What will someone remember 24 hours later? If nothing, the design needs more ambition, not more polish.
5. **Constraint creates identity** — What you exclude defines the design. Two fonts beat five. Constraint is focus, not minimalism for its own sake.
6. **Start with too much whitespace** — Then remove. Easier than adding after cramming.
7. **Match code complexity to vision** — Maximalist vision = elaborate code. Minimalist vision = precision.
8. **No profanity in output** — Mask strong language with ****.

---

## The 38 Anti-Slop Patterns

AI design converges on statistical averages. These are the convergence patterns — each with the one-line fix. Compound stacks matter more than isolated patterns: Inter alone is fine; Inter + purple gradient + identical cards + vague headline + centered everything = template output. Full detection details, scoring model, and evidence rules: `slop.md`.

### Color (1-8)

1. **Purple-to-blue gradients** → derive any gradient from the actual brand palette or go flat; if gradient, go unexpected: warm (coral→amber), earth (sage→cream), or monochromatic (dark navy→medium navy).
2. **Cyan/neon-on-dark** → warm or desaturated accents on dark (amber `#D97706`, coral, soft gold, slate blue, sage); cut saturation 20-30% from any neon value.
3. **Pure black `#000` / pure white `#FFF`** → near-black (`#0A0A0A`) and near-white (`#FAFAFA`); better, tint both with the brand hue.
4. **Gray text on colored backgrounds** → use a darker shade of the background hue, or white/near-white with verified contrast.
5. **Gradient text** → solid color + a distinctive typeface at dramatic size; mix weights within the heading if it needs punch.
6. **Glassmorphism everywhere** → at most one glass accent (e.g., the nav); every other surface opaque.
7. **Default dark mode with glowing accents** → intentional dark surface tiers (bg / surface-1 / surface-2 via lightness steps) + desaturated accents; zero neon box-shadows.
8. **Unmodified Tailwind palette** → custom palette in the Tailwind config, generated from brand colors.

### Typography (9-13)

9. **Inter/Roboto/Open Sans as only font** → pair a distinctive display face (Satoshi, Instrument Sans, Space Grotesk, Clash Display) or a serif (Fraunces, Newsreader) — AI almost never suggests serifs.
10. **Decorative monospace** → monospace only for actual code, data, or small labels; headlines get a proper display face.
11. **Large rounded icons above every heading** → icons only when they add information; vary size/placement, use them inline, or cut them.
12. **Weak type hierarchy** → dramatic scale (body 16-18px, H1 48-72px; largest-to-body ratio ≥ 2:1) + aggressive weight variation (300/400/600/700-800).
13. **Competing fonts with no relationship** → one family in multiple weights, or exactly two fonts with explicit role rules.

### Layout (14-21)

14. **Cookie-cutter hero** (centered heading + muted subtitle + two buttons + gradient bg) → break at least two conventions: left-align, single CTA, real product screenshot, a testimonial or code snippet instead of the subtitle.
15. **Identical card grids** → vary card size by importance (one large + smaller supporting), mix content types, or replace cards with a well-set typographic list.
16. **Hero metric template** ("10K+ Users / 99.9% Uptime") → one compelling metric with context beats four vanity numbers; or cut entirely.
17. **Everything centered** → containers stay centered; body text inside them is left-aligned; alternate full-width, contained, and offset sections for rhythm.
18. **Cards inside cards** → flatten: only the outermost container gets borders/shadows; inner grouping via spacing and background tints.
19. **Same spacing everywhere** → spacing communicates hierarchy: 80-120px between sections, 32-48px between groups, 12-24px within groups.
20. **Formulaic section sequence** (hero→logos→features→testimonials→pricing→FAQ) → let the content dictate architecture: a dev tool leads with code, a creative tool leads with a gallery.
21. **Thick colored borders on rounded cards** → keep only when the border carries meaning (status); otherwise subtle border or spacing-defined groups.

### Visual Detail (22-27)

22. **Floating orbs / particles / pulsing glows** → remove; if background interest is needed: subtle texture, one well-placed gradient, or a photograph.
23. **Uniform `rounded-xl shadow-lg` on everything** → intentional radius (0 for editorial, 4-6px subtle, 12px+ reserved for buttons/pills) + brand-tinted custom shadows in a 3-5 level elevation system.
24. **Decorative sparklines / fake charts** → real data gets axes, labels, interactivity; decoration gets deleted.
25. **Fade-on-scroll on everything** → hero gets one subtle entrance; everything else appears instantly; if a section must animate, opacity-only under 200ms.
26. **Elastic/bounce easing** → `ease-out` entrances, `ease-in` exits; reserve overshoot for a single delight moment (a like button), never modals or cards.
27. **Stock/AI imagery** → real product screenshots, custom illustration, brand-derived abstract art, or no image at all.

### Content (28-33)

28. **Vague transformation headlines** ("Unlock the power of…") → name the audience and quantify the benefit: "Cut deploy time from 45 minutes to 90 seconds."
29. **Feature-dumping** → "[Feature] so that you can [benefit]" — lead with the benefit, the feature is support.
30. **Placeholder-quality body copy** → every sentence states a specific, verifiable fact; real numbers, real product name, brand voice.
31. **"Trusted by" logo walls** → add context and case-study links, or cut; one detailed attributed testimonial beats 20 unverified logos.
32. **Verbose UX writing** → "Get started," not "Click here to get started today"; labels ≤ 4 words, instructions ≤ 1 line.
33. **Same professional tone everywhere** → map tone to context: marketing confident + specific, onboarding warm, errors direct + helpful, success brief.

### UX / Interaction (34-38)

34. **Modals for everything** → inline confirmations, drawers for detail views, dedicated pages for flows; modals only for truly interruptive moments.
35. **Every button primary** → ONE primary action per context; secondary = outline/ghost; tertiary = text link.
36. **Cookie-cutter navigation** ("Product, Features, Pricing, About") → name nav items after what users actually look for: "Templates," "API," "Changelog."
37. **Missing interaction states** → all 8 states for every interactive element: default, hover, focus, active, loading, disabled, error, success.
38. **Non-functional forms** → verified end-to-end before shipping, or visibly marked "Demo Only" — never fake success.

---

## Color Rules

**Always OKLCH.** Equal lightness steps look equal; chroma controls independently of lightness. Hex/RGB only as implementation fallbacks.

**Build order:** brand hue → primary scale → neutral scale → semantic families → surface levels → role tokens → dark overrides → interaction states. Never pick hex values component by component.

**The five structural rules:**
1. **Chroma peaks mid-scale.** Taper chroma near the lightest and darkest extremes — high chroma near white looks synthetic, near black it glows.
2. **Tint neutrals.** Dead grayscale feels sterile; carry chroma 0.004-0.012 toward the brand temperature.
3. **Accent is powerful because it is rare.** 60-30-10 spirit: neutral foundation, supporting structure, restrained accent. Accent = primary actions, links, focus, selected states, key highlights. Never large surfaces, body copy, every icon.
4. **Color is roles, not swatches.** Minimum role tokens: `bg`, `surface`, `surface-elevated`, `surface-subtle`, `text`, `text-muted`, `text-subtle`, `border`, `border-strong`, `primary`, `primary-hover`, `primary-active`, `link`, `focus`, `success`, `warning`, `error`, `info`.
5. **Accessibility is part of the palette, not a final check.** Verify pairings as you assign roles.

**Scale shape** (9-11 steps): 50/100 tinted backgrounds · 200/300 subtle fills · 400 quiet accents · 500 base action · 600/700 hover/active · 800/900/950 strong emphasis. Example anchor points: `oklch(97% 0.02 H)` at 50, `oklch(58% 0.17 H)` at 500, `oklch(17% 0.05 H)` at 950.

**Hue starting ranges:** trust/software 230-260 · health/growth 140-165 · energy/urgency 20-45 · luxury/creative 280-320 · friendly/warm 60-90. Starting points, not rules.

**Dark mode is a separate system, not an inversion:**
- No pure black; bg around `oklch(15% 0.004 H)`, depth from LIGHTER surfaces (surface-1 19%, surface-2 23%, surface-3 28%)
- Reduce accent chroma (e.g., light `0.17` → dark `0.12`)
- Body text off-white `oklch(93% 0 0)` — never `#fff`
- Borders quiet but visible (~30% lightness); re-verify muted text, it fails fast on dark

**Contrast targets:** body text 4.5:1 · large text 3:1 · UI components 3:1 · focus rings clearly visible against adjacent surfaces. Never convey state by color alone — add icons, text, shape, or position.

---

## Typography Rules

**Hierarchy of impact:** typeface choice > size scale > line height > letter spacing > color.

**Modular scale.** Derive every size from a base × ratio: 1.125 dense dashboards · 1.200 SaaS/docs · 1.250 default for marketing · 1.333 dramatic/editorial.

**Required roles:** display, h1, h2, h3, body, body-sm, label, caption (+ code/data if relevant).

**Fluid for display, fixed for UI.** Hero/display text uses `clamp()`; body, app UI, and data tables use fixed rem.

`clamp()` formula (320px → 1200px viewport): `VW = (MAX_rem − MIN_rem) × 1.818`, `REM = MIN_rem − VW/5`. Reference values:

| Role | Min | Max | clamp() |
|------|-----|-----|---------|
| Display | 2.5rem | 5rem | `clamp(2.5rem, 1.59rem + 4.55vw, 5rem)` |
| H1 | 2rem | 3.5rem | `clamp(2rem, 1.45rem + 2.73vw, 3.5rem)` |
| H2 | 1.5rem | 2.5rem | `clamp(1.5rem, 1.14rem + 1.82vw, 2.5rem)` |
| H3 | 1.25rem | 1.75rem | `clamp(1.25rem, 1.07rem + 0.91vw, 1.75rem)` |

**Line height:** body 1.5-1.6 · headings 1.1-1.25 · display (40px+) 1.0-1.1 · captions 1.4-1.5 · buttons/labels 1.0-1.2. **Tracking:** tight (-0.02em and beyond) for display, normal for body, slightly open (+0.05em) for small caps/labels.

**Weight discipline:** few weights doing real work beats many doing none. One family in 4 weights often beats two families.

**Measure:** 65ch max for reading blocks (`max-inline-size: 65ch`). Body minimum 16px, always rem. Tabular figures (`font-variant-numeric: tabular-nums`) wherever numbers are compared.

**Dark mode typography:** reduce weights by ~100 (body 400→300, headings 600→500), increase line-height +0.05-0.1, off-white text.

**Loading:** self-host, WOFF2, `font-display: swap`, subset to needed scripts, preload critical files, 2-4 font files max, variable fonts when they simplify weights.

### Font Pairing Shortlist

Ten dependable pairings (full database of 19 with imports and cautions: `font-pairings.md`):

| Pairing | Best for |
|---------|----------|
| Inter Tight + Inter | Modern product UI, dashboards — clean dependable default |
| Geist + Geist Mono | Developer tools, AI products — current technical voice |
| IBM Plex Sans + IBM Plex Mono | Enterprise, data tools — precision without trend |
| Source Serif 4 + Source Sans 3 | Institutions, editorial trust — warmth with authority |
| Newsreader + Inter | Content-heavy products — reading comfort + crisp UI |
| DM Serif Display + DM Sans | Product marketing, landing pages — expressive but safe |
| Fraunces + DM Sans | Brand-led, lifestyle, creative SaaS — personality with usability |
| Clash Display + Satoshi | Startup launches, bold marketing — energy without novelty |
| Satoshi + Zodiak | Luxury commerce, premium portfolios — refined contrast |
| Neue Montreal + Editorial New | Agencies, fashion-adjacent — free "premium agency" tone |

Avoid: two loud fonts fighting, decorative monospace in body copy, serif display faces for paragraphs, quirky fonts for serious products.

---

## Spacing & Layout Rules

**Canonical spacing scale** (the single source of truth — identical table in `layout.md`):

| Token | Value | Use for |
|-------|-------|---------|
| `--space-2xs` | 0.25rem (4px) | Icon-to-label gaps, inline spacing |
| `--space-xs` | 0.5rem (8px) | Tight grouping, tag gaps |
| `--space-sm` | 0.75rem (12px) | Related items, input padding |
| `--space-base` | 1rem (16px) | Default padding, standard gaps |
| `--space-md` | 1.5rem (24px) | Component padding, paragraph gaps |
| `--space-lg` | 2rem (32px) | Card padding, between components |
| `--space-xl` | 3rem (48px) | Between component groups |
| `--space-2xl` | 4.5rem (72px) | Section separation |
| `--space-3xl` | 6rem (96px) | Major section separation |
| `--space-section` | `clamp(4rem, 8vw, 8rem)` | Top-level fluid section rhythm |

**The critical rule:** section spacing must be VISIBLY larger than component spacing, which must be visibly larger than element spacing. If you can't tell the three levels apart by squinting, the scale isn't working.

**Composition rules:**
- Content hierarchy first, then layout mechanics. Grid over flex-math (`repeat(3, 1fr)`, never `calc(33.33% - 1rem)`).
- Center page containers (`max-width` + `margin-inline: auto`); left-align body text WITHIN them.
- Cards earn their place — spacing, borders, or background shifts can often replace them. Never nest cards.
- Intrinsic responsiveness first: `auto-fit`, `minmax()`, flex wrap, container queries. Viewport breakpoints only when intrinsic behavior is insufficient.
- Protect measure: readable line lengths beat visual balance.
- Never break DOM/source order for visual novelty.

**Section variety (required):** every page uses at least 2 different composition patterns plus one pattern-breaker. The monotony-breakers:
1. **Zig-zag** — content/media alternate sides per section
2. **Full-bleed break** — one section spans the full viewport width as a pause
3. **Asymmetric grid** — `2fr 1fr` or `3fr 1fr`, one column dominates
4. **Scale shift** — one element dramatically larger than siblings, instant focal point
5. **Negative-space statement** — minimal content, maximum whitespace, communicates confidence

**Squint test:** blur the page — the most critical element should be obvious; groups should read as distinct blocks. Uniform gray field = failed hierarchy.

---

## Dial Calibration

Set three dials from the user's description — never ask them to pick numbers.

- **DESIGN_VARIANCE (1-10):** layout departure from convention. 1-3 symmetric/centered/predictable · 4-7 offsets, overlaps, asymmetric grids · 8-10 masonry, fractional grids, massive whitespace.
- **MOTION_INTENSITY (1-10):** 1-3 CSS hover/active only · 4-7 transition cascades, staggered reveals · 8-10 scroll-driven parallax, complex choreography.
- **VISUAL_DENSITY (1-10):** 1-3 art gallery whitespace · 4-7 balanced · 8-10 cockpit-tight.

| User describes… | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| "clean dev tool" | 3 | 4 | 6 |
| "cinematic portfolio" | 8 | 7 | 2 |
| "bright and playful SaaS" | 5 | 5 | 5 |
| "dark and premium" | 5 | 4 | 4 |
| "brutalist editorial" | 9 | 2 | 3 |
| "enterprise dashboard" | 2 | 2 | 8 |
| "fun consumer app" | 6 | 6 | 5 |
| "luxury fashion brand" | 7 | 6 | 2 |

Advanced pattern usage scales with dials (full catalog: `inspiration.md`). Maximum 2-3 advanced patterns per page, one per section; every pattern needs a "why" tied to the Creative Brief.

---

## Copy Rules

**Kill on sight:**
- Hype: revolutionary, game-changing, groundbreaking, ultimate, transformative, unlock, empower, revolutionize
- AI vocabulary: additionally, delve, crucial, pivotal, landscape (abstract), tapestry, testament, underscore, showcase, foster, vibrant, intricate, boasts, "serves as," "stands as"
- Negative parallelisms ("It's not just X, it's Y"), rule-of-three stuffing, em-dash overuse, "the future looks bright" conclusions, vague attributions ("experts argue")

**Length rules (non-negotiable):** headlines 3-7 words · subheadlines 1 sentence, ≤15 words · feature descriptions 1-2 sentences · button labels 2-4 words, action-first · testimonials 1-2 specific-sounding sentences.

**Mock data ban:** no "John Doe"/"Sarah Chan" (invent: "Elara Vance," "Tobias Sterling") · no round numbers (`47.2%`, not `50%`) · no "Acme"/"Nexus" (invent premium contextual names) · **no emojis, ever** — in copy, code, or markup.

**The human part — what actually sells:** opinions ("I was skeptical too"), direct address ("you've probably felt this"), rhythm variation (short punches, then longer thoughts), admitting imperfection ("it's not magic, but it works"), tiny stories instead of stacked benefits.

**UX copy:** button labels name the exact outcome ("Save changes," never "Submit/OK") · errors answer what happened + why + how to fix, never blame the user · empty states acknowledge + explain value + give an action · one term per concept, everywhere (Sign in, Delete, Settings, Create) · "Please" at most once per flow.

**Voice vs tone:** voice is constant (brand personality); tone adapts — success celebratory-brief, errors empathetic (never humorous), loading reassuring, destructive-confirm serious.

---

## Interaction & Motion Rules

**The 8 states** — every interactive element: default, hover, focus, active, loading, disabled, error, success. Never design hover without focus; keyboard users never see hover.

**Focus:** `:focus-visible` ring (2px solid, 2px offset) on everything interactive. Removing outline without a replacement is forbidden. Native `<dialog>` + `showModal()` for modals (free focus trap, Escape, backdrop). Skip-to-content link first in tab order on pages with nav.

**Touch:** targets ≥ 44×44px. Hover-only affordances are inaccessible — provide touch/keyboard equivalents (`@media (hover: none)`).

**Motion durations (100/300/500 rule):**
- 50-80ms button press · 100-150ms color/opacity · 150-200ms dropdowns/tooltips · 200-300ms toasts · 300-400ms modal enter · 400-600ms scroll reveal · 600-800ms hero entrance — the maximum. Nothing animates longer than 800ms.
- Exits run at ~75% of enter duration. Always.

**Easing:** never default `ease`, never bounce/spring on UI. Entrances `--ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1)` or `--ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1)`; exits `--ease-in: cubic-bezier(0.7, 0, 0.84, 0)`.

**Performance:** animate `transform` and `opacity` only — never width/height/margin/box-shadow. Scroll reveals via IntersectionObserver, reveal once, total group stagger under 500ms. Max 3 simultaneous animations in viewport. No parallax on mobile.

**Reduced motion (required when MOTION > 3):** remove spatial movement (reveals, slides, scale), keep functional animation (spinners, progress) instant or intact.

---

## Production Non-Negotiables

Automatic FAILs:
- **dvh over vh** — any `100vh`/`h-screen` full-height layout must be `100dvh`/`min-h-[100dvh]` (iOS Safari address-bar jumping).
- **Mobile collapse** — every multi-column, overlapped, or absolute-positioned composition collapses to single column below 768px. Zero horizontal scroll tolerance.
- **Touch alternatives** — hover-dependent reveals need `@media (hover: none)` paths.
- **Safe-area insets** — fixed and full-bleed elements include `env(safe-area-inset-*)` for notched devices.

Always:
- Semantic HTML: native `<button>`, `<a href>`, `<dialog>`, `<details>` — never clickable `<div>`s. `<header>/<main>/<section>/<nav>/<footer>` structure.
- Loading, empty, AND error states for anything async — skeletons without failure recovery are decoration.
- Test at 200% zoom, with long labels, with content extremes.
- Images: explicit dimensions or `aspect-ratio` (no layout shift), modern formats, lazy-load below the fold.
- Forms: visible `<label>`s (placeholders are not labels), validate on blur, errors via `aria-describedby` + `role="alert"`.

---

## Icon Quick Rules

- One library only: Lucide (general) · Phosphor (editorial/premium, 6 weights) · Radix (dense/minimal). Never mix families; never hallucinate SVG paths; never emoji-as-icon.
- Stroke weight optically matches adjacent text weight (300 text → 1px stroke; 600+ text → 2px).
- Sizes: 16px inline · 16-20px buttons · 20px nav · 32-40px feature highlights · 64px absolute max (beyond that, use an illustration).
- `currentColor` by default. Icon-only buttons: `aria-label` + 44×44px hit area. Decorative icons: `aria-hidden="true"`.

---

## Specification Completeness Rules

Design specs must be COMPLETE. Banned in specs:
- "etc.", "and so on", "[TBD]", "[TODO]", ellipsis in place of decisions
- "similar to the above" without specifying what
- "use appropriate spacing" without naming the token
- "choose a suitable font" without naming the font
- "repeat this pattern" without defining each instance

Before implementing, verify: every layout section has explicit spacing tokens · every text role has font, size, weight, line-height · every color role has an OKLCH value · every interactive element has hover, focus, active states · every copy placeholder is filled with actual copy.

---

## Self-Audit Gate

Run after producing a spec, before implementing.

**1. Slop check.** Scan the 38 patterns above. Score: +4 per definite pattern, +2 per borderline, +5 when one category has 3+ patterns, +10 when patterns span 4+ categories, +10 when the same generic logic repeats across sections. 0-20 distinctive · 21-40 mostly intentional · 41-60 needs work · 61+ generic. **If score > 40:** identify the top 3 driving patterns, revise those specific decisions, re-score.

**2. Pre-flight checklist:**
- [ ] Dial compliance — decisions match VARIANCE/MOTION/DENSITY values
- [ ] Mobile collapse — every section has a < 480px adaptation
- [ ] dvh compliance — no `100vh` anywhere
- [ ] Touch alternatives for every hover interaction
- [ ] Copy completeness — every placeholder has matching copy
- [ ] Token coherence — spacing/color/type tokens self-consistent
- [ ] Contrast verification — all text/bg combos pass WCAG AA
- [ ] Memorable Thing preserved — still bold after self-audit
- [ ] Reduced-motion path specified (if MOTION > 3)
- [ ] Section variety — 2+ different composition patterns used

**3. The two quality tests** — work is not complete until it passes BOTH:
- **Is it impressive?** Would someone screenshot it? Boring is worse than slop — slop can be fixed with restraint; boring requires starting over with ambition.
- **Is it distinctive?** Fewer than 3 compound anti-slop flags. If you showed it to someone and said "AI made this," would they believe you?
