# Style Guide: Dark Premium

## Philosophy
Sleek, cinematic, high-end. This is the aesthetic of pro creative tools, luxury automotive interfaces, and premium dev tools. It relies on deep blacks, precise lighting, subtle glows, and high-contrast typography. It must feel expensive.

## Typography (from Typography Mastery & Font Pairings)

**Primary Pairing**: Satoshi (Heading) + Zodiak (Display) [Pairing #10]
Map to tokens: `--font-heading: 'Satoshi', sans-serif` / `--font-body: 'Satoshi', sans-serif` / Display: `--font-display: 'Zodiak', serif`
**Tech Alternative**: Geist + Geist Mono [Pairing #4]
**Editorial Alternative**: Neue Montreal + Editorial New [Pairing #9]

**Scale**: `1.250` (Major third).
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| Display | fluid `clamp()` | 400-500 | 1.1 |
| Heading | `xl` to `2xl` | 400-500 | 1.2 |
| Body | `base` (1rem) | 300-400 | 1.6 |
| Metadata | `sm` | 400 | 1.5 (letter-spacing: 0.02em) |

**Rules**:
- Light text on dark backgrounds glows; use lighter font weights (`300-400`) than you would in light mode.
- Increase line-height slightly (`+0.1`) to offset the glow.
- Track headings negatively (`-0.02em`) for a premium lockup.

## Color (from Color Mastery)

**Palette approach**: True black foundation with illuminated surfaces and one desaturated neon accent.
```css
--color-bg: oklch(12% 0.01 250);               /* Deep charcoal/navy, not pure black */
--color-surface: oklch(18% 0.01 250);          /* Slightly elevated */
--color-surface-elevated: oklch(24% 0.01 250); /* Modal/dropdown level */
--color-text: oklch(93% 0 0);                  /* Off-white, avoid pure #fff */
--color-text-muted: oklch(65% 0.01 250);       /* Legible gray */
--color-border: oklch(25% 0.01 250);           /* Subtle separation */
--color-primary: oklch(75% 0.12 250);          /* Desaturated blue/violet glow */
```

**Rules**:
- Never use pure black (`#000`) or pure white (`#fff`). They cause extreme eye strain and look cheap.
- Base background should sit around lightness `12%` to `15%`.
- Accents must be desaturated (chroma `< 0.15`) to prevent retina burn.

## Layout & Spacing (from Layout Mastery)

**Approach**: Theatrical, focused, and centered.
- Use **The Cover** for cinematic hero reveals.
- Enforce massive margins. Content should feel like it is floating in a void.
- Center-aligned layouts are highly effective here for isolated components.

**Spacing scale**:
`--space-xs` (8px), `--space-base` (16px), `--space-lg` (32px), `--space-2xl` (64px), `--space-3xl` (128px)

**Border radius**:
- Subtle curves (`6px` to `8px`) for structural elements.
- Or absolute sharp corners (`0px`) for an avant-garde editorial feel.

## Interaction & Motion (from Interaction & Motion Mastery)

**States**:
- **Hover**: Text brightens from `text-muted` to `text`, or borders illuminate. Focus on "lighting up" rather than moving.
- **Focus**: Soft, large-radius box shadow glow instead of a hard ring.
- **Buttons**: Prefer 1px borders that glow on hover over solid fills. Primary CTAs can be bright white with black text.

**Motion**:
- Cinematic and fluid.
- **Duration**: `500ms` - `800ms` for page/hero reveals.
- **Easing**: `--ease-out-quart` (`cubic-bezier(0.25, 1, 0.5, 1)`).
- Fade-ins (`opacity: 0` to `1`) are critical to avoid jarring flashes.

## Interaction CSS

Complete CSS for Dark Premium interactive states. These create the "lighting up" effect that defines the style.

### Button Border-Glow Hover

```css
.btn-dark {
  background: transparent;
  color: oklch(90% 0 0);
  border: 1px solid oklch(30% 0.01 250);
  padding: var(--space-sm, 0.75rem) var(--space-md, 1.5rem);
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 400;
  cursor: pointer;
  transition: border-color 200ms ease, box-shadow 200ms ease, color 200ms ease;
}
.btn-dark:hover {
  border-color: oklch(50% 0.08 250);
  box-shadow: 0 0 12px oklch(60% 0.12 250 / 0.15);
  color: oklch(93% 0 0);
}
.btn-dark:active {
  border-color: oklch(55% 0.10 250);
  box-shadow: 0 0 6px oklch(60% 0.12 250 / 0.1);
}
```

### Inverted Primary CTA (White on Dark)

```css
.btn-primary-dark {
  background: oklch(95% 0 0);
  color: oklch(12% 0.01 250);
  border: 1px solid oklch(95% 0 0);
  padding: var(--space-sm, 0.75rem) var(--space-md, 1.5rem);
  border-radius: 0.375rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 150ms ease, box-shadow 200ms ease;
}
.btn-primary-dark:hover {
  background: oklch(100% 0 0);
  box-shadow: 0 0 20px oklch(100% 0 0 / 0.15);
}
.btn-primary-dark:active {
  background: oklch(90% 0 0);
}
```

### Link Glow

```css
.link-dark {
  color: oklch(75% 0.12 250);
  text-decoration: none;
  transition: color 150ms ease, text-shadow 200ms ease;
}
.link-dark:hover {
  color: oklch(85% 0.12 250);
  text-shadow: 0 0 10px oklch(75% 0.12 250 / 0.3);
}
```

### Card Border Illumination

```css
.card-dark {
  background: oklch(18% 0.01 250);
  border: 1px solid oklch(25% 0.01 250);
  border-radius: 0.5rem;
  padding: var(--space-lg, 2rem);
  transition: border-color 200ms ease, box-shadow 300ms ease;
}
.card-dark:hover {
  border-color: oklch(35% 0.03 250);
  box-shadow: 0 0 20px oklch(50% 0.08 250 / 0.08);
}
```

### Focus Ring (Double-Shadow)

```css
.focus-dark:focus-visible {
  outline: none;
  box-shadow:
    0 0 0 2px oklch(12% 0.01 250),
    0 0 0 4px oklch(65% 0.10 250);
}
```

---

## Responsive Rules

### Mobile Spacing Reduction

On mobile, Dark Premium's theatrical spacing must compress without losing the void-like feel.

```css
@media (max-width: 768px) {
  :root {
    --space-section: clamp(3rem, 6vw, 5rem);
  }
  .hero {
    padding-block: 4rem 3rem;
    min-block-size: auto; /* Don't force full viewport on small screens */
  }
  .hero__headline {
    font-size: clamp(2rem, 1rem + 5vw, 3.5rem);
  }
}
```

### Hero Sizing

```css
.hero-dark {
  min-block-size: min(100dvh, 50rem);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-inline: var(--space-md);
  text-align: center;
}
.hero-dark__headline {
  font-size: clamp(2.5rem, 1.59rem + 4.55vw, 5rem);
  font-weight: 400;
  line-height: 1.05;
  letter-spacing: -0.03em;
  color: oklch(93% 0 0);
}
.hero-dark__subtitle {
  font-size: clamp(1rem, 0.85rem + 0.57vw, 1.25rem);
  font-weight: 300;
  line-height: 1.6;
  color: oklch(65% 0.01 250);
  max-inline-size: 50ch;
}
```

### Wide-Screen Theatrical Spacing

```css
@media (min-width: 1200px) {
  :root {
    --space-section: clamp(6rem, 10vw, 10rem);
  }
  .hero-dark {
    padding-block: 8rem;
  }
}
```

---

## Component Examples

### Dark Nav (Backdrop-Filter)

```html
<header class="nav-dark">
  <nav class="nav-dark__inner">
    <a class="nav-dark__logo" href="/">Brand</a>
    <ul class="nav-dark__links">
      <li><a href="/features">Features</a></li>
      <li><a href="/pricing">Pricing</a></li>
      <li><a href="/docs">Docs</a></li>
    </ul>
    <div class="nav-dark__actions">
      <a class="btn-dark" href="/login">Sign in</a>
      <a class="btn-primary-dark" href="/signup">Get started</a>
    </div>
  </nav>
</header>
```

```css
.nav-dark {
  position: sticky;
  top: 0;
  z-index: 10;
  background: oklch(12% 0.01 250 / 0.8);
  backdrop-filter: blur(16px) saturate(1.5);
  -webkit-backdrop-filter: blur(16px) saturate(1.5);
  border-bottom: 1px solid oklch(100% 0 0 / 0.06);
}
.nav-dark__inner {
  display: flex;
  align-items: center;
  gap: var(--space-lg, 2rem);
  padding: var(--space-sm, 0.75rem) var(--space-md, 1.5rem);
  max-inline-size: 90rem;
  margin-inline: auto;
}
.nav-dark__logo {
  font-weight: 600;
  font-size: 1.125rem;
  color: oklch(93% 0 0);
  text-decoration: none;
}
.nav-dark__links {
  display: flex;
  gap: var(--space-md, 1.5rem);
  list-style: none;
  margin: 0;
  padding: 0;
}
.nav-dark__links a {
  color: oklch(65% 0.01 250);
  text-decoration: none;
  font-size: 0.875rem;
  transition: color 150ms ease;
}
.nav-dark__links a:hover {
  color: oklch(90% 0 0);
}
.nav-dark__actions {
  margin-inline-start: auto;
  display: flex;
  gap: var(--space-sm, 0.75rem);
}
```

### Dark Hero Section

```html
<section class="hero-dark">
  <h1 class="hero-dark__headline">Build at the speed of thought</h1>
  <p class="hero-dark__subtitle">Ship code in seconds, not hours. Built for teams who refuse to wait.</p>
  <div class="hero-dark__actions">
    <a class="btn-primary-dark" href="/start">Get started</a>
    <a class="btn-dark" href="/demo">Watch demo</a>
  </div>
</section>
```

```css
.hero-dark__actions {
  display: flex;
  gap: var(--space-sm, 0.75rem);
  margin-top: var(--space-lg, 2rem);
  flex-wrap: wrap;
  justify-content: center;
}
```

---

## Anti-Slop Rules
- **No traditional drop shadows** — they disappear into dark backgrounds. Use top-borders (`border-top: 1px solid rgba(255,255,255,0.1)`) to simulate light hitting the edge.
- **No glowing gradient text** — it looks like an AI template. Use solid off-white text.
- **No highly saturated colors** — avoid pure red or electric blue; they bleed visually in dark mode.