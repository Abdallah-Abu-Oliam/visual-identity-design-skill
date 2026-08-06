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

## How to talk to the user — read this before anything else

**The user is not reading this file. They must never hear its vocabulary.**

They came to get a brand made. They do not know what a phase is, what a gate is, what a
reference file is, or what a subagent is. Saying those words does not sound rigorous — it
sounds like being handed someone else's paperwork.

### Never say

**Phase · Step · gate · hard gate · reference · `references/anything.md` · subagent · fan-out ·
Read/Review/Research · the skill · the runner · derivation · Q13 · element 7**

Say the thing instead. Not *"Phase 2 Step 5, the hard gate"* — say *"before I design
anything, I want to agree on the overall look. Nothing else starts until we do."*

### The opening message — send this, near enough verbatim

**Ask for all seven at once, as a list.** The user needs to see the whole shape to answer
it — they can then write one reply covering everything, in their own order, at their own
depth. Do not drip the questions out one at a time; these are facts they already have, and
seven round trips to collect them is a form, not an interview.

No process summary, no cost warning, no explanation of what happens next. Just the ask:

> Tell me about the project. Answer what you can — rough is fine, and skip anything that
> does not apply.
>
> 1. **What is it?** A quick tour — what it does, and what someone actually does with it.
> 2. **Name** — *optional, skip it if you do not have one yet.*
> 3. **Why that name?** — *optional.*
> 4. **Who is it for?** The people who would be genuinely disappointed if it disappeared.
> 5. **Competitors.** Who someone looks at before choosing you — include the local ones.
> 6. **Your advantage.** Why they pick you instead. Not what you are good at — what makes
>    someone switch.
> 7. **How should it feel?** Someone uses it and it goes well. What do they feel in that
>    moment?

**Then follow up only on what is missing or too vague to use** — one sharper question per
gap, not a second pass through the list. If they wrote three sentences covering four items,
take it and ask about the rest.

**Name and naming reason are genuinely optional.** Plenty of people arrive without a name;
that is normal, it blocks nothing, and if they want help finding one, just start helping
rather than announcing a process.

### After the brief, one thing at a time

Batching is right for the brief because those are facts. Everywhere after it — choosing a
direction, a mark, a palette — present one thing and let them react to it. Those are
judgements, and judgements do not survive being asked five at once.

### While the work runs

- **Mention cost only when you are about to spend it**, never up front. "This next part
  means searching and downloading a few hundred images — worth doing?" at the moment it
  matters. Not as a preamble to someone who has not described their company yet.
- **Describe what you are doing in plain terms.** *"I'm going to look at what your
  competitors already own, so we don't land on top of them."*
- **Show, then ask.** Every choice arrives as something to react to, never as a blank
  question.
- **Say why, in their language.** *"Red is out — you told me this brand refuses anything
  that reads as blood or weapons."* Not *"per the forbidden list in element 7."*

---

## The rules everything rests on

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

**4 · What the user typed outranks anything you inferred. Always.**

Research findings, competitor analysis, category conventions, your own drafted answers — all
of it is **inference**. The words the user actually typed are **evidence**. Evidence wins.

**Where they conflict, say so and let the user decide.** Never resolve it silently, and
never quietly translate their word into your word.

This is the most expensive failure this skill has produced, and it has happened more than
once:

> The user's questionnaire said **playful, cartoon-like, mascot**, and twice, unprompted,
> *"they should love it to understand it."* The competitor research said the mark should
> stay **calm**, because in that category a loud logo is the tell.
>
> "Calm" was converted into **"abstract and minimal."** Those are not the same thing — the
> brand the user themselves named as a reference is calm *and* figurative.
>
> **291,000 tokens were spent executing a brief that was wrong before any agent read it.**
> Then 460,000 more.

The same class of error, elsewhere: a leftover folder on disk outranking the project the
user named; a rebuilt questionnaire outranking the shipped one.

**Three enforcement points, where it actually costs money:**

- **Drafted questionnaire answers.** A draft you wrote is a guess. **An untouched draft
  never outranks an explicit edit** — if the user typed over it, their words are final.
- **Any brief handed to a subagent.** Read it against the user's own words *before*
  dispatching. A wrong brief costs 1× in the main thread and **N× across N agents** —
  fan-out multiplies brief errors, so the check belongs before the fan, not after.
- **Any translation of research into a visual instruction.** "Calm" and "abstract" and
  "minimal" and "restrained" are different words. If the user used one of them, use theirs.
  If research suggests another, put both to the user in one sentence.

These four are not style preferences. They are what separates this from a form with a
design theme.

---

## Before anything: whose project is this?

**Start by finding out what the user wants to build. Not by reading files.**

If `brand/` exists, **read it but do not adopt it.** Report what you found and confirm it
is the project they mean, in one sentence, before doing anything else:

> "There is existing work here for **<name>**, at <phase>. Is that what we are continuing,
> or are you starting something new?"

**Never infer the project from leftover files.** This failed in practice: a fresh session
found a previous project's `brand/` folder, adopted its brief, its mind map and its
approved art direction, and dispatched agents to generate logos for **a company the user
had never mentioned**. The user was never asked what they were building.

