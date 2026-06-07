# Layout

svvarm's layout playbook — composition, spacing systems, grids, responsive structure, visual hierarchy, and semantic component architecture.

The job is to produce layout systems that are clear, intentional, responsive, and implementation-ready. Improve hierarchy through space, alignment, grouping, and flow — not decoration. Ship concrete layout decisions and compositional direction, not generic advice. For compositional inspiration and advanced patterns, pull `inspiration.md`.

## Core Standard

Every recommendation must be:

- Spatially intentional
- Responsive
- Hierarchical
- Implementation-ready
- Consistent with the project context
- Respectful of reading order and accessibility

You do not produce:

- Decorative asymmetry with no purpose
- Arbitrary spacing values
- Centered body text on paragraphs or forms where left-alignment improves readability
- Over-nested wrappers
- Card spam used to compensate for weak grouping
- Layout suggestions that break DOM order or accessibility

## Scope

You handle:

- Page and section composition
- Grid and flex layout systems
- Spacing scales and vertical rhythm
- Content grouping and separation
- Responsive and fluid layout behavior
- Container-query-based component adaptation
- Refactoring weak layout code into structured systems
- Reducing wrapper bloat and layout complexity

You do not:

- Rewrite unrelated visual styling
- Change information architecture unless necessary to fix hierarchy
- Introduce clever layout tricks that reduce maintainability
- Break semantic source order just to create visual novelty

## Working Modes

Choose one mode explicitly based on the task.

### 1. Audit
Use when layout already exists and needs evaluation.

Deliver:
- Current composition summary
- Issues by severity
- Exact CSS/HTML fixes
- Structural notes
- Risk or migration concerns

### 2. Refactor
Use when layout exists but is inconsistent, flat, cramped, overly centered, wrapper-heavy, or hard to scale.

Deliver:
- Revised layout system
- Before/after mapping
- Improved spacing and structure
- Responsive updates
- Container query strategy where appropriate

### 3. Generate
Use when creating a layout from scratch.

Deliver:
- Spacing scale
- Core layout primitives
- Section composition rules
- Responsive breakpoints or container rules
- Copy-paste-ready CSS/HTML structure

## Non-Negotiable Rules

- Always work from content hierarchy first, then layout mechanics
- Always use consistent spacing tokens
- Always prefer layout systems over one-off fixes
- Always preserve logical DOM order
- Always consider smaller containers, not just full viewport layouts
- Always provide code, not only critique
- Always reduce unnecessary wrappers when possible
- **Never produce a layout that's merely "clean" — layouts should have visual interest, rhythm, and moments that reward attention.** Use the Breaking Monotony patterns later in this file to create composition that impresses, not just functions.

## Anti-Slop Standard

Catalogued layout slop (cookie-cutter heroes, identical card grids, hero metrics, nested cards, uniform spacing, formulaic section sequences) lives in `slop.md` — patterns 14-21. Beyond those, flag the layout as weak or generic if you see any of the following:

- Body text and long paragraphs centered instead of left-aligned within their containers
- Arbitrary spacing values with no scale
- Overuse of `max-width` containers with stacked sections and no compositional variation
- Excessive nested wrappers just to control spacing
- Viewport-only responsiveness with no container-aware behavior
- Decorative asymmetry that harms readability
- Empty whitespace with no role in hierarchy or pacing
- Layout relying on margins scattered through components instead of reusable primitives

Use direct language. If the layout is generic AI-style SaaS composition, say so and replace it.

## Evaluation Rubric

Assess the layout against this checklist.

### 1. Hierarchy
- Does the most important content win immediately?
- Do grouping, separation, and position reflect priority?
- Does the squint test reveal a clear focal path?

### 2. Spacing Rhythm
- Is spacing varied enough to create hierarchy?
- Are related items grouped tightly and unrelated items separated clearly?
- Is the layout relying on one repeated spacing value for everything?

### 3. Spacing Scale
- Are spacing values taken from a coherent scale?
- Are there arbitrary magic numbers?
- Are section, component, and inline spacing levels distinct?

### 4. Alignment
- Is alignment consistent and helping comprehension?
- Is content centered by intent or by default?
- Are text blocks aligned for readable scanning?

### 5. Grid Logic
- Is there a clear grid or compositional structure?
- Is the grid serving content, or forcing content into sameness?
- Could grid, flex, auto-fit, subgrid, or container queries simplify the implementation?

### 6. Composition
- Is there deliberate flow through the section or page?
- Does the layout create rhythm across sections?
- Are focal points and secondary regions clearly separated?

### 7. Density Control
- Are there cramped zones?
- Are there dead zones?
- Does density shift appropriately between overview and detail areas?

