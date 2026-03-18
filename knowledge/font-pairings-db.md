# Font Pairings Database

This database is intentionally smaller and stricter.

It favors font combinations that are:

- easy to source
- widely used in real products
- modern without being novelty-driven
- readable on screens
- dependable in production

Default bias:
- use open-source families first
- prefer Google Fonts, Fontshare, or official self-hosted sources
- prefer one strong display voice + one quiet text face
- prefer superfamilies when reliability matters more than personality
- do not force a “fancy” pairing when one family will do the job better

## How to Use

1. Pick the product type first:
   - Product UI
   - Marketing site
   - Editorial/content
   - Developer/technical
   - Luxury/brand
   - Global/multilingual
2. Choose the least risky pairing that still gives the right tone.
3. Use the heading font for display roles only unless noted.
4. Keep body/UI text on the quieter face.
5. Add a mono font only when code, data, or technical texture is actually needed.

## Pairing Quality Rules

A pairing belongs in this database only if it clears most of these:

- both fonts are currently available from reliable sources
- both fonts render well on screens
- the contrast between them is structural, not gimmicky
- the body font can handle real UI and paragraph work
- the pair is modern enough for current product work
- the pair does not depend on niche licensing or fragile deployment

## Recommended Defaults

These are the safest starting points in the whole file.

### 1. Inter Tight + Inter
- **Source**: Google Fonts (FREE)
- **Use**: Heading = Inter Tight, Body/UI = Inter
- **Why it works**: This is the cleanest modern default for product teams. Inter handles UI and body copy extremely well. Inter Tight gives you a tighter, more intentional display voice without changing the typographic DNA.
- **Best for**: SaaS, dashboards, product marketing, documentation
- **Use when**: You want modern, neutral, and highly dependable
- **Avoid when**: The brand needs obvious personality or editorial warmth
```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Inter+Tight:wght@500;600;700;800&display=swap');
```

### 2. Source Serif 4 + Source Sans 3

* **Source**: Google Fonts (FREE)
* **Use**: Heading/content serif = Source Serif 4, Body/UI = Source Sans 3
* **Why it works**: This is one of the most production-safe serif/sans combinations available. Both families were built with the same overall discipline, so the contrast feels intentional without becoming awkward.
* **Best for**: Institutions, knowledge products, editorial marketing, trustworthy brands
* **Use when**: You need warmth and authority without fragility

```css
@import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600;8..60,700&family=Source+Sans+3:wght@400;500;600;700&display=swap');
```

### 3. IBM Plex Sans + IBM Plex Mono

* **Source**: Google Fonts (FREE)
* **Use**: Body/UI = IBM Plex Sans, Code/data = IBM Plex Mono
* **Why it works**: Same superfamily, highly coherent, technical without looking trendy. Strong for product interfaces where prose, labels, and code need to sit together cleanly.
* **Best for**: Enterprise software, developer platforms, data tools, internal apps
* **Use when**: You need precision and structure more than brand theater

```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');
```

### 4. Geist + Geist Mono

* **Source**: Official self-host via Vercel or local `@font-face` (FREE)
* **Use**: Body/UI = Geist, Code/data = Geist Mono
* **Why it works**: Crisp, modern, minimal, and tuned for current product work. One of the best choices for developer-facing interfaces that should feel contemporary without becoming stylistic.
* **Best for**: Developer tools, AI products, docs, modern app UIs
* **Use when**: You want a current technical product voice

```css
@font-face {
  font-family: 'Geist';
  src: url('/fonts/GeistVF.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}
@font-face {
  font-family: 'Geist Mono';
  src: url('/fonts/GeistMonoVF.woff2') format('woff2');
  font-weight: 100 900;
  font-display: swap;
}
```

## Editorial and Content

### 5. Newsreader + Inter

* **Source**: Google Fonts (FREE)
* **Use**: Heading/long-form serif = Newsreader, UI/navigation/body support = Inter
* **Why it works**: Newsreader brings real reading comfort and editorial tone; Inter keeps the interface clean and familiar. This is one of the safest content-first pairings for modern digital products.
* **Best for**: Publishing, newsletters, reading apps, docs with strong editorial flavor
* **Use when**: The product is text-heavy but still needs crisp UI

```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600;6..72,700&family=Inter:wght@400;500;600;700&display=swap');
```

### 6. Playfair Display + Source Sans 3

