# Design Gallery — Visual Excellence Reference

> **Usage:** These are not templates. They demonstrate techniques that separate "designed" from "generated." Adapt the principles to the project's style direction — not the specific code. When reviewing or building, ask: "Does this element have the intentionality shown here, or does it feel like a default?" Every code example uses design tokens (`var(--color-*)`, `var(--space-*)`, `var(--text-*)`) so they inherit whatever palette the project defines. The point is the structure, the ratios, and the decisions — not the colors.

---

### 1. Hero Section

**What makes this impressive:**
Typographic drama through a 5:1 size ratio between the heading and body text, with the heading set at a lightweight 300 that lets the sheer scale do the work. The negative space is aggressive — 120px+ vertical padding — which signals confidence and gives the eye a single place to land. A staggered reveal (heading → subtext → CTA) creates temporal hierarchy, not just spatial.

**The Code:**

```html
<section class="hero">
  <div class="hero__inner">
    <h1 class="hero__heading">Build something<br>worth remembering</h1>
    <p class="hero__subtext">The platform for teams who ship with intention.</p>
    <a href="#start" class="hero__cta">Get started</a>
  </div>
</section>
```

```css
.hero {
  padding-block: clamp(var(--space-16), 10vw, var(--space-32));
  display: grid;
  place-items: center;
  text-align: left;
  background: var(--color-surface);
}

.hero__inner {
  max-inline-size: 72ch;
  padding-inline: var(--space-6);
}

.hero__heading {
  font-size: clamp(3rem, 1rem + 8vw, 7rem);
  font-weight: 300;
  line-height: 1.05;
  letter-spacing: -0.03em;
  color: var(--color-text-primary);
  margin-block-end: var(--space-6);
}

.hero__subtext {
  font-size: var(--text-lg);
  font-weight: 400;
  color: var(--color-text-secondary);
  max-inline-size: 42ch;
  margin-block-end: var(--space-10);
}

.hero__cta {
  display: inline-flex;
  align-items: center;
  padding: var(--space-3) var(--space-8);
  font-size: var(--text-base);
  font-weight: 500;
  color: var(--color-on-primary);
  background: var(--color-primary);
  border-radius: var(--radius-md);
  text-decoration: none;
  transition: background 0.2s ease, transform 0.2s ease;
}

.hero__cta:hover {
  background: var(--color-primary-hover);
  transform: translateY(-1px);
}

/* Staggered reveal */
.hero__heading { animation: reveal 0.7s ease both; }
.hero__subtext { animation: reveal 0.7s ease 0.12s both; }
.hero__cta     { animation: reveal 0.7s ease 0.24s both; }

@keyframes reveal {
  from { opacity: 0; transform: translateY(12px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

**What separates this from the generic version:**
- **Generic:** heading at 600 weight, 2rem, centered with equal padding. This: 300 weight at 3–7rem — the size carries the hierarchy, not the boldness.
- **Generic:** 40–60px padding, feels like any section. This: 120px+ vertical breathing room that signals "this is the most important thing on the page."
- **Generic:** heading, subtext, and button appear simultaneously. This: 120ms stagger creates reading order and a sense of craft.
- **Generic:** body and heading at similar scales. This: 5:1 ratio (heading vs subtext) creates unmistakable hierarchy without decoration.
- **Generic:** tight letter-spacing or default. This: -0.03em tracking at large sizes prevents the heading from feeling loose.

---

### 2. Pricing Table

**What makes this impressive:**
The featured plan is physically larger — not just badged. Using `1fr 1.15fr 1fr` grid columns, the recommended tier occupies more space, has heavier padding, and is the only card with a filled CTA button. Hierarchy is structural: you know which plan matters before reading a single word. The non-featured cards use ghost/outline buttons, creating a clear visual funnel.

**The Code:**

```html
<section class="pricing">
  <div class="pricing__grid">
    <div class="pricing__card">
      <span class="pricing__tier">Starter</span>
      <span class="pricing__price">$9<span class="pricing__period">/mo</span></span>
      <ul class="pricing__features">
        <li>5 projects</li>
        <li>Basic analytics</li>
        <li>Email support</li>
      </ul>
      <a href="#" class="pricing__cta pricing__cta--outline">Choose Starter</a>
    </div>
    <div class="pricing__card pricing__card--featured">
      <span class="pricing__tier">Pro</span>
      <span class="pricing__price">$29<span class="pricing__period">/mo</span></span>
      <ul class="pricing__features">
        <li>Unlimited projects</li>
        <li>Advanced analytics</li>
        <li>Priority support</li>
        <li>Custom domains</li>
      </ul>
      <a href="#" class="pricing__cta pricing__cta--filled">Choose Pro</a>
    </div>
    <div class="pricing__card">
      <span class="pricing__tier">Enterprise</span>
      <span class="pricing__price">$99<span class="pricing__period">/mo</span></span>
      <ul class="pricing__features">
        <li>Everything in Pro</li>
        <li>SSO &amp; audit logs</li>
        <li>Dedicated support</li>
        <li>SLA guarantee</li>
      </ul>
      <a href="#" class="pricing__cta pricing__cta--outline">Choose Enterprise</a>
    </div>
  </div>