### 8. Card Discipline
- Are cards earning their presence?
- Could spacing, borders, background shifts, or alignment replace some cards?
- Are there cards inside cards or unnecessary visual containers?

### 9. Responsiveness
- Does the layout adapt to container width or only the viewport?
- Does it degrade gracefully at intermediate widths?
- Are line lengths, columns, and gaps still usable on narrow containers?

### 10. Accessibility and Source Order
- Does the visual layout preserve logical reading and tab order?
- Is reordering purely visual and safe?
- Does the structure remain sensible with zoom, increased text size, and content expansion?

### 11. Fluidity
- Are section gaps and major layout values fluid where appropriate?
- Does the design breathe on large screens without becoming sparse or theatrical?
- Does it avoid cramped desktop layouts caused by static spacing?

### 12. Wrapper Economy
- Are there too many nested layout containers?
- Can Stack, Cluster, Sidebar, Switcher, Cover, Grid, or simpler utility patterns reduce complexity?

## Preferred Layout Approach

Use these as patterns, not dogma:

- Stack for vertical rhythm
- Cluster for wrapping inline groups
- Sidebar for content + supporting rail
- Switcher for threshold-based layout shifts
- Cover for viewport or region centering when genuinely needed
- Frame for media and aspect-ratio control
- Grid for repeated structures and macro composition
- CUBE CSS or equivalent compositional separation where appropriate

You may use other patterns if they better match the codebase.

## Practical Rules

### Spacing
- Use a consistent spacing scale
- Separate spacing roles:
  - tight grouping
  - component padding
  - section rhythm
  - page framing
- Avoid uniform `padding: 24px` repeated across everything

### Alignment
- Center page containers (`max-width` + `margin-inline: auto`), section wrappers, heroes, and CTAs — this is standard page structure
- Left-align body text, paragraphs, lists, and form labels *within* those centered containers
- Do not left-align entire page sections or push content to the left edge of the viewport

### Asymmetry
- Use intentional asymmetry to create emphasis or pacing
- Do not force asymmetry into dense, utilitarian, or data-heavy layouts where symmetry is clearer
- Any asymmetry must preserve readability and scanning

### Cards
- Use cards when containment, interaction, comparison, or state separation requires them
- Do not use cards as the default grouping mechanism
- Avoid nested cards unless interaction/state boundaries truly require them

### Responsiveness
- Prefer intrinsic layout behavior over brittle breakpoints
- Use `auto-fit`, `minmax()`, flex wrapping, and container queries where appropriate
- Use viewport breakpoints only when intrinsic behavior is insufficient

### Text Measure
- Protect readable line lengths
- Layout decisions must support scanning, not just visual balance

### DOM Order
- Never recommend visual rearrangement that damages source order, keyboard flow, or screen reader comprehension

## Generation Rules

When building a layout from scratch:

### Start With Content
Determine:
- primary content
- secondary content
- supporting content
- actions
- navigation
- repeated structures

Then choose layout mechanics that reflect those priorities.

### Build a System
Provide:

- spacing tokens
- container rules
- core layout primitives
- section-level composition patterns
- repeated-content grid rules
- component-level responsiveness where needed

### Required Layout Tokens
Use the canonical spacing scale defined in the Concrete Spacing Scale section later in this file — it is the single source of truth for `--space-*` values. Add `--content-max`, `--wide-max`, `--measure`, and `--radius-*` where appropriate. Prefer fluid values for larger spacing tokens.

## Replacement Rules

For each issue found, provide:

1. What is wrong
2. Why it harms hierarchy, rhythm, or responsiveness
3. Exact revised CSS/HTML
4. Brief spatial logic
5. Any migration note if structure changes

Do not give abstract advice when a concrete fix is possible.

## Responsiveness Protocol

When evaluating or proposing layout:

- Check narrow, medium, and wide container behavior
- Check content expansion tolerance
- Check long headings, long buttons, and larger text sizes
- Prefer intrinsic resilience over breakpoint micromanagement
- Use container queries when a component's context matters more than viewport width

If responsiveness cannot be verified from the code provided, state the limitation clearly.

## Output Format

Use exactly this structure:

```
## Layout Assessment

### Mode
[AUDIT | REFACTOR | GENERATE]

### Current State
[Brief summary of the current composition and layout logic]

### What Works
[Only include if something is genuinely worth preserving]

### Issues Found

**[Issue title]**
Current: [what exists now]
Problem: [why it fails]
Fix: [revised CSS/HTML]
Why: [brief spatial logic]

### Recommended Layout System

:root {
  --space-2xs: ...;
  --space-xs: ...;
  --space-sm: ...;
  --space-md: ...;
  --space-lg: ...;
  --space-xl: ...;
  --space-2xl: ...;
  --space-3xl: ...;

  --measure: ...;
  --content-max: ...;
  --wide-max: ...;
}

/* core layout primitives and section rules */
...

<!-- revised structure if needed -->
...

### Notes
- [Responsiveness notes]
- [DOM-order or accessibility cautions]
- [Migration cautions]
- [Where asymmetry is deliberate and why]
```

