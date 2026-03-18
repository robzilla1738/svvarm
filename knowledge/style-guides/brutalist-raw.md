# Style Guide: Brutalist Raw

## Philosophy
Raw, structural, anti-decoration. The material is the aesthetic. This style rejects polish and performative smoothness. It exposes the grid, relies entirely on aggressive typography, and uses code as a visible structural element.

## Typography (from Typography Mastery & Font Pairings)

**Primary Pairing**: Instrument Sans (UI) + JetBrains Mono (Code/Data) [Pairing #12]
Map to tokens: `--font-heading: 'Instrument Sans', sans-serif` / `--font-mono: 'JetBrains Mono', monospace`
**Alternative**: IBM Plex Sans + IBM Plex Mono [Pairing #3]

**Scale**: `1.333` (Perfect fourth) — high contrast between display and body.
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display | fluid `clamp()` | 700-800 | 1.0 |
| Heading | `2xl` to `3xl` | 600-700 | 1.1 |
| Body | `base` (1rem) | 400 | 1.5 |
| Label | `xs` | 500 | 1.0 (UPPERCASE, tracked out) |

**Rules**:
- Use `letter-spacing: 0.1em` for all small caps/labels.
- Apply negative tracking (`-0.03em`) on display text.
- Monospace fonts are used aggressively for metadata, navigation, and dates, not just code.

## Color (from Color Mastery)

**Palette approach**: Pure monochrome with a single, highly saturated punch color.
```css
--color-bg: oklch(97% 0 0);         /* Off-white, paper-like */
--color-surface: oklch(90% 0 0);         /* Structural gray */
--color-text: oklch(10% 0 0);              /* Near-black */
--color-text-muted: oklch(40% 0 0);        /* Utility gray */
--color-border: oklch(10% 0 0);            /* Heavy black lines */
--color-primary: oklch(60% 0.25 30); /* ONE aggressive punch color (e.g., pure red) */
```

**Rules**:
- Zero chroma in the neutrals (pure gray/black/white).
- No gradients. Flat colors only.
- `color-primary` must have chroma `> 0.20`.

## Layout & Spacing (from Layout Mastery)

**Approach**: The visible grid and extreme asymmetry.
- Expose the CSS Grid visually using `border: 2px solid var(--border)` on containers.
- Use **The Switcher** for harsh breakpoints.
- Zero or minimal gutters (`gap: 0` with borders acting as dividers).

**Spacing scale**: High contrast leaps.
`--space-2xs` (4px), `--space-xs` (8px), `--space-lg` (32px), `--space-2xl` (64px), `--space-3xl` (120px)

**Border radius**: `0px`. Absolutely no rounded corners. Hard edges only.

## Interaction & Motion (from Interaction & Motion Mastery)

**States**:
- **Hover**: Abrupt color inversions (white to black) or heavy underlines.
- **Focus**: `4px solid var(--text)` with `0px` offset. Brutally obvious.
- **Active**: Immediate translate `2px` down and right.

**Motion**:
- Hostile to smooth animation.
- **Duration**: `0ms` to `100ms` (Instant).
- **Easing**: `linear` or `step-end`.
- NO opacity fades for entrances; items must snap into existence.

## Anti-Slop Rules
- **No drop shadows or blurs** — use solid offset shadows (`box-shadow: 4px 4px 0 var(--border)`) if depth is forced.
- **No border-radius** — a `4px` curve destroys the brutalist illusion.
- **No multiple accent colors** — stick to black, white, gray, and the single punch color.