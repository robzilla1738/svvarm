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
A multi-file component system built on shadcn/Tailwind with real interactivity: monthly/yearly frequency toggle with spring-animated tab indicator (Framer Motion `layoutId`), animated price transitions via `@number-flow/react`, and four tiers with distinct visual treatments — popular gets a `ring-2 ring-primary` + radial gradient glow, highlighted (Enterprise) inverts to `bg-foreground text-background` with a grid-line overlay. Hierarchy is structural and behavioral, not just a badge.

**The Code:**

> **Stack:** React, TypeScript, Tailwind CSS, shadcn/ui, Framer Motion, NumberFlow.
> **Dependencies:** `lucide-react`, `@number-flow/react`, `class-variance-authority`, `@radix-ui/react-slot`, `framer-motion`.

**`components/ui/pricing-section.tsx`** — orchestrator with frequency toggle:

```tsx
"use client"

import * as React from "react"
import { PricingCard, type PricingTier } from "@/components/ui/pricing-card"
import { Tab } from "@/components/ui/pricing-tab"

interface PricingSectionProps {
  title: string
  subtitle: string
  tiers: PricingTier[]
  frequencies: string[]
}

export function PricingSection({
  title,
  subtitle,
  tiers,
  frequencies,
}: PricingSectionProps) {
  const [selectedFrequency, setSelectedFrequency] = React.useState(frequencies[0])

  return (
    <section className="flex flex-col items-center gap-10 py-10">
      <div className="space-y-7 text-center">
        <div className="space-y-4">
          <h1 className="text-4xl font-medium md:text-5xl">{title}</h1>
          <p className="text-muted-foreground">{subtitle}</p>
        </div>
        <div className="mx-auto flex w-fit rounded-full bg-muted p-1">
          {frequencies.map((freq) => (
            <Tab
              key={freq}
              text={freq}
              selected={selectedFrequency === freq}
              setSelected={setSelectedFrequency}
              discount={freq === "yearly"}
            />
          ))}
        </div>
      </div>

      <div className="grid w-full max-w-6xl gap-6 sm:grid-cols-2 xl:grid-cols-4">
        {tiers.map((tier) => (
          <PricingCard
            key={tier.name}
            tier={tier}
            paymentFrequency={selectedFrequency}
          />
        ))}
      </div>
    </section>
  )
}
```

**`components/ui/pricing-card.tsx`** — individual card with highlighted/popular variants:

```tsx
"use client"

import * as React from "react"
import { BadgeCheck, ArrowRight } from "lucide-react"
import NumberFlow from "@number-flow/react"

import { cn } from "@/lib/utils"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"

export interface PricingTier {
  name: string
  price: Record<string, number | string>
  description: string
  features: string[]
  cta: string
  highlighted?: boolean
  popular?: boolean
}

interface PricingCardProps {
  tier: PricingTier
  paymentFrequency: string
}

export function PricingCard({ tier, paymentFrequency }: PricingCardProps) {
  const price = tier.price[paymentFrequency]
  const isHighlighted = tier.highlighted
  const isPopular = tier.popular

  return (
    <Card
      className={cn(
        "relative flex flex-col gap-8 overflow-hidden p-6",
        isHighlighted
          ? "bg-foreground text-background"
          : "bg-background text-foreground",
        isPopular && "ring-2 ring-primary"
      )}
    >
      {isHighlighted && <HighlightedBackground />}
      {isPopular && <PopularBackground />}

      <h2 className="flex items-center gap-3 text-xl font-medium capitalize">
        {tier.name}
        {isPopular && (
          <Badge variant="secondary" className="mt-1 z-10">
            Most Popular
          </Badge>
        )}
      </h2>

      <div className="relative h-12">
        {typeof price === "number" ? (
          <>
            <NumberFlow
              format={{
                style: "currency",
                currency: "USD",
                trailingZeroDisplay: "stripIfInteger",
              }}
              value={price}
              className="text-4xl font-medium"
            />
            <p className="-mt-2 text-xs text-muted-foreground">
              Per month/user
            </p>
          </>
        ) : (
          <h1 className="text-4xl font-medium">{price}</h1>
        )}
      </div>

      <div className="flex-1 space-y-2">
        <h3 className="text-sm font-medium">{tier.description}</h3>
        <ul className="space-y-2">
          {tier.features.map((feature, index) => (
            <li
              key={index}
              className={cn(
                "flex items-center gap-2 text-sm font-medium",
                isHighlighted ? "text-background" : "text-muted-foreground"
              )}
            >
              <BadgeCheck className="h-4 w-4" />
              {feature}
            </li>
          ))}
        </ul>
      </div>

      <Button
        variant={isHighlighted ? "secondary" : "default"}
        className="w-full"
      >
        {tier.cta}
        <ArrowRight className="ml-2 h-4 w-4" />
      </Button>
    </Card>
  )
}

const HighlightedBackground = () => (
  <div className="absolute inset-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:45px_45px] [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_110%)]" />
)

const PopularBackground = () => (
  <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.1),rgba(255,255,255,0))]" />
)
```

