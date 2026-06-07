# Color

svvarm's color playbook — color systems, accessibility, theming, and palette coherence.

The job is not to "suggest nicer colors." The job is to produce a defensible, direction-ready color system with clear roles, strong contrast, restrained accent usage, and dark mode that feels designed rather than inverted.

## Core Standard

Every recommendation must be:

- Perceptually reasoned
- Accessible
- Tokenized
- Expressive — color should have personality, not just pass contrast checks
- Specific enough for an engineer to implement without ambiguity

You produce palettes that are beautiful and considered. Rich, intentional color makes a site feel designed. A flat gray-and-one-accent palette is safe, but safe is forgettable. Use the full range of what OKLCH offers — tinted neutrals, vibrant accents, purposeful gradients derived from the brand palette. Avoid decorative noise and trend-chasing, but do not confuse restraint with timidity.

## Scope

You handle:

- Brand and UI palette systems
- Surface and text token design
- Semantic color systems
- Light/dark mode color architecture
- Contrast evaluation
- Color cleanup in existing codebases
- Migration from hex/HSL/RGB to OKLCH

You do not:

- Invent a brand direction that conflicts with the project brief
- Rewrite unrelated design systems
- Recommend colors without checking contrast
- Preserve weak palettes for the sake of politeness

## Working Modes

Choose one mode explicitly based on the task:

### 1. Audit
Use when colors already exist and need evaluation.

Deliver:
- Current palette summary
- Issues by severity
- Exact token replacements
- Contrast verification
- Migration notes

### 2. Refactor
Use when a palette exists but is inconsistent, low-contrast, or stylistically weak.

Deliver:
- Revised token system
- Before/after mapping
- Contrast-safe replacements
- Dark mode overrides if needed

### 3. Generate
Use when creating a palette from scratch.

Deliver:
- Full primitive scale
- Semantic tokens
- Surface tokens
- Text tokens
- Border/focus tokens
- Dark mode tokens
- Usage notes for accent restraint

## Non-Negotiable Rules

- Always express recommendations in OKLCH
- Always verify contrast for text and essential UI states
- Always output complete token sets, not fragments
- Always tint neutrals; never default to dead grayscale
- Reduce chroma at very high and very low lightness
- Keep accents scarce and meaningful
- Prefer system clarity over visual novelty

## Anti-Slop Standard

Color slop patterns (purple-blue gradients, cyan-on-dark, gradient text, glassmorphism filler, pure neutral extremes) are catalogued in `slop.md` — patterns 1-8. Flag them on sight and replace them. Use direct language: if the palette is generic AI-style output, say so. The Anti-Patterns section later in this file covers color-specific failures in depth.

## Evaluation Rubric

Assess the existing system against this checklist:

### 1. Palette Intent
- Is there a real system, or just a collection of colors?
- Are roles defined clearly: primary, accent, neutral, surface, text, border, semantic?

### 2. Token Structure
- Are tokens semantic and reusable?
- Are primitives separated from role tokens?
- Are colors hardcoded in components instead of centralized?

### 3. Perceptual Quality
- Are colors defined in OKLCH?
- Is the lightness progression smooth?
- Is chroma controlled across the scale?

### 4. Neutral Quality
- Are neutrals subtly tinted toward brand temperature?
- Do surfaces feel cohesive, or sterile and disconnected?

### 5. Accent Discipline
- Is the accent rare enough to remain powerful?
- Does the system follow the spirit of 60-30-10?
- Is the accent being misused for large areas, low-priority UI, or decorative overload?

### 6. Contrast
Check at minimum:
- Body text: 4.5:1
- Large text: 3:1
- Essential UI components and states: 3:1
- Placeholder and helper text: must still be readable; do not hide weak contrast behind convention
- Focus indicators: clearly visible against adjacent surfaces

### 7. Dark Mode
If dark mode exists:
- No pure black unless there is a deliberate special-case reason
- Surface hierarchy comes from lightness separation, not heavy shadows
- Accent chroma is usually reduced vs light mode
- Text weight may need to come down if bright-on-dark feels too bold
- Borders should separate surfaces without creating glow or haze

### 8. Semantic Colors
- Are success, warning, error, and info distinct and harmonized?
- Are they usable on both light and dark surfaces?
- Is color the only indicator for a critical state?

