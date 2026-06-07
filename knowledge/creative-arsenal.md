# Creative Arsenal — Advanced UI Pattern Catalog

> **Usage:** A curated vocabulary of ambitious UI patterns agents can reference when making design decisions. Each pattern includes dial affinity tags so agents can match patterns to the project's DESIGN_VARIANCE, MOTION_INTENSITY, and VISUAL_DENSITY settings. Patterns are techniques to consider, not templates to copy wholesale.

> **Slop vs. Earned:** Every pattern here can be slop if used without purpose. The notes under each pattern explain when it's earned (adds meaning, hierarchy, or delight) vs. when it's decoration (used because it looks cool in a demo). Agents must justify pattern selection against the Creative Brief.

---

## Navigation Patterns

### Mac OS Dock
Magnification effect on hover — icons or nav items scale up near the cursor, neighbors scale proportionally. Creates a playful, tactile navigation feel.
**Dial affinity:** VARIANCE 6+ / MOTION 5+
**Earned when:** navigation items are visual (icons, thumbnails) and the product has a playful personality. **Slop when:** applied to text-only nav links or corporate/enterprise products where it reads as gimmicky.

### Magnetic Button
Button face tracks the cursor within a proximity radius, creating a gravity-pull effect before click. Subtle elastic return on mouse-out.
**Dial affinity:** VARIANCE 4+ / MOTION 5+
**Earned when:** used on 1-2 hero CTAs to add weight and intentionality to the primary action. **Slop when:** applied to every button on the page — the effect loses meaning through repetition.

### Gooey Menu
SVG filter-based menu where items blob together during open/close transitions. Organic, fluid feel that breaks the rigid rectangle paradigm.
**Dial affinity:** VARIANCE 7+ / MOTION 7+
**Earned when:** the brand personality is playful, organic, or experimental. **Slop when:** used on utility/enterprise interfaces where users need speed and predictability.

### Dynamic Island
Contextual container that morphs shape and content based on state — expanding from a pill to a panel, shifting content without a full page transition.
**Dial affinity:** VARIANCE 5+ / MOTION 6+
**Earned when:** there's a persistent status element (now playing, upload progress, notification) that benefits from spatial continuity. **Slop when:** used as a generic modal replacement with no state continuity.

### Command Palette
Keyboard-triggered search overlay (Cmd+K pattern) with fuzzy matching, categorized results, and keyboard navigation. Power-user affordance.
**Dial affinity:** VARIANCE 3+ / MOTION 3+ / DENSITY 5+
**Earned when:** the product has enough actions/pages to warrant search-based navigation. **Slop when:** the product has 4 pages and 3 actions — a simple nav suffices.

### Floating Action Menu
Radial or fan menu triggered from a single anchor point. Actions expand outward with staggered spring animations.
**Dial affinity:** VARIANCE 5+ / MOTION 5+
**Earned when:** there are 3-6 contextual actions that relate to a specific workspace area. **Slop when:** used as a dumping ground for unrelated actions or when a toolbar would be clearer.

---

## Layout Patterns

### Masonry Flow
Pinterest-style layout where items of varying heights pack into columns without row alignment. Creates organic visual rhythm from heterogeneous content.
**Dial affinity:** VARIANCE 7+ / DENSITY 5+
**Earned when:** content has genuinely variable dimensions (images, cards with varying text, mixed media). **Slop when:** all items are the same height anyway — just use a grid.

### Chroma Grid
Color-blocked grid where each cell has a distinct background color from the palette. Content overlays the color blocks. Creates a vibrant, editorial composition.
**Dial affinity:** VARIANCE 7+ / DENSITY 4+
**Earned when:** the brand palette has 4+ distinct hues and the content benefits from visual segmentation. **Slop when:** used with a monochromatic palette where the color blocks add no information.

### Curtain Reveal
Sections that slide or fold away like curtains as the user scrolls, revealing the next section beneath. Creates theatrical pacing between content blocks.
**Dial affinity:** VARIANCE 7+ / MOTION 7+
**Earned when:** the page has a narrative structure where sequential revelation adds dramatic tension. **Slop when:** used between unrelated sections where it just slows down scanning.

### Asymmetric Bento
Grid composition with intentionally unequal cell sizes — one large hero cell surrounded by smaller supporting cells. Creates immediate focal hierarchy through size contrast.
**Dial affinity:** VARIANCE 5+ / DENSITY 5+
**Earned when:** content has a clear primary item and secondary items that benefit from being shown simultaneously. **Slop when:** all content is equally important and the size disparity creates false hierarchy.

### Z-Axis Cascade
Stacked layers with slight offset and shadow creating physical depth. Content cards appear to float at different elevations, creating a 3D composition on a 2D plane.
**Dial affinity:** VARIANCE 6+ / MOTION 4+
**Earned when:** showing a stack of related items (notifications, cards, pages) where depth communicates recency or priority. **Slop when:** used purely for decoration with no semantic meaning to the layering.

