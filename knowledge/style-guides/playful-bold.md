# Style Guide: Playful Bold

## Philosophy
Vibrant, energetic, and personality-forward. This style radiates confidence and approachability. It relies on highly saturated colors, generous, chunky spacing, and rounded geometry. It must remain functional while feeling rewarding to use.

## Typography (from Typography Mastery & Font Pairings)

**Primary Pairing**: DM Serif Display (Heading) + DM Sans (Body) [Pairing #7]
Map to tokens: `--font-heading: 'DM Serif Display', serif` / `--font-body: 'DM Sans', sans-serif`
**Alternative**: Clash Display (Heading) + Satoshi (Body) [Pairing #11]

**Scale**: `1.333` (Perfect fourth) or `1.500` (Perfect fifth) — dramatic contrast.
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display | fluid `clamp()` | 700-800 | 1.0 |
| Heading | `2xl` to `3xl` | 700 | 1.1 |
| Body | `base` (1rem) or `lg` | 400-500 | 1.5 |
| Label | `sm` | 600-700 | 1.2 |

**Rules**:
- Display text must be exceptionally large and heavy.
- Track headings tightly (`-0.02em` to `-0.04em`) to create solid text blocks.
- Never use thin or light weights (`<400`).

## Color (from Color Mastery)

**Palette approach**: High chroma color blocking against warm off-white.
```css
--color-bg: oklch(98% 0.01 80);      /* Warm off-white */
--color-surface: oklch(100% 0 0);         /* Pure white cards */
--color-text: oklch(15% 0.02 280);          /* Deep ink */
--color-primary: oklch(65% 0.25 330); /* Vibrant pink/magenta */
--color-secondary: oklch(75% 0.15 140);/* Fresh green */
```

**Rules**:
- Accents and primary colors must be highly saturated (chroma `> 0.18`).
- Use solid color blocks for entire section backgrounds (e.g., a massive `--color-primary` hero section).
- Ensure semantic colors (Success, Error) match the vibrancy of the brand palette.

## Layout & Spacing (from Layout Mastery)

**Approach**: Chunky and breathable Bento grids.
- Use **Bento Grid Layouts** to alternate card sizes and break rigid symmetry.
- Use **The Stack** with massive gaps between distinct concepts.
- Pad cards heavily (e.g., `32px` or `48px` internally).

**Spacing scale**: Large intervals.
`--space-xs` (8px), `--space-base` (16px), `--space-lg` (32px), `--space-xl` (48px), `--space-2xl` (64px), `--space-3xl` (96px), `--space-section` (160px)

**Border radius**: Extreme rounding.
- Cards: `16px` to `24px`.
- Buttons and Badges: `9999px` (fully rounded pills).

## Interaction & Motion (from Interaction & Motion Mastery)

**States**:
- **Hover**: Physical feedback. Elements scale up (`transform: scale(1.02)`) and shadows deepen.
- **Active**: Elements physically press down (`transform: scale(0.95)`).
- **Focus**: Thick, high-contrast rings (`3px solid var(--color-primary)`).

**Motion**:
- **Duration**: `200ms` - `300ms`. Snappy.
- **Easing**: Spring physics. Use `cubic-bezier(0.34, 1.56, 0.64, 1)`.
- *Note: This is the ONLY style guide permitted to use overshoot/bounce easing.*

## Anti-Slop Rules
- **No sterile palettes** — avoid standard Tailwind grays; tint everything.
- **No timid radiuses** — `4px` looks like a mistake here.
- **No slow fade-ins** — motion must pop, not crawl.
- **No "Cards inside Cards"** — keep the container hierarchy flat to maintain the chunky feel.