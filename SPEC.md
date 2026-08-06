# Working Spec — the method, as it was worked out

> This is the design notebook, not the skill. The shipped skill is in
> `skills/visual-identity/`. Kept because the reasoning behind each rule is here,
> and several rules only make sense with it.

Status: in progress. Built collaboratively, phase by phase.

---

## What this skill is

Turns a project or idea into a **brand**, whose deliverable is a **visual identity**.

Not a design skill. A design skill makes things look good. This one decides *who the
brand is*, then derives how it looks from that. Order is enforced: brand identity
first, visual identity second. Visual is the expression, strategy is the source.

Two premises it is built on:

1. **The user often doesn't know what they want.** The skill's job is to help them
   find it, not to hand them a blank form.
2. **Every visual decision traces back to a strategy decision.** No orphan choices.
   Blue is not "nice" — it is trust, which came from a value, which came from the brief.

Scope: strategy-lite → visual. Strategy is captured only to the depth that drives
visual decisions. Voice, tone, messaging, and customer experience are out of scope.

---

## Phase 1 — The Brief

Seven elements. Facts the project owner already has.

Full method — meaning, processing, and the right question for each — in
`skills/visual-identity/references/brief.md`.

| # | Element | Processes into | The question |
|---|---------|----------------|--------------|
| 1 | Quick tour — what it does | Category conventions · the surface list | "Walk me through it like I am a customer seeing it for the first time." |
| 2 | Name | Wordmark viability · how many times it is drawn · trademark risk | "Spell it exactly as it should appear. Is that final or provisional?" |
| 3 | Reason for the name | **Symbol territory** — the richest source in the brief | "Why that word, and what made you pick it over the alternatives?" |
| 4 | Targeted audience | Legibility floors · cultural colour reading · register | "Who would be genuinely disappointed if this disappeared tomorrow?" |
| 5 | Competitors | **Differentiation** — decides the palette | "Who does a customer seriously consider before you? Name three, including local." |
| 6 | Competitive advantages | What the identity must say loudest | "Why do they switch? Not what you are good at." |
| 7 | Targeted feelings | **The main bridge** — colour temperature, shape, weight | "It goes well. What do they feel in that moment? A sentence, not adjectives." |

Every element carries one failure mode with a single scripted push-back — "everyone"
becomes "pick the one person who would be most annoyed" — then the process moves on.

### Notes on Phase 1

- These are **facts**, not creative work. The owner knows them. Ask and record.
- **Exception: elements 2 and 3.** When the project has no name yet, the skill runs a
  naming method rather than asking. Source:
  https://stripe.com/resources/more/how-to-pick-a-name-for-your-startup-a-step-by-step-guide
  That one source covers both the name and the reasoning behind it.
- Vision and mission are **not** here. They belong to Phase 2.

---

## Phase 2 — Mood Board & Art Direction

### What it is

A visual artifact showing where the identity is heading, before any of it is built.
Delivered as a single self-contained HTML file rather than scraped images — no
copyright exposure, no dead links, editable and versionable.

### Why it exists

1. **Proves comprehension.** Shows the user we understood what they asked for.
2. **Harvests modifications while they are still cheap.** The user sees roughly how the
   final thing will look while nothing has been built yet. This phase is where the bulk
   of the user's changes should be extracted.
3. **Sets expectations.** The user may be picturing dense and colorful while we are
   heading toward simple. Better to collide here than at delivery.

This phase is also the skill's divergence step — the point where direction is chosen
by reaction rather than by asking the user to generate an answer from nothing.

### How it is built — 5 steps

The three R's, then two more:

| # | Step | Purpose |
|---|------|---------|
| 1 | **Read** | Read the brief, the questionnaire, and every file the user shared. Understand the requirements and extract **keywords**. |
| 2 | **Review** | Go back over the documents and the conversation with the user. Ask the few questions that remain. |
| 3 | **Research** | Search out and collect real-world references — competitors, category, admired brands, the name, the audience — into a project folder, with written findings. |
| 4 | **Mind map & brainstorming** | Put every keyword from the 3 R's in one place, connect it to the company, and derive sub-words until abstract ideas turn into drawable ones. |
| 5 | **Art direction** | Collect a large, cohesive set of images into a board and put it to the user. **Hard gate** — nothing else begins until it is approved. |

### Step 1 — Read

Input: the brief, the questionnaire, any files the user shared.
Output: **keywords**, and the reading notes that produced them.

The questionnaire lives in the skill as a fixed template. The model does not invent a
new one per project — it works the standard instrument, drafting proposed answers from
the brief so the user corrects rather than composes.

- Template: `questionnaire-template.md` — 6 sections, blank.
- Worked example: `questionnaire-example-alnisal.md` — filled, and annotated to
  demonstrate reading.

**Reading is extraction, not summarizing.** Strategy answers silently decide visual
things. "We stand against treating knives as weapons" eliminates red, tactical black,
and aggressive angles — before anyone opens a color picker. The model's job in this step
is to catch those and write them down as it goes. The example file marks every one of
them with `→ Reading note`.

**Rule for conflicts.** When a stated answer contradicts an implied constraint, the
implication usually wins — but it is raised with the user, never resolved silently.
(Al-Nissal: client said no colors are excluded; the values section had already excluded
red.)

#### Delivering the questionnaire