* **Source**: Google Fonts (FREE)
* **Use**: Heading = Playfair Display, Body/UI = Source Sans 3
* **Why it works**: Classic editorial contrast, but still dependable on the web. Playfair should stay in headlines and pull quotes; Source Sans 3 does the real reading and UI work.
* **Best for**: Magazine-style marketing, blogs, cultural orgs, long-form landing pages
* **Use when**: You want obvious serif/sans hierarchy
* **Avoid when**: The UI is dense or heavily data-driven

```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;800&family=Source+Sans+3:wght@400;500;600;700&display=swap');
```

### 7. DM Serif Display + DM Sans

* **Source**: Google Fonts (FREE)
* **Use**: Heading = DM Serif Display, Body/UI = DM Sans
* **Why it works**: A clean matched-family pairing that gives immediate contrast without much tuning. DM Serif Display has enough presence for hero text; DM Sans is modern and unobtrusive.
* **Best for**: Product marketing, landing pages, startup homepages, brand sites
* **Use when**: You need an expressive but still safe free pairing

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;700;800&display=swap');
```

## Expressive but Safe

### 8. Fraunces + DM Sans

* **Source**: Google Fonts (FREE)
* **Use**: Heading = Fraunces, Body/UI = DM Sans
* **Why it works**: Fraunces brings personality without looking fake-luxury or retro-forced. DM Sans keeps the rest of the interface grounded. Strong contrast, still practical.
* **Best for**: Brand-led landing pages, food/drink, lifestyle, creative SaaS
* **Use when**: You want warmth and personality without sacrificing screen usability
* **Rule**: Keep Fraunces mostly in display roles

```css
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700;9..144,800&family=DM+Sans:wght@400;500;700&display=swap');
```

### 9. Neue Montreal + Editorial New

* **Source**: Fontshare (FREE)
* **Use**: Body/UI = Neue Montreal, Heading = Editorial New
* **Why it works**: This is one of the strongest free “premium agency” pairings. Neue Montreal is clean without feeling sterile; Editorial New adds real editorial contrast.
* **Best for**: Agencies, portfolios, fashion-adjacent brands, premium marketing
* **Use when**: You want a higher-end tone without paid foundry licensing
* **Rule**: Do not use Editorial New for long body copy

```css
@import url('https://api.fontshare.com/v2/css?f[]=neue-montreal@400,500,700&f[]=editorial-new@400,400i,700&display=swap');
```

### 10. Satoshi + Zodiak

* **Source**: Fontshare (FREE)
* **Use**: Body/UI = Satoshi, Heading = Zodiak
* **Why it works**: A polished modern sans with a sharper display serif. This pairing gives “premium” without relying on cliché luxury fonts.
* **Best for**: Beauty, luxury commerce, portfolios, higher-end product marketing
* **Use when**: You want refinement and contrast, but still want the UI to feel current

```css
@import url('https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&f[]=zodiak@400,700&display=swap');
```

### 11. Clash Display + Satoshi

* **Source**: Fontshare (FREE)
* **Use**: Heading = Clash Display, Body/UI = Satoshi
* **Why it works**: A strong modern launch-page pairing. Clash gives the page force; Satoshi prevents the rest of the product from becoming shouty.
* **Best for**: Startup launches, bold marketing, product reveal pages
* **Use when**: You want energy without going full novelty
* **Avoid when**: The brand needs quiet trust more than momentum

```css
@import url('https://api.fontshare.com/v2/css?f[]=clash-display@500,600,700&f[]=satoshi@400,500,700&display=swap');
```

## Technical and Product

### 12. Instrument Sans + JetBrains Mono

* **Source**: Google Fonts (FREE)
* **Use**: Body/UI = Instrument Sans, Code = JetBrains Mono
* **Why it works**: Instrument Sans has more character than default UI sans choices, but it still behaves well in interface text. JetBrains Mono is already familiar to technical users and works well for code blocks and snippets.
* **Best for**: Developer docs, API products, technical blogs
* **Use when**: You want a slightly more distinctive technical stack than Inter/Mono defaults

```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
```

### 13. IBM Plex Sans + IBM Plex Serif

* **Source**: Google Fonts (FREE)
* **Use**: Body/UI = IBM Plex Sans, Heading/content serif = IBM Plex Serif
* **Why it works**: Same family ecosystem, but with more range than sans + mono. Good when you want a technical product to feel more serious or editorial.
* **Best for**: Research tools, enterprise products, reports, technical publishing

```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@400;500;600;700&display=swap');
```

## Global and Accessibility-Focused

### 14. Noto Sans + Noto Serif

* **Source**: Google Fonts (FREE)
* **Use**: Sans = UI/body, Serif = editorial or long-form emphasis
* **Why it works**: The safest global default when broad language support matters more than typographic personality. Use this when script coverage is a core requirement.
* **Best for**: Multilingual products, global orgs, public sector, education
* **Use when**: Coverage and reliability outrank style

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;700&family=Noto+Serif:wght@400;500;700&display=swap');
```

