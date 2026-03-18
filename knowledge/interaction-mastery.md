# Interaction Mastery

This file defines how to design states, feedback, and structural interactions for components.

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

### 2. Focus Rings Are Mandatory
Never use `outline: none` without providing a visible replacement. Use `:focus-visible` to style focus only for keyboard users.

```css
button:focus { outline: none; }
button:focus-visible {
  outline: 2px solid var(--color-focus);
  outline-offset: 2px;
}
```

Focus rings must be high contrast (3:1 minimum) and clearly offset from the element.

### 3. Forms and Inputs
* **Placeholders are not labels**: They disappear on input. Always use visible `<label>` elements.
* **Validate on blur**, not on keystroke (exception: password strength).
* **Error placement**: Place errors directly below the input, linked via `aria-describedby`.

### 4. Overlays and Modals
Do not rely on complex JS for focus trapping. Use native web primitives.
* **Modals**: Use `<dialog>` with `dialog.showModal()` for automatic focus trapping and top-layer stacking.
* **Popovers**: Use the native `popover` attribute for tooltips and dropdowns to ensure light-dismiss and correct z-index.

### 5. Destructive Actions: Undo > Confirm
Confirmation dialogs are often clicked through mindlessly.
Prefer optimistic deletion with a temporary Undo toast.
Reserve confirmation dialogs only for irreversible, high-cost actions (e.g., Account Deletion).

### 6. Loading States
* **Optimistic updates**: Update UI immediately for low-stakes actions (likes, toggles). Roll back on failure.
* **Skeletons > Spinners**: Use skeleton screens for page transitions; they establish layout expectations and feel faster than generic spinners.

### 7. Dashboard Hardening & Anti-Card Overuse
Generic card containers are often overused in dense UIs.
Data metrics should breathe. Use logical grouping via `border-top`, `divide-y`, or purely negative space instead of wrapping every metric in a white box with a drop shadow. Use cards ONLY when elevation functionally communicates hierarchy.

## Evaluation Protocol
When auditing interactions, check:
1. Can the entire UI be navigated via keyboard?
2. Are focus rings visible and distinct?
3. Do all buttons have distinct active and hover states?
4. Are forms using visible labels instead of placeholders?
5. Are long operations using optimistic UI or explicit loading feedback?