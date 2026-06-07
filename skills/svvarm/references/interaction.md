# Production & Interaction

svvarm's production playbook — responsive behavior, resilience, accessibility, performance, interaction states, and real-world UI hardening. The deep interaction knowledge (8-state patterns, focus management, keyboard navigation, forms, overlays) follows the audit methodology below.

The job is to make sure a design survives real devices, real content, real users, and real failure conditions. Do not evaluate the interface as a mockup. Evaluate it as software.

No vague quality advice. Identify concrete production risks, assign severity, and provide implementation-ready fixes. For motion-specific rules pull `motion.md`; for icon rules pull `icons.md`.

## Core Standard

Every recommendation must be:

- Real-world
- Testable
- Specific
- Risk-ranked
- Implementation-ready
- Grounded in the provided code and context

You do not optimize only for ideal conditions. You optimize for failure tolerance, content variability, accessibility, and performance under constraint.

## Scope

You handle:

- Responsive behavior
- Container and viewport adaptation
- Resilience to content extremes and missing data
- Accessibility and keyboard behavior
- Performance and rendering efficiency
- Production-safe motion and interaction patterns
- Form robustness
- Failure, loading, empty, and offline states
- Internationalization and text expansion risks
- Device and input-method edge cases

You do not:

- Redesign the product unless a production issue requires a structural fix
- Assume runtime behavior that is not visible in the provided code
- Mark a check as passing if it cannot actually be verified
- Treat accessibility as a side checklist rather than a core requirement
- Recommend premature micro-optimizations without meaningful benefit

If important context is missing, say so briefly and continue with the available evidence. Do not invent runtime conditions, analytics, browser support, or framework behavior.

## Working Modes

Choose one mode explicitly based on the task.

### 1. Audit
Use when the goal is to evaluate production readiness.

Deliver:
- PASS / WARN / FAIL by category
- severity-ranked issues
- exact code fixes where possible
- clear notes on what could not be verified

### 2. Harden
Use when the goal is to actively improve the code for production readiness.

Deliver:
- revised code
- before/after changes
- resolved risks
- remaining risks that need broader architectural work

### 3. Preflight
Use before launch, handoff, or review.

Deliver:
- release-blocking issues
- should-fix issues
- low-priority improvements
- concise go/no-go summary

## Non-Negotiable Rules

- Be thorough
- Do not mark PASS unless the condition is visible and verifiable
- Every FAIL must include an exact fix or a clearly scoped remediation path
- Separate release blockers from non-blockers
- Preserve semantic HTML, source order, and keyboard access
- Evaluate at minimum for narrow, medium, wide, and zoomed contexts
- Treat accessibility failures as critical unless clearly minor
- Prefer resilient, simple solutions over clever but brittle ones

## Anti-Slop Standard

Flag the implementation as weak or incomplete if you see any of the following:

- Responsive behavior based only on a couple of viewport breakpoints
- Components that ignore container context
- UI that only works with short English copy
- Layouts that collapse under zoom or long labels
- Loading states with no error, empty, or retry path
- Decorative performance tricks without structural optimization
- Hover-only affordances
- Inaccessible custom controls replacing native behavior unnecessarily (Div Soup)
- Skeletons everywhere but no actual failure recovery
- Mobile layouts with desktop assumptions about pointer precision
- "Accessible" markup that still has weak focus, source order, or labeling
- PASS claims based on guesswork rather than code evidence

Use direct language. If the design works only in ideal demo conditions, say so.

## Assessment Model

Use these severity levels:

- **FAIL** — must fix before production or release
- **WARN** — should fix soon; meaningful risk or degradation
- **PASS** — verified in code and acceptable

When evidence is incomplete, say:
- **UNVERIFIED** — cannot confirm from provided code

Do not convert uncertainty into PASS.

## Chain-of-Thought Evaluation Protocol

You MUST run these passes strictly sequentially. Do not attempt to process all passes simultaneously. Process Pass 1, then Pass 2, etc.

### Pass 1: Semantic Architecture & DOM
Verify semantic architecture compliance (see `layout.md` — Components & Semantic HTML).
- Are interactive elements native (`<button>`, `<a>`, `<dialog>`)?
- Is it "div soup"? Are there unnecessary wrappers?
- Are structural tags (`<section>`, `<main>`) used correctly?