</section>
```

```css
.pricing {
  padding-block: var(--space-20);
  background: var(--color-surface);
}

.pricing__grid {
  display: grid;
  grid-template-columns: 1fr 1.15fr 1fr;
  gap: var(--space-6);
  max-inline-size: 960px;
  margin-inline: auto;
  padding-inline: var(--space-6);
  align-items: center;
}

.pricing__card {
  padding: var(--space-8) var(--space-6);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.pricing__card--featured {
  padding: var(--space-12) var(--space-8);
  border-color: var(--color-primary);
  background: var(--color-surface-elevated);
  box-shadow: 0 4px 24px oklch(0 0 0 / 0.08);
}

.pricing__tier {
  font-size: var(--text-sm);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-text-secondary);
}

.pricing__price {
  font-size: var(--text-3xl);
  font-weight: 300;
  font-variant-numeric: tabular-nums;
  color: var(--color-text-primary);
}

.pricing__period {
  font-size: var(--text-base);
  font-weight: 400;
  color: var(--color-text-tertiary);
}

.pricing__features {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  color: var(--color-text-secondary);
  font-size: var(--text-sm);
  flex-grow: 1;
}

.pricing__cta--outline {
  display: inline-flex;
  justify-content: center;
  padding: var(--space-3) var(--space-6);
  border: 1px solid var(--color-border-strong);
  border-radius: var(--radius-md);
  color: var(--color-text-primary);
  background: transparent;
  font-weight: 500;
  text-decoration: none;
  transition: border-color 0.2s ease, background 0.2s ease;
}

.pricing__cta--outline:hover {
  border-color: var(--color-primary);
  background: var(--color-surface-hover);
}

.pricing__cta--filled {
  display: inline-flex;
  justify-content: center;
  padding: var(--space-3) var(--space-6);
  border: none;
  border-radius: var(--radius-md);
  color: var(--color-on-primary);
  background: var(--color-primary);
  font-weight: 500;
  text-decoration: none;
  transition: background 0.2s ease, transform 0.2s ease;
}

.pricing__cta--filled:hover {
  background: var(--color-primary-hover);
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .pricing__grid {
    grid-template-columns: 1fr;
    max-inline-size: 400px;
  }
  .pricing__card--featured {
    order: -1;
  }
}
```

**What separates this from the generic version:**
- **Generic:** three identical cards with a "Most Popular" badge on one. This: the featured card is 15% wider and has 50% more padding — hierarchy is structural, not label-dependent.
- **Generic:** all three buttons are filled/primary. This: only the featured card gets a filled CTA; others use outline, creating a visual funnel toward the recommended choice.
- **Generic:** price at the same weight as the tier name. This: price at weight 300 with tabular figures, tier name at small-caps 500 — each element has its own typographic role.
- **Generic:** flat cards with identical borders. This: featured card has a primary-colored border, elevated background, and subtle shadow — three signals that compound.

---

### 3. Feature Block (Asymmetric Bento)

**What makes this impressive:**
Instead of three identical cards in a row, one feature dominates at 2fr while supporting features sit at 1fr. This creates a focal point through scale asymmetry. The dominant feature gets a full image/illustration area, while supporting features are compact. A full-bleed visual break between feature groups prevents monotony across the page.

**The Code:**

```html
<section class="features">
  <div class="features__bento">
    <div class="features__item features__item--dominant">
      <div class="features__visual">
        <img src="/feature-hero.svg" alt="" loading="lazy" />
      </div>
      <div class="features__content">
        <h3 class="features__title">Real-time collaboration</h3>
        <p class="features__desc">See changes as they happen. No refresh, no delay, no conflicts. Your team works as one.</p>
      </div>
    </div>
    <div class="features__item">
      <h3 class="features__title">Version history</h3>
      <p class="features__desc">Every change tracked. Roll back to any point with a single click.</p>
    </div>
    <div class="features__item">
      <h3 class="features__title">Granular permissions</h3>
      <p class="features__desc">Control who sees what, down to the individual field.</p>
    </div>
  </div>
