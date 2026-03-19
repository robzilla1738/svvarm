# Design Gallery — Visual Excellence Reference

> **Usage:** These are not templates to copy verbatim. They demonstrate techniques and structural patterns that separate "designed" from "generated." When reviewing or building, ask: "Does this element have the intentionality shown here, or does it feel like a default?" The point is the composition, the interaction choreography, and the design decisions — not specific implementations.

---

### 1. Hero Section

**What makes this impressive:**
A full-page cinematic hero with layered depth: a dark atmospheric background image fades via radial gradient mask, ambient light rays created by rotated radial-gradient elements produce subtle volumetric lighting, and content enters through spring-physics staggered reveals (blur + y-offset). The navbar condenses on scroll — shrinking width, gaining backdrop blur and a border — creating a state-aware header that responds to context. Dual CTA treatment: primary button wrapped in a subtle border ring creating a double-border glow effect, secondary as ghost. A logo bar below uses blur + opacity reduction on group hover with a centered link that scales in — the entire grid becomes an interactive discovery moment.

**Design Anatomy:**

- **Composition strategy:** Full-viewport hero with layered z-depth — background image, gradient mask overlay, ambient light ray elements, and content layer. Content is centered with generous padding (96px+ top). The navbar sits above everything and transitions between two states based on scroll position.
- **Typography techniques:** Large headline with tight tracking serves as the visual anchor. Subtext at a comfortable reading width (max ~50ch). The size ratio between headline and body creates immediate hierarchy without needing decoration.
- **Color & surface approach:** Dark atmospheric background with subtle volumetric light effects created through rotated radial gradients at very low opacity (4-8%). The background image is masked with a radial gradient that fades to the page background color at 75%, creating depth without hard edges.
- **Interaction patterns:** Three-phase spring-physics entrance — background fades in first (1s delay), then headline + subtext blur-slide in (bounce: 0.3, 1.5s duration), then CTAs stagger with 50ms offset. Navbar transitions from wide/transparent to narrow/blurred on scroll, collapsing secondary actions. Logo bar has group-hover blur effect revealing a centered link.
- **The distinctive moves:** The volumetric light rays (rotated gradient elements at low opacity), the scroll-aware navbar that physically contracts, the logo bar as interactive moment rather than static grid, and the primary CTA's double-border glow ring.

**What separates this from the generic version:**
- **Generic:** static hero with text centered on a flat background. This: layered depth — atmospheric background image masked by radial gradient, plus rotated radial-gradient elements creating volumetric ambient light rays.
- **Generic:** content appears all at once on page load. This: three-phase spring-physics reveal — background fades in first, then headline + subtext blur-slide in, then CTAs stagger with offset. Temporal hierarchy.
- **Generic:** navbar is always the same. This: scroll-aware header that transitions from wide transparent to narrow with backdrop blur, border, and rounded corners. Secondary actions collapse on scroll.
- **Generic:** logo bar is a static grid of images. This: group-hover blur + opacity reduction on the entire grid with a centered link that scales in — the logo bar is an interactive discovery moment.
- **Generic:** single CTA button. This: primary button wrapped in a subtle border ring creating a double-border glow effect, paired with a ghost variant — weight hierarchy between actions.

---

### 2. Pricing Table

**What makes this impressive:**
A pricing system with real interactivity: monthly/yearly frequency toggle with spring-animated tab indicator, animated price transitions with interpolated digits, and four tiers with distinct visual treatments — popular gets a ring + radial gradient glow, highlighted (Enterprise) inverts to foreground/background with a grid-line overlay. Hierarchy is structural and behavioral, not just a badge.

**Design Anatomy:**