The instrument holds **47 questions**. Nobody answers 47 questions in a chat; they quit
around twelve. A designer does not ask 47 either — they ask a handful and infer the rest.

**So it is not 47 questions. It is 7 asked and 6 review passes.** Phase 1's brief comes
first for exactly this reason. Knowing what the thing does, who it serves, the
competitors, the targeted feelings, and the name with its reasoning is enough to draft
credible answers to roughly 35 of the 47. The user corrects rather than composes.

**Two delivery modes, one set of drafts.** The form is a *view* of the same drafted
answers, never a second questionnaire.

| | Conversational | Web form |
|---|----------------|----------|
| Whole scope visible | ✗ | ✓ |
| Answer out of order | ✗ | ✓ |
| Leave and return | ✗ | ✓ via localStorage |
| Q14 with real logo images | ✗ | ✓ |
| Look & Feel axes as sliders | ✗ words only | ✓ position |
| Push back on a weak answer | ✓ | ✗ |
| Follow a surprising answer | ✓ | ✗ |
| Works on a phone | ✓ | ✗ |

**Form for breadth, chat for depth.** Collect everything in the form, then take the two or
three answers that are vague or contradictory into conversation. *"You put Look & Feel at
80% modern but named Opinel as a reference — those pull apart. Which is true?"* That is the
designer move, and it needs the form's completeness and the chat's follow-up.

##### The web form mechanism — tested, works end to end

1. Model writes the HTML with drafted answers **pre-filled as field values**.
2. Opens it in the browser pane.
3. User edits directly.
4. Model reads the edited values back via JavaScript — **no copy-paste**.
5. `localStorage` persists on every input, so closing and returning loses nothing.

Implementation: every field carries a `data-q` attribute; a `collect()` function walks
`[data-q]` and returns an object; an `input` listener writes that object to
`localStorage`. The model calls `collect()` to read, then writes the answers to markdown.

**Hard constraint: the HTML file must live inside the project folder.** Files outside it
render as static snapshots with no JavaScript, which breaks the entire mechanism.

##### Delivery by question type

| Type | Questions | How |
|------|-----------|-----|
| **Axes** | §2 Look & Feel, §3 Tone — 9 | Sliders in the form, or one or two modal multiple-choice calls in chat |
| **Visual choice** | Q14 | Five types shown with famous examples; pick two |
| **Facts** | Name, audience, competitors | Already captured in the brief; confirm only |
| **Generative** | Values, purpose, what they stand against, vision | **Draft first, always.** Never asked cold |
| **References** | Q7–12 | Offered, never blocking |

##### What a drafted section looks like in practice

> I read your brief. Here is what I think your values are — correct anything wrong:
>
> **1. Authenticity before product.** You said counterfeits are the market's problem.
> That is not a feature, it is a position.
> **2. Trust through detail.** You listed steel type, heat treatment, and packaging —
> specifications, not slogans.
> **3. Knowledge before the sale.** You mentioned educating buyers twice.
>
> And one I am unsure of: do you stand *against* anything specific? Most brands have no
> real enemy. Yours might.

Three drafted, one asked. The user reacts in thirty seconds, and the correction is sharper
than anything they would have written from a blank prompt.

---

**Never ask a user to generate. Ask them to choose.** Blank questions return blanks.
Questions with named options and recognizable examples return real answers in seconds,
and better ones — the user is reacting to something real instead of describing something
imagined. Q14 is the model: five logo types, each shown with famous examples, pick two.

**Q14 and Q7 are a pair.** Q14 gets the category cheaply. When its answer overflows the
two-pick limit, that overflow is a reading, not a filling error — category settled, taste
unresolved. That is the moment Q7 ("send logos you like") becomes both worth asking and
answerable, because it is now anchored to a choice already made. Asked cold, it returns
nothing.

**Questions 7–12 are often blank, and that is fine.** Never block on them. Q14 covers
most of the gap; the mood board answers whatever remains.

### Step 2 — Review

Go back over the documents and the conversation with the user, then ask the few
questions that are still open. That is the whole step. It is deliberately light.

Two things naturally land here:

- **The conflicts caught during Read.** Read's job was to notice them, not settle them.
  This is where they go to the user. (Al-Nissal: the client said no colors were
  excluded, but the values had already excluded red; and two logo metaphors — blades and
  a falcon — were competing for the same mark.)
- **Answers still too vague to compute on.** If "audience: everyone" survived the
  questionnaire, push back once with a sharper question, take whatever comes back, and
  move on. Once. No interrogation loops.

### Step 3 — Research

Keywords again, but pointed outward this time. In Read they were extracted; here they
are what we go searching with.

**What we search for, and why each one earns its place:**

| Target | What we are actually after |
|--------|----------------------------|
| Company name | Is it taken, who else uses it, trademark exposure |
| Naming reason and meaning | Visual metaphors the word already carries |
| Why the company exists | Category conventions it must sit inside or deliberately break |
| The area or industry | What this whole category looks like |
| Customers | What they already respond to, what reads as credible to them |
| Competitors | What is **taken** — the colors and forms we cannot have |

Competitors is the differentiation input, not an inspiration board. If every brand in
the category is black and steel, that is occupied territory, not a direction.

**The practical part.** Create a folder named for the company and go on a search
mission. Some destinations are handed to us by the questionnaire — the brands the user
named as having photography or art direction they admire. The rest we find. Save URLs
and screenshots so we can come back to them.

