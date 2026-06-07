# Motion Mastery

This file defines how to use animation and transitions in interfaces.

Good motion is invisible; it supports comprehension without drawing attention to itself. Bad motion is theatrical and slow.

## Core Principles

### 1. The Only Animatable Properties
Only animate `transform` and `opacity`.
Animating `width`, `height`, `margin`, `padding`, or `box-shadow` causes layout recalculation and jank.
* For accordions, animate `grid-template-rows: 0fr` to `1fr` instead of `height`.

### 2. The 100/300/500 Duration Rule
Timing matters more than easing.
* **100–150ms**: Instant feedback (button press, toggle, color change).
* **200–300ms**: State changes (menu open, tooltip, hover).
* **300–500ms**: Layout changes (accordion, modal enter).
* **500–800ms**: Page/hero reveals.

Rule: Exit animations must be faster than entrances. Use ~75% of the enter duration.

### 3. Easing Curves
Never use the default `ease`. It is a compromise. Use precise exponential curves based on real physics.

```css
/* Entrances (Decelerating) */
--ease-out-quart: cubic-bezier(0.25, 1, 0.5, 1);
--ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);

/* Exits (Accelerating) */
--ease-in: cubic-bezier(0.7, 0, 0.84, 0);

/* State toggles (Both) */
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
```

**Rule**: Never use `bounce` or `spring` with overshoot for UI elements. They feel tacky. Real objects decelerate smoothly.

### 4. Staggered Animations
Use CSS custom properties for clean stagger sequences.
```css
.item {
  animation-delay: calc(var(--i, 0) * 50ms);
}
```
**Rule**: Cap total stagger time. If you have 20 items, do not stagger them by 50ms (1000ms total). Reduce the delay or batch them to keep total entrance time under 500ms.

### 5. Perceived Performance
* **The 80ms Threshold**: Visual changes under 80ms feel instantaneous. Aim for this on micro-interactions.
* **Preemptive Start**: Trigger transitions on `mousedown` instead of `click` where safe, to shave off perceived latency.

---

## Duration & Easing Reference Table

Every motion decision should reference this table. Do not improvise timing.

| Use Case | Duration | Easing | Notes |
|----------|----------|--------|-------|
| Button press/active | 50–80ms | `ease-out` | Must feel instantaneous |
| Color/opacity change | 100–150ms | `ease-out` | Hover states, toggles |
| Tooltip appear | 150–200ms | `--ease-out-quart` | Delay 300ms before showing |
| Dropdown/menu open | 150–200ms | `--ease-out-expo` | Exit at 100–150ms |
| Toast/snackbar enter | 200–300ms | `--ease-out-expo` | Slide + fade |
| Modal enter | 300–400ms | `--ease-out-expo` | Scale from 0.96 + fade |
| Modal exit | 200–250ms | `--ease-in` | Faster than enter |
| Accordion expand | 250–350ms | `--ease-in-out` | Use `grid-template-rows` |
| Page transition | 300–500ms | `--ease-out-expo` | Cross-fade or slide |
| Scroll reveal | 400–600ms | `--ease-out-quart` | `opacity` + `translateY(20px)` |
| Hero entrance | 600–800ms | `--ease-out-expo` | Maximum. Never exceed. |
| Tooltip hide delay | 100ms | — | Prevent flicker on mouse path |

### Duration Rules
- **Nothing in a UI should ever animate longer than 800ms.** If it does, it's decoration, not interface.
- **Exit < Enter.** Always. 75% of enter duration, rounded to nearest 50ms.
- **Tooltip delay before showing: 300ms.** Prevents tooltip flashing when the cursor passes over elements.
- **Tooltip delay before hiding: 100ms.** Allows the user to move the cursor to the tooltip content.

---

## What Bad Motion Looks Like

These are the motion mistakes AI-generated code makes. Memorize and eliminate them.

### Bounce on UI Elements
```css
/* BAD — bounce has no place on buttons, modals, or cards */
.modal {
  animation: bounceIn 800ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
```
Bounce implies the UI is a toy. Real software decelerates smoothly. The only acceptable overshoot is in playful/gaming contexts — never in SaaS, fintech, or professional tools.