- **Composition strategy:** Four tiers in a row with three distinct visual treatments: default (clean card), popular (ring border + radial glow), and highlighted (full foreground/background color inversion with grid-line overlay). The popular tier gets subtle lift through ring treatment, while the highlighted tier commands attention through complete visual inversion.
- **Typography techniques:** Price numbers are the dominant element — large, weighted, and animated during toggle transitions. Tier names are secondary. Feature lists use consistent, scannable sizing. The price animation (interpolated digit transitions) adds perceived quality.
- **Color & surface approach:** Default cards are neutral surface. Popular card adds a primary-color ring with a radial gradient glow behind it. Highlighted card inverts the entire color scheme (foreground becomes background) and overlays a CSS grid-line pattern masked with a radial gradient for texture and depth without images.
- **Interaction patterns:** Spring-physics tab indicator animates between monthly/yearly positions using layout animation. Price digits interpolate between values rather than snapping. CTAs adapt their variant to match the card's visual context (inverted card gets inverted button).
- **The distinctive moves:** Three-tier visual hierarchy (default / ring+glow / full inversion), the grid-line texture overlay on the highlighted card, animated digit transitions on prices, and context-aware CTA variants that adapt to their card's color scheme.

**What separates this from the generic version:**
- **Generic:** three identical cards with a "Most Popular" text badge. This: four tiers with three distinct visual treatments — default, popular (ring + radial glow), and highlighted (full foreground/background inversion with grid-line overlay). Hierarchy is compounded, not single-signal.
- **Generic:** static price text that snaps between monthly/yearly. This: animated numeric transitions with interpolated digits, and a spring-physics tab indicator makes the frequency toggle feel physical.
- **Generic:** all buttons identical. This: highlighted tier gets an inverted variant (matching inverted context), others get default — the CTA adapts to its card's visual context rather than being uniform.
- **Generic:** no background texture or depth. This: highlighted card gets a CSS grid-line overlay masked with a radial gradient; popular card gets a subtle radial glow. Texture creates depth without images.

---

### 3. Feature Block (Bento Grid)

**What makes this impressive:**
A composable bento grid where each card claims its own grid territory via explicit row/column spans, creating an asymmetric layout where one card spans 3 rows while others share 2-row and 1-row slots. Each card has layered interactivity: a background slot for imagery/effects, icon that scales down on hover while the content slides up, revealing a hidden CTA that translates from beneath with opacity fade. Dual-theme shadow treatment — light uses layered rgba shadows for depth, dark uses an inset white glow.

**Design Anatomy:**

- **Composition strategy:** Explicit grid coordinate placement rather than auto-flow — each card occupies specific rows and columns, creating an asymmetric mosaic. One card dominates by spanning 3 rows. The grid breaks the "equal cards" pattern by giving different content different visual weight based on importance.
- **Typography techniques:** Card titles and descriptions are sized for scanning. The hidden CTA text only appears on hover, creating a clean resting state. Icon scales down on hover to make room for the revealed content — the typography hierarchy shifts during interaction.
- **Color & surface approach:** Layered box-shadows create physical depth — light mode uses multiple rgba shadows (hairline for definition + medium for lift + large for depth), dark mode inverts to an inset white glow. Each card can carry its own background visual (image, gradient, effect) positioned absolutely behind content.
- **Interaction patterns:** Three-layer hover choreography — icon scales to 75%, content slides up, and a hidden CTA fades in from below, all at 300ms with GPU-accelerated transforms. A transparent overlay creates a subtle scrim that's theme-aware (different opacity for light and dark).
- **The distinctive moves:** The asymmetric grid territory claiming, the three-layer hover choreography (scale + slide + reveal), theme-aware shadow inversion (layered shadows in light, inset glow in dark), and the background slot system allowing per-card visual customization.