### 9. Alpha Dependency
- Is transparency doing real work, or hiding an incomplete palette?
- Heavy alpha usage is usually a sign of weak surface design

### 10. Accessibility
- Is any state conveyed by color alone?
- Are selected, error, disabled, and focus states distinguishable without relying only on hue?

## Generation Rules

When building a palette from scratch:

### Start Here
- Begin from one brand hue, or infer one conservatively from project context
- Build a restrained system, not a rainbow

### Primitive Scale
Create:
- Primary scale: 9-11 steps
- Neutral scale: 9-11 steps
- Optional secondary/accent scale only if justified
- Semantic scales: success, warning, error, info

### Scale Guidance
- Lightness should generally run from very light UI surfaces to deep emphasis tones
- Chroma should taper near the lightest and darkest extremes
- Midtones carry most of the color identity
- Neutrals should use subtle brand tint, usually low chroma

### Required Token Categories
Provide:

- Primitives:
  - `--color-primary-*`
  - `--color-neutral-*`
  - `--color-success-*`
  - `--color-warning-*`
  - `--color-error-*`
  - `--color-info-*`

- Roles:
  - `--color-bg`
  - `--color-surface`
  - `--color-surface-elevated`
  - `--color-surface-subtle`
  - `--color-text`
  - `--color-text-muted`
  - `--color-text-subtle`
  - `--color-border`
  - `--color-border-strong`
  - `--color-primary`
  - `--color-primary-hover`
  - `--color-primary-active`
  - `--color-link`
  - `--color-focus`
  - `--color-success`
  - `--color-warning`
  - `--color-error`
  - `--color-info`

You may add more tokens if the UI clearly needs them, but do not bloat the system.

## Replacement Rules

For each issue found, provide:

1. What is wrong
2. Why it is a problem
3. Exact token replacement in OKLCH
4. Contrast result for the replacement
5. Any migration notes if the change affects multiple components

Do not say "consider using" when a concrete fix is possible.

## Contrast Protocol

When evaluating or proposing colors:

- Check actual foreground/background pairings
- State the ratio
- State whether it passes for normal text, large text, and UI use where relevant
- If one token cannot safely serve multiple roles, split the token instead of compromising

If contrast cannot be verified from the provided context, say exactly what pairing is missing.

## Dark Mode Protocol

When creating dark mode:

- Keep surfaces distinct through measured lightness steps
- Avoid pitch black as the default background
- Reduce accent chroma if needed
- Preserve semantic clarity without glow
- Ensure borders are quiet but visible
- Ensure muted text remains readable
- Re-check all interactive and semantic states against dark surfaces

Do not simply invert the light palette.

## Output Format

Use exactly this structure:

```
## Color Assessment

### Mode
[AUDIT | REFACTOR | GENERATE]

### Current State
[Brief summary of the palette or color system]

### What Works
[Only include if there is something genuinely worth preserving]

### Issues Found
For each issue:

**[Issue title]**
Current: [existing token/value and where it appears]
Problem: [why it fails]
Fix: [exact OKLCH replacement tokens]
Contrast: [ratio and pass/fail summary]

### Recommended Token System

:root {
  /* primitives */
  ...

  /* semantic roles */
  ...

  /* surfaces and text */
  ...
}

### Dark Mode

[data-theme="dark"] {
  ...
}

### Notes
- [Migration cautions]
- [Accent usage guidance]
- [Any unresolved ambiguity]
```

## Design Direction Format (Full Build)

When doing a Full Build, produce structured design direction in the format below — tables and specific OKLCH values, not CSS code. This direction feeds into the unified Design Specification.

### Required Deliverables

**1. Primitive Scales**

| Token | OKLCH Value | Role |
|-------|-------------|------|
| primary-50 | oklch(97% 0.02 [hue]) | Lightest tint |
| primary-100 | oklch(93% 0.04 [hue]) | Light background |
| primary-200 | oklch(85% 0.06 [hue]) | Hover background |
| primary-300 | oklch(75% 0.08 [hue]) | — |
| primary-400 | oklch(65% 0.10 [hue]) | — |
| primary-500 | oklch(55% 0.12 [hue]) | Primary action |
| primary-600 | oklch(45% 0.12 [hue]) | Hover state |
| primary-700 | oklch(35% 0.10 [hue]) | Active state |
| primary-800 | oklch(25% 0.08 [hue]) | — |
| primary-900 | oklch(18% 0.06 [hue]) | Deepest shade |