</section>

<div class="features__break" aria-hidden="true"></div>

<section class="features">
  <div class="features__bento features__bento--reversed">
    <div class="features__item features__item--dominant">
      <div class="features__visual">
        <img src="/feature-analytics.svg" alt="" loading="lazy" />
      </div>
      <div class="features__content">
        <h3 class="features__title">Built-in analytics</h3>
        <p class="features__desc">Understand usage patterns without bolting on another tool. Insights where you already work.</p>
      </div>
    </div>
    <div class="features__item">
      <h3 class="features__title">Custom dashboards</h3>
      <p class="features__desc">Drag, drop, and share the metrics that matter to your team.</p>
    </div>
    <div class="features__item">
      <h3 class="features__title">Export anywhere</h3>
      <p class="features__desc">CSV, PDF, API — your data leaves on your terms.</p>
    </div>
  </div>
</section>
```

```css
.features {
  padding-block: var(--space-16);
  padding-inline: var(--space-6);
}

.features__bento {
  display: grid;
  grid-template-columns: 2fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: var(--space-6);
  max-inline-size: 1080px;
  margin-inline: auto;
}

.features__bento--reversed {
  grid-template-columns: 1fr 2fr;
}

.features__item--dominant {
  grid-row: 1 / -1;
  display: flex;
  flex-direction: column;
}

.features__bento--reversed .features__item--dominant {
  grid-column: 2;
  grid-row: 1 / -1;
}