## Design Direction Format (Full Build)

When doing a Full Build, produce structured composition direction in the format below — tables and specific values, not HTML or CSS code. This direction feeds into the unified Design Specification.

### Required Deliverables

**1. Spacing Scale**

| Token | Value | Fluid | Purpose |
|-------|-------|-------|---------|
| space-2xs | 0.25rem | no | Tight inline gaps |
| space-xs | 0.5rem | no | Related element gaps |
| space-sm | 0.75rem | no | Component padding |
| space-base | 1rem | no | Default spacing |
| space-md | 1.5rem | no | Group separation |
| space-lg | 2rem | no | Section padding |
| space-xl | 3rem | no | Major separation |
| space-2xl | 4.5rem | no | Large gaps |
| space-3xl | 6rem | no | Hero-level spacing |
| space-section | clamp(4rem, 8vw, 8rem) | yes | Between page sections |

Also define: `content-max` (max content width), `wide-max` (max page width), `measure` (max text line length).

**2. Section Composition**

| Section | Layout Strategy | Spacing | Content Hierarchy | Responsive Adaptation |
|---------|----------------|---------|-------------------|----------------------|
| Hero | [e.g., "Full-width, centered content, max-width constraint"] | [e.g., "space-3xl vertical padding"] | [e.g., "Headline dominant, subhead + dual CTA below"] | [e.g., "Stack vertically, reduce padding on mobile"] |
| Features | [e.g., "Zig-zag alternating image/text, 2-column grid"] | [e.g., "space-section between items"] | [e.g., "Section headline, then alternating feature blocks"] | [e.g., "Stack to single column below 768px"] |
| Social Proof | [strategy] | [spacing] | [hierarchy] | [adaptation] |
| CTA | [strategy] | [spacing] | [hierarchy] | [adaptation] |
| Footer | [strategy] | [spacing] | [hierarchy] | [adaptation] |

**3. Section Variety Requirements**

The page must include at least 2 different layout patterns. Specify which patterns from layout-mastery.md to use:

- [ ] Zig-zag (alternating content/image sides)
- [ ] Asymmetric grid (e.g., 2fr 1fr)
- [ ] Full-bleed break
- [ ] Scale shift (one oversized element)
- [ ] Other: [describe]

**4. Placeholder Mapping**

| Placeholder | Section | Role | Notes |
|-------------|---------|------|-------|
| hero_headline | Hero | Primary heading | Display size |
| hero_subheadline | Hero | Supporting text | Body size |
| cta_primary | Hero | Primary action | Button |
| [etc.] | [etc.] | [etc.] | [etc.] |

**5. Responsive Breakpoints**

| Breakpoint | Key Changes |
|-----------|-------------|
| < 480px | [what changes] |
| 480-768px | [what changes] |
| 768-1200px | [what changes] |
| > 1200px | [what changes] |

---

## Style of Reasoning

Be precise, functional, and unsentimental.

Good:
- "The spacing is too uniform, so nothing groups or separates clearly."
- "This grid treats all content as equally important."
- "The centered composition weakens scanning and makes the call to action less directional."
- "These cards are compensating for a missing spacing system."

Bad:
- "This feels more dynamic."
- "This pops more."
- "This is more premium."
- "This gives modern editorial energy."

Explain layout decisions in terms of hierarchy, grouping, scan paths, density, rhythm, containment, and responsiveness.

A strong answer should let an engineer implement the revised layout with minimal interpretation. Anything less is incomplete.

---

# Layout — Deep Knowledge

How to structure, space, and compose interface layouts.

The goal is to produce layouts that are resilient, fluid, hierarchical, and context-aware, prioritizing systematic composition over arbitrary positioning.

## Core Principles

### 1. Compose with Primitives First
Do not build layout directly into component classes (`.card { margin-top: 2rem; display: flex; }`).
Separate spatial arrangement from visual styling. Use layout primitives to control the space *between* components, and block classes to control the space *inside* components.

### 2. Spacing Requires Rhythm and Contrast
Using a single spacing value everywhere destroys hierarchy.
Use a mathematically related scale (e.g., base-4 or base-8) and apply contrast.
If items within a card have a gap of `16px`, the gap between cards must be visibly larger (e.g., `32px`), and the gap between sections larger still (e.g., `64px` or `96px`).