### Editorial Split
Asymmetric two-column layout where one column is dramatically wider (e.g., 2fr 1fr or 3fr 1fr). The narrow column serves as a sidebar, caption rail, or annotation track.
**Dial affinity:** VARIANCE 4+ / DENSITY 4+
**Earned when:** content has a primary narrative with supporting metadata, annotations, or navigation. **Slop when:** both columns have equally important content and the asymmetry creates an awkward reading experience.

---

## Cards & Surfaces

### Parallax Tilt
Card surface tilts in 3D space tracking cursor position. Subtle light reflection shifts across the surface. Creates a physical, tactile card that rewards hover.
**Dial affinity:** VARIANCE 5+ / MOTION 5+
**Earned when:** used on 1-3 featured cards that deserve extra attention. The tilt should reveal additional depth (shine, reflection, holographic effect). **Slop when:** applied to every card in a grid — the effect becomes noise.

### Spotlight Border
Gradient border that follows the cursor around the card perimeter. Creates a flashlight-scanning effect that makes the card feel interactive and alive.
**Dial affinity:** VARIANCE 5+ / MOTION 4+
**Earned when:** cards represent interactive items (projects, tools, features) where the hover state should signal "this is explorable." **Slop when:** applied to static content cards where hover adds no functional meaning.

### Double-Bezel
Nested container with outer subtle border + inner distinct border, creating a machined/premium double-frame effect. The inner and outer borders use different colors or opacities.
**Dial affinity:** VARIANCE 4+ / DENSITY 4+
**Earned when:** used on 1-2 focal elements per page (featured card, hero panel, pricing highlight) to create premium depth. **Slop when:** applied to every card — double borders everywhere become visual noise. See also: `knowledge/component-mastery.md` Double-Bezel section.

### Holographic Foil
CSS gradient animation that shifts hue/saturation on hover or scroll, simulating the prismatic effect of holographic material. Metallic, premium, collectible feel.
**Dial affinity:** VARIANCE 7+ / MOTION 5+
**Earned when:** the product has a collectible, premium, or luxury positioning (limited editions, special features, achievement badges). **Slop when:** used on standard UI elements where it reads as over-decorated.

---

## Scroll Effects

### Sticky Stack
Sections that stick to the top of the viewport as you scroll, stacking behind the next section. Creates a card-deck effect where each section overlays the previous.
**Dial affinity:** VARIANCE 5+ / MOTION 5+
**Earned when:** sections tell a sequential story and the stacking reinforces the narrative progression. **Slop when:** sections are independent and the stacking just makes it harder to scroll back.

### Horizontal Hijack
A section that converts vertical scroll into horizontal movement, revealing a horizontal gallery or timeline within a vertical page. Scroll is returned to vertical after the section completes.
**Dial affinity:** VARIANCE 7+ / MOTION 7+
**Earned when:** content is inherently horizontal (timeline, process flow, gallery) and the hijack reveals it in context. **Slop when:** used for content that would work fine vertically — hijacking scroll for no reason frustrates users. Must include clear progress indicator and escape hatch.

### Zoom Parallax
Elements that scale up or down as the user scrolls, creating depth through differential zoom speeds. Foreground elements grow while background recedes.
**Dial affinity:** VARIANCE 6+ / MOTION 6+
**Earned when:** the page has a cinematic, immersive quality and the zoom reinforces a journey metaphor (zooming into detail, pulling back for context). **Slop when:** random elements zoom for no semantic reason.

### Scroll-Driven Reveals
Content elements that fade, slide, or scale into view as they enter the viewport. The most common scroll effect — earned through restraint and choreography, not ubiquity.
**Dial affinity:** VARIANCE 3+ / MOTION 4+
**Earned when:** reveals are staggered with intentional timing, use varied directions/effects per section, and respect `prefers-reduced-motion`. **Slop when:** every single element fades up with the same timing — this is the #1 most overused scroll effect.

### Scroll Progress
Visual indicator (bar, line, dot trail, filling shape) that shows how far through a section or page the user has scrolled. Provides spatial awareness in long content.
**Dial affinity:** VARIANCE 3+ / MOTION 3+
**Earned when:** content is long-form (articles, case studies, multi-step processes) where progress awareness improves the reading experience. **Slop when:** the page is short enough that scroll position is obvious.

---

## Gallery Patterns

### Dome Gallery
Circular or arc-arranged gallery where items curve around a central point, creating a 3D carousel effect. Items scale and blur based on distance from center.
**Dial affinity:** VARIANCE 8+ / MOTION 6+
**Earned when:** showcasing a curated collection (portfolio pieces, product shots) where the theatrical presentation matches the content quality. **Slop when:** used for a list of blog posts or feature icons.

### Coverflow
Perspective-transformed horizontal gallery where the center item faces forward and flanking items rotate away. Classic iTunes/Apple TV pattern.
**Dial affinity:** VARIANCE 6+ / MOTION 5+
**Earned when:** items are visual (album art, screenshots, product photos) and the user is browsing/selecting. **Slop when:** items are text-heavy cards where the perspective distortion makes them unreadable.