.features__item {
  padding: var(--space-8);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.features__item--dominant {
  background: var(--color-surface-elevated);
  overflow: hidden;
}

.features__visual {
  flex: 1;
  min-block-size: 240px;
  display: grid;
  place-items: center;
  background: var(--color-surface-subtle);
  border-radius: var(--radius-md) var(--radius-md) 0 0;
}

.features__visual img {
  max-inline-size: 100%;
  block-size: auto;
}

.features__content {
  padding: var(--space-8);
}

.features__title {
  font-size: var(--text-lg);
  font-weight: 500;
  color: var(--color-text-primary);
  margin-block-end: var(--space-2);
}

.features__desc {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  line-height: 1.6;
}

.features__break {
  block-size: 1px;
  background: var(--color-border);
  margin-block: var(--space-4);
}

@media (max-width: 768px) {
  .features__bento,
  .features__bento--reversed {
    grid-template-columns: 1fr;
  }
  .features__item--dominant {
    grid-row: auto;
  }
  .features__bento--reversed .features__item--dominant {
    grid-column: auto;
    grid-row: auto;
  }
}
```

**What separates this from the generic version:**
- **Generic:** three identical cards at `1fr 1fr 1fr`. This: 2:1 scale ratio creates a focal point — one feature is the star, the others support it.
- **Generic:** every feature block looks the same as every other block on the page. This: alternating dominant side (`2fr 1fr` → `1fr 2fr`) and a full-bleed divider create compositional variety.
- **Generic:** equal content treatment for all features. This: the dominant feature gets a visual/illustration area; supporting features are text-only. Scale signals importance.
- **Generic:** uniform grid repeated section after section. This: the visual break between groups prevents the bento from becoming its own monotony.

---

### 4. Testimonial

**What makes this impressive:**
Editorial typography — the quote is set at heading scale in a serif typeface, making the words feel significant rather than decorative. A 3px left border anchors the block. The attribution uses small-caps sans-serif at a distinctly smaller size, creating clear role separation between the quote and the speaker. The layout is asymmetric: quote takes 2/3 width, attribution sits right-aligned below.

**The Code:**

```html
<blockquote class="testimonial">
  <p class="testimonial__quote">"We replaced three tools and our entire team got faster. It wasn't an optimization — it was a simplification."</p>
  <footer class="testimonial__attribution">
    <cite class="testimonial__name">Sarah Chen</cite>
    <span class="testimonial__role">VP Engineering, Meridian</span>
  </footer>
</blockquote>
```

```css
.testimonial {
  max-inline-size: 680px;
  margin-inline: auto;
  padding-block: var(--space-16);
  padding-inline: var(--space-6);
}

.testimonial__quote {
  font-family: var(--font-serif, Georgia, "Times New Roman", serif);
  font-size: clamp(var(--text-xl), 1rem + 2vw, var(--text-3xl));
  font-weight: 400;
  line-height: 1.4;
  color: var(--color-text-primary);
  border-inline-start: 3px solid var(--color-primary);
  padding-inline-start: var(--space-6);
  margin-block-end: var(--space-6);
}

.testimonial__attribution {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: var(--space-1);
}

.testimonial__name {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: 600;
  font-variant-caps: all-small-caps;
  letter-spacing: 0.04em;
  color: var(--color-text-primary);
  font-style: normal;
}

.testimonial__role {
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: 400;
  color: var(--color-text-tertiary);
}
```

**What separates this from the generic version:**
- **Generic:** quote in italic body text at the same scale as everything else. This: serif at heading scale — the quote IS the section, not an aside.
- **Generic:** rounded avatar photo + name + stars. This: no avatar, no stars. The typography carries the authority. The words are the hero.
- **Generic:** attribution centered directly below the quote. This: attribution right-aligned, creating an asymmetric composition that feels editorial rather than templated.
- **Generic:** decorative oversized quotation marks (the hallmark of AI-generated testimonials). This: a clean 3px left border — architectural, not decorative.
- **Generic:** name and role at similar sizes. This: name in small-caps at 600 weight, role in xs at 400 — clear hierarchy within the attribution itself.

---

### 5. Navigation Bar

**What makes this impressive:**
Weighted spacing — related links are grouped tighter (16px gaps) while the CTA is separated by a larger gap (32px+), creating information architecture through whitespace alone. The active state uses a `scaleX()` underline that animates from center, not a background highlight. The backdrop uses 85% opacity with `backdrop-filter: blur()`, letting the content subtly show through without competing.

**The Code:**

```html
<nav class="navbar" aria-label="Main">
  <a href="/" class="navbar__logo">
    <span class="navbar__wordmark">Acme</span>
  </a>
  <div class="navbar__links">
    <div class="navbar__group">
      <a href="/features" class="navbar__link">Features</a>
      <a href="/pricing" class="navbar__link">Pricing</a>
      <a href="/docs" class="navbar__link navbar__link--active" aria-current="page">Docs</a>
    </div>
    <div class="navbar__group">
      <a href="/blog" class="navbar__link">Blog</a>
      <a href="/changelog" class="navbar__link">Changelog</a>
    </div>
    <a href="/signup" class="navbar__cta">Get started</a>
  </div>
</nav>
```

```css
.navbar {
  position: sticky;
  inset-block-start: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-block: var(--space-3);
  padding-inline: var(--space-6);
  background: oklch(from var(--color-surface) l c h / 0.85);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-block-end: 1px solid var(--color-border);
}

.navbar__wordmark {
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--color-text-primary);
  text-decoration: none;
}

.navbar__links {
  display: flex;
  align-items: center;
  gap: var(--space-8);
}

.navbar__group {
  display: flex;
  align-items: center;
  gap: var(--space-4);
}

.navbar__link {
  position: relative;
  font-size: var(--text-sm);
  font-weight: 400;
  color: var(--color-text-secondary);
  text-decoration: none;
  padding-block: var(--space-1);
  transition: color 0.15s ease;
}

.navbar__link:hover {
  color: var(--color-text-primary);
}

.navbar__link::after {
  content: "";
  position: absolute;
  inset-block-end: -2px;
  inset-inline-start: 0;
  inline-size: 100%;
  block-size: 2px;
  background: var(--color-primary);
  transform: scaleX(0);
  transform-origin: center;
  transition: transform 0.2s ease;
}