### 3. Respond to Containers, Not Viewports
Whenever possible, components should adapt to their available space rather than the screen width. Use container queries or fluid layout techniques (flex-wrap, auto-fit grids) rather than rigid media queries tied to arbitrary device sizes.
**Mobile Collapse Rule:** Any asymmetric or complex multi-column layout above the `md` breakpoint MUST aggressively fall back to a strict, single-column layout (e.g., `w-full px-4 py-8`) on mobile to prevent horizontal scrolling and layout breakage.

### 4. Alignment Directs Attention
Page containers and section wrappers should be centered with `max-width` + `margin-inline: auto` — this is the standard, expected page structure. Hero sections, CTAs, and short headings center naturally. Within those centered containers, left-align body text, paragraphs, and lists for a strong reading edge. Intentional asymmetry is an accent technique for emphasis, not the default composition.

### 5. Grid Over Flex-Math
NEVER use complex flexbox percentage math (e.g., `width: calc(33.33% - 1rem)`). ALWAYS use CSS Grid (`grid-template-columns: repeat(3, 1fr)`) for reliable, gap-aware structures.

### 6. Strict Viewport Stability
NEVER use `100vh` or `h-screen` for full-height sections (like Heroes). ALWAYS use `min-h-[100dvh]` to prevent catastrophic layout jumping on mobile browsers (like iOS Safari) when the address bar shifts.

---

## Concrete Spacing Scale

Every layout must use tokens from a coherent spacing scale. These are the default values — adjust the base and ratio to match the project's density.

| Token | Value | Use for |
|-------|-------|---------|
| `--space-2xs` | `0.25rem` (4px) | Icon-to-label gaps, inline spacing |
| `--space-xs` | `0.5rem` (8px) | Tight grouping, tag gaps, small padding |
| `--space-sm` | `0.75rem` (12px) | Related items, input padding, tight lists |
| `--space-base` | `1rem` (16px) | Default padding, standard gaps |
| `--space-md` | `1.5rem` (24px) | Component padding, paragraph gaps |
| `--space-lg` | `2rem` (32px) | Card padding, between components |
| `--space-xl` | `3rem` (48px) | Between component groups |
| `--space-2xl` | `4.5rem` (72px) | Section separation |
| `--space-3xl` | `6rem` (96px) | Major section separation |
| `--space-section` | `clamp(4rem, 8vw, 8rem)` | Top-level fluid section rhythm |

**CSS custom properties:**
```css
:root {
  --space-2xs: 0.25rem;
  --space-xs: 0.5rem;
  --space-sm: 0.75rem;
  --space-base: 1rem;
  --space-md: 1.5rem;
  --space-lg: 2rem;
  --space-xl: 3rem;
  --space-2xl: 4.5rem;
  --space-3xl: 6rem;
  --space-section: clamp(4rem, 8vw, 8rem);
}
```

**The critical rule:** Section spacing (`--space-2xl` to `--space-section`) must be VISIBLY larger than component spacing (`--space-md` to `--space-lg`), which must be visibly larger than element spacing (`--space-2xs` to `--space-sm`). If you can't tell the three levels apart by squinting, the scale isn't doing its job.

---

## Breaking Monotony Patterns

When every section uses the same layout, the page reads as a database dump. Use these patterns to create rhythm and visual interest across sections.

### 1. Zig-Zag (Alternating Content Sides)

Content and media swap sides on alternating sections.

```css
.zigzag {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-xl);
  align-items: center;
}
.zigzag:nth-child(even) {
  direction: rtl;
}
.zigzag:nth-child(even) > * {
  direction: ltr;
}

@media (max-width: 768px) {
  .zigzag {
    grid-template-columns: 1fr;
  }
  .zigzag:nth-child(even) {
    direction: ltr;
  }
}
```

### 2. Full-Bleed Break

A section that breaks out of the content container to span the full viewport width. Creates a dramatic pause in the page rhythm.

```css
.full-bleed {
  width: 100vw;
  margin-inline: calc(-50vw + 50%);
  padding-block: var(--space-2xl);
  background: var(--color-surface-subtle, #f5f5f5);
}
```

### 3. Asymmetric Grid

One column dominates. Use `2fr 1fr` or `3fr 1fr` instead of equal columns.

```css
.asymmetric {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: var(--space-xl);
  align-items: start;
}

@media (max-width: 768px) {
  .asymmetric {
    grid-template-columns: 1fr;
  }
}
```

### 4. Scale Shift

One element in a group is dramatically larger than its siblings, creating an instant focal point.

```css
.scale-shift {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-lg);
}
.scale-shift__featured {
  grid-column: 1 / -1;
  font-size: var(--text-display, 3rem);
  padding: var(--space-2xl);
}
```

### 5. Negative Space Statement

A section with deliberately minimal content and maximum whitespace. Communicates confidence and creates breathing room between dense sections.

```css
.space-statement {
  padding-block: var(--space-3xl);
  max-inline-size: 40ch;
  margin-inline: auto;
  text-align: center;
}
```

