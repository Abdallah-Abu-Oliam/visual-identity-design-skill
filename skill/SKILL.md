---
name: visual-identity
description: |
  Turn a project or idea into a brand, and derive its visual identity from that.
  Use when the user asks to "create a brand", "design a visual identity", "make a
  logo", "build brand guidelines", "brand my project", "choose brand colours",
  "name my startup", or discusses brand identity, logo design, brand books, or
  identity systems. Runs strategy first, then derives every visual decision from it.
version: 1.0.0
---

# Visual Identity

Turns a project into a **brand**, whose deliverable is a **visual identity**.

This is not a design skill. A design skill makes things look good. This one decides who
the brand *is*, then derives how it looks. **The order is enforced.**

---

## The two rules everything rests on

**1 · Every visual decision traces back to a strategy decision.** Blue is not "nice" — it
is trust, which came from a value, which came from the brief. When presenting any choice,
show the chain. A decision nobody can trace back gets overturned by the first person who
dislikes it.

**2 · Never ask the user to generate. Ask them to choose.** Most people cannot answer
"what are your brand values?" — they can react instantly to three proposed ones. A blank
question returns a blank. Draft from what you already know, present it, let them correct.

**3 · This is a recursive process. Looping is the process working, not failing.**

The gates exist to catch problems while they are still cheap. A loop at the art direction
gate costs an afternoon. The same problem discovered at the guidelines stage costs the
identity. **Never push forward to avoid going back** — and never present a loop to the user
as a setback.

| Signal | Return to | What it means |
|--------|-----------|---------------|
| A direction is rejected | Same step — new directions | Normal. This is what the gate is for |
| Directions rejected repeatedly | **Phase 1, the brief** | Stop iterating on images. Something in the strategy was never captured |
| No logo concept lands | **Step 4, the mind map** | Not enough drawable nodes. Push the keywords further down |
| Assembly looks generic — the boring test | **3.5, pattern** | Expected. This is the designed path, not a failure |
| The mark dies on packaging or signage | **3.1, logo** | Repair |
| The palette turns muddy in print | **3.2, colour** | Repair. CMYK cannot reach every RGB colour |
| A guideline rule contradicts another | Wherever the rule was decided | Defect. Fix the source, not the sentence |

**Tell the user which loop is happening and why.** "This is the third direction you have
turned down — that usually means the brief missed something, so let us go back to it" is a
diagnosis. Silently generating a fourth set of boards is not.

These three are not style preferences. They are what separates this from a form with a
design theme.

---

## Before anything: resume

**Read `brand/` first. Always.** This process spans sessions — a user does the brief on
Monday and looks at boards on Wednesday. Re-asking the seven questions because you did not
check is the fastest way to lose them.

```
brand/
  brief.md              Phase 1
  questionnaire.md      answers, read back from the form
  research/             FINDINGS.md + folders per target
  mindmap.html
  art-direction/        one folder per direction + boards.html
  logos/                concepts/ · iterations/ · export/
  identity/             palette · type · pattern
  mockups/
  presentation/
  guidelines/
  STATE.md              what is done, what gate we are at, what is next
```

If `brand/STATE.md` exists, read it and say where things stand before doing anything else.
If not, start at Phase 1. **Write to these files as you go, not at the end** — an
unrecorded decision is a lost one.

---

## Phase 1 — The brief

Seven elements. **Facts the owner already has** — capture, not creative work.

Load `references/brief.md` for each element's meaning, processing method, the question
that actually gets an answer, and the single scripted push-back for its failure mode.

1. Quick tour — what it does
2. Name
3. Reason for the name
4. Targeted audience
5. Competitors
6. Competitive advantages
7. Targeted feelings

**Ask the questions as written in the reference, not the labels.** "What is your target
audience?" returns "everyone". "Who would be genuinely disappointed if this disappeared
tomorrow?" returns actual people.

**Push back once, then move on.** One sharper follow-up per vague answer. Take what comes
back. This is a brief, not an interrogation.