### 800ms+ on Interactions
```css
/* BAD — user is waiting nearly a full second for a menu */
.dropdown {
  transition: all 800ms ease;
}
```
Interactions that take longer than 300ms feel laggy. 800ms is an eternity. Users will click again, thinking the UI is broken.

### Animating `width`, `height`, or `margin`
```css
/* BAD — triggers layout recalculation every frame */
.sidebar {
  transition: width 300ms ease;
}

/* GOOD — use transform instead */
.sidebar {
  transform: translateX(-100%);
  transition: transform 300ms var(--ease-out-expo);
}
.sidebar.is-open {
  transform: translateX(0);
}
```

### Everything Animating on Load
```css
/* BAD — every section fades/slides in. The page feels like it's assembling itself. */
.section { animation: fadeInUp 600ms ease forwards; }
.section:nth-child(1) { animation-delay: 0ms; }
.section:nth-child(2) { animation-delay: 200ms; }
.section:nth-child(3) { animation-delay: 400ms; }
.section:nth-child(4) { animation-delay: 600ms; }
.section:nth-child(5) { animation-delay: 800ms; }
/* User waits 1400ms to see the full page. Unacceptable. */
```
**Fix:** Animate the above-the-fold content immediately. Below-the-fold content reveals on scroll. Never stagger more than 3 elements on initial load.

### Parallax on Mobile
Parallax scrolling on mobile:
- Causes jank (scroll events + transforms on every frame)
- Fights with native scroll momentum
- Creates motion sickness for vestibular disorder users
- Wastes GPU layers

**Rule:** Disable parallax on touch devices. Use `IntersectionObserver` reveals instead.

---

## Page Transitions

### View Transitions API
The modern way to animate between page navigations. No libraries needed.

```css
/* Cross-fade (default behavior) */
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 300ms;
  animation-timing-function: var(--ease-out-expo);
}

/* Slide transition for navigation depth */
::view-transition-old(root) {
  animation: slide-out-left 300ms var(--ease-in) forwards;
}
::view-transition-new(root) {
  animation: slide-in-right 300ms var(--ease-out-expo) forwards;
}

@keyframes slide-out-left {
  to { transform: translateX(-20%); opacity: 0; }
}
@keyframes slide-in-right {
  from { transform: translateX(20%); opacity: 0; }
}
```

```js
// Trigger view transition on navigation
document.addEventListener('click', async (e) => {
  const link = e.target.closest('a[data-transition]');
  if (!link) return;
  e.preventDefault();

  if (!document.startViewTransition) {
    window.location.href = link.href; // fallback
    return;
  }

  const transition = document.startViewTransition(async () => {
    const response = await fetch(link.href);
    const html = await response.text();
    document.documentElement.innerHTML = new DOMParser()
      .parseFromString(html, 'text/html')
      .documentElement.innerHTML;
  });
});
```

### Transition Direction Conventions
- **Navigating deeper** (list → detail): Slide content left / new content from right
- **Navigating back** (detail → list): Slide content right / new content from left
- **Peer navigation** (tab to tab): Cross-fade only, no directional slide
- **Modal/overlay open**: Scale up from 0.96 + fade in
- **Modal/overlay close**: Fade out (no scale — exits should be simpler than entrances)

---

## Scroll-Triggered Animations

### IntersectionObserver Setup
The standard pattern for scroll reveals. Do not use scroll event listeners.

```js
function createRevealObserver(options = {}) {
  const { threshold = 0.15, rootMargin = '0px 0px -60px 0px', once = true } = options;

  return new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          if (once) observer.unobserve(entry.target);
        }
      });
    },
    { threshold, rootMargin }
  );
}

const observer = createRevealObserver();
document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
```

### Stagger Budget
When revealing a group of items (cards, list items, features), the total reveal time for the group must stay under 500ms.

| Items | Delay per item | Total |
|-------|---------------|-------|
| 3 | 120ms | 360ms |
| 4 | 100ms | 400ms |
| 6 | 70ms | 420ms |
| 8 | 50ms | 400ms |
| 12+ | 30ms | Cap at 400ms, batch remaining |