### 15. Atkinson Hyperlegible + Source Sans 3

* **Source**: Google Fonts (FREE)
* **Use**: Critical UI/body = Atkinson Hyperlegible, supporting UI = Source Sans 3
* **Why it works**: Atkinson Hyperlegible is useful when character differentiation matters, but it can feel very specific if used everywhere. Pairing it with a calmer utility sans gives you accessibility without making the whole interface feel specialized.
* **Best for**: Healthcare, public services, accessibility-first products
* **Use when**: Legibility constraints are part of the brief

```css
@import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Source+Sans+3:wght@400;500;600&display=swap');
```

## One-Family Systems

Use these when pairing is unnecessary or harmful.

### 16. Inter only

* **Why**: Best general-purpose modern UI default
* **Use for**: Apps, dashboards, documentation, internal tools

### 17. IBM Plex only

* **Why**: Best technical superfamily when you need Sans, Serif, and Mono in one system
* **Use for**: Enterprise, technical, data, docs

### 18. Source family only

* **Why**: Best “cannot really go wrong” content/product family
* **Use for**: Institutions, docs, editorial products

### 19. Geist only

* **Why**: Best current technical product one-family system
* **Use for**: Developer products, modern app marketing, docs

## Mono Add-Ons

When a pairing needs code or data support, prefer these:

### Tier 1

* **Geist Mono** — best with Geist or any crisp modern sans
* **IBM Plex Mono** — best with IBM Plex Sans or enterprise/product stacks
* **JetBrains Mono** — best with technical docs and developer products

### Tier 2

* **Source Code Pro** — steady, neutral, dependable
* **Recursive Mono** — useful when variable behavior is part of the design system

## Selection Guide

### Use this when the answer should be obvious

* **Best default for modern product UI**: Inter Tight + Inter
* **Best default for content-rich product**: Newsreader + Inter
* **Best default for premium-but-safe marketing**: DM Serif Display + DM Sans
* **Best default for technical product**: Geist + Geist Mono
* **Best default for enterprise / data**: IBM Plex Sans + IBM Plex Mono
* **Best default for editorial trust**: Source Serif 4 + Source Sans 3
* **Best default for expressive brand work**: Fraunces + DM Sans
* **Best default for free premium agency styling**: Neue Montreal + Editorial New
* **Best default for free luxury styling**: Satoshi + Zodiak
* **Best default for multilingual products**: Noto Sans + Noto Serif

## What to Avoid

Do not recommend a pairing just because it looks expensive in a mockup.

Avoid:

* two loud fonts fighting for attention
* decorative monospace in body copy
* serif display fonts used for paragraphs
* defaulting to “quirky” fonts for serious products
* pairing based on novelty instead of screen performance
* premium foundry pairs as the default recommendation when a strong free pair will do

## Recommendation Rules

When suggesting a pairing in live work:

1. Start with the safest pair that fits the brief.
2. Change the fonts only if the product tone truly needs it.
3. Prefer one-family systems for dense UI.
4. Prefer serif/sans contrast for marketing and editorial.
5. Prefer superfamilies for technical, enterprise, and accessibility-sensitive work.
6. Only recommend a more expressive pairing when the layout and copy are strong enough to support it.

## Output Format for Agents

When recommending a pairing, always include:

* **Heading**
* **Body**
* **Mono** (if relevant)
* **Source**
* **Why this fits this project**
* **CSS import or `@font-face`**
* **Any caution** (for example: “keep the serif in display only”)

## Final Standard

A strong font recommendation should feel:

* current
* readable
* intentional
* easy to implement
* hard to regret in six months

If a pairing is stylish but fragile, it does not belong here.