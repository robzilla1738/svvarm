# Style Guide: Minimal Refined

## Philosophy
Ruthless restraint and precision. This is the "Apple" or "Linear" aesthetic. Every pixel must earn its place. It relies entirely on flawless typography, exact alignment, and subtle contrast. There is no place to hide bad layout with decoration.

## Typography (from Typography Mastery & Font Pairings)

**Primary Pairing**: Inter Tight (Heading) + Inter (Body/UI) [Pairing #1]
Map to tokens: `--font-heading: 'Inter Tight', sans-serif` / `--font-body: 'Inter', sans-serif`
**Technical Alternative**: Geist (Body) + Geist Mono (Code) [Pairing #4]

**Scale**: `1.125` (Major second) — mathematically tight.
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display | fluid `clamp()` | 500-600 | 1.1 |
| Heading | `xl` to `2xl` | 500 | 1.2 |
| Body | `base` (1rem) | 400 | 1.5 or 1.6 |
| Label | `xs` | 500 | 1.0 (tabular-nums) |

**Rules**:
- Apply `-0.02em` tracking to headings.
- Enforce `font-variant-numeric: tabular-nums` for all metrics and data.
- Avoid heavy font weights (>600); use subtle size and color contrast for hierarchy.

## Color (from Color Mastery)

**Palette approach**: 95% grayscale with tinted neutrals and ONE precise accent.
```css
--color-bg: oklch(99% 0.002 250);   /* Near-pure white */
--color-surface: oklch(97% 0.003 250);   /* Barely off-white */
--color-text: oklch(15% 0.005 250);        /* Sharp dark gray */
--color-text-muted: oklch(55% 0.005 250);  /* Mid gray for metadata */
--color-border: oklch(92% 0.005 250);      /* Almost invisible borders */
--color-primary: oklch(60% 0.15 250); /* Quiet indigo accent */
```

**Rules**:
- Base neutral chroma must be extremely low (`0.002` - `0.005`).
- Never use pure black `#000` or pure white `#fff`.
- `color-primary` is reserved exclusively for primary actions, active states, and focus rings.

## Layout & Spacing (from Layout Mastery)

**Approach**: Mathematical grid, high whitespace.
- Use **The Stack** for vertical flow.
- Enforce a strict 4px/8px baseline grid for all component internals.
- **Max line length**: `65ch` with auto margins.

**Spacing scale**: Base-8 rhythm.
`--space-xs` (8px), `--space-base` (16px), `--space-md` (24px), `--space-lg` (32px), `--space-xl` (48px), `--space-2xl` (64px), `--space-3xl` (96px)

**Border radius**: Small, precise (`4px` to `8px`). No pills unless specifically for tags.

## Interaction & Motion (from Interaction & Motion Mastery)

**States**:
- **Hover**: Subtle background shift (e.g., `--color-bg` to `--color-surface`), no shadow growth.
- **Focus**: Mandatory `:focus-visible` ring. `2px solid var(--color-primary)` with `1px` offset.

**Motion**:
- **Duration**: `100ms` - `200ms` max. Snappy and near-instant.
- **Easing**: `--ease-out-quart` (`cubic-bezier(0.25, 1, 0.5, 1)`).
- **Properties**: `opacity` and `transform` only. 
- NO bounce, NO spring, NO stagger delays.

## Anti-Slop Rules
- **No gradients** — completely forbidden.
- **No heavy shadows** — use `0 4px 12px oklch(0% 0 0 / 0.05)` strictly for floating overlays (popovers), not cards.
- **No gray text on colored backgrounds** — use dark tints of the background color.