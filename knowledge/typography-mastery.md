# Typography Mastery

This file defines how to build, evaluate, and refine typographic systems for digital products.

The hierarchy of impact: typeface choice > font size scale > line height > letter spacing > color. 

A page set in well-chosen type at proper sizes with correct line height needs almost nothing else.

## Core Principles

### 1. The Modular Scale

Every font size in your system must be derived from a single base size multiplied by powers of a chosen ratio. Do not use arbitrary pixel values.

Common ratios:
- `1.125` (Major second): Subtle, tight. Best for dense dashboards, data UIs.
- `1.200` (Minor third): Balanced, calm. Best for SaaS apps, documentation.
- `1.250` (Major third): Recommended default. Best for marketing sites, general use.
- `1.333` (Perfect fourth): Dramatic. Best for editorial, landing pages.

A standard 5-size system covers most needs:
- `xs` (base / ratio): Captions, labels, legal text
- `sm` (base / ratio^0.5): Secondary text, metadata, timestamps
- `base` (1rem): Body text, paragraphs, form inputs
- `lg` (base * ratio): Subheadings, card titles
- `xl` (base * ratio^2): Section headings
- `2xl` (base * ratio^3): Page titles
- `3xl` (base * ratio^4): Hero headlines

### 2. Fluid Type for Display, Fixed Type for UI

Use fluid typography (`clamp()`) for display text, hero headlines, and marketing pages so type scales smoothly between viewport sizes.

```css
/* Hero headline: 32px at 320px viewport, scales to 64px at 1200px */
.hero-title { font-size: clamp(2rem, 1.09rem + 3.64vw, 4rem); }
```

Do **not** use fluid type for body text, app UIs, dashboards, or data tables. Fixed `rem` scales provide predictable, controllable results in dense interfaces.

### clamp() Formula Reference

**Formula:** `clamp(MIN, CALC_REM + CALC_VW, MAX)`
- `VW = (MAX_rem - MIN_rem) × 1.818`
- `REM = MIN_rem - (VW / 100 × 20)`

This scales linearly from MIN at 320px viewport to MAX at 1200px viewport.

| Role | Min (320px) | Max (1200px) | clamp() |
|------|-------------|--------------|---------|
| Display | 2.5rem | 5rem | `clamp(2.5rem, 1.59rem + 4.55vw, 5rem)` |
| H1 | 2rem | 3.5rem | `clamp(2rem, 1.45rem + 2.73vw, 3.5rem)` |
| H2 | 1.5rem | 2.5rem | `clamp(1.5rem, 1.14rem + 1.82vw, 2.5rem)` |
| H3 | 1.25rem | 1.75rem | `clamp(1.25rem, 1.07rem + 0.91vw, 1.75rem)` |
| H4 | 1.125rem | 1.375rem | `clamp(1.125rem, 1.04rem + 0.45vw, 1.375rem)` |
| Body-lg | 1.0625rem | 1.25rem | `clamp(1.0625rem, 0.99rem + 0.34vw, 1.25rem)` |

**Worked example for Display (2.5rem → 5rem):**
1. VW = (5 - 2.5) × 1.818 = 4.545 → round to `4.55vw`
2. REM = 2.5 - (4.55 / 100 × 20) = 2.5 - 0.91 = 1.59 → verify: at 320px (20rem), 1.59 + 4.55 × 0.2 = 1.59 + 0.91 = 2.5rem ✓. Result: `clamp(2.5rem, 1.59rem + 4.55vw, 5rem)`.

Use this table as a starting point. Adjust min/max values based on the project's scale ratio and density.

### 3. Vertical Rhythm 

Line height determines the vertical rhythm of the layout. Every vertical measurement (margins, padding, gaps) should derive from it.

If body text is 16px (`1rem`) with a line-height of `1.5`, the baseline unit is `24px` (`1.5rem`). All vertical spacing should be multiples of this unit (`12px`, `24px`, `48px`, `72px`).

Line-height guidelines by context:
- Body text: `1.5` - `1.6` (Optimal readability for paragraphs)
- Headings: `1.1` - `1.25` (Tighter keeps multi-line headings cohesive)
- Large display text (40px+): `1.0` - `1.1` (Large text needs less leading)
- Captions / small text: `1.4` - `1.5` (Small text needs proportionally more air)
- UI labels / buttons: `1.0` - `1.2` (Single-line, vertically centered)

## Font Selection & Pairing

### Avoiding Invisible Defaults
Inter, Roboto, Open Sans, Lato, Montserrat, and Poppins are overexposed. Using them signals a lack of deliberate design decision.

### Better Alternatives
- **Modern Sans**: Instrument Sans, Plus Jakarta Sans, Outfit, Figtree, Onest, Geist, General Sans, Satoshi, Switzer.
- **Editorial Serif**: Fraunces, Newsreader, Lora, Literata, Crimson Pro, Source Serif 4, Spectral.
- **Display / Headline**: DM Serif Display, Playfair Display, Bricolage Grotesque, Syne, Space Grotesk, Cabinet Grotesk, Clash Display, Zodiak.

### Pairing Rules
1. **Contrast on multiple axes**: Pair fonts that differ in classification (serif + sans), construction (geometric + humanist), or proportion (condensed + wide). Similarity breeds confusion.
2. **Match x-heights**: Fonts with similar x-heights sit comfortably together on a page.
3. **Never pair fonts that are similar but not identical**: If they are not clearly different, use one font in multiple weights instead.
4. **One font, multiple weights**: Often better than two fonts. A single family in light/regular/semibold/bold creates hierarchy without introducing complexity.
5. **Max 2-3 families per project**: Heading font + body font covers 95% of cases. Add a monospace for code if needed.