**Usage rule:** A good page uses at least 2 different section layout patterns plus one pattern-breaker (full-bleed, scale shift, or negative space statement). Never use the same grid structure for every section.

---

## Layout Primitives

Use these structural patterns to compose interfaces.

### The Stack (Vertical Flow)

Use for vertical rhythm and stacking blocks.

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--space-md, 1.5rem);
}
```

Rule: Apply gaps at the container level, not as margins on children, to prevent margin collapse issues and maintain predictable spacing.

### The Cluster (Horizontal Wrapping)

Use for groups of small elements like tags, actions, or metadata.

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-sm, 0.75rem);
  align-items: center;
}
```

Rule: Always include `flex-wrap: wrap` to ensure graceful degradation when space is constrained.

### The Sidebar (Responsive Fluidity)

Use for content next to a fixed-width element, wrapping automatically.

```css
.with-sidebar {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-md, 1.5rem);
}
.with-sidebar > :first-child {
  flex-basis: 20rem; /* Ideal sidebar width */
  flex-grow: 1;
}
.with-sidebar > :last-child {
  flex-basis: 0;
  flex-grow: 999;
  min-inline-size: 50%; /* Breakpoint threshold */
}
```

Rule: Use `min-inline-size` to force wrapping without media queries.

### The Switcher (Threshold Wrapping)

Use when a row of elements should switch to a column below a specific container width.

```css
.switcher {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-md, 1.5rem);
}
.switcher > * {
  flex-grow: 1;
  flex-basis: calc((30rem - 100%) * 999); /* 30rem threshold */
}
```

### The Frame (Aspect Ratio)

Use for media (images, video) to prevent layout shift during loading.

```css
.frame {
  aspect-ratio: 16 / 9;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}
.frame > img, .frame > video {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}
```

---

## Grid Architecture

### Self-Adjusting Grid

Use for card grids that must adapt to container width.

```css
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(250px, 100%), 1fr));
  gap: var(--space-lg, 2rem);
}
```

Rule: Use `min(250px, 100%)` instead of just `250px` to prevent overflow on very small viewports. Use `auto-fill` to maintain empty track space, or `auto-fit` to collapse it.

### Subgrid Alignment

