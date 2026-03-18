# Color Mastery

This file defines how to build, evaluate, and refine color systems for digital products.

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