```
<company-name>/
  research/
    admired-brands/     ← named by the user in the questionnaire
    competitors/        ← direct rivals, including the local market
    category/           ← wider conventions
    name/               ← meaning, existing uses, trademark
    audience/           ← where they already are
    FINDINGS.md         ← what we saw, and what it means
```

**FINDINGS.md is the actual deliverable of this step.** A folder of screenshots nobody
wrote about is dead weight. The observation is the output; the image is only evidence
for it. Every saved reference gets a line: what it is, why it was saved, what it implies
for us.

**Line to hold: reference versus shipped asset.** Found images are legitimate as
reference — that is what research and mood boards are made of, and it is how the work is
done in practice. What they never become is the brand's own photography. Anything that
ships as a brand asset must be original or licensed. Research is the raw, unfiltered
dump; the mood board in Step 5 is the curated selection drawn from it.

### Step 4 — Mind map & brainstorming

Every keyword gathered across Read, Review, and Research goes into one place: a single
map with the company at the center.

**Structure.** Company at the center. Main keywords radiating out. Sub-words derived
from each. Everything connected back to the company, so no branch floats free.

**Connect the regular and the irregular.** Obvious associations are worth mapping but
they are not where the value is. Knives → strength → sharpness → steel and grey is the
category's identity, not this brand's. Every competitor's map has that branch. The
strange word — the one that showed up sideways during the three R's — is where anything
ownable comes from. A map that only records the obvious guarantees a generic result.

**Derive until the word has a shape. This is the point of the step.** Keep pushing each
keyword down into sub-words until a child of it is something that can actually be drawn.
Abstractions cannot be designed. "Precision" has no silhouette. "Trust" has no
silhouette. **عين الصقر — the falcon's eye — does:** pupil, ring, a sharp curve. That is
a form a hand can make.

This is the crossing point of the whole process. Everything before it is words.
Everything after it is form. The mind map is the mechanism that gets from one to the
other, and it works by derivation rather than inspiration.

Output: **visible, feelable words connected to the company** — and the next steps get
easier because of them.

**It is also where competing metaphors get resolved.** Al-Nissal's brief carried two —
blades and a falcon — flagged as a conflict during Read. On the map they sit as separate
branches, and عين الصقر next to الحدة suggests they can merge rather than compete: one
form, an eye whose curve is an edge. The map finds that; an argument would not have.

**Format.** Generated as an artifact, like the mood board — not hand-drawn, not a plain
list. The connections are the content, so it has to be seen.

### Step 5 — Art direction

Collect a large number of images into one board that holds together as a single visual
world, and put it to the user.

**Why.** It shows the user roughly what the end product is going to look like, while
nothing has been built. Good or not good — the answer is cheap here and expensive
later.

**This is a hard gate.** If there is no agreement on the art direction, the process does
not advance. No logo, no palette, no typography, nothing. The step repeats — new
direction, new board — until the user agrees. Every later phase inherits this decision,
so it is the last place a change of mind costs nothing.

If the board is rejected several times over, the problem is upstream. Stop iterating on
images and go back to the brief and the questionnaire; something in the strategy was
never captured correctly.

There are two separate decisions here, and they run in order.

#### First: which art directions are even eligible

Many art directions exist. Only some can apply to this company. Three filters decide
which ones are candidates:

1. **The company itself.** A tech company cannot be given an old-luxury direction; a
   futuristic one fits, along with a handful of others. The category rules whole
   territories in and out before taste enters.
2. **The target customer.** Young, old, professional, hobbyist — who is being spoken to.
3. **The competitors and the competitive advantage.** Competitors mark what is already
   occupied. The advantage marks what has to be the loudest thing in the room. The full
   method is below.

#### How to think about competitors

Once the research is in, the strongest chance of competing is to look different from
them. That is what the visual identity is for.

**The method:**

1. Collect the competitor marks and sites — Step 3 already did this.
2. Map each one across every axis: hue region, saturation, value, type
   classification, weight, composition, texture, and **volume**.
3. Find the cluster — where they all converge.
4. Name the empty space.
5. **Filter that space through the brand strategy**, deleting anything strategy forbids.
6. What survives is the differentiation territory.

**Step 5 is the one that generic advice omits, and omitting it breaks real briefs.**
Pure opposition on Al-Nissal reads: every competitor is steel, black, and neutral, so go
bright pink. The strategy — refined premium, quiet mastery, no noise — kills that
instantly. Competitors do not choose the direction; they *eliminate* options. Strategy
holds the veto, and the answer sits in the intersection of the two.

**Differentiate on register before hue.** Hue is the most visible axis and the easiest to
copy — a competitor changes a hex code in an afternoon. In a sample of three strong
regional competitors, all three shared flat saturated color, heavy type, solid blocks,
zero texture, and maximum contrast. Every one of them was *loud*. Choosing a different
loud color changes one variable and still reads as one of them at a glance. The genuinely
open space was quiet: tonal, muted, textured, generously spaced. Volume, texture, and
composition are usually emptier than hue, and far harder for a competitor to take back.

**The exception.** In trust-critical categories — banking, medical, security — looking
nothing like the category costs trust. Conformity is occasionally the right call, but it
is made deliberately, never by default.