### Pass 2: Accessibility & Keyboard Flow
Check:
- Focus visibility (`:focus-visible`).
- Logical source/tab order vs visual order.
- Accessible names (aria-labels on icon buttons).
- Contrast ratios.
- Skip links where applicable.

### Pass 3: Responsive Behavior & Resilience
Check:
- Container queries where component context matters.
- Text expansion/truncation behavior (long labels/names).
- Safe-area handling on mobile.
- Minimum touch target sizing (44x44px min).
- Zoom behavior at 200%.

**Non-Negotiable Mobile Safety (FAIL if violated):**
- **dvh over vh** — `100vh` / `h-screen` must use `min-h-[100dvh]` or `100dvh`. iOS Safari's dynamic viewport causes layout jumping with static `vh` units. Any instance of `100vh` or `h-screen` for full-height layouts is an automatic FAIL.
- **Mobile collapse guarantee** — Overlaps, rotations, multi-column asymmetry, and absolute-positioned compositions must collapse to single-column with horizontal padding below 768px. Zero horizontal scroll tolerance on mobile.
- **Touch device cleanup** — Hover-dependent reveals, tooltips, or state changes need `@media (hover: none)` / `@media (pointer: coarse)` alternatives. Content hidden behind hover on touch devices is inaccessible content.
- **Safe area insets** — Full-bleed elements, fixed-position elements, and bottom-anchored UI must include `env(safe-area-inset-*)` for notched/Dynamic Island devices.

### Pass 4: Performance & Motion
Check:
- Are animations using `transform` and `opacity` only?
- Are easing curves intentional (no default `ease`) per `motion.md`?
- Is `prefers-reduced-motion` respected?
- Image format and sizing.

### Pass 5: Forms & Interaction
Check:
- Labels vs placeholders (per the Form Patterns knowledge below).
- Validation behavior (on blur, not keystroke).
- Loading/Empty/Error states explicitly defined.

## Verification Rules

Only mark PASS when the code clearly demonstrates the behavior.

Examples:
- If no `:focus-visible` styles exist, do not assume focus is handled
- If no error state markup exists, do not assume the component has one
- If responsive behavior depends on runtime content, state the risk
- If line numbers are unavailable, cite the selector, component, or file region instead

If a check cannot be verified, mark it UNVERIFIED and explain the missing evidence.

## Fix Rules

For every FAIL, provide:
1. what is wrong
2. why it matters in production
3. exact code fix
4. any implementation note or tradeoff
5. severity

For every WARN, provide:
- what should change
- why
- a concise fix path

Do not only describe the problem if a concrete fix is possible.

## Output Format

Use exactly this structure:

```
## Production Readiness Report

### Mode
[AUDIT | HARDEN | PREFLIGHT]

### Assumptions
[Only include assumptions forced by missing context]

### Responsive

**[Check name] — [PASS | WARN | FAIL | UNVERIFIED]**
Evidence: [file, selector, component, or line reference if available]
Issue: [what is happening]
Fix: [exact code fix or remediation path]

### Resilience

**[Check name] — [PASS | WARN | FAIL | UNVERIFIED]**
Evidence: [file, selector, component, or line reference if available]
Issue: [what is happening]
Fix: [exact code fix or remediation path]

### Accessibility

**[Check name] — [PASS | WARN | FAIL | UNVERIFIED]**
Evidence: [file, selector, component, or line reference if available]
Issue: [what is happening]
Fix: [exact code fix or remediation path]

### Performance

**[Check name] — [PASS | WARN | FAIL | UNVERIFIED]**
Evidence: [file, selector, component, or line reference if available]
Issue: [what is happening]
Fix: [exact code fix or remediation path]

### Forms and Interaction
[Include only if relevant]

**[Check name] — [PASS | WARN | FAIL | UNVERIFIED]**
Evidence: [file, selector, component, or line reference if available]
Issue: [what is happening]
Fix: [exact code fix or remediation path]

### Summary
- Passed: [X]
- Warnings: [X]
- Failures: [X]
- Unverified: [X]

### Release Blockers
1. [Most critical must-fix]
2. [Second must-fix]
3. [Third must-fix]

### High-Value Fixes
1. [Best improvement for effort]
2. [Second]
3. [Third]

### Go / No-Go
[Concise production judgment]
```

## Style of Reasoning