Three rules that prevent it:

1. **The user names the project, not the filesystem.** If their opening request names a
   different brand — or names none — the folder on disk is not authority.
2. **Confirm before continuing, always.** Even when it looks like an obvious resume. One
   sentence costs nothing; adopting the wrong brief costs the whole run.
3. **If it is a different project, do not delete or overwrite.** Ask whether to archive
   the existing folder or work somewhere else. Someone's unfinished work is not scratch
   space.

Once confirmed as a genuine resume, `brand/STATE.md` tells you where things stand — this
process spans sessions, and re-asking the seven questions because you did not check is the
fastest way to lose someone.

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

**Write to these files as you go, not at the end** — an unrecorded decision is a lost one.

**`brand/` belongs to the user's project, never to this skill.** Nothing shipped with the
skill may live there, and no example brand may be written into it. Demonstration content
lives in `references/` and `assets/`, clearly labelled as example, and is **never copied
into a working project as a starting point.** A prior run's output left in place is how a
fresh session ends up designing for the wrong company.

### Shipped assets are copied, never rebuilt

Everything in `assets/` is finished work. **If an asset exists, use it — do not write your
own version.** Rebuilding takes longer and produces something worse, because the shipped
version carries behaviour that is invisible in a description: translations, readback
functions, persistence, working toggles, embedded images.

| Asset | Copy with |
|-------|-----------|
| `assets/questionnaire.html` | **its `photos/` folder** — the picker breaks without it |
| `assets/preview.css` + `assets/pick.js` | **copy both at Phase 2, before the first page** |
| `assets/design-system/` | its `styles.css` and `theme.json` |

### Every generated page links `preview.css`. None declares its own CSS.

Copy `assets/preview.css` and `assets/pick.js` into `brand/` at the start of Phase 2, then
link them from **every** page the process makes — mind map, boards, logo previews, palette,
type, assembly, pattern, mockups.

```html
<link rel="stylesheet" href="../preview.css">
<script src="../pick.js" data-key="art-direction"></script>
```

On one real run, eleven pages each re-declared the same colour variables, the same `.why`
block and the same card grid inline — roughly 20–25k tokens of pure duplication, plus the
cost of re-deciding identical styling eleven times.

**Its tokens are neutral on purpose.** When colour is derived at 3.2, overwrite the six
`--b-*` values in `brand/preview.css` and **every page built earlier silently re-renders in
the brand.**

`pick.js` gives every gate the same readback. Mark anything selectable with
`data-pick="id"`, then read it with one call that is identical on every page:

```js
Pick.collect()   // -> { key:"art-direction", picked:"seal", at:"…" }
```

It persists to `localStorage`, and `data-limit` **reports** an overflow rather than
blocking it — going over a limit is a signal that the choice is unresolved, not a filling
error.

When an asset references files by relative path, **copy the whole folder, not the one
file.** Then open it and confirm it works before showing the user. A silently broken asset
looks exactly like a working one until they click something.

**`assets/design-system/` carries a demonstration brand.** Its palette, name and pattern are
an example. Replace the tokens before delivering anything — never ship the example brand's
colours to a real client.

---

## Phase 1 — The brief

Seven things. **Facts the owner already has** — capture, not creative work.

**Ask for all seven in one message, using the opening message in "How to talk to the user".**
The user needs the whole list in front of them to answer it. Follow up only on gaps.

1. Quick tour — what it does
2. Name — **optional**
3. Reason for the name — **optional**
4. Targeted audience
5. Competitors
6. Competitive advantages
7. Targeted feelings

Load `references/brief.md` for what each one is *for*, how its answer converts into a
visual decision, and the single scripted push-back for its failure mode.

**Ask the question, not the label.** "What is your target audience?" returns "everyone".
"Who would be genuinely disappointed if this disappeared tomorrow?" returns actual people.

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

#### ⛔ NEVER BUILD THE QUESTIONNAIRE. COPY IT.

`assets/questionnaire.html` is a **finished, shipped asset**. It is not a specification to
implement, not a template to adapt, and not an example to imitate. Writing a new one is
always wrong.

It already contains 47 fields, full English/Arabic translation with RTL, a working theme
toggle, sliders that report meaning rather than numbers, the logo-type picker with real
example images, autosave to `localStorage`, and the `prefill()` / `collect()` pair the
readback depends on. **A rebuilt version has none of that**, and rebuilding it takes
minutes to produce something worse.

**Copy the HTML and the `photos/` folder together.** The picker loads its images by
relative path, so the folder must sit beside the file or the logo examples silently break.

```bash
mkdir -p brand
cp "<skill>/assets/questionnaire.html" brand/
cp -r "<skill>/assets/photos" brand/
```

It must live **inside the user's project folder** — a file outside it renders as a static
snapshot with no JavaScript, and nothing works.

**Verify before showing it to the user.** Open it and run:

```js
JSON.stringify({
  fields: document.querySelectorAll('[data-q]').length,   // must be 47
  i18n:   typeof setLang,                                  // must be "function"
  images: document.getElementById('typesimg')?.getAttribute('src')
})
```