### Drag-to-Pan Gallery
Cursor-driven horizontal scrolling where the user drags to pan through a wide gallery. Momentum-based deceleration. Mobile-friendly with touch swipe.
**Dial affinity:** VARIANCE 5+ / MOTION 4+
**Earned when:** the gallery has many items and the drag interaction creates a browsing experience. **Slop when:** there are only 3-4 items — buttons or a simple carousel would be clearer.

### Accordion Slider
Full-width panels that expand on hover/click while siblings contract. Creates a dynamic allocation of space that lets users explore without page transitions.
**Dial affinity:** VARIANCE 6+ / MOTION 5+
**Earned when:** comparing 3-5 visual items (portfolio categories, product lines, before/after) where the expand/contract interaction adds discovery. **Slop when:** content within panels is text-heavy and needs stable reading width.

---

## Typography Effects

### Kinetic Marquee
Continuously scrolling text band — horizontal, angled, or curved. Speed and direction can respond to scroll velocity. Creates energy and movement in otherwise static sections.
**Dial affinity:** VARIANCE 6+ / MOTION 5+
**Earned when:** used for brand statements, client lists, or ambient texture in sections that need energy. **Slop when:** used for content that users need to actually read — marquees are for impression, not information.

### Text Mask
Text that reveals an image, video, or gradient through its letterforms. The text becomes a window into underlying content. High visual impact for hero headlines.
**Dial affinity:** VARIANCE 7+ / MOTION 4+
**Earned when:** the headline is short (2-4 words), uses a bold/heavy weight, and the masked content reinforces the message. **Slop when:** used on body text or long headlines where legibility suffers.

### Text Scramble
Characters shuffle/randomize before resolving to the final text. Creates a decoding/revealing effect that adds drama to text appearance.
**Dial affinity:** VARIANCE 6+ / MOTION 6+
**Earned when:** the brand has a tech/hacker/cipher aesthetic and the scramble reinforces the personality. **Slop when:** used on every heading — the effect loses impact through repetition. Best on 1 element per page.

### Gradient Stroke
Text with transparent fill and a gradient-colored stroke/outline. Creates a hollow, neon, or wireframe typographic effect.
**Dial affinity:** VARIANCE 7+ / MOTION 3+
**Earned when:** used as a background decorative element or on 1 oversized display heading where the stroke creates visual interest. **Slop when:** used as the primary heading treatment — stroke-only text has poor readability at body sizes.

---

## Micro-Interactions

### Particle Burst
Click or action triggers a burst of particles (confetti, sparks, dots) from the interaction point. Celebrates completion or success.
**Dial affinity:** VARIANCE 5+ / MOTION 6+
**Earned when:** marking a meaningful moment (task complete, purchase confirmed, achievement unlocked). **Slop when:** triggered on every button click — celebration fatigue kills the delight.

### Ripple Feedback
Material-design-inspired ripple that emanates from the click point on interactive surfaces. Provides immediate, physical-feeling click feedback.
**Dial affinity:** VARIANCE 3+ / MOTION 3+
**Earned when:** the interface has many clickable surfaces and needs consistent, subtle feedback. **Slop when:** the product isn't touch-focused or when used alongside other click effects that conflict.

### Mesh Gradient
Animated multi-point gradient that shifts colors smoothly, creating an organic, living background. More complex and distinctive than linear/radial gradients.
**Dial affinity:** VARIANCE 5+ / MOTION 4+
**Earned when:** used as a hero background or section accent that reinforces the brand palette. The mesh should use brand colors, not random rainbow. **Slop when:** used as a generic "make it look modern" background with no connection to the palette.

### Magnetic Cursor
Custom cursor that distorts, scales, or attracts nearby elements as it moves across the page. Creates a force-field effect that makes the entire page feel interactive.
**Dial affinity:** VARIANCE 8+ / MOTION 7+
**Earned when:** the site is a portfolio, brand experience, or creative showcase where the cursor IS part of the experience. **Slop when:** used on utility interfaces, forms, or content-heavy pages where it interferes with normal interaction.

---

## Usage Rules

1. **Match dials before suggesting.** If VARIANCE is 3, don't suggest Masonry Flow (VARIANCE 7+). The dials exist to prevent overreach.
2. **Maximum 2-3 advanced patterns per page.** Pattern overload is worse than no patterns. Pick the 1-2 that serve The Memorable Thing and leave the rest conventional.
3. **Every pattern needs a "why."** "Because it looks cool" is not sufficient. The pattern must serve hierarchy, narrative, brand personality, or user delight.
4. **Respect `prefers-reduced-motion`.** Every motion-dependent pattern must have a static fallback. Patterns with MOTION 5+ must explicitly define what happens when motion is reduced.
5. **Mobile degradation plan required.** Patterns that depend on hover, cursor tracking, or wide viewports must specify how they degrade on touch devices. If they can't degrade gracefully, they're desktop-only and the spec must say so.
6. **Don't stack patterns in the same section.** Parallax Tilt cards inside a Sticky Stack section with Text Scramble headlines = visual chaos. One advanced pattern per section maximum.