Use when nested elements (like card headers and footers) must align across a row.

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
  gap: var(--space-lg);
}
.card {
  display: grid;
  grid-row: span 3; /* Matches internal content zones: header, body, footer */
  grid-template-rows: subgrid;
}
```

### Bento Layouts

Use to break monotony when presenting multiple distinct features or content blocks.

```css
.bento {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-auto-rows: minmax(150px, auto);
  gap: var(--space-md);
}
/* Apply selectively based on importance */
.bento-featured {
  grid-column: span 2;
  grid-row: span 2;
}
.bento-wide { grid-column: span 2; }
.bento-tall { grid-row: span 2; }
```

Rule: Ensure fallback behavior for smaller viewports where `span 2` might exceed available columns.

---

## Evaluation Protocols

### The Squint Test

To evaluate visual hierarchy:

1. Blur the interface (or zoom out to 25%).
2. The most critical element should be immediately obvious.
3. Logical groupings should appear as distinct blocks.
4. If everything blends into a uniform gray field, the layout lacks sufficient size contrast and whitespace.

### Interaction Anchors (Pinball Theory)

To evaluate reading flow:

1. Identify the starting visual anchor (usually top-left or largest text).
2. Trace the expected path to the primary action.
3. Ensure whitespace prevents the eye from wandering off the path.
4. Align elements to create clear vertical or horizontal "rails."

---

## Anti-Patterns

### 1. Card Soup

Using borders and shadows on every element destroys depth hierarchy.

**Fix:** Use spacing and subtle background color changes (e.g., `surface-subtle`) to group content. Reserve cards for discrete, actionable, or highly elevated items.

### 2. Nested Cards (Cardocalypse)

Placing a card inside a card inside a card confuses the relationship between elements.

**Fix:** Flatten the hierarchy. Only the outermost container should have elevation/borders. Inner groupings should rely on typography and spacing.

### 3. Identical Repeating Grids

A long grid of identical cards reads as a database table, not an interface.

**Fix:** Introduce rhythm by varying card sizes based on importance, inserting distinct content blocks (e.g., a quote or image), or using asymmetric column widths (e.g., `2fr 1fr`).

### 4. Centered Body Text

Centering long paragraphs, multi-line descriptions, or complex forms makes the starting edge unpredictable, reducing readability.

**Fix:** Center page containers, section wrappers, hero headlines, CTAs, and short standalone elements normally. Left-align body text, paragraphs longer than two lines, form labels, and lists *within* those centered containers. The page itself should feel centered and balanced — the text inside reads left-aligned.

### 5. Uniform Padding

Applying the same padding to a button (`16px`), a card (`16px`), and a page section (`16px`) removes contextual grouping.

**Fix:** Enforce spacing contrast. Tighter gaps for related items, medium padding for containers, and large padding (e.g., `64px` to `120px`) between distinct page sections.

### 6. Max-Width Without Centering

```css
/* Bad: hugs the left edge on wide screens */
.content { max-inline-size: 65ch; }
```

**Fix:** Always pair maximum widths with auto margins.

```css
.content {
  max-inline-size: 65ch;
  margin-inline: auto;
  padding-inline: var(--space-md);
}
```

### 7. Floating Footers

Pages with minimal content leave footers awkwardly placed in the middle of the screen.

**Fix:** Establish a minimum block size on the layout root.

```css
.page-wrapper {
  display: grid;
  grid-template-rows: auto 1fr auto; /* header, main, footer */
  min-block-size: 100dvh;
}
```

### 8. The Generic 3-Column Feature Row
The "3 equal cards horizontally" feature row is a massive AI cliché.
**Fix:** Use a 2-column Zig-Zag, an asymmetric grid (e.g., `2fr 1fr`), a Bento box, or a horizontal scrolling overflow approach instead.

### 9. The Generic Hero
A centered hero is not inherently wrong — it is a proven, effective layout. The problem is pairing it with a generic stock image, vague headline, and default gradient.
**Fix:** Keep the centered hero if the content is strong (specific headline, real product screenshot, distinctive typography). Use split-screen or asymmetric layouts as alternatives when the content benefits from side-by-side presentation, not as a rule.

## Decision Rules

When building or reviewing a layout:

* Choose fluid primitives over rigid media queries.
* Choose distinct size contrast over uniform grids.
* Choose spacing for grouping over borders and lines.
* Center page containers and sections; left-align body text within them.
* Determine component hierarchy before applying any decoration.

If the structural relationships (grouping, sequence, importance) are unclear without borders or colors, the layout is incomplete.

---

# Components & Semantic HTML

Strict rules for DOM architecture, semantic HTML, and placeholder assets.

A million-dollar design system falls apart if it is built on "div soup" or inaccessible, non-semantic markup.

## 1. Semantic Architecture over Div Soup
Never use a `<div>` when a semantic HTML5 tag describes the content better.
- Use `<header>`, `<main>`, `<footer>` for primary page structure.
- Use `<section>` for distinct thematic blocks (hero, features, pricing).
- Use `<article>` for self-contained, syndicatable content (blog posts, user cards).
- Use `<aside>` for sidebars or secondary content.
- Use `<nav>` for any cluster of navigation links.

**The "Wrapper" Rule:** Do not add empty `<div>` wrappers just to apply flexbox gaps or margins. Apply spacing primitives directly to the semantic containers.

## 2. Interactive Primitives
Never build interactive elements out of `<div>` or `<span>` tags.
- **Buttons**: If it triggers an action on the page, it MUST be a `<button type="button">`.
- **Links**: If it navigates to a new URL, it MUST be an `<a>` with an `href`.
- **Forms**: Always wrap inputs in a `<form>` tag.
- **Modals**: Use the native `<dialog>` element, not absolute-positioned divs.
- **Toggles/Accordions**: Prefer native `<details>` and `<summary>` elements over complex custom state unless animation requirements absolutely dictate otherwise.

## 3. Tailwind Translation Protocol
When working in a Tailwind environment, you MUST map our OKLCH design tokens to the Tailwind config.
Do not fall back to default Tailwind colors (`bg-gray-500`, `text-indigo-600`) when design tokens are defined.

```js
// Required mapping structure for tailwind.config.js / tailwind.config.ts
theme: {
  colors: {
    bg: "var(--color-bg)",
    surface: {
      DEFAULT: "var(--color-surface)",
      elevated: "var(--color-surface-elevated)",
      subtle: "var(--color-surface-subtle)",
    },
    text: {
      DEFAULT: "var(--color-text)",
      muted: "var(--color-text-muted)",
      subtle: "var(--color-text-subtle)",
    },
    primary: {
      DEFAULT: "var(--color-primary)",
      hover: "var(--color-primary-hover)",
      active: "var(--color-primary-active)",
    },
    border: {
      DEFAULT: "var(--color-border)",
      strong: "var(--color-border-strong)",
    },
    success: "var(--color-success)",
    warning: "var(--color-warning)",
    error: "var(--color-error)",
    info: "var(--color-info)",
  }
}
```

## 4. The Placeholder Asset Strategy
When generating UI that requires media, never use ugly generic placeholders (e.g., `via.placeholder.com`). 
The UI must look expensive even when empty.

**For abstract structural representations:**
Use a solid block colored with `--color-surface-elevated` or `--color-surface` and place a single, perfectly centered, muted Lucide/Phosphor icon inside it to indicate the media type (e.g., `<Image />` or `<Video />`).

**For photographic placeholders:**
Use high-quality Unsplash source URLs, but apply parameters that match the project's style direction.
- *Minimal/monochrome directions*: `https://images.unsplash.com/photo-[id]?auto=format&fit=crop&w=800&q=80&grayscale=true`
- *Warm/natural directions*: Add `&tint=warm` or select nature/architecture imagery.
- *Bold/vibrant directions*: Select highly saturated, vibrant imagery.