Be precise, practical, and unsentimental.

Good:
- "This layout depends on short labels and will wrap badly under text expansion."
- "The custom control is not keyboard-complete and should fall back to native semantics."
- "This hover pattern disappears on coarse pointers and needs a persistent affordance."
- "This blur-heavy surface adds paint cost without adding meaningful hierarchy."

Bad:
- "This should probably be okay."
- "Looks responsive enough."
- "Accessibility seems fine."
- "Performance might be improved."

Explain issues in terms of failure risk, user impact, and production behavior.

A strong answer helps an engineer fix the issues that would otherwise appear only after release, on a constrained device, with difficult content, under non-ideal conditions. Anything less is incomplete.

---

# Interaction — Deep Knowledge

How to design states, feedback, and structural interactions for components.

An interface that looks good at rest but breaks during use is unfinished.

## Core Principles

### 1. The Eight Interactive States
Every interactive element must account for eight states:
1. **Default**: At rest.
2. **Hover**: Pointer over (mouse only).
3. **Focus**: Keyboard/programmatic focus.
4. **Active**: Being pressed. MUST include tactile feedback (e.g., `transform: scale(0.98)` or `translateY(1px)`) to simulate a physical push.
5. **Disabled**: Not interactive (reduced opacity).
6. **Loading**: Processing state (spinner/skeleton).
7. **Error**: Invalid state.
8. **Success**: Completed action.

Never design hover without focus. Keyboard users never see hover.

---

## 8-State Component Patterns

### Button — All 8 States

```css
/* 1. Default */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.625rem 1.25rem;
  font-family: inherit;
  font-size: var(--text-body, 1rem);
  font-weight: 500;
  line-height: 1;
  color: var(--color-bg);
  background: var(--color-primary);
  border: 1px solid transparent;
  border-radius: var(--radius-md, 0.5rem);
  cursor: pointer;
  transition: background-color 150ms ease, box-shadow 150ms ease, transform 100ms ease;
  min-height: 44px; /* touch target */
}

/* 2. Hover */
.btn:hover {
  background: var(--color-primary-hover);
  box-shadow: 0 2px 8px oklch(0% 0 0 / 0.12);
}

/* 3. Focus */
.btn:focus { outline: none; }
.btn:focus-visible {
  outline: 2px solid var(--color-focus, var(--color-primary));
  outline-offset: 2px;
}

/* 4. Active */
.btn:active {
  transform: scale(0.98);
  box-shadow: 0 1px 2px oklch(0% 0 0 / 0.1);
  transition-duration: 50ms;
}

/* 5. Disabled */
.btn:disabled,
.btn[aria-disabled="true"] {
  opacity: 0.5;
  cursor: not-allowed;
  pointer-events: none;
}

/* 6. Loading */
.btn[data-loading="true"] {
  color: transparent;
  pointer-events: none;
  position: relative;
}
.btn[data-loading="true"]::after {
  content: "";
  position: absolute;
  width: 1em;
  height: 1em;
  border: 2px solid currentColor;
  border-right-color: transparent;
  border-radius: 50%;
  animation: btn-spin 600ms linear infinite;
}
@keyframes btn-spin {
  to { transform: rotate(360deg); }
}

/* 7. Error */
.btn[data-state="error"] {
  background: var(--color-error);
  animation: btn-shake 300ms ease;
}
@keyframes btn-shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-4px); }
  75% { transform: translateX(4px); }
}

/* 8. Success */
.btn[data-state="success"] {
  background: var(--color-success);
}
```

### Input — All 8 States

```css
/* 1. Default */
.input {
  display: block;
  width: 100%;
  padding: 0.625rem 0.75rem;
  font-family: inherit;
  font-size: var(--text-body, 1rem);
  line-height: 1.5;
  color: var(--color-text);
  background: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md, 0.5rem);
  transition: border-color 150ms ease, box-shadow 150ms ease;
}

/* 2. Hover */
.input:hover:not(:focus):not(:disabled) {
  border-color: var(--color-border-hover, oklch(from var(--color-border) calc(l - 0.1) c h));
}

/* 3. Focus */
.input:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px oklch(from var(--color-primary) l c h / 0.15);
}

/* 4. Active (typing) — same as focus, no additional treatment needed */

/* 5. Disabled */
.input:disabled {
  opacity: 0.5;
  background: var(--color-surface-subtle, #f5f5f5);
  cursor: not-allowed;
}

/* 6. Loading (e.g., async validation) */
.input[data-loading="true"] {
  background-image: url("data:image/svg+xml,..."); /* spinner */
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 1rem;
  padding-right: 2.5rem;
}

/* 7. Error */
.input[aria-invalid="true"] {
  border-color: var(--color-error);
  box-shadow: 0 0 0 3px oklch(from var(--color-error) l c h / 0.1);
}

/* 8. Success */
.input[data-state="success"] {
  border-color: var(--color-success);
  box-shadow: 0 0 0 3px oklch(from var(--color-success) l c h / 0.1);
}
```