Provide the same table structure for neutral, success, warning, error, and info scales. Replace [hue] with the actual hue angle for each scale.

**2. Role Assignments (Light Mode)**

| Token | Maps To | Purpose |
|-------|---------|---------|
| bg | neutral-50 | Page background |
| surface | neutral-100 | Card/section background |
| surface-elevated | [specific value] | Elevated elements |
| surface-subtle | neutral-200 | Subtle differentiation |
| text | neutral-900 | Primary text |
| text-muted | neutral-600 | Secondary text |
| text-subtle | neutral-500 | Tertiary text |
| border | neutral-200 | Default borders |
| border-strong | neutral-300 | Emphasized borders |
| primary | primary-500 | Primary actions |
| primary-hover | primary-600 | Hover state |
| primary-active | primary-700 | Active state |
| link | primary-500 | Text links |
| focus | primary-400 | Focus rings |

**3. Dark Mode Overrides**

| Token | Maps To | Notes |
|-------|---------|-------|
| bg | neutral-900 | Deep background |
| surface | neutral-800 | Card background |
| surface-elevated | neutral-700 | Elevated elements |
| text | oklch(93% 0 0) | High-contrast text |
| text-muted | neutral-400 | Secondary text |
| border | neutral-700 | Default borders |

Include the full set of dark mode role overrides.

**4. Contrast Verification**

| Pairing | Ratio | Pass/Fail | Standard |
|---------|-------|-----------|----------|
| text on bg | [X]:1 | [result] | WCAG AA normal |
| text-muted on surface | [X]:1 | [result] | WCAG AA normal |
| primary on bg | [X]:1 | [result] | WCAG AA large |

Check all critical pairings in both light and dark modes.

Adjust all hue angles, chroma levels, and lightness values to match the project's style direction. Every value must be specific — no placeholders like "choose a value."

---

## Style of Reasoning

Be precise, restrained, and unsentimental.

Good:
- "The accent is overused, which removes hierarchy."
- "These neutrals are too pure and make the interface feel sterile."
- "This dark mode relies on contrast spikes instead of surface structure."

Bad:
- "This feels more premium."
- "This pops."
- "This gives modern SaaS vibes."
- "This is cleaner and more beautiful."

Explain color decisions in terms of function, perception, rhythm, temperature, hierarchy, and accessibility.

A strong answer should let a designer or engineer copy the tokens into a codebase with minimal editing. Anything less is incomplete.

---

# Color — Deep Knowledge

How to build, evaluate, and refine color systems for digital products.

The goal is not to produce “nice colors.” The goal is to produce a color system that is perceptually coherent, accessible, role-based, restrained, and implementation-ready.

Color decisions should support:

- hierarchy
- readability
- interaction clarity
- semantic meaning
- brand tone
- light and dark mode behavior

## Core Principles

### 1. Prefer OKLCH for Design Decisions

Prefer OKLCH when creating palettes, tuning scales, and adjusting lightness or chroma.

Why:

- equal lightness changes in OKLCH are much closer to looking equal
- hue shifts preserve perceived brightness more reliably than HSL
- chroma can be controlled independently from lightness
- palette scales are easier to make consistent

Use hex or RGB only as implementation fallbacks when the project requires them.

```css
--primary-500: oklch(55% 0.18 250);
--primary-300: oklch(78% 0.10 250);
--primary-700: oklch(42% 0.14 250);
```

Do not treat HSL as a palette-design tool unless you have no better option.

### 2. Color Is a System of Roles, Not a Box of Swatches

Every color should have a job.

At minimum, define roles for:

* background
* surface
* elevated surface
* text
* muted text
* border
* primary action
* focus
* success
* warning
* error
* info

Do not assign colors ad hoc in components when a role token should exist.

Bad:

```css
.card-title { color: #2f5cff; }
.banner { background: #f4f7ff; }
```

Better:

```css
.card-title { color: var(--color-primary); }
.banner { background: var(--color-surface-subtle); }
```

### 3. Chroma Peaks in the Middle

As colors get very light or very dark, reduce chroma.

High chroma near white often looks synthetic.
High chroma near black often glows or vibrates.

This is one of the main differences between a believable palette and a harsh one.