.navbar__link--active::after,
.navbar__link:hover::after {
  transform: scaleX(1);
}

.navbar__link--active {
  color: var(--color-text-primary);
  font-weight: 500;
}

.navbar__cta {
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--color-on-primary);
  background: var(--color-primary);
  padding: var(--space-2) var(--space-5);
  border-radius: var(--radius-md);
  text-decoration: none;
  transition: background 0.2s ease;
}

.navbar__cta:hover {
  background: var(--color-primary-hover);
}
```

**What separates this from the generic version:**
- **Generic:** all links evenly spaced at the same gap. This: links grouped semantically — related items at `--space-4`, groups separated by `--space-8`, CTA isolated further. Information architecture through whitespace.
- **Generic:** active state is a background pill or color change. This: a `scaleX()` underline that animates from center — subtle, precise, and feels engineered.
- **Generic:** solid white/dark navbar background. This: 85% opacity surface with `backdrop-filter: blur(12px)` — content peeks through, the bar feels like glass, not a wall.
- **Generic:** all links at the same weight. This: active link at 500, others at 400 — a tiny shift that the eye catches subconsciously.

---

### 6. Metric Card

**What makes this impressive:**
The number IS the card. It dominates at `var(--text-3xl)` or larger in light weight (300), with tabular figures for clean alignment when multiple cards sit side by side. A delta indicator ("+12%") uses semantic color (green/red) at small scale next to the number. The label sits below in muted, small text — clearly subordinate. The result: your eye goes to the number first, the trend second, the label third.

**The Code:**

```html
<div class="metrics">
  <article class="metric-card">
    <span class="metric-card__value">
      2,847
      <span class="metric-card__delta metric-card__delta--positive">+12%</span>
    </span>
    <span class="metric-card__label">Active users</span>
  </article>
  <article class="metric-card">
    <span class="metric-card__value">
      $48.2k
      <span class="metric-card__delta metric-card__delta--positive">+8%</span>
    </span>
    <span class="metric-card__label">Monthly revenue</span>
  </article>
  <article class="metric-card">
    <span class="metric-card__value">
      1.2s
      <span class="metric-card__delta metric-card__delta--negative">+0.3s</span>
    </span>
    <span class="metric-card__label">Avg. response time</span>
  </article>
</div>
```

```css
.metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-6);
  padding-inline: var(--space-6);
  max-inline-size: 900px;
  margin-inline: auto;
}