### Link — All 8 States

```css
/* 1. Default */
.link {
  color: var(--color-link, var(--color-primary));
  text-decoration: underline;
  text-decoration-color: oklch(from var(--color-primary) l c h / 0.3);
  text-underline-offset: 0.15em;
  transition: color 150ms ease, text-decoration-color 150ms ease;
}

/* 2. Hover */
.link:hover {
  color: var(--color-primary-hover);
  text-decoration-color: currentColor;
}

/* 3. Focus */
.link:focus { outline: none; }
.link:focus-visible {
  outline: 2px solid var(--color-focus, var(--color-primary));
  outline-offset: 2px;
  border-radius: 2px;
}

/* 4. Active */
.link:active {
  color: var(--color-primary-active, oklch(from var(--color-primary) calc(l - 0.1) c h));
}

/* 5. Disabled */
.link[aria-disabled="true"] {
  opacity: 0.5;
  pointer-events: none;
  text-decoration: none;
}

/* 6. Loading — use inline spinner next to link text, not on the link itself */

/* 7. Error — links rarely have error state; style the parent context */

/* 8. Visited (variant of success — completed action) */
.link:visited {
  color: var(--color-text-muted);
  text-decoration-color: oklch(from var(--color-text-muted) l c h / 0.3);
}
```

---

## Focus Management

### `focus-visible` vs `focus`
- `:focus` fires on ANY focus (click, tab, programmatic). Noisy for mouse users.
- `:focus-visible` fires only when the browser determines keyboard/programmatic focus. Use this for visual rings.
- `:focus` (without `:focus-visible`) should still remove default outlines and apply your custom ring — use `:focus-visible` as the trigger for showing it.

```css
/* Remove default, show ring only for keyboard */
:focus { outline: none; }
:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

### Focus Trapping in `<dialog>`
Native `<dialog>` with `showModal()` traps focus automatically. No JS focus trap libraries needed.

```html
<dialog id="confirm-dialog">
  <h2>Delete project?</h2>
  <p>This cannot be undone.</p>
  <form method="dialog">
    <button value="cancel" autofocus>Keep project</button>
    <button value="confirm" class="btn-destructive">Delete project</button>
  </form>
</dialog>
```

```js
const dialog = document.getElementById('confirm-dialog');
dialog.showModal(); // focus is trapped automatically

dialog.addEventListener('close', () => {
  if (dialog.returnValue === 'confirm') {
    deleteProject();
  }
});
```

Key rules:
- Set `autofocus` on the **safest** action (Cancel, not Delete).
- Use `<form method="dialog">` so buttons close the dialog automatically.
- Never build custom focus traps when `<dialog>` exists.

### `tabindex` Discipline
- `tabindex="0"` — adds an element to natural tab order. Use sparingly (custom widgets only).
- `tabindex="-1"` — programmatically focusable but not in tab order. Use for focus targets (headings after navigation, error messages).
- `tabindex="1+"` — NEVER. Positive tabindex creates unpredictable ordering.

### Skip-to-Content Pattern
Every page with a navigation header needs a skip link as the first focusable element.

```html
<a href="#main-content" class="skip-link">Skip to content</a>
<nav>...</nav>
<main id="main-content" tabindex="-1">...</main>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 1rem;
  padding: 0.5rem 1rem;
  background: var(--color-primary);
  color: var(--color-bg);
  border-radius: var(--radius-sm);
  z-index: 100;
  font-weight: 500;
}
.skip-link:focus {
  top: 1rem;
}
```

---

## Keyboard Navigation

### Arrow Keys for Tabs
Tab panels use **roving tabindex** — Tab moves to the tab list, then arrows move between tabs.

```html
<div role="tablist" aria-label="Account settings">
  <button role="tab" aria-selected="true" tabindex="0" id="tab-1" aria-controls="panel-1">Profile</button>
  <button role="tab" aria-selected="false" tabindex="-1" id="tab-2" aria-controls="panel-2">Security</button>
  <button role="tab" aria-selected="false" tabindex="-1" id="tab-3" aria-controls="panel-3">Billing</button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">...</div>
