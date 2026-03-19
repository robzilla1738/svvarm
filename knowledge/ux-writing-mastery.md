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

For confirmation dialogs, make both options specific:
* **Bad**: "Delete this file?" → [Cancel] [OK]
* **Good**: "Delete this file?" → [Keep file] [Delete file]
* **Good**: "Discard unsaved changes?" → [Keep editing] [Discard changes]
* **Good**: "Remove from team?" → [Keep member] [Remove from team]

For multi-step flows, the CTA should indicate the next step, not the final outcome:
* **Step 1**: "Continue to payment" (not "Buy now")
* **Step 2**: "Review order" (not "Buy now")
* **Step 3**: "Place order — $49.99" (include the price on the final action)

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

---

## 5 Complete Empty States

### 1. First-Time User (No Data Yet)
```html
<div class="empty-state">
  <svg class="empty-state__icon" aria-hidden="true"><!-- simple illustration --></svg>
  <h2>No projects yet</h2>
  <p>Projects help you organize your work into focused spaces. Create your first one to get started.</p>
  <button class="btn">Create project</button>
</div>
```
Tone: Warm, encouraging. The user hasn't failed — they just haven't started.

### 2. No Search Results
```html
<div class="empty-state">
  <h2>No results for "quarterly report"</h2>
  <p>Try a different search term or check the spelling.</p>
  <ul class="empty-state__suggestions">
    <li><button class="link">Browse all documents</button></li>
    <li><button class="link">Clear filters</button></li>
  </ul>
</div>
```
Tone: Helpful, directive. Show the exact query. Offer concrete next steps, never just "try again."

### 3. Error-Caused Empty
```html
<div class="empty-state">
  <h2>Unable to load messages</h2>
  <p>Something went wrong on our end. Your messages are safe — we just can't show them right now.</p>
  <button class="btn" onclick="retry()">Try again</button>
  <p class="text-muted">If this keeps happening, <a href="/support">contact support</a>.</p>
</div>
```
Tone: Reassuring, honest. Acknowledge the error without jargon. "Something went wrong" — never "Error 500" or "An unexpected error occurred."

### 4. Filtered Empty
```html
<div class="empty-state">
  <h2>No tasks match these filters</h2>
  <p>There are 24 tasks total, but none match "high priority" + "assigned to me."</p>
  <button class="btn-secondary" onclick="clearFilters()">Clear all filters</button>
</div>
```
Tone: Factual. Show what filters are active and how many items exist without them. The user needs to understand WHY the list is empty.

### 5. Completed List (All Done)
```html
<div class="empty-state empty-state--success">
  <svg class="empty-state__icon" aria-hidden="true"><!-- checkmark --></svg>
  <h2>All caught up</h2>
  <p>You've completed every task in this sprint. Nice work.</p>
</div>
```
Tone: Satisfied, brief. This is a success state disguised as an empty state. Celebrate without being over-the-top. No confetti, no exclamation marks.

---

## Terminology Consistency Table

Pick one term per row and use it everywhere. Document the choice in the project's design system.

| Concept | Recommended | Avoid | Notes |
|---------|------------|-------|-------|
| Authentication | **Sign in** / **Sign out** | Log in, Log out, Login | "Sign in" is more widely understood; matches Apple, Google, Microsoft conventions |
| Destruction | **Delete** | Remove, Trash, Erase | "Delete" is unambiguous. Use "Remove" only for non-destructive detachment (remove from list, not destroy) |
| Configuration | **Settings** | Preferences, Options, Config | "Settings" is the most common pattern across platforms |
| Creation | **Create** | Add, New, Make | "Create" for new entities ("Create project"). "Add" only for adding TO something ("Add member to team") |
| Modification | **Edit** | Modify, Update, Change | "Edit" for entering edit mode. "Save" for persisting changes |
| Navigation back | **Back** | Go back, Return, Previous | Just "Back" — no verb prefix needed |
| Confirmation | **Save** | Apply, Confirm, Done | "Save changes" for forms. "Done" only for flows with no persistence |
| Account | **Account** | Profile, My account | "Account" for settings/billing. "Profile" only for public-facing identity |
| Search | **Search** | Find, Look up, Query | "Search" as both label and action verb |
| Upload | **Upload** | Attach, Import | "Upload" for files. "Import" only for structured data (CSV, database) |

---

## Form Validation Messages

### By Validation Type