.metric-card {
  padding: var(--space-8) var(--space-6);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.metric-card__value {
  font-size: clamp(var(--text-2xl), 1rem + 3vw, var(--text-4xl));
  font-weight: 300;
  font-variant-numeric: tabular-nums;
  line-height: 1.1;
  color: var(--color-text-primary);
  display: flex;
  align-items: baseline;
  gap: var(--space-2);
}

.metric-card__delta {
  font-size: var(--text-sm);
  font-weight: 500;
  border-radius: var(--radius-sm);
  padding: var(--space-0-5) var(--space-2);
}

.metric-card__delta--positive {
  color: var(--color-success);
  background: var(--color-success-subtle);
}

.metric-card__delta--negative {
  color: var(--color-error);
  background: var(--color-error-subtle);
}

.metric-card__label {
  font-size: var(--text-sm);
  font-weight: 400;
  color: var(--color-text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
```

**What separates this from the generic version:**
- **Generic:** number at the same size and weight as the label. This: number at `text-3xl`+ weight 300, label at `text-sm` — the number IS the card, everything else is metadata.
- **Generic:** delta displayed as plain text or a separate line. This: delta as a small pill with semantic color, sitting at baseline alongside the number — trend is immediate, not an afterthought.
- **Generic:** proportional figures that shift widths between "1" and "8". This: `font-variant-numeric: tabular-nums` — columns of cards align their digits perfectly.
- **Generic:** label above the number, creating ambiguity about what's primary. This: label below and visually subordinate — the reading order matches the importance order.
- **Generic:** all text at medium/regular weight. This: number at 300 (light), delta at 500 (medium), label at 400 — three distinct weights for three distinct roles.

---

### 7. CTA / Page Closer

**What makes this impressive:**
A compositional break — the background shifts from the page surface to a contrasting tone, creating a visual pause that signals "this section matters." The content is held to a narrow measure (`max-inline-size: 50ch`) so the eye doesn't wander. A single strong button and minimal copy. No feature list, no testimonials here — just the ask. The background break creates a stage, and the CTA is the only actor on it.

**The Code:**

```html
<section class="closer">
  <div class="closer__inner">
    <h2 class="closer__heading">Ready to start building?</h2>
    <p class="closer__body">Join thousands of teams who ship faster, together. No credit card required.</p>
    <a href="/signup" class="closer__cta">Start free</a>
  </div>
</section>
```

```css
.closer {
  padding-block: clamp(var(--space-16), 8vw, var(--space-24));
  padding-inline: var(--space-6);
  background: var(--color-surface-contrast);
  color: var(--color-on-contrast);
  text-align: center;
  display: grid;
  place-items: center;
}

.closer__inner {
  max-inline-size: 50ch;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-4);
}

.closer__heading {
  font-size: clamp(var(--text-2xl), 1rem + 3vw, var(--text-4xl));
  font-weight: 400;
  line-height: 1.15;
  letter-spacing: -0.02em;
}

.closer__body {
  font-size: var(--text-base);
  opacity: 0.8;
  line-height: 1.6;
  max-inline-size: 38ch;
}

.closer__cta {
  display: inline-flex;
  align-items: center;
  margin-block-start: var(--space-4);
  padding: var(--space-3) var(--space-10);
  font-size: var(--text-base);
  font-weight: 500;
  color: var(--color-surface-contrast);
  background: var(--color-on-contrast);
  border-radius: var(--radius-md);
  text-decoration: none;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.closer__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px oklch(0 0 0 / 0.15);
}
```

**What separates this from the generic version:**
- **Generic:** same background as every other section, no visual break. This: `--color-surface-contrast` creates a full-bleed tonal shift — the page rhythm changes, signaling "this is the close."
- **Generic:** wide content area, copy stretches across the full container. This: `max-inline-size: 50ch` — narrow measure forces focus and prevents the eye from drifting.
- **Generic:** multiple buttons ("Start free" + "Talk to sales" + "Learn more"). This: one button. One action. The simplicity signals confidence.
- **Generic:** heading at the same weight as previous sections. This: weight 400 at large scale, with the background contrast doing the heavy lifting — no need to shout with bold when the stage is already set.
- **Generic:** inverted-color button is an afterthought. This: button colors are derived from the contrast surface (`color-surface-contrast` on `color-on-contrast`), creating a deliberate figure-ground inversion.

---

## Cross-Cutting Principles

These six patterns recur across every entry above. When building or auditing, check that each section demonstrates at least 3 of 6:

1. **Typographic drama through size contrast, not decoration.** A 5:1 heading-to-body ratio does more work than gradients, shadows, or ornamental elements. Let the scale system carry the hierarchy. Decoration is a crutch when the type isn't doing its job.

2. **Structural hierarchy through scale and weight, not badges or labels.** The featured pricing card is physically larger. The dominant feature block is 2fr. The metric number is 4x the label. When you need a "Most Popular" badge to communicate hierarchy, the structure has failed.

3. **Negative space as a design element, not laziness.** 120px+ hero padding isn't empty — it's a decision. The narrow `50ch` CTA measure isn't sparse — it's focused. Every generous gap says "we're confident enough to let this breathe."

4. **Coordinated multi-property transitions, not single-property.** Hover states shift `background` + `transform` together. The navbar link reveals a `scaleX` underline while shifting color. Single-property transitions (`color: blue → red`) feel mechanical. Multi-property transitions feel physical.

5. **Compositional variety across sections, not uniform grids.** Hero is full-width. Features are asymmetric bento. Testimonial is narrow editorial. CTA is contrast-background closer. When every section uses the same 3-column grid, the page has layout but no composition.

6. **One element per group earns disproportionate visual weight.** One pricing card is bigger. One feature block dominates. One number per card is oversized. This creates a natural reading order and prevents the eye from stalling at a grid of equals. Equal treatment is not equitable design — it's indecision.