```css
.reveal-group [data-reveal] {
  --stagger: 80ms;
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 400ms var(--ease-out-quart), transform 400ms var(--ease-out-quart);
  transition-delay: calc(var(--i, 0) * var(--stagger));
}
.reveal-group [data-reveal].is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Reveal-Once Pattern
Elements should reveal once and stay visible. Re-hiding elements when they scroll out of view is disorienting and creates a "peek-a-boo" effect.

```js
// GOOD — reveal once, then stop observing
if (entry.isIntersecting) {
  entry.target.classList.add('is-visible');
  observer.unobserve(entry.target);
}

// BAD — revealing and hiding on every scroll
entry.target.classList.toggle('is-visible', entry.isIntersecting);
```

### CSS `animation-timeline: scroll()` (Progressive Enhancement)
For purely decorative scroll-linked effects (progress bars, parallax backgrounds), CSS scroll timelines eliminate JS entirely.

```css
.progress-bar {
  transform-origin: left;
  transform: scaleX(0);
  animation: grow-bar linear forwards;
  animation-timeline: scroll();
}
@keyframes grow-bar {
  to { transform: scaleX(1); }
}

/* Only use if supported */
@supports not (animation-timeline: scroll()) {
  .progress-bar { transform: scaleX(1); } /* static fallback */
}
```

---

## Performance Audit

### The `transform`/`opacity` Rule
If an animation causes the browser to recalculate layout or repaint, it will jank on lower-end devices.

| Property | Trigger | Verdict |
|----------|---------|---------|
| `transform` | Composite only | Safe |
| `opacity` | Composite only | Safe |
| `filter` | Repaint | Acceptable with caution |
| `background-color` | Repaint | Acceptable for small elements |
| `box-shadow` | Repaint | Avoid animating |
| `width`, `height` | Layout + Repaint | Never animate |
| `margin`, `padding` | Layout + Repaint | Never animate |
| `border-width` | Layout + Repaint | Never animate |
| `top`, `left` | Layout + Repaint | Use `transform: translate()` instead |

### `will-change` Placement and Cleanup
`will-change` promotes an element to its own GPU layer. This uses VRAM. Do not apply it to every element.

```css
/* BAD — permanent will-change on all items */
.card { will-change: transform; }