**What separates this from the generic version:**
- **Generic:** three identical cards at equal widths. This: each card claims specific grid coordinates creating an asymmetric mosaic where one card spans 3 rows while others share 1-2 row slots.
- **Generic:** static cards with no interaction. This: three-layer hover choreography — icon scales down, content slides up, and a hidden CTA fades in from below, all at 300ms with GPU-accelerated transforms.
- **Generic:** flat cards with a single border. This: layered box-shadow (hairline for definition + medium for lift + large for depth) in light mode, inverted to an inset white glow in dark mode — the card feels physically different per theme.
- **Generic:** background is a solid color. This: a background slot lets each card carry its own visual — images, gradients, or effects — positioned absolutely behind content.
- **Generic:** hover darkens the whole card. This: a transparent overlay creates a subtle scrim that's theme-aware with different opacities for light and dark modes.

---

### 4. Testimonials (Auto-Scrolling Columns)

**What makes this impressive:**
Three columns of testimonial cards auto-scroll vertically at different speeds (15s, 19s, 17s) using infinite translateY loops, creating a living, breathing social proof wall. A CSS mask with linear gradient fades the top and bottom edges, removing hard boundaries and creating the illusion of infinite content. Columns progressively reveal on smaller screens, and the section header animates in with spring physics when scrolled into view.

**Design Anatomy:**

- **Composition strategy:** Three columns scrolling at deliberately different speeds (15s, 19s, 17s) — the staggered rates prevent synchronization and create organic, living motion. The content is doubled to create a seamless infinite loop (translated by -50%). Progressive column reveal: 1 column on mobile, 2 on medium, 3 on large.
- **Typography techniques:** Testimonial cards use a consistent quote + author + role structure. The section header uses a larger display size with spring-physics entrance animation. Author names are weighted differently from quote text to create scannable attribution.
- **Color & surface approach:** CSS mask with linear gradient creates fade zones at 25% from top and 25% from bottom — testimonials emerge from and dissolve into the background rather than having hard edges. Cards use surface color with subtle borders.
- **Interaction patterns:** Auto-scrolling with different column speeds creates ambient motion. Section header uses whileInView animation with custom cubic-bezier easing and fires only once. The scrolling animation is continuous and infinite with no user interaction needed.
- **The distinctive moves:** The staggered scroll speeds preventing column synchronization, the CSS mask creating fade-in/fade-out edges for an infinite-scroll illusion, progressive column density scaling with viewport, and the seamless content loop via 50% translation on doubled content.

**What separates this from the generic version:**
- **Generic:** static grid of 3 quote cards. This: three columns auto-scrolling at different speeds (15s, 19s, 17s) — the staggered rates prevent synchronization and create organic, living motion.
- **Generic:** testimonials have hard edges at top and bottom. This: CSS mask with linear gradient fades both edges, creating an infinite-scroll illusion.
- **Generic:** all columns visible on mobile creating a wall of text. This: progressive reveal — 1 column on mobile, 2 on medium, 3 on large — the density scales with the viewport.
- **Generic:** section header appears instantly. This: whileInView animation with custom cubic-bezier easing that fires only once — the header slides in when scrolled to.
- **Generic:** duplicate content loop is visible. This: translateY -50% on a doubled array creates a seamless infinite loop — the seam is invisible.

---

### 5. Navigation Bar (Mega Menu)

**What makes this impressive:**
A full navigation system with two distinct responsive modes: desktop uses an accessible menu component with animated dropdown panels (directional slide-in/fade-in), while mobile uses a slide-in drawer with accordion for nested items. Dropdown items include icon + title + description layouts. The mobile drawer includes extra links in a 2-column grid and auth buttons — a complete navigation experience, not a hamburger afterthought.

**Design Anatomy:**