## OpenType Features

Activate OpenType features to improve typographic refinement.

```css
/* Tabular figures for aligned data (tables, prices, dashboards) */
.price, .table-cell, .stat { font-variant-numeric: tabular-nums; }

/* Old-style figures for body text paragraphs */
.prose { font-variant-numeric: oldstyle-nums; }

/* True small caps for acronyms/labels (add slight tracking) */
.acronym, .label { 
  font-variant-caps: small-caps; 
  letter-spacing: 0.05em; 
}

/* Enable pair kerning and common ligatures */
body {
  font-kerning: normal;               
  font-variant-ligatures: common-ligatures; 
}
```

## Variable Fonts

Prefer variable fonts over static weights when available. They provide a single file (WOFF2) covering every weight and allow fluid weight animation.

```css
@font-face {
  font-family: 'Plus Jakarta Sans';
  src: url('/fonts/PlusJakartaSans[wght].woff2') format('woff2');
  font-weight: 200 800;
  font-display: swap;
}

/* Use any precise weight */
.subtle { font-weight: 350; }
.emphasis { font-weight: 580; }
```

## Performance & Loading

### Font Loading Strategy
- Use `font-display: swap` for body text to show fallback immediately.
- Use `font-display: optional` for performance-critical pages (only uses web font if loaded quickly).
- Use `font-display: fallback` as a middle ground (short block, short swap).

### Fallback Metrics (Layout Shift Reduction)
Define fallback metrics to prevent cumulative layout shift (CLS) when the web font loads.

```css
@font-face {
  font-family: 'Font Fallback';
  src: local('Arial');
  ascent-override: 98%;
  descent-override: 24%;
  line-gap-override: 0%;
  size-adjust: 104%;
}
```

### Performance Rules
1. Self-host fonts (do not rely on Google Fonts CDN).
2. Use WOFF2 format only.
3. Subset fonts to Latin characters if full Unicode is unnecessary.
4. Preload critical font files.
5. Limit to 2-4 font files total.

## Accessibility Rules

Typographic accessibility is non-negotiable.

1. **Never disable zoom**: Ensure `user-scalable=no` and `maximum-scale=1` are NOT in the viewport meta tag.
2. **Use rem/em for font sizes**: Never use `px` for body text. `1rem` respects user browser defaults.
3. **Minimum 16px body text**: 14px is acceptable only for secondary/metadata text.
4. **Max line length of 65ch**: Use `max-inline-size: 65ch` on text containers to prevent eye tracking loss.
5. **Adjust dark mode weight/line-height**: Light text on dark backgrounds appears thinner. Add +0.05 to +0.1 to line-height and slightly increase font-weight.
6. **Sufficient contrast**: Enforce WCAG AA (4.5:1 for body text, 3:1 for large text).
7. **Do not rely on font weight alone**: Combine weight with color, size, or spatial position to convey meaning. 

## Evaluation Protocol

When auditing a typographic system, check:
1. Are all sizes derived from a mathematical ratio?
2. Does the vertical rhythm align with the body line-height?
3. Are the typefaces intentional (avoiding the generic defaults)?
4. Is `rem` used for all sizing to respect accessibility preferences?
5. Are tabular numbers used for data/metrics?
6. Does the hierarchy pass the Squint Test (is the order of importance obvious)?
7. Is the line length constrained to ~65 characters for reading blocks?

## Dark Mode Typography

Light text on dark backgrounds creates optical illusions that require specific typographic adjustments. Ignoring these makes dark mode text look too heavy and hard to read.

### Weight Reduction

Bright text on dark surfaces appears heavier than the same weight on light surfaces (halation effect). Reduce font weights in dark mode:

| Role | Light Mode Weight | Dark Mode Weight |
|------|-------------------|------------------|
| Body | 400 | 300 |
| Headings | 600 | 500 |
| Display | 500 | 400 |
| Bold emphasis | 700 | 600 |
| Labels | 500 | 400 |

### Line-Height Increase

Dark mode text needs more vertical breathing room. Increase line-height by `+0.05` to `+0.1`:

| Role | Light Mode | Dark Mode |
|------|------------|-----------|
| Body | 1.5–1.6 | 1.6–1.7 |
| Headings | 1.1–1.25 | 1.15–1.3 |
| Captions | 1.4–1.5 | 1.5–1.6 |

### Off-White Text Rule

Never use pure `#fff` or `oklch(100% 0 0)` for body text in dark mode. Pure white creates excessive contrast and eye strain. Use off-white values:

- **Primary text**: `oklch(93% 0 0)` or `#ededed`
- **Secondary text**: `oklch(75% 0 0)` or `#b3b3b3`
- **Muted text**: `oklch(60% 0.01 250)` (with slight brand tint)

### Complete Dark Mode Typography CSS

```css
[data-theme="dark"] {
  /* Weight reduction */
  body {
    font-weight: 300;
    line-height: 1.65;
  }
  h1, h2, h3 {
    font-weight: 500;
    line-height: 1.2;
  }
  .display {
    font-weight: 400;
    line-height: 1.15;
  }
  .label, .caption {
    font-weight: 400;
  }

  /* Off-white text — never pure #fff */
  --color-text: oklch(93% 0 0);
  --color-text-muted: oklch(65% 0.01 250);
  --color-text-subtle: oklch(50% 0.01 250);

  /* Slightly increased letter-spacing for body at lighter weights */
  p, li, dd {
    letter-spacing: 0.005em;
  }
}
```