**Do not fix the number of directions in advance.** How many survive these filters
depends entirely on the company. Some briefs leave one viable direction, others leave
five. Show the ones that genuinely survive — never pad the list to hit a count, never
cut a real option to stay under one.

Whatever the number, the directions must genuinely differ. Variations on a single idea
are not a choice, and the user will feel that immediately. Name each one — a named
direction can be chosen and discussed; an unnamed one can only be reacted to.

When more than one survives, showing them together beats showing one, for the same
reason question 14 beats a blank question: choosing is easy, judging in isolation is
hard. A rejection that arrives with a preference tells us where to go. A bare rejection
tells us only where not to.

#### Second: which images populate each direction

Three inputs, combined — never one alone:

1. **Brand strategy.** What the values, vision, and stated feelings demand and forbid.
2. **User preferences.** Everything they said they like and dislike.
3. **The examples they gave us.** The brands they named in the questionnaire.

**Cohesive and homogeneous is the quality bar.** A pile of individually good images is
not an art direction. Each board has to look like it came from one world — consistent
light, palette, distance, texture, mood. Incoherence reads as indecision, and the user
cannot approve something that has no single direction to approve.

**Format.** A local HTML file in the project folder with the images downloaded beside
it. Not a published artifact — external images are blocked there. Local means no link
rot, and the board can be edited and re-sent as it iterates.

#### Where the images come from — tested, not assumed

| Source | Can we find images? | Can we download them? |
|--------|---------------------|-----------------------|
| **Unsplash** | Yes — 32 photo URLs off a single search page, no login | Yes, verified 200 |
| **Pexels** | Untested | Yes, verified 200 |
| **Behance** | Yes — 29 CDN images and 48 gallery links off one search, no login, titles in `alt` | Yes, verified 200 |
| **Pinterest** | **No.** Auth-walled. The page ships ~1MB of app shell with `login required` in the HTML and renders zero pins | Yes — direct `i.pinimg.com` URLs return 200 |
| **Named brand sites** | Yes, via browser screenshot | n/a |

**Unsplash is the workhorse for boards.** Verified end to end: navigate the search page,
extract image URLs from the DOM, download, save. The license also permits commercial use,
so these images carry no cleanup burden if they outlive the board.

**Behance belongs to Step 3, not Step 5, and the distinction is a licensing one.** It
holds finished brand identities, logos, and brand books rather than stock photography —
which makes it the strongest research source available and disqualifies it entirely from
client-facing boards.

| | Behance | Unsplash / Pexels |
|---|---------|-------------------|
| Content | Finished brand identities, logos, brand books | Stock photography |
| Belongs to | Step 3 — Research | Step 5 — Art direction boards |
| License | Other designers' copyrighted portfolio work | Free, commercial use |
| May it reach the client? | **Never** | Yes |

Putting another designer's brand system into a client mood board is not a copyright edge
case — it is presenting their work as our direction. Behance stays in `research/`
permanently. Thumbnails run 444×347; full resolution requires opening the project page.

One search for `knife brand identity` returned *"Nesal: (knife brand idintity)"* — a
near-identical name already used for a published knife identity — alongside *"SKIF Knives
Brand Identity"*. A name collision and a direct category reference in a single query.
This is what Step 3 is for, and no photography source can produce it.

**Pinterest needs a session, and the user can provide one.** Anonymously it renders
nothing. Three ways through it, in order of preference:

1. **User-assisted login.** Open Pinterest in the browser pane and ask the user to sign
   in there themselves. Once the session is live, the normal pipeline works — pins
   render, `i.pinimg.com` URLs come out of the DOM, and download is already verified.
2. **User-supplied links.** The user browses on their own and pastes board or pin URLs.
   We fetch the originals directly. Their taste, our fetching. Costs nothing and needs
   no session.
3. **The user's own logged-in Chrome**, where a Pinterest session may already exist.

Two rules hold across all three. **Never type the credentials** — the user signs in
themselves, and we neither handle nor ask for a password. And **collect modestly**: a few
dozen references for one project is ordinary use, while bulk automated harvesting is what
Pinterest's terms exist to stop. The difference is volume, so keep it small.

#### Collection with subagents

One agent per direction. Cohesion is a judgment made across a whole set, so a single
agent owning one world end to end can hold it; splitting the work by search term would
fragment exactly the thing that matters.

Each agent receives: the direction name, its mood description, the forbidden list from
the brief, the audience, its own output folder, and seed search terms. Each returns
downloaded images plus a `manifest.md` — one line per image, saying why it was kept.

```
art-direction/
  quiet-craft/      ← agent 1
  modern-steel/     ← agent 2
  warm-heritage/    ← agent 3
```

**Agents over-collect; the main thread makes the final cut.** If every agent decides for
itself what cohesive means, the result is one taste per agent. Agents gather roughly
three times the target with reasoning attached, then a single judgment curates each set
down to what actually holds together.

**Model: Sonnet.** The work is largely mechanical — search, extract, download, write a
manifest line — but not purely. The agent has to apply the brief's forbidden list and
hold one direction's mood while filtering, and it has to adapt when a page does not match
the expected shape. Weaker models drift on both. Opus is wasted on downloading files.

Model choice matters less here than it appears, because the taste judgment deliberately
lives in the main thread. An agent only has to avoid discarding good candidates and avoid
smuggling in banned ones.