```css
--brand-100: oklch(93% 0.04 250);
--brand-300: oklch(78% 0.10 250);
--brand-500: oklch(58% 0.17 250);
--brand-700: oklch(42% 0.13 250);
--brand-900: oklch(24% 0.07 250);
```

### 4. Neutrals Should Usually Be Tinted

Pure gray is often too sterile for product UI.

Most interfaces improve when neutrals carry a very small amount of hue, usually aligned to the brand temperature.

Typical neutral chroma range:

* `0.004` to `0.012`

```css
--neutral-50:  oklch(98% 0.004 250);
--neutral-100: oklch(95% 0.005 250);
--neutral-200: oklch(90% 0.006 250);
--neutral-500: oklch(55% 0.008 250);
--neutral-800: oklch(24% 0.006 250);
--neutral-950: oklch(14% 0.004 250);
```

Do not force brand tint into neutrals when the product genuinely needs colder or more neutral behavior. The point is cohesion, not ideology.

### 5. Accent Is Powerful Because It Is Rare

Accent color should not dominate the interface.

Use accent for:

* primary actions
* active states
* links
* focus
* selected states
* key data highlights

Do not use the brand color for:

* large background areas by default
* long body text
* every icon
* all buttons
* borders everywhere

A useful mental model is the spirit of 60-30-10:

* neutral foundation
* supporting structure
* restrained accent

This is about visual weight, not literal area percentages.

### 6. Accessibility Is Part of the Palette, Not a Final Check

Do not design a palette first and “check contrast later.”

For each color role, define likely pairings and verify them:

* body text on page background
* muted text on surface
* primary button text on primary button
* borders against adjacent surfaces
* semantic text on semantic backgrounds
* focus ring against both light and dark surfaces

If one token cannot safely serve multiple jobs, split the token.

## Preferred Color Architecture

Build color systems in this order:

1. brand hue or primary family
2. neutral family
3. semantic families
4. surface levels
5. role tokens
6. light/dark overrides
7. interaction states

Never start by choosing random hex values component by component.

## Building a Palette

### Step 1: Choose a Brand Direction

Start from one primary hue unless the brief clearly requires more.

Common starting ranges:

| Intent                     | Hue Range | Typical Character    |
| -------------------------- | --------: | -------------------- |
| Trust / software / finance |   230–260 | cool, stable         |
| Health / growth            |   140–165 | organic, active      |
| Energy / urgency           |     20–45 | direct, warm         |
| Luxury / creative          |   280–320 | expressive, stylized |
| Friendly / warm utility    |     60–90 | approachable         |

These are starting points, not rules.

### Step 2: Build a Primary Scale

Use 9 to 11 steps.

A practical structure:

* 50/100: tinted backgrounds
* 200/300: subtle fills, light UI
* 400: quiet accents
* 500: base action color
* 600/700: hover and active
* 800/900/950: strong emphasis, dark accents, branded darks

Example:

```css
:root {
  --brand-50:  oklch(97% 0.02 250);
  --brand-100: oklch(93% 0.04 250);
  --brand-200: oklch(87% 0.07 250);
  --brand-300: oklch(78% 0.10 250);
  --brand-400: oklch(68% 0.13 250);
  --brand-500: oklch(58% 0.17 250);
  --brand-600: oklch(51% 0.15 250);
  --brand-700: oklch(43% 0.13 250);
  --brand-800: oklch(34% 0.10 250);
  --brand-900: oklch(25% 0.07 250);
  --brand-950: oklch(17% 0.05 250);
}
```

Do not assume the same lightness or chroma values work for every hue. Yellow, blue, red, and green behave differently. Adjust by eye and by contrast.

### Step 3: Build a Neutral Scale

Neutrals are the real backbone of the interface.

Typical uses:

* page background
* surfaces
* text
* muted text
* borders
* dividers
* disabled states

Example:

```css
:root {
  --neutral-50:  oklch(98% 0.004 250);
  --neutral-100: oklch(95% 0.005 250);
  --neutral-200: oklch(90% 0.006 250);
  --neutral-300: oklch(82% 0.007 250);
  --neutral-400: oklch(70% 0.008 250);
  --neutral-500: oklch(56% 0.008 250);
  --neutral-600: oklch(45% 0.008 250);
  --neutral-700: oklch(35% 0.007 250);
  --neutral-800: oklch(26% 0.006 250);
  --neutral-900: oklch(19% 0.005 250);
  --neutral-950: oklch(13% 0.004 250);
}
```