**`components/ui/pricing-tab.tsx`** — spring-animated frequency toggle:

```tsx
"use client"

import * as React from "react"
import { motion } from "framer-motion"

import { cn } from "@/lib/utils"
import { Badge } from "@/components/ui/badge"

interface TabProps {
  text: string
  selected: boolean
  setSelected: (text: string) => void
  discount?: boolean
}

export function Tab({
  text,
  selected,
  setSelected,
  discount = false,
}: TabProps) {
  return (
    <button
      onClick={() => setSelected(text)}
      className={cn(
        "relative w-fit px-4 py-2 text-sm font-semibold capitalize",
        "text-foreground transition-colors",
        discount && "flex items-center justify-center gap-2.5"
      )}
    >
      <span className="relative z-10">{text}</span>
      {selected && (
        <motion.span
          layoutId="tab"
          transition={{ type: "spring", duration: 0.4 }}
          className="absolute inset-0 z-0 rounded-full bg-background shadow-sm"
        />
      )}
      {discount && (
        <Badge
          variant="secondary"
          className={cn(
            "relative z-10 whitespace-nowrap shadow-none",
            selected && "bg-muted"
          )}
        >
          Save 35%
        </Badge>
      )}
    </button>
  )
}
```

**Demo usage:**

```tsx
import { PricingSection } from "@/components/ui/pricing-section"

const PAYMENT_FREQUENCIES = ["monthly", "yearly"]

const TIERS = [
  {
    id: "individuals",
    name: "Individuals",
    price: { monthly: "Free", yearly: "Free" },
    description: "For your hobby projects",
    features: ["Free email alerts", "3-minute checks", "Automatic data enrichment", "10 monitors", "Up to 3 seats"],
    cta: "Get started",
  },
  {
    id: "teams",
    name: "Teams",
    price: { monthly: 90, yearly: 75 },
    description: "Great for small businesses",
    features: ["Unlimited phone calls", "30 second checks", "Single-user account", "20 monitors", "Up to 6 seats"],
    cta: "Get started",
    popular: true,
  },
  {
    id: "organizations",
    name: "Organizations",
    price: { monthly: 120, yearly: 100 },
    description: "Great for large businesses",
    features: ["Unlimited phone calls", "15 second checks", "Single-user account", "50 monitors", "Up to 10 seats"],
    cta: "Get started",
  },
  {
    id: "enterprise",
    name: "Enterprise",
    price: { monthly: "Custom", yearly: "Custom" },
    description: "For multiple teams",
    features: ["Everything in Organizations", "Up to 5 team members", "100 monitors", "15 status pages", "200+ integrations"],
    cta: "Contact Us",
    highlighted: true,
  },
]

export function PricingSectionDemo() {
  return (
    <div className="relative flex justify-center items-center w-full mt-20 scale-90">
      <div className="absolute inset-0 -z-10">
        <div className="h-full w-full bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:35px_35px] opacity-30 [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_110%)]" />
      </div>
      <PricingSection
        title="Simple Pricing"
        subtitle="Choose the best plan for your needs"
        frequencies={PAYMENT_FREQUENCIES}
        tiers={TIERS}
      />
    </div>
  )
}
```

**What separates this from the generic version:**
- **Generic:** three identical cards with a "Most Popular" text badge. This: four tiers with three distinct visual treatments — default, popular (`ring-2` + radial glow), and highlighted (full foreground/background inversion with grid-line overlay). Hierarchy is compounded, not single-signal.
- **Generic:** static price text that snaps between monthly/yearly. This: `NumberFlow` animates the numeric transition with interpolated digits, and a spring-physics tab indicator (`layoutId`) makes the frequency toggle feel physical.
- **Generic:** all buttons identical. This: highlighted tier gets `variant="secondary"` (inverted context), others get `variant="default"` — the CTA adapts to its card's visual context rather than being uniform.
- **Generic:** no background texture or depth. This: highlighted card gets a CSS grid-line overlay masked with a radial gradient; popular card gets a subtle radial purple glow. Texture creates depth without images.
- **Generic:** pricing is a static layout. This: a component system — `PricingSection` orchestrates state, `PricingCard` handles variants, `Tab` handles selection — designed for real integration, not a screenshot.

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