Two things would change it: if the URLs are supplied up front — a user's Pinterest links,
a fixed query list — the step becomes pure fetch-and-save and Haiku is enough. And if
curation ever moved into the agents, the answer would be Opus, but the better move is to
not make that change.

**Monitoring** is reading the manifests and the folders before anything reaches the
user — not watching progress.

**Cost.** Directions × oversampling × searches per agent makes this the most expensive
step in the process by a wide margin. Say so before running it.

---

## Phase 3 — Visual Identity

Worked through the **جمرة (Jamrah)** example — an ember, Saudi.

### Order of construction

**Logo → color → typography → assembly → pattern.** The mark is the hardest constraint;
palette and type accommodate it, never the reverse.

### 3.1 Logo

#### What a logo actually is

Three things get confused, and the difference decides how the mark is designed:

- **Logo** — the signature. An identifier, nothing more.
- **Brand identity** — the whole system the signature signs.
- **Reputation** — what people actually think. Earned, not controlled.

**A logo does not carry meaning; it collects it.** The swoosh meant nothing in 1971 and
means today what Nike spent fifty years putting into it. A mark that tries to explain the
business is doing a job that was never its own.

**This is the model's default failure and it must be designed against.** Asked for a
knife brand's logo, a model draws a knife. Coffee shop, a bean. Literal, descriptive, and
wrong. Jamrah's mark is not a picture of an ember — it is a folded geometric form that
*feels* like one.

#### The three rules

Every effective logo satisfies all three.

1. **Appropriate.** It fits the company and its field through emotion, not description.
   It does not say what the work is. Sharp, aggressive forms on a baby brand fail no
   matter how well drawn. Knowing how shapes produce feelings is the designer's actual
   job here.
2. **Distinctive.** Different from everything else in the field — the logo's primary
   function — and memorable in an operational sense: **see it once, redraw it from
   memory.** That is a test, not a preference.
3. **Simple.**

#### Logo types

Full reference: `logo-types.md` — seven types, three treatments, with when-to-use and
when-to-avoid for each, and a table mapping our own inputs to the decision.

Two things it settles. **Type is derived, not preferred:** the name's length and
distinctiveness, the brand's existing recognition, the competitor audit, the personality,
and the required applications between them narrow it before taste enters. And **three of
the source's ten are treatments, not types** — negative space, 3D, and dynamic are ways
of executing a mark, not alternatives to choosing one. Filed as peers, they let a model
pick "3D" and believe it has chosen a type.

Q14 is an input to this decision, not a replacement for it. Where the rules and the
user's stated preference disagree, say so and explain the reasoning — never silently
overrule, never silently comply.

#### Rules 2 and 3 pull against each other

```
too simple ───────── sweet spot ───────── too complex
generic, taken       redraw from memory    unrecognizable
already exists       and still unique      nobody retains it
```

A sheet of fifteen marks built from circles, triangles, and squares illustrates the
left-hand failure: every one is simple, six are a triangle inside a circle, and they are
interchangeable. Simplicity pushed far enough lands on shapes everyone already owns —
rule 3 satisfied by destroying rule 2.

Both ends fail memorability for opposite reasons. One is forgotten because nothing
distinguishes it; the other because there is too much to hold.

#### Present it colorless

Options are shown as pure line work, no fill, many to a sheet.

**Color is removed on purpose.** It is seductive: it rescues a weak mark and flatters a
bad one. Stripped back to line, the user is judging the form itself. Color arrives only
after the shape survives alone.

**Divergence then refinement — both stages, resolved.** The Jamrah sheets held sixteen
marks that were all one concept, varied by angle and weight: that is refinement. The
process runs both, in order — three to five genuinely different concepts first, then
variations inside the chosen one.

**Generation method: `logo-generation.md`.** Engine adapted from
neonwatty/logo-designer-skill (MIT). SVG, never image generation — a mark must be vector,
editable as curves, and exactly repeatable. Parallel subagents produce one concept each;
a preview page presents them; `export.sh` produces PNG at seven sizes.

Its interview is discarded entirely. That skill asks for style, colour, and format as
preferences; we derive all three, and it has **no competitor input at all**, which makes
it capable of reproducing the category leader. By this point our Phases 1–2 have produced
a richer brief than any interview would, and each agent's creative direction comes from a
drawable node on the mind map rather than a style menu.

**Keep its favicon size strip.** Every option rendered at 64, 32, and 16px beneath the
grid. That turns the versatility rule from an aspiration into something visibly failing or
passing.

### 3.2 Color

Jamrah's palette, chosen after trials, standing for fire and Saudi desert nature:

| | Name | Hex |
|---|------|-----|
| ■ | فحمي — charcoal | `#232323` |
| ■ | جمري — ember | `#e85f1a` |
| ■ | كريمي — cream | `#f5e1cd` |

Supporting: `#b7b7b8`, `#f09035`, `#fcf6d5`, `#0a0a0a`. Every swatch carries RGB, CMYK,
and HEX — print and screen both.

**This palette is the competitor method's output, not a taste call.** The rule said the
category clustered in blue, green, and yellow, so move up the wheel toward red-orange.
It produced `#e85f1a`.

Full method: `color.md` — the 60/30/10 rule, how the primary is derived, the meanings
table, the five harmony methods for secondary and accent, RGB versus CMYK, and the
mistakes.

