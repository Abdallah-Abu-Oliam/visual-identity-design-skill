# The Logo Step

**This step does not produce a finished mark. It produces a brief and a set of concept
directions, and hands them to the user to draw with — then verifies what comes back.**

That is a deliberate design, not a limitation being papered over.

---

## Why the handoff exists

Two independent runs, different brands, different briefs, different prompting:

| Run | Concepts generated | Usable |
|-----|-------------------|--------|
| Run A — one context, five marks in a row | 5 | 1, and it was mediocre |
| Run B — parallel agents, two rounds | 9 | **0** |

Run B cost **~750,000 subagent tokens** and the user drew the final mark themselves.

Three causes, all structural rather than fixable by better prompting:

**1 · The agents were blind.** They wrote SVG path coordinates with no way to look at the
result. On one run, **six separate rasterisers** were built by different agents inside their
own budgets — one drove headless Chrome, one wrote a Pillow renderer, one hand-wrote a
bezier flattener with point-in-polygon sampling. Each reinvented a render loop that already
existed in the main thread. *The ones that did not build one shipped Pac-Man.*

**2 · The prompts were mostly prohibitions.** Roughly 30% forbidden territory, 15% technical
constraints, and **12% actual creative instruction.** Telling a designer at length what not
to draw reliably produces timid work — and it did: a letter C, a bullseye, two floating
blobs.

**3 · Fan-out multiplies brief errors.** A wrong brief costs 1× in the main thread and N×
across N agents, in parallel, before anyone can see the result.

**The user has the one thing no subagent has: eyes, and a reaction in real time.** So the
drawing goes to them, and this skill keeps the parts it is genuinely good at — deriving
what the mark must be, and judging whether what came back survives.

---

## A · Derive the type — we do this

Load `logo-types.md`. The type is **derived, not asked**: name length and distinctiveness,
whether the brand has existing recognition, the competitor audit, personality, and the
applications listed in Q13.

Q14 is an input to this, never a substitute. Where the rules and the user's stated
preference disagree, **say so and explain** — never silently overrule, never silently
comply.

## B · Turn mind-map nodes into concept directions — we do this

Three to five directions, **in words**, each tracing to a different drawable node.

A direction is not a description of a picture. It names the **construction** and the
**source**:

> **The Hallmark** — a struck ring holding an eye whose upper and lower curves are blade
> profiles. *From عين الصقر merged with الحدّة: the falcon supplies the enclosure, the blade
> supplies the line that makes it.*

**Make them genuinely different constructions**, not five versions of one idea. A lettermark
built from the script · a negative-space cut · an asymmetric composition · a mark built from
repetition · a mark built from one continuous gesture.

**Check each against the cultural read before writing it down.** Ask what else the form
resembles in the stated market — flags, religious symbols, political emblems, existing
marks. A six-fold radial form was generated for an Iraqi brand on a real run and reached
presentation before anyone noticed what it was.

## C · The handoff package — we build this, the user runs it

Give the user everything needed to drive a logo tool themselves, in one paste-ready block.

The upstream **logo-designer skill** (MIT, https://github.com/neonwatty/logo-designer-skill)
is a good target: it runs Interview → Explore → Refine → Export with a human in the loop,
which is exactly the loop the agents lacked. Its interview questions are already answered by
our work — supply the answers rather than making the user invent them.

```
BRAND         name in both scripts · what it does · audience · market
MEANING       what the name means, why it was chosen
ADVANTAGE     what the mark must make felt first
FEELINGS      the targeted feelings, IN THE USER'S OWN WORDS
DIRECTION     the approved art direction: name + world description
FORMAT        the derived logo type
COLOUR        monochrome — black on white, no colour at concept stage
FORBIDDEN     the exclusion list, including cultural exclusions
OCCUPIED      what competitors already hold, so the mark avoids it
DIRECTIONS    the three-to-five concept directions from B, each with its source
CONVENTIONS   the SVG conventions below
```

**`FEELINGS` uses the user's words, verbatim.** Not your translation of them. If they wrote
*playful* and *mascot*, the brief says playful and mascot — not *"approachable, minimal."*
This is where the most expensive failure in this skill's history happened.

**Invert the ratio the upstream prompts used.** Prohibitions belong in a linked file or a
short appendix; the creative instruction belongs at the top and should be the longest part.

## D · Verify what comes back — we do this

The user returns with a mark. **This is where the skill earns its keep**, and none of it is
expensive.

- **Run `scripts/export.sh` before anything else.** Not at the end. A browser-scaled SVG is
  not a favicon — the rasteriser is the only thing that tells the truth. On a real run a
  mark read as a legible eye at 16px in a CSS-scaled preview and rasterised to a blurry
  bullseye with the eye gone.
- **Look at the real 16px PNG.** If it dies there, it is not finished.
- **Check the monochrome version.** `export.sh` produces it. Engraving, foil and stamping
  will strip the colour whether the mark survives it or not.
- **Confirm no live `<text>`.** The export guard refuses it — rasterisers substitute fonts,
  which distorts Latin letterforms and breaks Arabic letter joining outright.
- **Run the cultural read again** on the actual form, not the description.
- **Redraw test.** Describe the mark in one sentence someone could draw from. If the
  sentence needs three clauses, it is too complex.
- **Judge distinctiveness against the competitor audit**, not against taste.

Then derive clear space in X units, minimum sizes for print and digital, and the ranked
colourways. That work is cheap, mechanical, and genuinely ours.

---

## If the user asks us to sketch anyway

Some will. Then:

- **Main thread only. Never fan out.** The main thread can render and look; a subagent
  cannot.
- **Two or three, not five.** Render each, look at it, iterate. A loop with eyes beats
  volume without them.
- **Say plainly what they are:** rough sketches to react to, not finished marks. On the
  evidence above, that is what they are.

---

## SVG conventions — for whoever draws

- `viewBox="0 0 512 512"` for icons, `1024x512` for wordmarks and lockups. **No `width` or
  `height` on the root.**
- **Self-contained.** No external fonts, images, or cross-file `<use>`.
- **No live `<text>` in a finished mark.** Convert to `<path>`. A logo that depends on an
  installed font is not a logo.
- **Meaningful group IDs** — `id="icon"`, `id="wordmark"`, `id="tagline"` — so "enlarge the
  icon" is a one-line edit.
- **Flat fills by default.** Gradients only when the direction genuinely calls for them.
- **Small-size survival** — solid fills over thin strokes, `stroke-width` 6 or more, and no
  detail that dies at 32px.
- **Monochrome at concept stage.** Colour rescues weak forms and flatters bad ones.
- **A single-colour version is mandatory**, not optional — engraving, embossing, foil,
  stamping and one-colour print all need it.
- **Bilingual wordmarks are drawn twice**, locking to one symbol. Never translated at the
  end. Arabic calligraphic wordmarks are a specialist craft: set them in a real Arabic
  typeface or hand them to a human — do not emit approximate bezier paths.

---

## Evidence

One run left behind eighteen files the subagents had written **for themselves**: six
separate rasterisers and six separate search helpers, none of which anyone asked for.

That is the clearest argument for the handoff. Six agents, working in parallel on the same
task, each independently concluded it could not do its job without eyes — and each spent a
large share of its creative budget building them. The two that did not build one shipped
marks that could not have survived a single glance.

**If you find yourself writing a renderer inside an agent prompt, stop.** The conclusion has
already been drawn: the drawing belongs where the eyes are.