**If there is no name yet — or it is provisional — load `references/naming.md`** and run
the method. Do not hand the user eleven steps; generate candidates from the brief, filter
them yourself, and bring back a short list with reasoning. Never present a name as legally
cleared — we can search, we cannot clear.

Write to `brand/brief.md`.

---

## Phase 2 — Mood board and art direction

**Why this phase exists.** Three reasons, and the middle one is where its value is:

1. **It proves we understood the request.** The user sees their brief turned into
   something visual before anything is committed.
2. **It harvests modifications while they are still cheap.** The user sees roughly how the
   final thing will look while nothing has been built. **The bulk of their changes should
   be extracted here** — every one caught now costs nothing, and every one missed costs a
   rebuild later.
3. **It sets expectations.** They may be picturing dense and colourful while the work is
   heading toward simple and quiet. Far better to collide here than at delivery.

Five steps. The first three are the three R's.

### Step 1 · Read

Read the brief, the questionnaire and every file the user shared. Output **keywords, and
the reading notes that produced them.**

**Reading is extraction, not summarising.** Strategy answers silently decide visual things.
"We stand against treating knives as weapons" eliminates red, tactical black and aggressive
angles — before anyone opens a colour picker. Catch those and write them down as you go.
`references/questionnaire-example-alnisal.md` demonstrates this; every extraction is marked
`→ Reading note`.

**Conflicts get caught here, not resolved here.** When a stated answer contradicts an
implied constraint, the implication usually wins — but it goes to the user, never decided
silently.

#### The questionnaire

47 questions. Nobody answers 47 in a chat; they quit around twelve.

**So it is 7 asked and 6 review passes.** The brief already supplies enough to draft
roughly 35 of them. The user corrects rather than composes.

- Template and its rationale: `references/questionnaire-template.md`
- Worked, annotated example: `references/questionnaire-example-alnisal.md`
- The form: `assets/questionnaire.html` — **copy it into the project folder** (it must live
  inside the project or the browser renders it static and no JavaScript runs), open it,
  call `prefill({...}, true)` to inject drafts, wait, then call `collect()` to read back.
  It autosaves; it is bilingual with RTL; it never blocks on a blank field.

**Form for breadth, chat for depth.** Collect everything in the form, then take the two or
three answers that are vague or contradictory into conversation.

**Question 14 is the model for every hard question.** Rather than "send me logos you like"
— which returns nothing — it shows five logo types with famous examples and asks for two.
Everyone can answer that. **Reach for this shape whenever a question keeps coming back
empty:** named options, recognisable examples, a hard limit.

**Questions 7–12 are usually blank. Never block on them.** Q14 covers most of the gap and
the mood board answers the rest.

### Step 2 · Review

Re-read the documents and the conversation, then ask the few questions still open.
Deliberately light. The conflicts caught during Read go to the user here.

### Step 3 · Research

Load `references/research.md` — six search targets, every source with its tested status and
role, the folder layout, and how to run it with subagents.

The essentials:

- **Behance** is the strongest source and the only one that surfaces finished identity
  systems. It renders without login. **It never reaches the client** — other designers'
  copyrighted portfolio work.
- **Unsplash / Pexels** fill the boards. Free for commercial use.
- **Pinterest** renders nothing anonymously. Ask the user to sign in themselves, or have
  them paste pin URLs. **Never type their credentials.**
- **The named brands' own sites**, via browser screenshot, for first-party category
  conventions.
- **Search in the market's own language.** A brand in Iraq or the Gulf loses sales to local
  competitors, not the global category leader.

**`FINDINGS.md` is the deliverable.** A folder of screenshots nobody wrote about is dead
weight.

**Say the cost before running it.** This is the most expensive step in the process.

### Step 4 · Mind map and brainstorming

Every keyword from all three R's into one map, company at the centre.

**Connect the regular and the irregular.** Knives → strength → sharpness → steel and grey
is the category's identity, not this brand's. Every competitor's map has that branch. **The
strange word is where anything ownable comes from.**