Three things from it that govern the whole step:

- **60/30/10 is about area, not importance.** The 60% is usually the calmest color; the
  10% is where the eye goes. Palettes fail by making the loudest color the dominant one.
- **The meanings table is cultural, not universal, and it is where everyone starts.**
  Followed mechanically it delivers the category's existing palette — banks blue, health
  green, knives black. The table gives the convention; the competitor audit decides
  whether to take it or break it. Neither works alone.
- **Choosing the primary is the moment differentiation is spent.** Everything the
  competitor study found applies at this exact step and nowhere else.

### 3.3 Typography

Jamrah uses **Lyon** — sharp, modern, strong. Kai Bernau, 2006; Renaissance forms carried
into a contemporary feel. Specified across Light / Medium / Bold, in **both Arabic and
Latin**, with full character sets, numerals, and punctuation shown.

### 3.4 Assembly — and the boring test

Put logo, color, and type together and look at the result.

**Then ask: could this belong to any identity?**

For Jamrah the answer was yes. Correct, competent, and completely generic — and nothing
in it was *wrong*. That is the trap. Correct-but-generic is the default output of a
competent process, and without a step that names it, it ships.

This is a real gate. Failing it sends the work to 3.5.

### 3.5 Pattern — where ownability comes from

The fix is a pattern, and it is not decoration applied afterwards. It is drawn from the
brand's own material world — for Jamrah, the cracked surface of burning coal.

**Meet لهب — the flame.** Named, not called "the pattern." A named asset can be
discussed, reused, and defended, for the same reason art directions get names.

**It comes from the same root as everything else.** جمرة (ember) → لهب (flame) → the
crack structure of a burning coal. This is the mind map paying off exactly as designed:
a concrete, drawable node from Step 4 becoming a graphic system.

**And it is a register move, not a hue move.** Orange alone is a single variable a
competitor changes in an afternoon. A pattern derived from the brand's own material
cannot be taken back without abandoning their identity — which is why the differentiation
survives.

Applied across every surface: stationery, business cards, letterhead, social, packaging,
backgrounds. The before-and-after is the argument.

---

## Phase 4 — Presentation

The work has to reach the user properly. Two vehicles: **mockups** and **the
presentation**.

### Mockups

A mockup is a visualization illustrating the final outcome. Two requirements, and both
are pass/fail.

**1. Realism.** High quality, and genuinely photographic. A flat render with uniform
lighting, no depth of field, and shadows that match no real light source reads as fake
and undermines the work it is showing. A real photograph — real concrete, real shadow
falling across the surface, real dirt — sells it.

**2. Appropriateness.** The mockup must show the logo where it will actually appear.
An app's logo belongs on a home screen as an app icon. A construction company's belongs
on a site. A residential developer's belongs on hoardings, building signage, a sales
office, keys, and handover documents — **not** on a coffee cup and paperclips.

**The generic stationery flat-lay is the tell of a template applied without thinking.**
Coffee cup, binder clips, notebook, cards at an angle: it is the default mockup pack and
it says nothing about the business.

**Q13 is the mockup list.** The questionnaire already asks what elements the visual
identity requires. That answer determines what gets mocked up. Al-Nissal's answer names
packaging, stationery, social assets, and stickers — so: knife packaging, an engraved
blade, a knife roll, a shop sign. Never a generic pack.

#### What can actually be produced

There is no image generation available. This governs what is promised.

| Mockup type | Feasible | Method |
|-------------|----------|--------|
| App icon on a home screen | **Yes, well** | It is HTML — real device frame, real grid |
| Web page, dashboard, social post | **Yes, well** | Actually rendered UI |
| Favicon, browser tab | **Yes, well** | Literally the real thing |
| Flat print — cards, letterhead, poster | Adequate | Composite onto a real photo with a perspective transform |
| Signage, banners | Adequate | Same, and it works because the surface is flat |
| Curved or textured — cups, bottles, leather, engraving | **No** | Requires real warping; hand the user a template |

**The split:** build every screen-based mockup natively, composite the flat-surface ones,
and treat curved or textured surfaces as optional.

#### Mockups are not a direction choice

Direction was settled four gates earlier. A mockup does not ask *which way* — it answers
*does the way we chose survive a shop sign*. The gates that do offer choices are:

| Gate | What is offered |
|------|-----------------|
| Art direction (Ph2·5) | Named worlds. **Hard gate**, loops until approved |
| Logo concepts (Ph3.1) | Three to five different concepts, colourless |
| Palette and type (Ph3.2–3) | Derived, presented for confirmation |
| Boring test (Ph3.4) | Whether the assembly needs a pattern |

**Mockups can still send the work backwards.** A mark that dies on packaging, or a
palette that turns muddy in print, is a real failure found late — return to Phase 3. That
recursion is repair, not choice.

#### Always ask which surfaces, before building any

Q13 supplies the list, but tier-three mockups cost the user real effort or money. Building
all of them unasked is exactly the waste the process exists to prevent.

> "Q13 listed packaging, stationery, social, and stickers. The social and app mockups I
> can build now at no cost. Packaging and the engraved blade need either ten minutes in
> Photopea or an image tool — do you want those, and which route?"

The rule is the same one that governs the art direction gate, one level down: **never do
expensive work the user has not agreed to.** There it means *which world*; here it means
*which surfaces, and who pays the cost*.