| Type | Bad | Good |
|------|-----|------|
| Required | "This field is required" | "Enter your email address" |
| Email format | "Invalid email" | "Enter a valid email address. Example: name@company.com" |
| Password length | "Too short" | "Password must be at least 8 characters" |
| Password match | "Passwords don't match" | "Passwords don't match. Re-enter your password." |
| Min length | "Too short" | "Company name must be at least 2 characters" |
| Max length | "Too long" | "Bio must be 160 characters or fewer. You have 23 characters remaining." |
| Number range | "Invalid number" | "Enter a number between 1 and 100" |
| URL format | "Invalid URL" | "Enter a valid URL starting with https://" |
| Phone format | "Invalid phone" | "Enter a phone number with area code. Example: (555) 123-4567" |
| Date format | "Invalid date" | "Enter a date in MM/DD/YYYY format" |
| Unique/taken | "Already exists" | "This username is taken. Try another one." |

### Server & Rate Errors

```
// Server error (generic)
"Something went wrong. Your changes weren't saved. Try again."

// Server error (specific)
"We couldn't update your email. Our servers are temporarily unavailable. Try again in a few minutes."

// Rate limiting
"You're making requests too quickly. Wait a moment and try again."

// File too large
"This file is over 10 MB. Choose a smaller file or compress it first."

// Unsupported format
"This file format isn't supported. Upload a JPG, PNG, or WebP image."
```

---

## Loading State Copy

### Progress Indicators
Use specific language when you know what's happening. Never just "Loading..."

| Context | Bad | Good |
|---------|-----|------|
| Saving a document | "Loading..." | "Saving your changes..." |
| Uploading a file | "Please wait" | "Uploading report.pdf... 45%" |
| Generating content | "Loading..." | "Generating summary..." |
| Searching | "Loading..." | "Searching 2,340 documents..." |
| Initial page load | "Loading..." | Show skeleton screens — no text needed |

### Skeleton Behavior
Skeleton screens need no copy. They communicate "content is coming" through visual shape. Adding "Loading..." text on top of a skeleton is redundant.

### Long-Running Operations (>5 seconds)
```html
<div class="processing-state">
  <div class="progress-bar" role="progressbar" aria-valuenow="65" aria-valuemin="0" aria-valuemax="100">
    <div class="progress-bar__fill" style="width: 65%"></div>
  </div>
  <p>Processing your export... This may take a minute for large datasets.</p>
  <p class="text-muted">You can leave this page. We'll email you when it's ready.</p>
</div>
```

### Background Processing
When work continues after the user navigates away:
```
// Toast on action
"Export started. We'll email you when it's ready."

// Email subject
"Your data export is ready"

// Email body
"The export you requested on March 18 is ready to download. This link expires in 7 days."
```

---

## Microcopy Patterns

### Timestamps
| Time elapsed | Display |
|-------------|---------|
| < 1 minute | "Just now" |
| 1–59 minutes | "12 minutes ago" |
| 1–23 hours | "3 hours ago" |
| 1–6 days | "Tuesday" (day name) |
| 7–364 days | "Mar 12" |
| 1+ years | "Mar 12, 2025" |

Never: "3/12/2025 14:23:45" in user-facing UI. Save ISO timestamps for data tables and APIs.

### Counts
| Count | Display |
|-------|---------|
| 0 | "No comments" (not "0 comments") |
| 1 | "1 comment" (singular) |
| 2–999 | "42 comments" |
| 1,000–9,999 | "2,340 comments" (comma separator) |
| 10,000–999,999 | "12.3K comments" |
| 1,000,000+ | "1.2M comments" |

### Truncation
When text must be cut, use an ellipsis (`…`) and ensure the full text is available (tooltip, expand, or click-through).
```css
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
/* Multi-line truncation */
.truncate-multiline {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

Never truncate in the middle of a word. Never truncate labels, headings, or CTAs.

### Confirmation Feedback
After a successful action, confirm what happened with brief, specific copy:

| Action | Bad | Good |
|--------|-----|------|
| Save | "Success!" | "Changes saved" |
| Delete | "Done" | "Project deleted" |
| Copy | "Copied!" | "Link copied to clipboard" |
| Send | "Sent!" | "Invitation sent to 3 members" |
| Upload | "Upload complete" | "report.pdf uploaded" |

---

## Anti-Patterns

### "Please" Overuse
One "please" per flow is fine. More than that reads as servile or passive-aggressive.
- **Bad**: "Please enter your name. Please make sure it matches your ID. Please click continue."
- **Good**: "Enter your name as it appears on your ID." → [Continue]

### Exclamation Marks in Errors
Exclamation marks in error messages sound alarming or accusatory.
- **Bad**: "Invalid password!"
- **Good**: "Incorrect password. Try again or reset your password."

### "Oops!" for Serious Errors
"Oops" trivializes the user's problem. It's appropriate for a 404. It's not appropriate for "we lost your data."
- **Bad**: "Oops! Something went wrong."
- **Good**: "Something went wrong. Your changes weren't saved. Try again."

### Technical Jargon in User-Facing Copy
- **Bad**: "Error 500: Internal server error. Request ID: abc123"
- **Good**: "Something went wrong on our end. Try again in a few minutes."
- Exception: Developer tools, APIs, and admin panels can use technical language when the audience expects it.

### Vague CTAs in Marketing
- **Bad**: "Get started" (started with what?), "Learn more" (learn more about what?)
- **Good**: "Start your free trial", "See pricing plans", "Read the case study"

### Gendered Language
- **Bad**: "The user can manage his settings"
- **Good**: "Users can manage their settings" or "You can manage your settings"

---

## Worked Example: AI SaaS Pricing Page Copy

### Before (typical AI output)

```
Unlock the Power of AI-Driven Analytics!

