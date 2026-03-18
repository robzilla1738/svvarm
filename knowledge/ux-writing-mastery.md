# UX Writing Mastery

This file defines how to write, evaluate, and refine copy for digital interfaces.

The goal is to produce copy that is unambiguous, actionable, and appropriately toned. UX writing is not marketing; it is interaction design through words.

## Core Principles

### 1. The Button Label Rule
Never use ambiguous verbs. A button label must describe the exact outcome of clicking it.

* **Bad**: OK, Submit, Yes, No, Cancel, Click here
* **Good**: Save changes, Create account, Delete message, Keep editing, Download PDF

For destructive actions, name the destruction:
* **Bad**: Remove, Delete selected
* **Good**: Delete project, Delete 5 items

### 2. Error Message Formula
Every error message must answer three questions:
1. What happened?
2. Why?
3. How to fix it?

* **Format error**: "[Field] must be [format]. Example: [example]"
* **Missing required**: "Please enter [what's missing]."
* **Network error**: "We couldn't reach [thing]. Check your connection and [action]."

Do not blame the user.
* **Bad**: "You entered an invalid date."
* **Good**: "Please enter a date in MM/DD/YYYY format."

### 3. Voice vs. Tone
Voice is the brand's personality (always consistent). Tone adapts to the moment.
* **Success**: Celebratory, brief.
* **Error**: Empathetic, helpful. Never use humor for errors.
* **Loading**: Reassuring ("Saving your work...").
* **Destructive confirm**: Serious, clear.

### 4. Empty States Are Onboarding
An empty state must do three things:
1. Acknowledge the state.
2. Explain the value.
3. Provide a primary action.

* **Bad**: "No items."
* **Good**: "No projects yet. Create your first project to get started."

### 5. Terminology Consistency
Pick one term per concept and never vary it for "creative variety."
* Pick one: Delete, Remove, or Trash.
* Pick one: Settings, Preferences, or Options.
* Pick one: Sign in, Log in, or Enter.

### 6. Accessibility in Writing
* **Link text**: Must have standalone meaning. ("View pricing plans," not "Click here").
* **Alt text**: Describe the information, not the visual. ("Revenue increased 40% in Q4," not "Line chart").
* **Redundancy**: If a heading explains it, do not repeat it in the intro. 

## Evaluation Protocol
When auditing UX copy, check:
1. Are buttons verb-led and specific?
2. Do errors explain how to recover?
3. Are empty states actionable?
4. Is terminology strictly consistent?
5. Are there any ambiguous "Submit" or "Cancel" actions?