#### Routes for curved and textured surfaces

Ranked. Present all of them with the honesty attached, and never block.

**A · PSD template in Photopea — accurate, free, about ten minutes.** Photopea is a
browser-based editor requiring no install and no licence. Mockup PSDs use smart objects:
double-click, paste the logo, done. The mark stays exactly correct because it is *placed*
rather than generated. **Recommended by default.**

**B · Generate the scene, composite the mark ourselves.** Have an image tool produce the
empty surface — the bare cup on a walnut table, lit correctly — then place the real logo
on top. Keeps the mark accurate and gets the surface cheaply. Works well on flat and
gently curved surfaces.

**C · Full image generation.** Fastest, and the mark will be wrong. Image generators
approximate logos: invented letterforms, wrong proportions, and mangled Arabic in
particular. Acceptable for an internal mood check, never for anything a client sees.

**D · Skip.** Always available. Mockups are a presentation aid, not the identity.

**When offering B or C, generate the prompt from the brief** — the approved art direction,
the palette with hex codes, the materials from the top-ten image list, the lighting, and
the exact surface from Q13. A generic template is not worth pasting. Ship the exported
PNGs from `export.sh` alongside it.

**Template sources** — almost all PSD, so they are for the user, not for us to execute:
mockups-design.com · mockupworld.co · unblast.com · Freepik · Placeit · LS Graphics.

### Presentation

The other half of showing the work properly. Mockups prove the identity survives contact
with the real world; the presentation is where everything gets composed and walked
through in order.

**Nothing new is decided here.** Every element already exists by this point. This is
assembly and delivery.

**The order, taken from the Jamrah presentation:**

1. **Typeface** — the family, its weights, and every script the brand uses, with full
   character sets and numerals.
2. **Colour** — the palette, each swatch carrying all four codes.
3. **Logo options** — presented colourless, so form is judged before colour.
4. **Assembly** — logo, colour, and type shown together. This is where the *boring test*
   is put to the user, not just applied privately.
5. **Pattern** — the named element, and the before-and-after that shows why it exists.
6. **Applications** — the composed boards: stationery, cards, letterhead, packaging,
   social, signage. Whatever Q13 listed.

**The before-and-after is the argument.** Assembly without the pattern looks correct and
generic; with it, the identity becomes ownable. Showing both, in that order, explains the
pattern better than any paragraph about it — and it is the same technique the reference
guidelines use for misuses: show the wrong version beside the right one.

Composed as HTML pages in the project folder, same mechanism as the questionnaire and the
boards.

---

## Phase 5 — Brand / Visual Identity Guidelines

The document that makes the identity survivable without us. Six elements.

### 1. Brand essence

Drawn from brand strategy — vision, mission, brand character, and tone of voice.

Brand strategy is a whole subject on its own and stays out of scope here. **The
questionnaire already captures all four inputs**: vision and mission in §1, brand
character in §2 Look & Feel, tone of voice in §3. Nothing new is gathered; what strategy
produced is what gets used.

### 2. Logo usage

Shows anyone how to use the logo across real applications. Anatomy, taken from the Saudi
Founding Day guideline (77 pages, bilingual):

| § | Section | What it fixes |
|---|---------|---------------|
| 01.1 | **Structure** | What the mark is made of — symbol plus wordmark. The lockup is never altered |
| 01.2 | **Colors** | Which colorways are permitted on which backgrounds; any reserved color and its allowed context |
| 01.3 | **Variations** | Primary lockup, secondary lockup, when each applies, and whether the parts may be used separately |
| 01.4 | **Clear space and minimum size** | Clear space in relative units; minimum size for print and digital |
| 01.5 | **Misuses** | The don'ts, shown as images with a red ✗ |
| 01.6 | **Positioning** | Where the mark sits on a layout |
| 01.7 | **Co-branding** | Placement among partner logos, and relative size |

Three techniques worth carrying into every guideline we produce:

- **Clear space in relative units.** X = the symbol's height, never a fixed millimetre
  value. One rule then scales from business card to billboard.
- **Minimum size in both systems.** Print in mm and digital in px — 16mm / 9.5mm and
  100px / 53px in the source. This turns the versatility rule from an aspiration into
  something testable.
- **Misuses shown, not described.** Eight wrong versions with a red ✗ beats any
  paragraph. People copy pictures.

**Bilingual guidelines must be cross-checked, not translated and shipped.** In the 2024
edition, section 01.6 contradicted itself between languages: the Arabic forbade placing
the logo at the bottom outright — *وعدم استخدامه في الأسفل إطلاقاً* — while the English
listed bottom as permitted.

**The 2026 edition fixed it:** *"may be placed in either upper corner or at the center. It
must not be used at the bottom."* A national brand team shipped the contradiction and
corrected it a year later. This is a defect class that reaches production, not a
hypothetical.

### Reference: what real guidelines do

`guidelines-analysis.md` — three books read in full (Coca-Cola, Discord, Saudi Founding
Day 2026), with the structural comparison and ten techniques worth adopting.

The most directly usable:

- **Clear space is always derived from the mark**, never an arbitrary measurement. All
  three do this — cap height, a rotated letter, symbol height.
- **Forbid pairings with stated reasons.** Discord bans specific color combinations and
  says why. A rule with a reason survives a designer who wants to break it.