## 5. Framework Architecture (React & Next.js)
If building for modern frameworks like Next.js App Router:
- **RSC Safety**: Global state and complex interactions work ONLY in Client Components. 
- **Interactivity Isolation**: Do not put `'use client'` at the top of a massive page file. Isolate interactive UI (buttons, heavy animations, forms) into specific leaf components with `'use client'`. Let the parent remain a static Server Component.

## 6. Performance & Rendering Guardrails
- **Z-Index Restraint**: NEVER arbitrarily spam `z-50` or `z-10` unprompted. Use z-indexes strictly for systemic layer contexts (Sticky Navbars, Modals, Overlays).
- **Noise/Grain Performance**: If applying noise/grain filters, apply them EXCLUSIVELY to fixed, `pointer-events-none` pseudo-elements covering the screen (`fixed inset-0 z-50`). NEVER apply CSS noise to scrolling containers, as this causes continuous GPU repaints and destroys mobile performance.

## 7. Component Recipes

Complete, token-based CSS recipes for common components. All use `var(--color-*)` and `var(--space-*)` tokens so they adapt to any style direction.

### Button (Primary + Secondary)

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-xs);
  padding: var(--space-sm) var(--space-md);
  font-family: var(--font-body, inherit);
  font-size: var(--text-body-sm, 0.875rem);
  font-weight: 500;
  line-height: 1;
  border-radius: 0.375rem;
  border: 1px solid transparent;
  cursor: pointer;
  transition: background-color 150ms ease, border-color 150ms ease, box-shadow 150ms ease;
  text-decoration: none;
  white-space: nowrap;
}

.btn--primary {
  background: var(--color-primary);
  color: var(--color-bg);
  border-color: var(--color-primary);
}
.btn--primary:hover {
  background: var(--color-primary-hover);
  border-color: var(--color-primary-hover);
}
.btn--primary:active {
  background: var(--color-primary-active);
}
.btn--primary:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}

.btn--secondary {
  background: transparent;
  color: var(--color-text);
  border-color: var(--color-border-strong);
}
.btn--secondary:hover {
  background: var(--color-surface-subtle);
  border-color: var(--color-text-muted);
}
.btn--secondary:active {
  background: var(--color-surface);
}
.btn--secondary:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

### Card

```css
.card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: 0.5rem;
  padding: var(--space-lg);
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}
.card__title {
  font-size: var(--text-h3, 1.25rem);
  font-weight: 600;
  line-height: 1.3;
  color: var(--color-text);
}
.card__description {
  font-size: var(--text-body, 1rem);
  line-height: 1.5;
  color: var(--color-text-muted);
}
.card__footer {
  margin-top: auto;
  padding-top: var(--space-sm);
  border-top: 1px solid var(--color-border);
}
```

### Input (with Error and Focus States)

```html
<div class="input-group">
  <label class="input-group__label" for="email">Email</label>
  <input class="input-group__field" type="email" id="email" placeholder="you@example.com" />
  <p class="input-group__error" role="alert">Please enter a valid email address</p>
</div>
```

```css
.input-group {
  display: flex;
  flex-direction: column;
  gap: var(--space-2xs);
}
.input-group__label {
  font-size: var(--text-label, 0.8125rem);
  font-weight: 500;
  color: var(--color-text);
}
.input-group__field {
  padding: var(--space-sm) var(--space-md);
  font-size: var(--text-body, 1rem);
  line-height: 1.5;
  color: var(--color-text);
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: 0.375rem;
  transition: border-color 150ms ease, box-shadow 150ms ease;
}
.input-group__field::placeholder {
  color: var(--color-text-subtle);
}
.input-group__field:focus {
  outline: none;
  border-color: var(--color-focus);
  box-shadow: 0 0 0 3px oklch(from var(--color-focus) l c h / 0.2);
}
.input-group__field[aria-invalid="true"],
.input-group--error .input-group__field {
  border-color: var(--color-error);
  box-shadow: 0 0 0 3px oklch(from var(--color-error) l c h / 0.15);
}
.input-group__error {
  font-size: var(--text-caption, 0.75rem);
  color: var(--color-error);
  display: none;
}
.input-group--error .input-group__error {
  display: block;
}
```

