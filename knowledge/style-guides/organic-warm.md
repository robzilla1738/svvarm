# Style Guide: Organic Warm

## Philosophy
Natural, tactile, and intentionally imperfect. This style rejects the cold precision of tech aesthetics in favor of human warmth. It relies on earth tones, soft edges, subtle textures, and generous breathing room.

## Typography (from Typography Mastery & Font Pairings)

**Primary Pairing**: Fraunces (Heading) + DM Sans (Body) [Pairing #8]
Map to tokens: `--font-heading: 'Fraunces', serif` / `--font-body: 'DM Sans', sans-serif`
**Alternative**: Newsreader (Heading) + Inter (Body) [Pairing #5]
**Global/Accessible Option**: Source Serif 4 + Source Sans 3 [Pairing #2]

**Scale**: `1.250` (Major third) — moderate and highly readable.
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display | fluid `clamp()` | 600 (use serif) | 1.1 |
| Heading | `xl` to `2xl` | 500-600 | 1.2 |
| Body | `base` (1rem) | 400 (use sans) | 1.6-1.7 |
| Caption | `sm` | 400 | 1.5 |

**Rules**:
- Exploit the `WONK` or `SOFT` axes in variable fonts like Fraunces.
- Prioritize reading comfort: constrain line lengths to `55-65ch`.
- Favor lowercase and sentence case; avoid ALL-CAPS text blocks.

## Color (from Color Mastery)

**Palette approach**: Earth tones with heavily tinted, warm neutrals.
```css
--color-bg: oklch(96% 0.015 80);    /* Warm cream */
--color-surface: oklch(98% 0.010 80);    /* Slightly lighter cream */
--color-text: oklch(25% 0.02 50);          /* Deep brown-black */
--color-text-muted: oklch(50% 0.03 60);    /* Warm medium taupe */
--color-primary: oklch(50% 0.12 150);/* Forest/sage green */
--color-border: oklch(85% 0.02 60);        /* Warm light border */
```

**Rules**:
- Neutral chroma must be distinct (`0.01` to `0.03`) and hue must lean warm (50 to 90).
- Absolutely no cool blues, cyans, or pure grays.
- Keep primary/accent chroma low to medium (`0.05` to `0.15`).

## Layout & Spacing (from Layout Mastery)

**Approach**: Unhurried, generous, and asymmetrical.
- Use **The Golden Canon Grid** or single-column layouts for reading flows.
- Use **The Cluster** for tags and actions, ensuring they wrap comfortably.
- Wide margins. Content should never touch the viewport edges.

**Spacing scale**: Generous baseline.
`--space-sm` (12px), `--space-md` (24px), `--space-xl` (48px), `--space-2xl` (80px), `--space-3xl` (120px)

**Border radius**: Soft and slightly varied.
- Cards: `8px` to `12px`
- Buttons: `6px`
- Never fully rounded (`9999px`) pills.

## Interaction & Motion (from Interaction & Motion Mastery)

**States**:
- **Hover**: Gentle transitions, subtle shadow expansion, slight warmth increase.
- **Focus**: `2px solid var(--color-primary)` with `2px` offset.
- **Empty States**: Warm illustrations with empathetic UX writing (per UX Writing Mastery).

**Motion**:
- **Duration**: `300ms` - `500ms`. Gentle and unhurried.
- **Easing**: `--ease-out-quart` (`cubic-bezier(0.25, 1, 0.5, 1)`).
- **Properties**: `opacity` crossfades preferred over heavy spatial translations.
- NO bounce or snapping.

## Anti-Slop Rules
- **No pure blacks (`#000`) or pure whites (`#fff`)** — everything must be tinted.
- **No geometric sans-serif dominance** — interject serifs to break the SaaS feel.
- **No sharp, clinical layouts** — allow elements to stagger and breathe.