- **Composition strategy:** Two completely different navigation experiences for desktop and mobile — not one collapsed into the other. Desktop: horizontal nav with animated dropdown panels. Mobile: full sheet drawer with accordion structure, 2-column extra links grid, and auth buttons. Data-driven structure distinguishes between leaf items (plain links) and branch items (trigger + content panel).
- **Typography techniques:** Dropdown items use a three-level hierarchy: icon (visual anchor), title (scannable), and description (detail on demand). Navigation link text uses subtle color with hover transitions. The mobile accordion uses clear section headers with expandable content.
- **Color & surface approach:** Dropdown panels use elevated surface color with subtle borders. Link hover states use background color change. The mobile drawer uses standard sheet styling with backdrop. Active/current states are indicated through color rather than decoration.
- **Interaction patterns:** Desktop dropdowns slide in directionally based on which item was previously open (motion direction awareness). Mobile uses sheet (slide-in drawer) with accordion for nested items. Hover states use background transition. The navigation distinguishes between items that navigate and items that expand.
- **The distinctive moves:** Direction-aware dropdown animations (sliding based on previous active item), the complete mobile navigation experience (drawer + accordion + extra links grid + auth), icon + title + description layouts inside dropdowns for information density, and data-driven structure that distinguishes leaf from branch items.

**What separates this from the generic version:**
- **Generic:** hamburger menu that shows the same links in a list. This: mobile gets a full slide-in drawer with accordion for nested items, a 2-column extra links grid, and auth buttons — a complete app-quality mobile nav, not a collapsed desktop nav.
- **Generic:** dropdown is a plain list that appears/disappears. This: dropdowns slide in directionally based on which item was previously open — motion-aware animations.
- **Generic:** dropdown items are just text links. This: icon + title + description layout per item, creating scannable information density inside the dropdown.
- **Generic:** all menu items treated identically. This: the component distinguishes between leaf items (plain links with hover background) and branch items (trigger + content panel) via data-driven structure.

---

### 6. Metric Card (Spotlight Effect)

**What makes this impressive:**
A card that tracks your mouse cursor in real-time, creating a radial spotlight effect via dynamic mask positioning that follows the pointer. On hover, the spotlight reveals an animated canvas effect — procedural dot matrices rendered via GPU shaders with configurable colors, opacities, and animation speeds. The card starts as a simple dark container and transforms into a living, breathing interactive surface on hover. GPU-accelerated, 60fps-capped.

**Design Anatomy:**

- **Composition strategy:** A metric display card with a large dominant number, label, and supporting text. The card's visual interest comes entirely from its interaction behavior rather than static decoration — the resting state is deliberately minimal (dark surface, simple content) so the hover reveal creates contrast.
- **Typography techniques:** The metric number is the dominant element — oversized relative to everything else on the card. Label and description are subdued. The typography is clean enough that the interactive effects don't compete with readability.
- **Color & surface approach:** Dark surface at rest with subtle border. On hover, a radial gradient mask reveals a procedural animated texture (dot matrices) beneath the surface. The shader accepts configurable color arrays that blend at the GPU level — the color mixing is more nuanced than CSS blending.
- **Interaction patterns:** Real-time cursor tracking creates a spotlight that follows the mouse at native frame rate. The spotlight mask reveals a canvas-rendered animated texture. The effect is GPU-accelerated with frame capping for smooth performance. The reveal is radial and centered on cursor position at all times.
- **The distinctive moves:** The cursor-tracking spotlight mask, the GPU-accelerated procedural texture reveal (never the same twice), the transformation from minimal resting state to living interactive surface, and the physical relationship between user cursor position and interface response.

**What separates this from the generic version:**
- **Generic:** static card with a border and background. This: real-time cursor tracking — the spotlight follows your mouse at native frame rate, creating a physical relationship between user and interface.
- **Generic:** hover state is a background color change. This: a radial gradient mask reveals an animated procedural texture — dot matrices rendered via GPU shaders, creating a texture that's never the same twice.
- **Generic:** decorative effects are CSS-only. This: GPU-accelerated rendering composited via absolute positioning — real procedural rendering inside a 2D card, at 60fps with frame capping.
- **Generic:** spotlight is a static gradient overlay. This: dynamically interpolated mask position so the reveal circle is always centered on the cursor.

---

### 7. CTA / Page Closer (Calendar Bento)