Our cutting-edge platform leverages state-of-the-art machine learning
to deliver actionable insights that drive growth and maximize ROI.

🚀 Starter Plan — $29/mo
Everything you need to get started on your journey!
- Up to 10,000 API calls
- Basic analytics dashboard
- Email support

⭐ Pro Plan — $99/mo (Most Popular!)
Take your business to the next level!
- Up to 100,000 API calls
- Advanced analytics & reporting
- Priority support
- Custom integrations

💎 Enterprise — Contact Sales
The ultimate solution for large-scale operations!
- Unlimited API calls
- Dedicated account manager
- SLA guarantee
- Custom everything
```

Problems: Exclamation marks everywhere, emoji as decoration, "cutting-edge" / "state-of-the-art" / "leverages" / "actionable insights" are meaningless filler, "Get started on your journey" says nothing, "Take your business to the next level" says nothing, "The ultimate solution" says nothing.

### After (specific, human, sharp)

```html
<section class="pricing">
  <h2>Simple pricing, no surprises</h2>
  <p>All plans include a 14-day free trial. No credit card required.</p>

  <div class="pricing-grid">
    <div class="plan">
      <h3>Starter</h3>
      <p class="plan__price">$29<span>/month</span></p>
      <p class="plan__description">For small teams analyzing up to 10K events per month.</p>
      <ul>
        <li>10,000 API calls / month</li>
        <li>7-day data retention</li>
        <li>3 team members</li>
        <li>Email support (48-hour response)</li>
      </ul>
      <a href="/signup?plan=starter" class="btn-secondary">Start free trial</a>
    </div>

    <div class="plan plan--featured">
      <h3>Pro</h3>
      <p class="plan__price">$99<span>/month</span></p>
      <p class="plan__description">For growing teams that need deeper analysis and faster support.</p>
      <ul>
        <li>100,000 API calls / month</li>
        <li>90-day data retention</li>
        <li>10 team members</li>
        <li>Slack + email support (4-hour response)</li>
        <li>Custom dashboards</li>
        <li>CSV + API export</li>
      </ul>
      <a href="/signup?plan=pro" class="btn">Start free trial</a>
    </div>

    <div class="plan">
      <h3>Enterprise</h3>
      <p class="plan__price">Custom</p>
      <p class="plan__description">For organizations with compliance requirements or high-volume needs.</p>
      <ul>
        <li>Unlimited API calls</li>
        <li>Unlimited data retention</li>
        <li>Unlimited team members</li>
        <li>Dedicated support engineer</li>
        <li>SSO + SCIM provisioning</li>
        <li>99.9% uptime SLA</li>
      </ul>
      <a href="/contact-sales" class="btn-secondary">Talk to sales</a>
    </div>
  </div>
</section>
```

Key improvements:
- No exclamation marks, no emoji
- Each plan description says WHO it's for and WHY, not generic hype
- Features are specific (numbers, timeframes) not vague ("advanced analytics")
- CTA is "Start free trial" (specific) not "Get started" (vague)
- Enterprise CTA is "Talk to sales" not "Contact us"
- No "Most Popular" badge — the visual treatment (`.plan--featured`) communicates it
- No buzzwords: "cutting-edge", "leverages", "actionable insights" all eliminated

---

## Evaluation Protocol
When auditing UX copy, check:
1. Are buttons verb-led and specific?
2. Do errors explain how to recover?
3. Are empty states actionable and contextual?
4. Is terminology strictly consistent throughout the interface?
5. Are there any ambiguous "Submit" or "Cancel" actions?
6. Do confirmation dialogs have two specific options (not OK/Cancel)?
7. Is "Please" used at most once per flow?
8. Are error messages free of exclamation marks and humor?
9. Are loading states specific about what's happening?
10. Do timestamps use relative time for recent events?
11. Is link text meaningful without surrounding context?
12. Are counts formatted with proper pluralization and abbreviation?
