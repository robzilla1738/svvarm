# Layout Mastery

This file defines how to structure, space, and compose interface layouts.

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
Center alignment is appropriate for discrete, self-contained elements (short hero text, isolated buttons). Left alignment provides a strong reading edge for body text and lists. Intentional asymmetry guides the eye more effectively than default centering.

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

### 4. Indiscriminate Centering

Centering long paragraphs or complex forms makes the starting edge unpredictable, reducing readability.

**Fix:** Left-align body text, form labels, and lists. Center only discrete elements like hero headlines, standalone buttons, or short metadata.

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

### 9. The Centered Hero Bias
Centering text over a generic image in the Hero section is the default fallback of uninspired design.
**Fix:** Force "Split Screen" (50/50), "Left Aligned content / Right Aligned asset", or "Asymmetric White-space" structures to create premium tension.

## Decision Rules

When building or reviewing a layout:

* Choose fluid primitives over rigid media queries.
* Choose distinct size contrast over uniform grids.
* Choose spacing for grouping over borders and lines.
* Choose alignment that supports reading flow over default centering.
* Determine component hierarchy before applying any decoration.

If the structural relationships (grouping, sequence, importance) are unclear without borders or colors, the layout is incomplete.