**Derive until the word has a shape. This is the point of the step.** Push each keyword
down into sub-words until a child of it can actually be drawn. "Precision" has no
silhouette. **عين الصقر — the falcon's eye — does.** Pupil, ring, a sharp curve.

This is the crossing point of the whole process: everything before it is words, everything
after is form.

**Competing metaphors get resolved here.** Two metaphors in one mark usually means neither
lands — the map is where they merge or one is dropped.

### Step 5 · Art direction — **HARD GATE**

**Nothing downstream begins until a direction is approved.** No logo, no palette, no
typography. The step repeats — new directions, new boards — until the user agrees.

If it is rejected several times over, the problem is upstream. Stop iterating on images and
go back to the brief; something in the strategy was never captured.

**Which directions are eligible** — three filters, in order:

1. **The company itself.** A tech company cannot take an old-luxury direction. Category
   rules whole territories out before taste enters.
2. **The target customer.**
3. **Competitors and the competitive advantage.** Competitors mark what is occupied; the
   advantage marks what must be loudest.

**Do not fix the number of directions in advance.** Some briefs leave one viable, others
five. Show what genuinely survives — never pad to a count, never cut a real option.

**Name each one.** A named direction can be discussed; an unnamed one can only be reacted
to.

**Which images fill each board** — brand strategy, user preferences, and the brands they
named, combined. Never one alone.

**Cohesion is the quality bar.** A pile of individually good images is not an art
direction. Each board must look like one world.

Delivered as a local HTML page per direction. User picks; read the choice back.

---

## Phase 3 — Visual identity

Order: **logo → colour → typography → assembly → pattern.** The mark is the hardest
constraint; the rest accommodate it.

### 3.1 Logo

**Load `references/logo-fundamentals.md` first.** It governs everything below.

Three things it fixes, all of which a model gets wrong by default:

- **A logo does not carry meaning; it collects it.** The swoosh meant nothing in 1971. A
  mark that tries to explain the business is doing a job that was never its own.
- **Appropriate means the *feel* fits, not that the picture explains.** Asked for a knife
  brand, a model draws a knife; asked for a coffee shop, a bean. **Test every concept
  against this before presenting it** — if the mark depicts the product, it is an
  illustration, not a logo.
- **The three rules: appropriate · distinctive · simple.** Rules 2 and 3 pull against each
  other, and that tension is the craft. Simplicity pushed far enough lands on shapes
  everyone already owns — a triangle in a circle satisfies "simple" by destroying
  "distinctive". **Distinctive is judged against the competitor audit, not against taste.**
  Memorable has an operational test: *see it once, redraw it from memory.*

Then load `references/logo-types.md` — the type is **derived, not asked.** Name length,
existing brand recognition, the competitor audit, personality, and the required
applications narrow it before taste enters. Q14 is an input to this, not a substitute for
it; where they disagree, say so and explain — never silently overrule, never silently
comply.

Load `references/logo-generation.md` for the pipeline. SVG, never image generation — a mark
must be vector, editable as curves, exactly repeatable.

**Concepts are presented colourless.** Colour rescues weak forms and flatters bad ones.
Judge the shape alone or the judgement is worthless.

**Three to five genuinely different concepts**, each tracing to a different drawable node
from the mind map — then iterations inside the chosen one. Parallel subagents for both.

**Include the favicon strip** — every option at 64, 32 and 16px. "It must survive at
favicon size" is an aspiration until you can see it failing.

**Present each concept with its derivation.** "The falcon's eye, where the curve doubles as
a blade edge." A concept nobody can trace cannot be defended later.

Export with `scripts/export.sh`. It refuses SVGs still holding live `<text>` — rasterisers
substitute fonts, which distorts Latin and can break Arabic letter joining outright.

**Bilingual wordmarks are drawn twice**, locking to one symbol. Never translated at the
end. Arabic calligraphic wordmarks are a specialist craft — set them in a real Arabic
typeface or hand them to a human; do not emit approximate bezier paths.

### 3.2 Colour

Load `references/color.md`.

