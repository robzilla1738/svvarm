# The Anti-Slop Bible

## Why AI Design Converges

AI models trained on web design data converge on statistical averages. The most common patterns in training data get the highest generation probability. Purple gradients dominate SaaS marketing pages. Card grids are the safest layout. Inter is on every fourth website. The result: every AI output looks like every other AI output.

This is not a flaw in AI. It is mathematics. And the fix is not to avoid common patterns entirely — it is to make INTENTIONAL choices that reflect a specific project's identity, not the average of all projects.

This document catalogs 38 known AI design convergence patterns across 6 categories. For each: what it looks like, why AI gravitates toward it, how to detect it, and exactly what to do instead.

---

## Category 1: Color Slop

**Pattern 1: Purple-to-Blue Gradients**

The number one AI tell in existence. `background: linear-gradient(135deg, #667eea, #764ba2)` or close variants on hero sections, buttons, and card backgrounds. This is the "Purple Paradox": Tailwind ships indigo-500 (#6366f1) as a default, tutorial authors use it, tutorials enter training data, AI generates more purple, which creates more tutorials. The loop reinforces itself.

- **What it looks like:** Any gradient using hues between 220-290 (blue through purple). Almost always at 135deg. Common hex pairs: #667eea/#764ba2, #6366f1/#8b5cf6, #4f46e5/#7c3aed.
- **Why AI does it:** Purple-to-blue gradients dominate SaaS landing pages in training data. Stripe's old gradients, Product Hunt launches, and Dribbble shots all reinforce this as the "default impressive" color.
- **How to detect:** Search for `linear-gradient` with hues in the 220-290 range. Check hero sections and primary CTAs first.
- **Fix:** Use a gradient derived from the brand's actual palette, or use no gradient at all. A single flat brand color with intentional contrast is more distinctive. If you must gradient, go unexpected: warm tones (coral #FF6B6B to amber #F59E0B), earth tones (sage #87A878 to cream #F5F0E8), or monochromatic (dark navy #0F172A to medium navy #1E3A5F).

**Pattern 2: Cyan-on-Dark / Neon-on-Dark**

Electric cyan (#00FFFF, #00D4FF, #00BCD4) as the primary accent on near-black (#0A0A0A, #0F0F0F, #111111). Headlines in cyan, buttons in cyan, glowing borders in cyan. Extends to any neon accent: neon green (#39FF14), hot pink (#FF006E), electric violet (#8B5CF6). Every blockchain site, AI tool, and dev product converges here.

- **What it looks like:** Accent color with saturation > 85% and lightness > 55% on a background with lightness < 15%. The design looks like a sci-fi movie poster.
- **Why AI does it:** "Modern dark UI" examples — crypto dashboards, developer tools, futuristic concept designs — flood training data with this combination.
- **How to detect:** Check if the primary accent hue falls in the 160-200 range on a near-black background. Count how many elements use the neon accent. If more than three element types share it, the design has converged.
- **Fix:** Warm accents on dark backgrounds feel far more distinctive: amber (#D97706), coral (#F87171), soft gold (#EAB308). Or use muted, desaturated alternatives: slate blue (#64748B), dusty rose (#BE8C8C), sage green (#6B8A6B). Reduce saturation by 20-30% from any neon value.

**Pattern 3: Pure Black (#000) and Pure White (#FFF)**

Maximum contrast does not equal good design. Pure black on pure white produces a 21:1 contrast ratio — far beyond the 4.5:1 WCAG requirement — and causes visual fatigue on extended reading. Real objects never have pure black shadows or pure white highlights.

- **What it looks like:** `color: #000000` on `background: #FFFFFF`. Harsh, sterile, digital-feeling pages.
- **Why AI does it:** Simplest values, most common in minimal code examples.
- **How to detect:** Search for `#000`, `#fff`, `rgb(0,0,0)`, `rgb(255,255,255)` in color and background properties.
- **Fix:** Near-black (#0A0A0A, #111111, #18181B) and near-white (#FAFAFA, #F8F8F8, #FEFEFE). Better yet, tint both with the brand hue: navy-tinted black (#0C1220) with warm white (#FAF8F5) feels immediately considered.

**Pattern 4: Gray Text on Colored Backgrounds**

Medium gray (#6B7280, #9CA3AF) text placed on a colored background. The gray absorbs into the color underneath and looks "blurry" or washed out. The text becomes difficult to read without the reader understanding why.

- **What it looks like:** `color: #6B7280` on a blue, green, or purple background. Text that looks unfocused.
- **Why AI does it:** It applies "muted text" styling uniformly, regardless of the background color beneath it. Gray works fine on white; it fails on color.
- **How to detect:** Check any text on a non-white/non-black background. If the text is a neutral gray rather than a shade derived from the background, it will look wrong.
- **Fix:** Use a darker shade of the background color for text (e.g., dark navy text on light blue), or use white/near-white text with sufficient contrast. Alternatively, use `rgba(0,0,0,0.7)` or `rgba(255,255,255,0.85)` which naturally adapts to the underlying color.

**Pattern 5: Gradient Text for Impact**

`background: linear-gradient(...); -webkit-background-clip: text; -webkit-text-fill-color: transparent;` on hero headings. Almost always purple-to-pink or blue-to-cyan. Used decoratively to signal "this heading is important."

- **What it looks like:** A shimmer-effect heading, usually the hero H1. The gradient is always in the blue-purple spectrum.
- **Why AI does it:** Gradient text is heavily represented in "hero section" training examples. It has become shorthand for visual importance.
- **How to detect:** Search for `background-clip: text` or `text-fill-color: transparent`. If the hero headline has a gradient, flag it.
- **Fix:** A well-chosen font at a well-chosen weight communicates importance without tricks. Use a single solid color. If you need punch, use a distinctive typeface, dramatic size (72px+), or strategic weight variation within the heading (mixing 300 and 700 weights).

**Pattern 6: Glassmorphism Everywhere**

`backdrop-filter: blur(10px)` with semi-transparent backgrounds (`bg-white/10`, `bg-white/5`) and glowing borders (`border border-white/20`) applied to cards, nav bars, modals, and every surface. The entire UI looks like frosted glass floating over a gradient. Creates "visual mush" where no element has clear boundaries.

- **What it looks like:** Multiple frosted-glass panels layered over a gradient or image background. Everything slightly transparent, nothing fully opaque.
- **Why AI does it:** Glassmorphism dominated design trends 2021-2023 and is overrepresented in Dribbble/Behance showcase work.
- **How to detect:** Search for `backdrop-filter`, `backdrop-blur`, or opacity modifiers like `/10`, `/20`, `/30` on backgrounds. If more than two elements use glass effects, it is overuse.
- **Fix:** Use glassmorphism as a single accent — one floating element (like a nav bar) with blur while everything else is opaque. Better yet, skip it. Solid backgrounds with good color choices are more readable, more performant (blur is computationally expensive), and more distinctive.

**Pattern 7: Default Dark Mode with Glowing Accents**

The entire site defaults to dark mode with no light mode consideration. Background is #0F0F0F to #1A1A2E. Cards float on slightly lighter dark surfaces. Neon box-shadows (`box-shadow: 0 0 20px rgba(99,102,241,0.3)`), text-shadows, and border glows everywhere. Avoids actual design decisions by hiding behind darkness.

- **What it looks like:** Dark background, dark cards with subtle elevation, neon accent glows on interactive elements. The "tech startup" default.
- **Why AI does it:** Dark mode "looks impressive" in screenshots and dominates portfolio/showcase sites in training data. Glowing accents add perceived sophistication cheaply.
- **How to detect:** Check if dark mode was requested or if AI just chose it. Look for `background-color` values below #222. Check for `box-shadow` or `text-shadow` with colored, semi-transparent values.
- **Fix:** If dark mode is right for the brand, make it intentional. Define specific dark surface tiers (background: #09090B, surface-1: #18181B, surface-2: #27272A). Use desaturated accents instead of neon. Consider Stripe's approach: dark sections used strategically within a light page.

**Pattern 8: Tailwind Default Colors Unmodified**

`indigo-500` (#6366F1) buttons, `gray-100` (#F3F4F6) backgrounds, `blue-500` (#3B82F6) links, `emerald-500` (#10B981) success states — all straight from Tailwind's default palette with zero customization. Instantly recognizable as "no design thought applied."

- **What it looks like:** A page that uses exclusively Tailwind's default color names without a custom theme. Every color is a Tailwind preset.
- **Why AI does it:** AI generates Tailwind classes and picks the most statistically common ones. The defaults are the highest-probability outputs.
- **How to detect:** Compare hex values against Tailwind defaults. Key suspects: #3B82F6 (blue-500), #8B5CF6 (violet-500), #6366F1 (indigo-500), #10B981 (emerald-500), #EF4444 (red-500), #F59E0B (amber-500).
- **Fix:** Always define a custom color palette in `tailwind.config`. Start from brand colors and generate a full scale. Use tools like Tailwind's color generator, Huetone, or ColorBox to build a palette with the same utility-class ergonomics but unique identity.

---

## Category 2: Typography Slop

**Pattern 9: Inter/Roboto/Open Sans as Only Font**

The "visual monoculture." Inter is the default in Figma, most component libraries, and a majority of modern web projects. Every AI SaaS page looks identical because they all use Inter at the same weights. It is a fine font — choosing it is like choosing beige paint.

- **What it looks like:** `font-family: 'Inter', sans-serif` as the sole typeface. No display font for headings, no character in the typography.
- **Why AI does it:** Inter appears in the majority of modern web projects in training data. It is the highest-probability font output.
- **How to detect:** Check `font-family` declarations. If Inter, Roboto, or Open Sans is the only typeface with no display or heading font paired alongside, flag it.
- **Fix:** Pair a distinctive display typeface with a neutral body font. Under-used alternatives: Satoshi (geometric, modern), Instrument Sans (friendly, distinctive), General Sans (Inter-adjacent but less common), Space Grotesk (technical but warm), Clash Display (headings). Or use a serif — Fraunces, Newsreader, Source Serif — which instantly differentiates because AI almost never suggests serifs.

**Pattern 10: Monospace for Non-Technical Contexts**

JetBrains Mono, Fira Code, or `monospace` applied to headings, navigation links, buttons, or body text that is not code. The "hacker aesthetic" applied to products that have nothing to do with code.

- **What it looks like:** Navigation links in monospace. Hero text in monospace. Button labels in monospace. Card headings in monospace. None of it is actual code.
- **Why AI does it:** Developer-tool and "hacker aesthetic" designs are heavily represented in modern web training data. Monospace is the quickest shorthand for "technical."
- **How to detect:** Check if monospace fonts are used outside of actual code blocks, terminal output, or data displays. Monospace nav links are the biggest red flag.
- **Fix:** If the brand has a technical identity, use monospace sparingly — for labels, metadata, or small supporting text only. Headlines should use a proper display face. Ask: is the product actually technical, or does it just want to appear technical?

**Pattern 11: Large Rounded Icons Above Every Heading**

Every feature section has a row of cards, each with a large (48-64px) Lucide, Heroicons, or Phosphor icon in a colored circle (`rounded-full bg-indigo-100 p-3`) sitting above a heading and description. Mechanical predictability.

- **What it looks like:** Repeated icon-above-heading pattern with all icons the same size, same colored circle background, same spacing. Three to six instances in a row.
- **Why AI does it:** "Icon + heading + description" is the most common feature-section pattern in training data. It is the safest, most-generated layout for feature sections.
- **How to detect:** Look for repeated card structures where each card leads with an icon in a `rounded-full` container with a light tinted background. Check if all icons are identical in size and treatment.
- **Fix:** Consider whether icons add genuine information. Often a well-written heading is enough. If icons add value, break the pattern: use them inline with text, vary sizes by importance, use custom illustrations, or place them left of text instead of above.

**Pattern 12: Weak Type Hierarchy**

Body text at 16px, subheadings at 18px, headings at 20-24px. Everything feels the same importance because the size scale is too compressed. Insufficient weight contrast — headings at 600, body at 400, not enough difference.

- **What it looks like:** A page where you cannot tell at a glance which text is most important. Sizes are too close together (14/15/16 muddy). Multiple heading levels share the same font-weight.
- **Why AI does it:** AI tends toward "safe" sizing that does not make anything too big or too small. Moderate values are the highest-probability outputs.
- **How to detect:** Measure the ratio between the largest heading and body text. If the ratio is less than 2:1, hierarchy is too flat. Check if more than two heading levels share the same weight.
- **Fix:** Establish a dramatic type scale. Body at 16-18px, H3 at 24-28px, H2 at 36-42px, H1 at 48-72px. Use weight variation aggressively: 300 for supporting text, 400 for body, 600 for subheadings, 700-800 for headings. The difference between levels should be obvious at a glance.

**Pattern 13: Multiple Competing Fonts Without Clear Relationships**

Inter for body, a system serif for headings, JetBrains Mono for "technical" elements, maybe a fourth for accents. No clear reason for each choice, no consistent pairing logic. Typographic cacophony.

- **What it looks like:** Three or more font families on a single page with no apparent system governing which is used where. Fonts that clash in personality (geometric sans + old-style serif + humanist mono).
- **Why AI does it:** Each element type gets a font assigned independently based on what is most common for that element type, without considering the page as a whole.
- **How to detect:** Count distinct font families. If there are more than two, check whether each has a clear, consistent role. If fonts appear to be assigned randomly, flag it.
- **Fix:** One well-chosen family for everything, or a deliberate pairing of exactly two fonts with clear hierarchy rules (e.g., Clash Display for headings at 700 weight, Satoshi for body at 400 weight, nothing else).

---

## Category 3: Layout Slop

**Pattern 14: Cookie-Cutter Hero Section**

Centered text with a large heading, a lighter subtitle paragraph below it, one filled CTA button + one outlined CTA button, all on a gradient or dark background. Sometimes a faint grid or dot pattern behind it. Heading reads "The future of [X] is here" or "Unlock the power of [Y]."

- **What it looks like:** `text-center`, heading > 48px, subtitle in `text-gray-400`, two buttons (`bg-indigo-500` + `border border-indigo-500`), gradient or dot-pattern background.
- **Why AI does it:** This is the single most generated layout in existence. Hero sections across the web have converged on this exact formula, and it is the highest-probability hero output.
- **How to detect:** Check: centered text? Large heading? Muted subtitle? Exactly two buttons (primary + secondary)? Decorative background? If it hits 4/5, it is the template.
- **Fix:** Break at least two conventions. Left-align the text. Use a single CTA. Replace the subtitle with something unexpected (a testimonial, a code snippet, a metric). Use a real product screenshot instead of abstract decoration. Start with the product UI itself as the hero.

**Pattern 15: Identical Card Grids**

Three or four cards in a row, each with identical dimensions: icon at top, heading in the middle, description at bottom. Equal padding (`p-6`), equal gaps (`gap-6`), equal border-radius (`rounded-xl`). Content is interchangeable.

- **What it looks like:** A `grid grid-cols-3 gap-6` where every child has the same structure. The only difference between cards is the text content.
- **Why AI does it:** "Icon + heading + description" is the most common card pattern. Three columns is the default grid.
- **How to detect:** Count repeated card elements with identical structure. If 3+ cards share the exact same layout with only content swapped, flag it. Check if the grid is always 3 columns.
- **Fix:** Vary card sizes based on content importance (one large feature card, two smaller supporting ones). Use masonry or asymmetric layouts. Mix content types within the grid (one with an image, one with a metric, one with a quote). Or abandon cards entirely — a list with good typography can be more effective.

**Pattern 16: Hero Metric Template**

A section with 3-4 large numbers ("10K+ Users", "99.9% Uptime", "50M+ Requests") in a row with small labels underneath. Always with plus signs and percentage symbols. `text-4xl font-bold` numbers with `text-sm text-gray-500` labels.

- **What it looks like:** A flex or grid row of 3-4 identical stat blocks. Each has a large bold number and a small muted label. Sometimes with a colored accent line above.
- **Why AI does it:** "Social proof metrics" sections appear in the vast majority of SaaS landing pages in training data.
- **How to detect:** Look for repeating `<div>` elements each containing a large-font number and small-font label. If the numbers include "+", "K", "M", or "%", it is this pattern.
- **Fix:** If metrics matter, present them with context: a chart, a comparison, a timeline, a before/after. If they are vanity metrics, cut them entirely. A single compelling metric with context ("We processed $2.1B in payments last quarter") is more credible than four generic big numbers.

**Pattern 17: Everything Centered**

Every section uses `text-center` and `mx-auto`. Hero centered, features centered, CTA centered, footer centered. The entire page is a vertical stack of centered blocks with no lateral movement.

- **What it looks like:** Scroll through the page and everything sits in the middle. No content extends to the edges, no asymmetry, no variation in alignment.
- **Why AI does it:** Centered layouts are "safe" — they work at any viewport width and rarely look broken. Centering is the lowest-risk alignment choice.
- **How to detect:** Check text alignment across sections. If more than 70% of sections use centered text, flag it.
- **Fix:** Page containers and sections should remain centered — that is standard page structure, not slop. The fix is to left-align body text *within* those centered containers (more readable for paragraphs longer than two lines). Create rhythm by alternating between full-width, contained, and offset sections. Asymmetric layouts are an accent, not the default.

**Pattern 18: Cards Inside Cards (Cardocalypse)**

A dashboard section that is a card, containing metric cards, containing icon cards. Four to five levels of nested containers, each adding another border, another shadow, another layer of padding. Visual matryoshka doll.

- **What it looks like:** Elements with `rounded-lg shadow` that are children of other elements with `rounded-lg shadow`, which are children of further `rounded-lg shadow` elements. Borders stacking on borders.
- **Why AI does it:** Each component gets its own container treatment independently. The model does not reason about the total nesting depth.
- **How to detect:** Count nesting levels of bordered/shadowed containers. More than two levels of visible "card-ness" is always wrong.
- **Fix:** Flatten the hierarchy. The outermost container gets the visual treatment. Inner elements use spacing, subtle background tints, or thin dividers for separation. Only one level of card-ness should be visible at any time.

**Pattern 19: Same Spacing Everywhere**

Every gap is `gap-4` or `gap-6`. Section padding is always `py-16`. Card padding is always `p-6`. There is one spacing value applied everywhere. No rhythm.

- **What it looks like:** Uniform whitespace with no variation. Related elements have the same distance as unrelated elements. Nothing feels grouped; nothing feels separated.
- **Why AI does it:** Varying spacing requires understanding content relationships. AI picks the most common spacing value and applies it uniformly.
- **How to detect:** Check if more than 3 element types share identical padding/gap values. Measure section spacing — if every section has identical vertical padding, it is uniform slop.
- **Fix:** Use spacing to communicate hierarchy. Major section breaks: 80-120px. Content groups: 32-48px. Items within a group: 12-24px. The variation should communicate what belongs together and what is separate without visual dividers.

**Pattern 20: Formulaic Section Sequence**

Hero, then logo wall, then feature grid, then testimonials, then pricing table, then FAQ accordion, then CTA section, then footer. Every SaaS landing page, regardless of what the product does or who the audience is.

- **What it looks like:** The same seven sections in the same order on every generated page. No section feels like it was chosen because the content demanded it.
- **Why AI does it:** This sequence is the statistical average of all SaaS landing pages in training data. It is the highest-probability page structure.
- **How to detect:** Count how many of these sections appear in order: hero, logos, features, testimonials, pricing, FAQ, footer. If 5+ match the canonical order, the page architecture is formulaic.
- **Fix:** Start with the content. What does this specific audience need to know, in what order, to make their decision? A developer tool might lead with a code example. A creative tool might lead with a gallery. A B2B tool might lead with a case study. Let the content dictate the architecture.

**Pattern 21: Thick Colored Borders on Rounded Cards**

Cards with `border-2 border-indigo-500 rounded-xl` or `border-l-4 border-purple-500 rounded-lg`. High-saturation 2-4px borders at 12-16px radius competing with the content inside for attention.

- **What it looks like:** Cards where the border is one of the most visually prominent elements. Colored left borders, top borders, or full borders on every card in a section.
- **Why AI does it:** It is the simplest way to add "personality" to a card without changing the layout. Appears in countless dashboard and notification component examples.
- **How to detect:** Search for `border-l-4`, `border-t-4`, `border-2` with accent colors paired with large border-radius values. Check if multiple cards use this as their primary visual differentiation.
- **Fix:** If the border communicates meaning (status: green for success, red for error), keep it as part of a clear system. If decorative, remove it. Differentiate cards through content, typography, or layout variation. Use subtle borders (`border border-gray-200`) or no borders, letting spacing define groups.

---

## Category 4: Visual Detail Slop

**Pattern 22: Floating Orbs / Particles / Pulsing Glows**

Background decorations with sinusoidal movement, uniform velocity, and no relationship to content. Blurred gradient circles (`blur-3xl opacity-20`) floating behind the hero. Particle systems with dots drifting at constant speed. Pulsing glow animations on loop.

- **What it looks like:** `position: absolute` elements with large `blur()` values, animated with `translateY(20px)` at `animation: float 6s ease-in-out infinite`. Purple and blue gradient orbs are most common.
- **Why AI does it:** "Background decoration" patterns appear in modern landing pages, and orbs/particles are the highest-probability decorative element. They add perceived sophistication cheaply.
- **How to detect:** Look for absolutely positioned elements with blur, opacity < 0.3, and CSS or JS animations. Check for canvas-based particle systems. If decorative elements have no relationship to page content, flag them.
- **Fix:** Remove them entirely — the page will look cleaner. If background interest is needed, use a subtle texture, a single well-placed gradient, or a photograph. Any remaining animation should be triggered by interaction, not looping indefinitely.

**Pattern 23: Rounded Rectangles with Generic Drop Shadows**

Every container has `rounded-xl shadow-lg` or `rounded-2xl shadow-md`. Border-radius always 12-16px. Shadow is always Tailwind's default multi-layer neutral shadow. Nothing has sharp corners, nothing has custom shadow values. Safe, forgettable, interchangeable.

- **What it looks like:** All cards, containers, and interactive surfaces share the same `rounded-xl shadow-lg` treatment. Uniform radius, uniform shadow color, uniform shadow spread.
- **Why AI does it:** `rounded-xl shadow-lg` is the most common card treatment in component libraries. It is the highest-probability container style.
- **How to detect:** Check if all containers share the same border-radius and shadow values. If every surface has the same treatment, it is generic.
- **Fix:** Be intentional with radius: 0px for a sharp editorial feel, 4-6px for subtle softness, reserve 12px+ for buttons and pills. For shadows, customize: use a single-layer `box-shadow` with brand-tinted color (`box-shadow: 0 4px 20px rgba(15, 23, 42, 0.08)` instead of Tailwind's default). Define an elevation system with 3-5 distinct shadow levels.

**Pattern 24: Sparklines as Decoration**

Small line charts, bar charts, or area charts inside dashboard cards that do not represent real data. No axes, no labels, no interactivity. Wavy SVG paths that say "data exists here" without communicating anything.

- **What it looks like:** SVG `<path>` elements with smooth curves inside metric cards. The chart has no axis labels, no data source reference, no legend, and no hover states.
- **Why AI does it:** Dashboard UI kits universally include decorative mini-charts. They are the highest-probability dashboard decoration.
- **How to detect:** Look for SVG paths or chart components inside cards without axis labels, data sources, legends, or interactivity. If a chart cannot be interpreted by a user, it is decoration.
- **Fix:** If the data is real, give it proper axes, labels, and interactivity. If it is a mockup, use clearly labeled placeholder data matching the actual data shape. If purely decorative, remove it — the space is better used for content.

**Pattern 25: Fade-on-Scroll Animations**

Every section fades in with `opacity: 0` to `opacity: 1` and slides up with `translateY(20px)` over 300-500ms as it enters the viewport. Users must wait for content they deliberately scrolled to. Cards stagger-animate in rows with 100ms delays between each.

- **What it looks like:** Scroll down and wait. Content you scrolled to appears gradually instead of being immediately visible. Often implemented with Intersection Observer or libraries like AOS/Framer Motion.
- **Why AI does it:** "Animate on scroll" is one of the most requested features, and training data includes many over-animated portfolio sites where every element animates.
- **How to detect:** Scroll through the page. If more than 50% of visible elements animate on first appearance, or the same fade-up animation appears on 5+ element types, it is too much.
- **Fix:** Page-level transitions (route changes) get animation. First-time reveal of the hero gets subtle animation. Everything else appears instantly. If you must animate sections, use `opacity` only (no translateY) with duration under 200ms. Never stagger cards with delays — show them all simultaneously.

**Pattern 26: Elastic/Bounce Easing**

`cubic-bezier(0.68, -0.55, 0.265, 1.55)` or `spring` physics on hovers, modals, page transitions. Elements overshoot their target and spring back. Draws attention to the animation, not the content.

- **What it looks like:** Hover a button and it scales up 10% then settles back to 5%. Open a modal and it overshoots its final size then bounces into place. Navigation transitions wobble.
- **Why AI does it:** Bouncy easing catches the eye in demos and is overrepresented in animation tutorials and CodePen examples. It is the "impressive" easing curve.
- **How to detect:** Search for cubic-bezier curves with negative values (the bounce signature). Check for `spring` or `bounce` keywords in Framer Motion configs. Hover elements — if multiple things overshoot, it is overuse.
- **Fix:** Use `ease-out` (`cubic-bezier(0, 0, 0.2, 1)`) for entrances, `ease-in` (`cubic-bezier(0.4, 0, 1, 1)`) for exits. For premium feel, use `ease-out-quart` (`cubic-bezier(0.25, 1, 0.5, 1)`) or `ease-out-expo` (`cubic-bezier(0.16, 1, 0.3, 1)`). Reserve bounce for a single delightful interaction (a like button, a success checkmark). Everything else should feel swift and decisive.

**Pattern 27: Gratuitous Stock/AI Imagery**

Obviously AI-generated images with impossible hand anatomy, smooth plastic skin, and corporate diversity casting. Or overfamiliar stock photos: the open-plan office high-five, the headset-wearing support agent, the laptop-on-a-cafe-table hero shot.

- **What it looks like:** Images that feel disconnected from the specific product, team, or use case. AI-generated faces with six fingers. Stock photos that appear on a thousand other sites.
- **Why AI does it:** It needs to fill image slots and generates or suggests the most statistically common images for each context (team section gets diverse headshots, hero gets abstract tech imagery).
- **How to detect:** Reverse image search stock photos. Check AI images for hand anatomy, text rendering, and background consistency. Ask: does this image show THIS specific product or team?
- **Fix:** Custom photography of the actual product, team, or use case. Custom illustration in a distinctive style. Screenshots of the real product UI. Abstract geometric art derived from brand elements. No image at all — a well-designed text-only section is better than a bad image.

---

## Category 5: Content Slop

**Pattern 28: Vague Transformation Headlines**

"Unlock the power of...", "Transform your workflow with...", "The future of X is here", "Revolutionize how you...", "Experience the next generation of...". Headlines that could apply to any product in any industry.

- **What it looks like:** A hero heading that contains no specific claim, no number, no named audience, and no concrete benefit. The heading works equally well for a CRM, a database, a design tool, and a sandwich shop.
- **Why AI does it:** Vague transformation language is the statistical average of all marketing headlines. It is the safest, most generic output that is unlikely to be "wrong."
- **How to detect:** Remove the product name from the headline. If it still makes sense for a completely different product, it is too vague.
- **Fix:** Name the specific audience and quantify the benefit. "Cut your deploy time from 45 minutes to 90 seconds" beats "Transform your deployment workflow." "The CRM that 2,300 real estate teams chose over Salesforce" beats "The future of customer relationships."

**Pattern 29: Feature-Dumping Without Benefits**

"AI-powered. Cloud-native. Enterprise-grade. SOC 2 compliant. Real-time collaboration." A spec sheet of capabilities with no explanation of why anyone should care.

- **What it looks like:** Bullet points or card grids listing technical capabilities without connecting them to user outcomes. Features described in the builder's language, not the user's language.
- **Why AI does it:** Feature lists are heavily represented in training data, and AI generates them by extracting technical attributes. Translating features to benefits requires understanding the user's context.
- **How to detect:** For each feature listed, ask: "So what?" If the page does not answer that question, the feature is dumped without benefit translation.
- **Fix:** For every feature, complete this sentence: "[Feature] so that you can [benefit]." "AI-powered search so you find the right document in 3 seconds instead of 3 minutes." Lead with the benefit, mention the feature as support.

**Pattern 30: Placeholder-Quality Body Copy**

Circular definitions ("Our platform helps you manage your platform"), hallucinated statistics ("Join 1M+ users" on a product with 47 users), monotonous sentence structure (every paragraph starts with "Our" or "We").

- **What it looks like:** Body text that sounds like it was generated to fill space rather than communicate. Repeated sentence patterns. Claims without evidence. Text that says nothing specific.
- **Why AI does it:** It generates the most probable sequence of tokens following a heading, which produces generic copy that sounds plausible but communicates nothing.
- **How to detect:** Read each paragraph and ask: "What specific thing did I learn?" If the answer is nothing, it is placeholder copy. Check for unverified statistics and circular reasoning.
- **Fix:** Every sentence must communicate a specific, verifiable fact or make a claim the product can back up. Replace "Our powerful platform" with the platform's actual name. Replace "thousands of users" with the real number. Write in the brand's actual voice, not generic SaaS voice.

**Pattern 31: "Trusted By" Logo Walls Without Context**

A row of company logos under "Trusted by leading companies" with no case studies, no quotes, no metrics, no verifiable relationship. Sometimes logos of companies that are not actually customers.

- **What it looks like:** 5-8 gray company logos in a horizontal row with "Trusted by" or "Used by" above them. No links to case studies, no context about what each company uses the product for.
- **Why AI does it:** Logo walls appear on nearly every SaaS landing page. They are a standard section in the formulaic page sequence.
- **How to detect:** Check if the logos link to case studies. Check if the company-product relationships are verifiable. Check if the logos represent an appropriate industry mix for the product.
- **Fix:** If the relationships are real, add context: "Stripe processes payments for [Company], reducing checkout abandonment by 23%." Link to full case studies. If the relationships are not verifiable, remove the section entirely. A single detailed testimonial with attribution is worth more than 20 unverified logos.

**Pattern 32: Redundant Japanese-Style UX Writing**

"Please kindly proceed to click the button below in order to submit your form." Overly polite, overly verbose instructions that quadruple the word count without adding information.

- **What it looks like:** Button labels like "Click here to get started now" instead of "Get started." Form instructions like "Please fill in the following required fields below" instead of removing the instruction entirely and marking required fields.
- **Why AI does it:** Polite, verbose phrasing is overrepresented in training data because many web applications use this style. AI optimizes for completeness over conciseness.
- **How to detect:** Count words in button labels, form instructions, error messages, and confirmation dialogs. If any label exceeds 4 words, or instructions exceed one line, check for redundancy.
- **Fix:** Button: "Get started." Not "Click here to get started today." Error: "Email required." Not "Please make sure to enter a valid email address in the field above." Confirmation: "Saved." Not "Your changes have been successfully saved to your account."

**Pattern 33: Same Professional Tone Everywhere**

Headlines, error messages, onboarding flows, success confirmations, empty states, and footer copy all sound identical: formal, distant, corporate. No variation in warmth, urgency, or personality.

- **What it looks like:** An error message that sounds like a marketing headline. An onboarding welcome that sounds like a terms-of-service clause. Every piece of text at the same emotional temperature.
- **Why AI does it:** It generates text in a consistent "professional" register because mixing tones requires understanding context, audience emotional state, and brand personality.
- **How to detect:** Read the hero headline, then an error message, then a success confirmation, then the empty state. If they all sound like the same person in the same mood wrote them, flag it.
- **Fix:** Map tone to context. Marketing copy: confident and specific. Onboarding: warm and encouraging. Errors: direct and helpful. Success states: brief and positive. Empty states: actionable and inviting. Define 3-4 tone registers and assign them to context categories.

---

## Category 6: UX/Interaction Slop

**Pattern 34: Modals for Everything**

Settings in a modal. Confirmation in a modal. Detail view in a modal. Creation flow in a modal. Modals opening other modals. Every action opens a floating box over a dimmed background.

- **What it looks like:** Click any action and a `position: fixed` overlay with a centered white box appears. Complex multi-step flows squeezed into a 500px-wide modal. Modal stacking where closing one reveals another.
- **Why AI does it:** Modals are the most common "show additional content" pattern in component libraries. They are the highest-probability solution for "user needs to see more."
- **How to detect:** Count modal/dialog components. If more than 3 distinct user flows involve modals, or if modals open other modals, the design is over-relying on them.
- **Fix:** Quick confirmations: inline confirmation (button transforms to "Are you sure? Yes / No"). Detail views: slide-out drawer or dedicated page. Creation flows: dedicated page with progress steps. Settings: dedicated page with sections. Reserve modals for truly interruptive moments requiring immediate attention.

**Pattern 35: Every Button is Primary**

Multiple buttons on a page with the same visual weight. Three CTAs in a hero, all styled identically with filled backgrounds and bold text. A card with two "equally important" actions.

- **What it looks like:** `bg-indigo-500 text-white font-semibold px-4 py-2 rounded-lg` on every button. No ghost buttons, no text links, no secondary styles. Everything screams for attention equally.
- **Why AI does it:** The filled button is the highest-probability button style. Each button gets styled independently as "important."
- **How to detect:** Count filled/solid buttons vs. ghost/text/link buttons. If more than 40% of buttons are primary-styled, hierarchy is broken. More than one primary button in any section is almost always wrong.
- **Fix:** One primary action per context (filled, brand color). Secondary actions: outline or ghost (`border border-gray-300 text-gray-700`). Tertiary actions: text-link styling (`text-indigo-600 hover:underline`). In any button group, only ONE gets primary treatment.

**Pattern 36: Cookie-Cutter Navigation**

"Product, Features, Pricing, About, Contact" regardless of what the product is, who the audience is, or what actions matter. Sometimes "Solutions, Resources, Company" as the enterprise variant.

- **What it looks like:** A horizontal nav bar with 4-6 generic labels that could belong to any website. No product-specific terminology, no audience-specific entry points.
- **Why AI does it:** These labels are the statistical mode of navigation items across all websites. They are the safest, most generic labels.
- **How to detect:** Check if the navigation labels are specific to this product. "Features" is generic; "Templates" or "Integrations" is specific. "About" is generic; "Our Approach" or "The Team" is specific.
- **Fix:** Name nav items after what users actually look for. Instead of "Features," use the specific feature category ("Templates," "Automations," "API"). Instead of "About," use what the user cares about ("Open Source," "Security," "Changelog"). Let user research drive the IA, not convention.

**Pattern 37: Missing Interaction States**

Only default and hover states implemented. No loading, error, success, disabled, focused, or empty states. The UI looks complete until someone actually uses it.

- **What it looks like:** A button that has a hover color but no loading spinner, no disabled opacity, no success confirmation. A form that validates on submit but shows no inline validation. Empty states that show a blank white area instead of guidance.
- **Why AI does it:** Default and hover are the only states that appear in most design examples and component library previews. The other 6 states require thinking about edge cases.
- **How to detect:** Audit each interactive element for 8 states: default, hover, focus, active, loading, disabled, error, success. If fewer than 5 are implemented, interaction design is incomplete.
- **Fix:** Design all 8 states for every interactive element. Start with the unhappy paths: what does the button look like while the request is pending? What happens when it fails? What does the empty state look like before any data exists? These states are where users spend most of their actual time.

**Pattern 38: Non-Functional Forms**

Forms with visual completion — styled inputs, validation messages, success toasts — but no backend connection. The form looks like it works. It does not work.

- **What it looks like:** A contact form with `onSubmit` that shows a "Thank you" toast but sends no email. A newsletter signup that validates the email format but POSTs nowhere. A login form with client-side validation and no auth backend.
- **Why AI does it:** AI generates frontend code. Forms are visual components. The backend connection is a separate concern that often gets omitted because the AI was asked to build a "page" not a "system."
- **How to detect:** Check form `onSubmit` handlers. Do they call an API endpoint? Is that endpoint implemented? Test by submitting — does any data actually persist? Check network requests in browser dev tools.
- **Fix:** Every form must have end-to-end functionality verified before shipping. If the backend is not ready, clearly mark the form as non-functional with a visible "Demo Only" badge rather than faking success. Test by actually submitting real data and verifying it arrives.

---

## The Scoring System

Score 0-100+ (higher = more slop):

| Score | Meaning | Action |
|-------|---------|--------|
| 0-20 | Distinctive, intentional design | Ship it. Minor polish only. |
| 21-40 | Some generic patterns, mostly intentional | Address flagged patterns in next iteration. |
| 41-60 | Noticeable AI influence, targeted fixes needed | Rework flagged categories before shipping. |
| 61-80 | Obviously AI-generated, major rework needed | Redesign from brand principles, not generated output. |
| 81-100+ | Pure slop, start over with intention | Discard and begin with mood board + brand constraints. |

### How to Calculate

1. **Check each of the 38 patterns.** Each pattern detected adds **+4 points**.
2. **Category penalty.** If 3 or more patterns from the same category are detected, add **+5 points** per qualifying category.
3. **Compound penalty.** If patterns from 4 or more different categories are present, add **+10 points** (systemic convergence, not isolated issues).
4. **Maximum theoretical score: 152 + 30 + 10 = 192.** In practice, scores above 100 all mean the same thing: start over.

### Example Scoring

A design with:
- Purple gradient hero (pattern 1): +4
- Tailwind defaults (pattern 8): +4
- Inter as only font (pattern 9): +4
- Cookie-cutter hero (pattern 14): +4
- Identical card grid (pattern 15): +4
- Same spacing (pattern 19): +4
- Layout category has 3 patterns (14, 15, 19): +5
- Glassmorphism cards (pattern 6): +4
- Color category has 3 patterns (1, 6, 8): +5
- Fade-on-scroll (pattern 25): +4
- Vague headline (pattern 28): +4
- Patterns in 5 categories (Color, Typography, Layout, Visual Detail, Content): +10

**Total: 56** — "Noticeable AI influence, targeted fixes needed." Fix the hero, swap the font, customize the palette, rewrite the headline, and the score could drop to the low 20s.

---

## Before You Start: 7 Decisions

Set these BEFORE generating any design. Intentional decisions create distinctiveness. Without them, AI converges on the statistical average.

**Important:** These decisions should push toward impressive, beautiful output — not toward safety. A stripped-down, over-restrained design that avoids all risk is just as bad as template slop. The goal is a site someone would screenshot and share, not one that merely avoids AI patterns.

**1. Choose colors with personality.**
Write down 2-3 specific hex values derived from the brand identity. If the brand has no established colors, pick a palette that reflects the product's personality and makes you feel something. Purple and blue are fine if they're intentional and considered — what matters is that the palette has depth (tinted neutrals, surface variations, accent hierarchy), not that it avoids popular hues.

**2. Pick typography with presence.**
Name the exact display font and body font. The font pairing should have character — it should feel like a deliberate choice. Consider serifs (Fraunces, Newsreader, Source Serif), geometric sans (Satoshi, General Sans), or distinctive grotesks (Space Grotesk, Instrument Sans). Inter is fine if the typography system itself is strong (dramatic scale, weight contrast, fluid sizing).

**3. Define who the audience is, specifically.**
Not "developers" — "senior backend engineers at companies with 50-200 employees who currently use AWS Lambda." The more specific the audience definition, the more distinctive the design decisions that follow from it.

**4. Decide the one memorable thing.**
Every great design has one element that makes it recognizable. Stripe has precise gradients. Linear has keyboard-first interaction. Vercel has dramatic typography on black. Decide what yours is before generating anything. This should be ambitious — not "clean spacing" but something that makes people pause.

**5. Choose a layout approach that serves the content.**
Think about what your specific audience needs to see, in what order, to make their decision. A developer tool might lead with a code example. A creative tool might lead with a gallery. The Hero → Logos → Features → Testimonials → Pricing → FAQ → Footer formula works for some products — the problem is using it without thought.

**6. Write the hero headline with a specific, quantified benefit.**
Before generating any design, write the actual headline by hand. It must name the audience or the problem and include a concrete claim. "Cut your deploy time from 45 minutes to 90 seconds." Not "The future of deployment is here."

**7. Set the emotional tone — and how it varies by context.**
Define 3-4 tone registers: marketing copy (confident, specific), onboarding (warm, encouraging), errors (direct, helpful), success states (brief, positive). A single flat tone across all contexts is a signal of unconsidered design.