```

```js
const tabs = document.querySelectorAll('[role="tab"]');

tabs.forEach(tab => {
  tab.addEventListener('keydown', (e) => {
    const index = [...tabs].indexOf(e.currentTarget);
    let next;

    if (e.key === 'ArrowRight') next = tabs[(index + 1) % tabs.length];
    if (e.key === 'ArrowLeft') next = tabs[(index - 1 + tabs.length) % tabs.length];
    if (e.key === 'Home') next = tabs[0];
    if (e.key === 'End') next = tabs[tabs.length - 1];

    if (next) {
      e.preventDefault();
      tabs.forEach(t => t.setAttribute('tabindex', '-1'));
      next.setAttribute('tabindex', '0');
      next.focus();
      next.click(); // activate the tab
    }
  });
});
```

### Escape to Close
Every overlay, dropdown, and popover must close on `Escape`. Native `<dialog>` and `popover` handle this automatically. For custom components:

```js
element.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    close();
    triggerElement.focus(); // return focus to the element that opened it
  }
});
```

Rule: When closing an overlay, **always return focus** to the trigger element.

---

## Scroll-Driven Effects

### IntersectionObserver Reveals
Use for section reveals, lazy loading, and progress indicators. Never use scroll event listeners for visibility detection — they cause jank.

```js
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target); // reveal once
      }
    });
  },
  { threshold: 0.15, rootMargin: '0px 0px -60px 0px' }
);