**The primary is derived**, from audience, feelings, added value, the competitor study, and
brand character — then matched against colour meanings. **This is the moment
differentiation is spent.**

**60/30/10 is about area, not importance.** The 60% is usually the calmest colour; the 10%
is where the eye goes.

**The meanings table is cultural, and it is where everyone starts** — which is why everyone
ends up in the same place. It gives the category convention; the competitor audit decides
whether to take it or break it.

**Differentiate on register before hue.** Hue is the most copyable axis. Volume, texture
and composition are emptier and harder to take back.

**Four codes per swatch** — HEX, RGB, CMYK, **PMS**. Check contrast and colour blindness.

### 3.3 Typography

Primary, secondary, hierarchy — **and fallbacks, always.** Without them the guideline
breaks the moment someone opens a document without the licensed font. Both scripts get set
separately if the brand is bilingual.

### 3.4 Assembly — the boring test

Put logo, colour and type together. **Then ask: could this belong to any identity?**

If yes — and it usually is — that is the trap. Nothing is *wrong*; it is correct and
generic, which is the default output of a competent process. Without a step that names it,
it ships. Failing this sends the work to 3.5.

### 3.5 Pattern — where ownability comes from

Load `references/pattern.md`.

Not decoration applied afterwards. **Two routes, both valid:**

- **From the brand's own material.** جمرة is an ember, so the pattern came from the cracked
  surface of burning coal — لهب, the flame. Ask what the brand is physically made of, made
  from, or used on. The material is already theirs; nobody takes it without taking the
  brand.
- **From an icon system.** Design a set, then repeat and combine. Saudi Founding Day built
  nine icons and generated modular and circular patterns from them. Scales further — a
  family of patterns plus an icon library — but costs more up front.

**Name it.** لهب, not "the pattern". A named asset can be discussed and defended.

**It comes from the same root as everything else** — the mind map's drawable node becoming
a graphic system. And it is a *register* move, not a hue move, which is why the
differentiation survives.

**Apply it across the identity, not in one place.** Used once it is decoration; used
consistently it becomes what people recognise before they read the name. Specify correct
and incorrect cropping, and decide how it behaves under content — a pattern that fights the
message has cost more than it gained.

---

## Phase 4 — Presentation

### Mockups

Two tests, both pass/fail: **realism** (genuinely photographic, not a flat render) and
**appropriateness** (the surface the logo will actually appear on). The generic stationery
flat-lay is the tell of a template applied without thinking.

**Q13 is the mockup list.**

**Mockups are not a direction choice** — direction was settled four gates earlier. They
answer *does the way we chose survive a shop sign*. They can still send work backwards; that
recursion is repair, not choice.

**Always ask which surfaces before building any.** Tier three costs the user real effort or
money.

| Tier | Route |
|------|-------|
| Screens — app icon, web, social, favicon | Built natively. Free |
| Flat — cards, letterhead, signage | Composited onto a photo |
| Curved, textured — cups, packaging, leather | Optional, see below |

**Composited mockups are review artifacts, not deliverables** — capture resolution is
roughly 800px, fine on screen and too small to print. Say so.

For curved and textured, ranked: **A** · PSD template in **Photopea** — free, browser-based,
smart objects keep the mark exactly correct. **Recommended.** **B** · generate the scene,
composite the real mark yourself. **C** · full image generation — fast, and the mark will be
wrong; image tools invent letterforms and mangle Arabic. Internal only. **D** · skip, always
allowed.

When offering B or C, **build the prompt from the brief** — approved direction, palette
with hex codes, materials, lighting, exact surface. A generic template is not worth
pasting.

### Presentation

Nothing new is decided. Assembly and delivery, in this order:

**typeface → palette → logo options → assembly → pattern → applications**

**The before-and-after is the argument.** Assembly without the pattern looks correct and
generic; with it, ownable. Showing both explains the pattern better than any paragraph.

---

## Phase 5 — Guidelines

**Load `references/guidelines.md`** — the six core elements with every subsection, thirteen
optional sections each with the trigger that decides inclusion, and the quality bar.