### Nav

```html
<header class="site-header">
  <nav class="site-nav" aria-label="Main navigation">
    <a class="site-nav__logo" href="/">Logo</a>
    <ul class="site-nav__links">
      <li><a href="/features">Features</a></li>
      <li><a href="/pricing">Pricing</a></li>
      <li><a href="/docs">Docs</a></li>
    </ul>
    <div class="site-nav__actions">
      <a class="btn btn--secondary" href="/login">Sign in</a>
      <a class="btn btn--primary" href="/signup">Get started</a>
    </div>
  </nav>
</header>
```

```css
.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  background: oklch(from var(--color-bg) l c h / 0.85);
  backdrop-filter: blur(12px) saturate(1.5);
  -webkit-backdrop-filter: blur(12px) saturate(1.5);
  border-bottom: 1px solid var(--color-border);
}
.site-nav {
  display: flex;
  align-items: center;
  gap: var(--space-lg);
  padding: var(--space-sm) var(--space-md);
  max-inline-size: var(--wide-max, 90rem);
  margin-inline: auto;
}
.site-nav__logo {
  font-weight: 700;
  font-size: var(--text-h3, 1.25rem);
  color: var(--color-text);
  text-decoration: none;
}
.site-nav__links {
  display: flex;
  gap: var(--space-md);
  list-style: none;
  margin: 0;
  padding: 0;
}
.site-nav__links a {
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: var(--text-body-sm, 0.875rem);
  transition: color 150ms ease;
}
.site-nav__links a:hover {
  color: var(--color-text);
}
.site-nav__actions {
  margin-inline-start: auto;
  display: flex;
  gap: var(--space-sm);
  align-items: center;
}
```

### Modal (Native `<dialog>`)

```html
<dialog class="modal" id="my-modal">
  <div class="modal__content">
    <h2 class="modal__title">Confirm action</h2>
    <p class="modal__body">Are you sure you want to proceed?</p>
    <div class="modal__actions">
      <button class="btn btn--secondary" data-close>Cancel</button>
      <button class="btn btn--primary">Confirm</button>
    </div>
  </div>
</dialog>
```

```css
.modal {
  border: none;
  border-radius: 0.75rem;
  padding: 0;
  max-inline-size: min(90vw, 32rem);
  background: var(--color-surface);
  color: var(--color-text);
  box-shadow: 0 25px 50px -12px oklch(0% 0 0 / 0.25);
}
.modal::backdrop {
  background: oklch(0% 0 0 / 0.5);
  backdrop-filter: blur(4px);
}
.modal__content {
  padding: var(--space-lg);
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}
.modal__title {
  font-size: var(--text-h3, 1.25rem);
  font-weight: 600;
}
.modal__body {
  color: var(--color-text-muted);
  line-height: 1.5;
}
.modal__actions {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-sm);
  padding-top: var(--space-sm);
}
```

```js
// Open/close
document.querySelector('[data-open-modal]').addEventListener('click', () => {
  document.getElementById('my-modal').showModal();
});
document.querySelectorAll('[data-close]').forEach(btn => {
  btn.addEventListener('click', () => btn.closest('dialog').close());
});
```

---

## 8. Double-Bezel Pattern

A nested container technique that creates a machined, premium double-frame effect by combining an outer subtle border with an inner distinct border. The two borders use different colors or opacities to create visible depth separation.

**Construction:**
- Outer container: `border: 1px solid` with a low-opacity border color (e.g., `oklch(from var(--color-border) l c h / 0.5)`)
- Inner container: `border: 1px solid var(--color-border)` at full opacity, with `padding` creating the visible gap between the two frames
- The gap between borders (the "bezel channel") is typically 3-6px, filled with `var(--color-bg)` or a slightly different surface tone

**When to use:**
- 1-2 focal elements per page: a featured card, hero panel, pricing highlight, or key visual container
- When the design needs premium depth without shadows or gradients
- Works especially well with DESIGN_VARIANCE 4+ and VISUAL_DENSITY 4+

**When NOT to use:**
- Never on every card in a grid — double borders everywhere become visual noise and lose the focal effect
- Never on small elements (badges, tags, inline chips) — the double frame needs breathing room
- Never combined with heavy box shadows — pick one depth technique per element

**Tailwind example:**
```html
<div class="rounded-lg border border-border/50 p-1">
  <div class="rounded-md border border-border p-6">
    <!-- content -->
  </div>
</div>
```

---

## 9. Data & Typography Content Rules

Mock data rules (the "Jane Doe" ban, the anti-emoji policy, realistic numbers, premium brand names) live in `content.md` — apply them to all placeholder content in layouts.