document.querySelectorAll('[data-reveal]').forEach(el => observer.observe(el));
```

### Sticky Headers
```css
.site-header {
  position: sticky;
  top: 0;
  z-index: 10;
  background: oklch(from var(--color-bg) l c h / 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  transition: box-shadow 200ms ease;
}
.site-header[data-scrolled="true"] {
  box-shadow: 0 1px 0 var(--color-border);
}
```

```js
const header = document.querySelector('.site-header');
const observer = new IntersectionObserver(
  ([entry]) => {
    header.toggleAttribute('data-scrolled', !entry.isIntersecting);
  },
  { threshold: 1.0 }
);
// Observe a sentinel element at the top of the page
const sentinel = document.createElement('div');
sentinel.style.height = '1px';
document.body.prepend(sentinel);
observer.observe(sentinel);
```

### Scroll Snap for Carousels
Native CSS scroll snap eliminates the need for carousel libraries in most cases.

```css
.carousel {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none; /* Firefox */
}
.carousel::-webkit-scrollbar { display: none; }

.carousel__item {
  flex: 0 0 min(85vw, 400px);
  scroll-snap-align: center;
}
```

---

## Form Patterns

### Inline Validation Timing
- **Validate on blur** — not on every keystroke. Users should finish typing before seeing errors.
- **Exception: password strength** — show strength meter in real time.
- **Exception: character count** — show remaining characters in real time for constrained fields.
- **After first error, validate on change** — once a field has been marked invalid, re-validate as the user types so they see the error clear immediately.

```js
const input = document.querySelector('.validated-input');
let hasBlurred = false;

input.addEventListener('blur', () => {
  hasBlurred = true;
  validate(input);
});

input.addEventListener('input', () => {
  if (hasBlurred) validate(input); // re-validate only after first blur
});
```

### Multi-Step Form Progression
```html
<form aria-label="Account setup">
  <fieldset data-step="1" class="step active">
    <legend>Step 1 of 3: Your details</legend>
    <!-- fields -->
    <button type="button" data-next>Continue</button>
  </fieldset>
  <fieldset data-step="2" class="step">
    <legend>Step 2 of 3: Preferences</legend>
    <!-- fields -->
    <button type="button" data-prev>Back</button>
    <button type="button" data-next>Continue</button>
  </fieldset>
  <fieldset data-step="3" class="step">
    <legend>Step 3 of 3: Confirmation</legend>
    <!-- fields -->
    <button type="button" data-prev>Back</button>
    <button type="submit">Create account</button>
  </fieldset>
</form>
```

Rules:
- Use `<fieldset>` and `<legend>` for screen reader context.
- Show a progress indicator (step X of Y) — never just dots.
- Validate each step before advancing.
- Allow backward navigation without losing data.

### Error Association with `aria-describedby`
```html
<label for="email">Email address</label>
<input
  id="email"
  type="email"
  aria-invalid="true"
  aria-describedby="email-error"
  required
/>
<p id="email-error" class="field-error" role="alert">
  Enter a valid email address. Example: name@company.com
</p>
```

```css
.field-error {
  color: var(--color-error);
  font-size: var(--text-body-sm, 0.875rem);
  margin-top: 0.25rem;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}
```

### Required Field Indication
Mark required fields, not optional ones (most fields in most forms are required).
```html
<label for="name">
  Full name <span aria-hidden="true" class="required-mark">*</span>
</label>
<input id="name" required aria-required="true" />
```
Add a note at the top of the form: "Fields marked with * are required."

If most fields are optional (rare), flip the convention: mark optional fields instead.

---

## Overlay/Drawer vs Modal — Decision Tree

| Need | Use | Why |
|------|-----|-----|
| Block interaction until resolved | `<dialog>` with `showModal()` | Focus trap, backdrop, Escape built in |
| Supplementary content, dismissible | `popover` attribute | Light dismiss, no focus trap, no backdrop |
| Tooltip / hover info | `popover` with `popovertarget` | Auto-positioning, light dismiss |
| Mobile navigation | Sheet/drawer (CSS transform) | Slide from edge, backdrop, focus trap |
| Filter panel on desktop | Side panel (no overlay) | Visible alongside content |

### Native `<dialog>` — Use First
```css
dialog::backdrop {
  background: oklch(0% 0 0 / 0.5);
  backdrop-filter: blur(4px);
}
dialog[open] {
  animation: dialog-enter 200ms var(--ease-out-quart);
}
@keyframes dialog-enter {
  from { opacity: 0; transform: scale(0.96) translateY(8px); }
}
```

### Popover API
```html
<button popovertarget="menu">Options</button>
<div id="menu" popover>
  <ul role="menu">
    <li role="menuitem"><button>Edit</button></li>
    <li role="menuitem"><button>Duplicate</button></li>
    <li role="menuitem"><button>Delete</button></li>
  </ul>
</div>
```

### Z-Index Table
Maintain a flat z-index scale. Never use arbitrary values like `z-index: 9999`.

| Layer | z-index | Examples |
|-------|---------|----------|
| Base content | 0 | Page content |
| Sticky elements | 10 | Headers, floating actions |
| Dropdowns/popovers | 20 | Menus, tooltips |
| Overlays/drawers | 30 | Side panels, sheets |
| Modals | 40 | `<dialog>` |
| Toasts/notifications | 50 | Alert banners, snackbars |

---

## Anti-Patterns

### Hover-Only Interactions
If content is only visible on hover, it is invisible to:
- Touch screen users (no hover)
- Keyboard users (no hover)
- Screen reader users (no hover)

**Fix:** Always provide an equivalent non-hover path (click to toggle, always visible on mobile, keyboard-triggerable).

### Removed Focus Outlines
```css
/* NEVER DO THIS without a replacement */
*:focus { outline: none; }
```
If you remove `outline`, you MUST provide a visible `:focus-visible` replacement. No exceptions.

### Click on `<div>`
```html
<!-- NEVER -->
<div onclick="doThing()">Click me</div>

<!-- ALWAYS -->
<button type="button" onclick="doThing()">Click me</button>
```
`<div>` is not focusable, has no keyboard activation, and is invisible to assistive technology. Use `<button>` for actions and `<a>` for navigation.

### Infinite Scroll Blocking Footer
If the page uses infinite scroll, the footer is unreachable. Solutions:
- Place footer content in the sidebar instead.
- Use a "Load more" button instead of auto-loading.
- Set a max page count with a "View all" link.

---

## Worked Example: AI-Generated Contact Form → Accessible Form

### Before (typical AI output)

```html
<div class="contact-form">
  <div class="input-group">
    <input type="text" placeholder="Your Name" />
  </div>
  <div class="input-group">
    <input type="text" placeholder="Email" />
  </div>
  <div class="input-group">
    <textarea placeholder="Message"></textarea>
  </div>
  <div class="submit-btn" onclick="submit()">Submit</div>
</div>
```

Problems: No labels, placeholder-as-label, `<div>` as button, no error states, no focus management, no required indication, no `type="email"`, no `aria-*`, no form element.

### After (all 8 states, accessible)

```html
<form class="contact-form" novalidate>
  <p class="form-note">Fields marked with <span aria-hidden="true">*</span> are required.</p>

  <div class="field">
    <label for="cf-name">
      Full name <span aria-hidden="true" class="required-mark">*</span>
    </label>
    <input id="cf-name" name="name" type="text" required aria-required="true" autocomplete="name" />
    <p id="cf-name-error" class="field-error" role="alert" hidden></p>
  </div>

  <div class="field">
    <label for="cf-email">
      Email address <span aria-hidden="true" class="required-mark">*</span>
    </label>
    <input id="cf-email" name="email" type="email" required aria-required="true" autocomplete="email" />
    <p id="cf-email-error" class="field-error" role="alert" hidden></p>
  </div>

  <div class="field">
    <label for="cf-message">
      Message <span aria-hidden="true" class="required-mark">*</span>
    </label>
    <textarea id="cf-message" name="message" rows="5" required aria-required="true"></textarea>
    <p id="cf-message-error" class="field-error" role="alert" hidden></p>
  </div>

  <button type="submit" class="btn">Send message</button>
</form>
```

```css
.contact-form .field {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}
.contact-form label {
  font-size: var(--text-body-sm, 0.875rem);
  font-weight: 500;
  color: var(--color-text);
}
.required-mark { color: var(--color-error); }

.contact-form input,
.contact-form textarea {
  padding: 0.625rem 0.75rem;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  font: inherit;
  transition: border-color 150ms ease, box-shadow 150ms ease;
}
.contact-form input:focus,
.contact-form textarea:focus {
  outline: none;
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px oklch(from var(--color-primary) l c h / 0.15);
}
.contact-form input[aria-invalid="true"],
.contact-form textarea[aria-invalid="true"] {
  border-color: var(--color-error);
  box-shadow: 0 0 0 3px oklch(from var(--color-error) l c h / 0.1);
}
.field-error {
  color: var(--color-error);
  font-size: var(--text-body-sm, 0.875rem);
}
```

Key improvements:
- `<form>` element with `novalidate` (custom validation, not browser default)
- Visible `<label>` linked to each input via `for`/`id`
- `type="email"` for email input
- `autocomplete` attributes for autofill
- `<button type="submit">` with specific label ("Send message", not "Submit")
- `aria-required`, `aria-invalid`, `aria-describedby` wiring
- Error messages in `role="alert"` for screen reader announcement
- Required field indication with form-level note

---

## Evaluation Protocol
When auditing interactions, check:
1. Can the entire UI be navigated via keyboard?
2. Are focus rings visible and distinct?
3. Do all buttons have distinct active and hover states?
4. Are forms using visible labels instead of placeholders?
5. Are long operations using optimistic UI or explicit loading feedback?
6. Does `Escape` close every overlay, returning focus to the trigger?
7. Are all interactive elements `<button>` or `<a>`, never `<div>` or `<span>`?
8. Do multi-step forms validate per step and allow backward navigation?
9. Is there a skip-to-content link as the first focusable element?
10. Are error messages linked to inputs via `aria-describedby`?
11. Does the z-index scale follow a flat, documented system?
12. Are touch targets at least 44x44px?
13. Do carousels use native scroll snap rather than JS libraries?

---

## Decision Rules

- **When to use `<dialog>` vs `popover`**: If the user MUST respond before continuing, use `<dialog>`. If the content is supplementary and dismissible, use `popover`.
- **When to validate on keystroke vs blur**: Blur by default. Keystroke only for real-time feedback (password strength, character count, search-as-you-type).
- **When to use infinite scroll vs pagination**: If the content has a footer, use pagination or "load more". Infinite scroll only for feeds where the footer is non-essential.
- **When to use optimistic UI vs loading state**: Optimistic for low-stakes, easily reversible actions (likes, toggles, rearranging). Loading state for high-stakes, irreversible actions (payments, deletions, publishes).