Then flip the language once and confirm the questions change. If fields are not 47, or
`setLang` is undefined, or the picker images are missing — **you are looking at a rebuilt
copy. Delete it and copy the real one.**

**Symptoms of a rebuilt questionnaire**, all reported from a real run: the language button
does nothing · the theme button does nothing · the logo-type images do not appear · Clear
does not clear. Every one means the shipped asset was not used.

#### Using it

Open it, call `prefill({...}, true)` to inject the drafted answers — they render with an
orange edge marked *drafted from your brief*, so the user never mistakes a guess for their
own answer — wait, then call `collect()` to read everything back. It autosaves on every
keystroke and never blocks on a blank field.

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

- **Never collect from a single source, and match the source to the direction.** On a real
  run the boards for a direction called *The Seal* were built entirely from Unsplash, which
  returned modern brass wax stamps with Latin monograms. One call to the Met's open access
  API returned a **10th–11th century Islamic seal stone carved in Kufic Arabic** — public
  domain, free, the right century and the right alphabet. A documentary or heritage
  direction lives in archives; stock alone produces a board about the wrong thing.
- **Museum and archive open access** — the Met and Wikimedia Commons are both tested and
  need no key; also Rijksmuseum, Smithsonian, Library of Congress, Europeana. Public
  domain, high resolution, and **the only place historical material exists**.
- **Behance** is the strongest source for finished identity systems, and renders without
  login. **It never reaches the client** — other designers' copyrighted portfolio work.
- **Unsplash / Pexels / Openverse** fill the boards. Free for commercial use.
- **Pinterest** renders nothing anonymously. Ask the user to sign in themselves, or have
  them paste pin URLs. **Never type their credentials.**
- **The named brands' own sites**, via browser screenshot, for first-party category
  conventions.
- **Search in the market's own language.** A brand in Iraq or the Gulf loses sales to local
  competitors, not the global category leader.

**Build every query as `subject + register + exclusion built in`.** Both halves were
learned by getting them wrong on a real brief:

- **The forbidden list goes in the query, not on a checklist beside it.** Searching
  `wax seal` for a brand that forbids red returns red wax. An agent told "avoid red" still
  types "wax seal" and still gets red. **Name what you want instead of what you don't** —
  `brass stamp embossed paper`, not `wax seal document`.
- **Subject alone returns stock.** `date palm frond desert` returns tourism postcards;
  `palm frond texture macro` returns the same subject in the right world. Put the register
  in the words: texture, macro, close, detail, monochrome, low light, muted.

**Write the query list before collecting and read it against the forbidden list.** A wrong
query costs an entire collection run — the most expensive step in the process.

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

**This step does not draw the mark. It briefs the user and verifies what comes back.**

Two independent runs produced 14 concepts and **1 usable one**; the second cost ~750k
subagent tokens and the user drew the final mark themselves. The agents were blind — on one
run six of them separately built their own rasterisers because none could see its own work.
**The user has eyes and reacts in real time. The drawing goes to them.**

| We do | The user does |
|-------|---------------|
| Derive the logo type | Runs a logo tool live |
| Turn mind-map nodes into 3–5 concept **directions**, in words, each with its source | Reacts, iterates, redirects |
| Build a paste-ready brief — format, style, palette state, directions, exclusions, occupied territory | Brings back a mark |
| Verify: export, real 16px, monochrome, no live text, cultural read, redraw test | |
| Derive clear space, minimum sizes, ranked colourways | |

**`FEELINGS` in that brief uses the user's own words, verbatim** — not your translation of
them. This is exactly where the 750k was lost.

**If the user asks us to sketch anyway:** main thread only, never fan out, two or three not
five, render and look at each, and say plainly they are rough sketches to react to.

**Run `scripts/export.sh` on every concept BEFORE presenting it.** Not at the end — before.
It is the verification step, and it is the only thing that tells the truth:

- **A browser-scaled SVG is not a favicon.** The preview strip anti-aliases cleaner than
  reality. Tested on this brief: a concept that read as a legible eye at 16px in the strip
  rasterised to a blurry bullseye with the eye gone. **The strip understated the failure,
  and the strip is what the decision gets made on.**
- It proves the SVG is valid, self-contained, and free of live `<text>` — rasterisers
  substitute fonts, which distorts Latin and breaks Arabic letter joining outright.
- The monochrome pass reveals shapes that collapse without colour, which engraving and
  stamping will do anyway.

**Put the real rasterised 16px PNGs in the favicon strip, not CSS-scaled SVG.**

**Present each concept with its derivation.** "The falcon's eye, where the curve doubles as
a blade edge." A concept nobody can trace cannot be defended later.

**Audit symbols for cultural reading before presenting.** The forbidden list catches what
the brief named; it will not catch what nobody thought to name. A six-pointed radial form
generated for an Iraqi brand on this very run carried religious and political weight that no
colour rule would have flagged. **Look at each mark and ask what else it resembles in the
stated market** — flags, religious symbols, political emblems, gestures, existing marks.

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