/* GOOD — apply on hover/focus, remove after transition */
.card:hover { will-change: transform; }
.card {
  transition: transform 200ms var(--ease-out-quart);
}
```

For elements that are ALWAYS animated (a loading spinner), `will-change` is acceptable. For everything else, apply it just before animation and let the browser clean up.

### GPU Layer Budget
Rule of thumb: **Maximum 3 simultaneous animations in the viewport at any time.** More than 3 creates visual noise and degrades performance on mobile. If a section has 8 animating elements, stagger them so only 2-3 are moving at once.

---

## Reduced Motion — Nuanced Approach

The nuclear approach (setting all durations to `0.01ms`) is functional but crude. A nuanced approach preserves functional animations while removing spatial movement.

```css
@media (prefers-reduced-motion: reduce) {
  /* Remove spatial movement */
  [data-reveal] {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }

  /* Remove parallax, scroll-linked motion */
  .parallax, [data-parallax] {
    transform: none !important;
    animation: none !important;
  }

  /* Keep functional animations — just remove movement */
  /* Loading spinners: keep rotating */
  .spinner {
    animation-duration: 800ms; /* keep, it's functional */
  }

  /* Progress bars: keep, but no easing — instant fill */
  .progress-bar {
    transition-duration: 0.01ms !important;
  }

  /* Color changes: keep but make instant */
  button {
    transition-property: background-color, color, border-color;
    transition-duration: 0.01ms !important;
  }

  /* Accordions: keep but instant */
  .accordion-content {
    transition-duration: 0.01ms !important;
  }
}
```

### What to Keep vs Remove

| Animation Type | Reduced Motion | Why |
|----------------|---------------|-----|
| Scroll reveals (fade + slide) | Remove entirely | Spatial movement triggers vestibular issues |
| Page transitions (slide) | Replace with instant cut | Spatial movement |
| Modal enter (scale + fade) | Instant appear | Scale is spatial |
| Color/opacity hover changes | Keep but instant | No spatial movement, functional feedback |
| Loading spinners | Keep | Functional — communicates "in progress" |
| Progress bars | Keep but instant fill | Functional |
| Carousels (auto-play) | Stop auto-play | Movement without user initiation |
| Parallax | Remove entirely | Spatial, performance-heavy, decorative |

### Testing Methodology
1. Enable `prefers-reduced-motion: reduce` in browser DevTools (Rendering tab → Emulate CSS media feature).
2. Navigate every page. Every animated element should either be static or instant.
3. Verify no `translateY`, `translateX`, `scale`, or `rotate` animations play.
4. Verify loading spinners and progress bars still function.
5. Verify the page is still usable and comprehensible without any motion.

---

## Worked Example: AI Page with 1000ms Bounce → Correctly Choreographed Reveal

### Before (typical AI output)

```css
.hero-title {
  animation: bounceIn 1000ms cubic-bezier(0.68, -0.55, 0.265, 1.55);
}
.hero-subtitle {
  animation: bounceIn 1000ms cubic-bezier(0.68, -0.55, 0.265, 1.55) 200ms;
}
.hero-cta {
  animation: bounceIn 1000ms cubic-bezier(0.68, -0.55, 0.265, 1.55) 400ms;
}
.feature-card {
  animation: bounceIn 800ms ease 600ms;
}
.feature-card:nth-child(2) { animation-delay: 800ms; }
.feature-card:nth-child(3) { animation-delay: 1000ms; }
/* Total time: 1800ms before the page is fully visible */
/* Bounce easing on everything */
/* User sees elements jumping around for nearly 2 seconds */
```

### After (choreographed, reduced-motion-safe)

```css
/* Hero elements: fast, no bounce */
.hero-title {
  opacity: 0;
  transform: translateY(12px);
  animation: reveal 500ms var(--ease-out-expo) forwards;
}
.hero-subtitle {
  opacity: 0;
  transform: translateY(12px);
  animation: reveal 500ms var(--ease-out-expo) 100ms forwards;
}
.hero-cta {
  opacity: 0;
  transform: translateY(8px);
  animation: reveal 400ms var(--ease-out-expo) 200ms forwards;
}

@keyframes reveal {
  to { opacity: 1; transform: translateY(0); }
}

/* Feature cards: reveal on scroll, not on load */
.feature-card {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 400ms var(--ease-out-quart), transform 400ms var(--ease-out-quart);
  transition-delay: calc(var(--i, 0) * 80ms);
}
.feature-card.is-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Reduced motion: everything appears instantly */
@media (prefers-reduced-motion: reduce) {
  .hero-title, .hero-subtitle, .hero-cta {
    opacity: 1;
    transform: none;
    animation: none;
  }
  .feature-card {
    opacity: 1;
    transform: none;
    transition: none;
  }
}
```

Key improvements:
- **Duration**: 500ms max (down from 1000ms)
- **Easing**: `ease-out-expo` (smooth deceleration, no bounce)
- **Stagger**: 100ms between hero elements (total 300ms, not 1800ms)
- **Scroll reveal**: Feature cards animate on scroll, not page load
- **translateY**: 12-16px (subtle, not dramatic)
- **Reduced motion**: Full fallback — instant appearance, no movement

---

## Evaluation Protocol
When auditing motion, check:
1. Is it using `transform` and `opacity` only?
2. Are durations snappy (under 300ms for UI, under 800ms for anything)?
3. Are easing curves intentional (no default `ease`)?
4. Is bounce/elasticity completely absent?
5. Is `prefers-reduced-motion` respected with nuanced approach?
6. Do exit animations resolve faster than enter animations?
7. Are there no more than 3 simultaneous animations in any viewport?
8. Is total stagger time for any group under 500ms?
9. Is parallax disabled on mobile/touch?
10. Are scroll reveals using `IntersectionObserver`, not scroll events?
11. Is `will-change` applied only when needed, not permanently?
12. Do tooltips have a 300ms show delay and 100ms hide delay?