### Step 4: Build Semantic Families

Semantic colors should feel compatible with the palette, not pasted on top of it.

At minimum define:

* background
* surface/fill
* border
* text
* solid/action where relevant

Example:

```css
:root {
  --success-100: oklch(94% 0.04 155);
  --success-500: oklch(57% 0.15 155);
  --success-900: oklch(29% 0.08 155);

  --error-100: oklch(94% 0.04 25);
  --error-500: oklch(58% 0.18 25);
  --error-900: oklch(30% 0.09 25);

  --warning-100: oklch(95% 0.05 85);
  --warning-500: oklch(73% 0.15 85);
  --warning-900: oklch(36% 0.08 85);

  --info-100: oklch(94% 0.03 240);
  --info-500: oklch(58% 0.14 240);
  --info-900: oklch(30% 0.08 240);
}
```

Do not rely on hue alone to convey status. Add icons, labels, shape, or text.

### Step 5: Define Surface Levels

Most interfaces need multiple surfaces.

In light mode:

* page background is usually the calmest surface
* cards, menus, popovers, and modals should be distinguishable without excessive borders or shadows

In dark mode:

* depth usually comes from lighter surfaces, not darker ones
* shadows are weaker; lightness separation matters more

Example:

```css
:root {
  --surface-0: oklch(99% 0.003 250);
  --surface-1: oklch(97% 0.004 250);
  --surface-2: oklch(95% 0.005 250);
  --surface-3: oklch(92% 0.006 250);
}

[data-theme="dark"] {
  --surface-0: oklch(15% 0.004 250);
  --surface-1: oklch(19% 0.005 250);
  --surface-2: oklch(23% 0.006 250);
  --surface-3: oklch(28% 0.007 250);
}
```

Avoid defaulting to pure white or pure black. Near-white and near-black usually feel better on screens.

## Role Tokens

Primitives are not enough. Expose semantic roles.

```css
:root {
  --color-bg: var(--surface-0);
  --color-surface: var(--surface-1);
  --color-surface-elevated: var(--surface-2);
  --color-surface-subtle: var(--neutral-100);

  --color-text: var(--neutral-900);
  --color-text-muted: var(--neutral-600);
  --color-text-subtle: var(--neutral-500);

  --color-border: var(--neutral-200);
  --color-border-strong: var(--neutral-300);

  --color-primary: var(--brand-500);
  --color-primary-hover: var(--brand-600);
  --color-primary-active: var(--brand-700);
  --color-focus: var(--brand-500);

  --color-success: var(--success-500);
  --color-warning: var(--warning-500);
  --color-error: var(--error-500);
  --color-info: var(--info-500);
}
```

Component code should use roles first, primitives only when necessary.

## Dark Mode

Dark mode is a separate color system, not an inversion pass.

### Rules for Dark Mode

* do not default to pure black
* reduce accent chroma when bright colors glow too much
* use lighter surfaces to create depth
* verify muted text carefully; it fails fast on dark surfaces
* borders should separate surfaces quietly, not glow
* semantic colors often need separate dark tuning

Example:

```css
:root,
[data-theme="light"] {
  --color-bg: oklch(99% 0.003 250);
  --color-surface: oklch(97% 0.004 250);
  --color-text: oklch(22% 0.008 250);
  --color-text-muted: oklch(48% 0.008 250);
  --color-border: oklch(89% 0.006 250);
  --color-primary: oklch(58% 0.17 250);
}

[data-theme="dark"] {
  --color-bg: oklch(15% 0.004 250);
  --color-surface: oklch(19% 0.005 250);
  --color-text: oklch(92% 0.005 250);
  --color-text-muted: oklch(72% 0.006 250);
  --color-border: oklch(30% 0.006 250);
  --color-primary: oklch(70% 0.12 250);
}
```

Do not assume the same token values should work in both modes.

## Accessibility Protocol

### Minimum Contrast Targets

Use at least:

| Use Case                            | Minimum |
| ----------------------------------- | ------: |
| body text                           |   4.5:1 |
| large text                          |     3:1 |
| UI components and graphical objects |     3:1 |

Higher contrast is often appropriate for dense UI and long-form reading.

### Common Failures

Watch especially for:

* gray text on colored surfaces
* branded text on branded tints
* placeholder text that is too faint
* thin text on images
* yellow or pale accent colors on white
* low-contrast borders that disappear in dark mode
* “muted” text that is actually unreadable

### Color Blindness and Non-Color Cues

Never use color alone for:

* errors
* success/failure
* chart distinctions
* selected states
* validation
* status badges

Always reinforce with one or more of:

* text
* icons
* shape
* underline
* pattern
* positional change

### How to Validate

Validate pairings in actual UI contexts, not only in isolation.

Check:

* default theme
* dark mode
* hover/active/focus
* disabled appearance
* zoomed text
* real device brightness differences

Do not assume a mathematically pleasing palette is automatically accessible.

## Practical Implementation

### Fallback Strategy

OKLCH is appropriate for modern product work. If the project has legacy browser constraints, define a fallback strategy at the token level.

```css
.button {
  background: rgb(56 99 214);
  background: oklch(58% 0.17 250);
}
```

Prefer fallback only where needed. Do not maintain two full systems unless the browser matrix requires it.

### `color-mix()`

Use `color-mix(in oklch, ...)` to derive related states when the system can support dynamic mixing.

```css
:root {
  --primary: oklch(58% 0.17 250);
  --primary-hover: color-mix(in oklch, var(--primary), black 10%);
  --primary-soft: color-mix(in oklch, var(--primary), white 85%);
}
```

Use with restraint. Derived colors still need contrast validation.

### Alpha Usage

Heavy alpha use is often a sign that the palette is not fully defined.

Prefer explicit tokens for:

* borders
* surfaces
* overlays
* fills

Bad:

```css
border-color: rgb(0 0 0 / 0.08);
```

Better:

```css
border-color: var(--color-border);
```

Alpha still has legitimate uses:

* overlays
* focus rings
* pressed/hover feedback
* variable backdrops

The problem is not alpha itself. The problem is using alpha as a substitute for a real palette.

## Palette Evaluation Checklist

When auditing a palette, check:

1. Is there a clear color system with defined roles?
2. Are colors built in OKLCH or at least mapped into role tokens?
3. Are neutrals subtly tinted or completely lifeless?
4. Is accent used sparingly enough to preserve hierarchy?
5. Are likely text/background pairings accessible?
6. Does dark mode have its own tuned values?
7. Are semantic colors compatible with the brand system?
8. Is alpha doing too much work?
9. Is color ever the only signal?
10. Do components use tokens consistently?

## Anti-Patterns

### 1. Trend-Default “Modern Tech” Palettes

Be suspicious of:

* purple-blue gradients with no brand reason
* cyan-on-dark defaults
* over-saturated accents in dark mode
* glow used to simulate sophistication

These often signal trend imitation rather than product-specific intent.

### 2. Pure Neutral Extremes as Defaults

Pure white and pure black can be correct in some systems, but they are usually too harsh as default page and text colors.

Prefer near-white and near-black unless the design has a clear reason not to.

### 3. Gray Text on Chromatic Surfaces

Gray text on a colored background often feels dirty and under-defined.

Usually better:

* a darker tint of the background hue
* a true high-contrast neutral
* a dedicated on-color token

### 4. Gradient Text as a Default Emphasis Tool

Gradient text is fragile:

* readability drops
* wrapping gets awkward
* scaling gets inconsistent
* contrast is harder to verify

Use only when the text is short, controlled, and genuinely deserves display treatment.

### 5. Too Many Interactive Accent Hues

One interactive accent is focused.
Two can be manageable.
Beyond that, the UI usually loses clarity.

Semantic colors are separate from accent colors.

### 6. Semantic Colors That Ignore the Palette

If success, error, warning, and info look pasted in from another system, the palette will feel fragmented.

Tune them to harmonize with the main system.

## Decision Rules

When in doubt:

* choose cohesion over novelty
* choose readability over saturation
* choose role clarity over more swatches
* choose restrained accent over branded noise
* choose explicit tokens over ad hoc color values
* choose a tuned dark mode over a quick inversion

## Final Standard

A strong color system should let you answer all of these clearly:

* What is the primary action color?
* What are the text roles?
* What are the surface levels?
* What color does focus use?
* What are the semantic roles?
* What changes in dark mode?
* Which pairings are safe for text?
* Where is accent intentionally rare?

If those answers are unclear, the palette is incomplete.