- **Name fallback fonts.** Discord does; most do not. Without them the guideline breaks
  the moment someone opens a document without the licensed font.
- **Specify layout in percentages, not pixels.** Founding Day's templates are built as
  percentage stacks, so one template works at any output size.
- **Quantify photography direction.** Founding Day specifies 40/40/20 across men, women,
  and children, and 60/40 day to night. Checkable, unlike "authentic and warm."
- **Rank colorway fallbacks** rather than listing them, so an unanticipated situation
  still has an answer.
- **Vary line-height by copy length** rather than fixing one number.

**None of the three states a contrast ratio or mentions color blindness.** The
accessibility requirement in `color.md` is an improvement on all three references, not an
invention — keep it.

### 3. Color usage

- **Primary colors** — الألوان الأساسية
- **Color codes** — أكواد الألوان
- **Secondary colors** — الألوان الثانوية

**Every swatch carries four codes**, because each serves a different job:

| Code | Exists for |
|------|-----------|
| HEX | Web and digital handoff |
| RGB | Screen — emitted light |
| CMYK | Process printing, four-color |
| **PMS** | Spot color — exact, repeatable match |

PMS is the one most often dropped and the one that matters most for physical goods. CMYK
is mixed on press and drifts between runs, papers, and suppliers; Pantone is pre-mixed
ink, identical from every supplier in every country. Packaging, signage, and merchandise
depend on it.

Full swatch: `HEX FEE75C` · `RGB 254, 231, 92` · `CMYK 0, 5, 80, 0` · `PMS 102 C`.
Method in `color.md`.

### 4. Typography usage

- **Primary fonts** — الخطوط الأساسية
- **Secondary fonts** — الخطوط الثانوية
- **Hierarchy** — التسلسل الهرمي

### 5. Visual language

- **The distinctive look** — المظهر المميز — photography style
- **Pattern** — الباترن
- **Icons and illustrations** — الأيقونات والرسومات

This is where the pattern from Phase 3.5 is codified — the element that made the identity
ownable rather than merely correct.

### 6. Real-life applications

- **Print applications** — التطبيقات المطبوعة
- **Digital applications** — التطبيقات الرقمية

---

### The six at a glance

| # | Element | Contains |
|---|---------|----------|
| 1 | **Brand essence** — جوهر العلامة | Vision and values · brand personality · tone of voice |
| 2 | **Logo usage** — استخدام الشعار | Correct usage · sub-logos · safe areas · misuses |
| 3 | **Color palette** — استخدام الألوان | Primary · codes · secondary |
| 4 | **Typography** — استخدام الخطوط | Primary · secondary · hierarchy |
| 5 | **Visual language** — اللغة البصرية | Distinctive look · pattern · icons and illustrations |
| 6 | **Applications** — أرض الواقع | Print · digital |

---

## Rules the skill must enforce

Sourced from Stripe, "What is a visual identity for a brand":
https://stripe.com/resources/more/what-is-a-visual-identity-for-a-brand-how-it-works-and-how-to-create-the-right-one

- **Versatility.** Every mark must survive from favicon to billboard. If it dies at
  16px, it is not finished.
- **Trademark.** Name and mark must be checked for existing claims. Binds hardest to
  the Phase 1 naming method.
- **Timeless over trendy.** Do not date the identity to the year it was made.
- **Cultural safety.** Colors and symbols carry different meanings by market. Check
  against the stated audience.
- **Consistency.** One system applied across every touchpoint, not a set of one-offs.

---

## Out of scope — stated plainly, not silently skipped

Stripe's process runs seven phases. Its last three cannot be performed by an AI:

- Market testing with real audiences, A/B tests
- Internal team training, phased rollout, launch communications
- Ongoing performance monitoring and periodic refresh

The skill ends at the guidelines document and hands these to the human. It must say
so rather than imply it delivered them.

---

## Open threads

- **Divergence phase (recommended, not yet approved).** Stripe never produces one
  answer — it produces mood boards, several directions, then refines by reaction.
  Current spec is single-track, which fights the skill's own premise that users cannot
  generate but can react instantly. Proposal: 2–3 named directions, user picks, then
  the full kit is built from the winner.
- **Feeling collision rule.** Element 7 is captured as an input, unlike Stripe which
  derives emotion downstream. This makes collisions possible: a stated feeling that
  contradicts the audience or the category. Processing step needs a resolution rule.
- How each brief element is processed into visual decisions — user will define per element.
- Output format of the skill (guidelines doc, tokens, SVG assets, HTML style guide) — not yet discussed.
- How logo options are generated and presented — deferred by the user.
- **Image generation for mockups.** Possibly via a Higgsfield MCP or similar, to be
  explored later. It would unlock exactly one row of the mockup table — curved and
  textured surfaces — which is currently impossible. It would **not** help with logos,
  which must be vector, editable as curves, and exactly repeatable; generated raster marks
  fail all three. It is unnecessary for mood boards, where real photos are already free,
  licensed, and immediate. Do not design around it until it exists.
- Phase 4 presentation format — not yet defined.

Closed:

- ~~Handling of vague answers~~ — resolved. Push back once during Phase 2 Step 2 (Review).
- ~~Divergence phase~~ — resolved. Phase 2 (mood board & art direction) is the divergence step.