**What makes this impressive:**
A CTA that earns attention by being useful — it renders a live calendar of the current month with dynamically highlighted days, wrapped in a bento card with layered interaction. The card has a hover gradient that fades in, a floating arrow icon that rotates and translates up on hover, and a double-border calendar widget (outer border that transitions color on hover, inner border with inset box-shadow). The CTA is a booking link — it converts by offering value, not by shouting.

**Design Anatomy:**

- **Composition strategy:** The CTA section breaks convention by embedding a functional calendar widget instead of the typical "Ready to get started?" + button pattern. The bento card layout creates visual distinction from the rest of the page — it looks like an embedded app, not a page section. The calendar shows the current month with highlighted available days.
- **Typography techniques:** Calendar day numbers use tabular figures for alignment. The CTA headline sits above or beside the calendar, not drowning in whitespace. Day labels and numbers create a dense but legible micro-typography grid.
- **Color & surface approach:** Double-border treatment on the calendar — outer rounded border with color transition on hover (neutral to accent), inner border with inset box-shadow creating physical depth. The hover gradient (directional, from accent color at low opacity) fades in from one corner.
- **Interaction patterns:** Four layered hover effects — gradient overlay fades in, calendar border transitions to accent color, floating arrow icon rotates (6deg to 0deg) and translates up, and the card background shifts subtly. Each layer compounds to create a rich hover experience. Smart link routing detects internal vs external URLs.
- **The distinctive moves:** The CTA as functional calendar widget (offering value, not asking for a click), the four-layer compound hover effect, the double-border calendar creating physical depth, and the compositional surprise of an embedded-app-looking widget in a landing page context.

**What separates this from the generic version:**
- **Generic:** "Ready to start building?" heading with a centered button. This: a live calendar rendering the current month with highlighted available days — the CTA offers value (booking) instead of just asking for a click.
- **Generic:** static card with no hover response. This: four layered hover effects — gradient overlay fades in, calendar border transitions to accent color, floating arrow icon rotates and translates up, and the card background shifts — each layer compounds.
- **Generic:** single border treatment. This: double-border calendar — outer rounded border with theme transition, inner border with inset box-shadow — creating physical depth without elevation.
- **Generic:** CTA is the same visual language as the rest of the page. This: the calendar widget is visually distinct — it looks like an embedded app, not a section of the landing page. Compositional surprise.

---

## Cross-Cutting Principles

These six patterns recur across every entry above. When building or auditing, check that each section demonstrates at least 3 of 6:

1. **Typographic drama through size contrast, not decoration.** A 5:1 heading-to-body ratio does more work than gradients, shadows, or ornamental elements. Let the scale system carry the hierarchy. Decoration is a crutch when the type isn't doing its job.

2. **Structural hierarchy through scale and weight, not badges or labels.** The featured pricing card is physically larger. The dominant feature block spans more rows. The metric number is 4x the label. When you need a "Most Popular" badge to communicate hierarchy, the structure has failed.

3. **Negative space as a design element, not laziness.** 120px+ hero padding isn't empty — it's a decision. The narrow 50ch CTA measure isn't sparse — it's focused. Every generous gap says "we're confident enough to let this breathe."

4. **Coordinated multi-property transitions, not single-property.** Hover states shift background + transform together. The navbar link reveals a scaleX underline while shifting color. Single-property transitions feel mechanical. Multi-property transitions feel physical.

5. **Compositional variety across sections, not uniform grids.** Hero is full-width. Features are asymmetric bento. Testimonial is narrow editorial. CTA is contrast-background closer. When every section uses the same 3-column grid, the page has layout but no composition.

6. **One element per group earns disproportionate visual weight.** One pricing card is bigger. One feature block dominates. One number per card is oversized. This creates a natural reading order and prevents the eye from stalling at a grid of equals. Equal treatment is not equitable design — it's indecision.
