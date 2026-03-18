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

### 5. Reduced Motion is Not Optional
Vestibular disorders affect a large portion of users. Always provide reduced motion fallbacks.
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```
Functional animations (progress bars) should remain, but without spatial movement.

### 6. Perceived Performance
* **The 80ms Threshold**: Visual changes under 80ms feel instantaneous. Aim for this on micro-interactions.
* **Preemptive Start**: Trigger transitions on `mousedown` instead of `click` where safe, to shave off perceived latency.

## Evaluation Protocol
When auditing motion, check:
1. Is it using `transform` and `opacity` only?
2. Are durations snappy (under 300ms for UI)?
3. Are easing curves intentional (no default `ease`)?
4. Is bounce/elasticity completely absent?
5. Is `prefers-reduced-motion` respected?
6. Do exit animations resolve faster than enter animations?