`references/guidelines-analysis.md` holds what three real brand books actually do, read in
full. The books themselves are not shipped with this skill; the analysis is.

| # | Element | Contains |
|---|---------|----------|
| 1 | Brand essence | Vision and values · personality · tone of voice · positioning |
| 2 | Logo usage | Structure · colourways · variations · clear space · minimum size · misuses · positioning · co-branding · registered mark |
| 3 | Colour | Primary · secondary · four codes each · approved and **forbidden** pairings · scheme layer order · type colour · contrast |
| 4 | Typography | Primary · secondary · both scripts · hierarchy · line-height by copy length · measure · **fallbacks** |
| 5 | Visual language | Photography and its categories · pattern · icons and illustration · heritage graphic elements |
| 6 | Applications | Print · digital · **percentage layout templates** |

**The four things that separate a world-class book from an adequate one:**

1. **Every rule carries its reason.** A bare prohibition gets broken; a reasoned one
   survives.
2. **Rules are shown, not described.** People copy pictures.
3. **Specifications are measurable.** "40% men, 40% women, 20% children" can be checked;
   "authentic and warm" cannot.
4. **Relative units, not fixed.** Clear space in X, layout in percentages. Anything fixed
   breaks at the next size.

**Optional sections exist — do not include them by default.** Strapline, sub-brands, motion
identity, UI style, iconography, 3D assets, packaging, environmental, merchandise, seasonal
extensions, campaign history, asset library, governance. Each has a trigger in
`guidelines.md`. **An unused section is padding, and padding is how a guideline stops being
read.**

**Two failure modes to sweep for before delivery:**

- **Bilingual contradiction.** One national guideline shipped an edition whose Arabic
  forbade placing the logo at the bottom while its English permitted it. Verify every rule
  says the same thing in both languages — translate-and-ship is how that is produced.
- **Placeholders left in.** A widely circulated brand manual names one typeface while
  displaying another, and carries a swatch called "Caffeine Gold" reading `HEX #000000`,
  `RGB TBC`. Sweep for TBC, lorem, unresolved values and contradictions. **A guideline that
  contradicts itself teaches people to ignore it.**

**Delivery: `references/design-delivery.md`.** A Claude Design project via `DesignSync`,
starting from `assets/design-system/`. Read → `finalize_plan` → write. It stays consumable —
another session can build the brand's site from the same tokens, which a PDF cannot.

**Prefer Claude Design; fall back cleanly.** If the user lacks design access, ship the same
files as a local `brand/guidelines/` folder with an `index.html` contents page. **Claude
Design is the shelf, not the book** — the book is `styles.css` and the pages, and it reads
the same either way. Say which path was taken, and if they are a Claude user without design
access, tell them it exists; the hosted version is materially better.

---

## Out of scope — say so, do not imply otherwise

Stripe's process runs seven phases; the last three cannot be performed here:

- Market testing with real audiences, A/B tests
- Team training, phased rollout, launch communications
- Ongoing performance monitoring and refresh

The work ends at the guidelines and hands these to the human.

---

## Rules that apply everywhere

- **Versatility** — every mark survives from favicon to billboard. If it dies at 16px it is
  not finished.
- **Trademark** — search, never claim to have cleared. Recommend an attorney before
  registration or print.
- **Timeless over trendy** — do not date the identity to the year it was made.
- **Cultural safety** — colours and symbols read differently by market. Check against the
  stated audience, not against a universal table.
- **Reference versus shipped asset** — found images are legitimate as reference and never
  become the brand's own photography. Anything that ships is original or licensed.
- **Consistency** — one system across every touchpoint, not a set of one-offs.
- **Gather inspiration; do not be moved by it.** The process is recursive, and looking at
  Pinterest or Behance once a direction is set is legitimate. But a palette that looks
  good on Behance was derived from *someone else's brief*. Ours governs. Reference informs
  a decision that was already derived — it never replaces the derivation. **Follow the
  rules.**
