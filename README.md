# Visual Identity

**Turns a project into a brand, then derives its visual identity from that.**

A Claude Code skill. Not a design skill — a design skill makes things look good. This one
decides *who the brand is* first, then derives how it looks. The order is enforced, and
every visual decision has to trace back to a strategy decision.

Blue is not "nice". Blue is trust, which came from a value, which came from the brief.

```
brief → mood board & art direction → logo → colour → type → pattern → mockups → guidelines
                    ▲
              hard gate: nothing after this begins until a direction is approved
```

---

## Install

```bash
claude plugin add Abdallah-Abu-Oliam/visual-identity-design-skill
```

Then just say what you want:

> *"I want to build a brand for my knife shop"* · *"design a visual identity"* ·
> *"make brand guidelines"* · *"help me name my startup"*

Optional, for logo rasterising and the palette audit:

```bash
npm install sharp
python -m pip install Pillow numpy shapely
```

---

## Two problems it is built around

**1 · Most people cannot answer "what are your brand values?"**

They can react instantly to three proposed ones. So the skill never hands you a blank
field — it drafts from what it already knows, shows you, and lets you correct. Reacting is
easy. Generating from nothing is not.

**2 · Correct-but-generic is the default outcome of a competent process.**

Logo, colour and typography done properly produce something that could belong to any
brand. The skill has a step that names this out loud — *could this belong to any
identity?* — and a phase for fixing it.

---

## What it actually does

### 1 · The brief

Seven things, asked as one list so you can answer in one go. Facts you already have.

What it is · the name *(optional)* · why that name *(optional)* · who it is for ·
competitors · your advantage · how it should feel.

No name yet? It runs a naming method **for** you rather than handing you an eleven-step
checklist.

### 2 · Mood board and art direction

Read what you gave it · review and resolve contradictions · research what competitors
already own · map every keyword until an idea becomes something drawable · then build
two or more named art directions and put them to you.

**This is a hard gate.** Nothing downstream starts until you approve a direction. It is
the last point where changing your mind costs nothing.

### 3 · Visual identity

Logo → colour → typography → assembly → pattern.

Concepts are presented **colourless**, because colour rescues weak forms. The palette is
derived from your audience, your feelings and what the category already occupies — never
picked because it looks good. Then the boring test, and a pattern to fix it if it fails.

### 4 · Mockups and presentation

Realistic and *appropriate* — the surfaces the mark will actually appear on, not a generic
stationery flat-lay.

### 5 · Guidelines

Six core sections plus thirteen optional ones, each with the trigger that decides whether
it belongs. Delivered as a live design system, not a flat PDF, so another session can build
your website from the same tokens.

---

## What makes it different

| | |
|---|---|
| **Every decision shows its reasoning** | A choice nobody can trace gets overturned by the first person who dislikes it |
| **What you typed outranks what it inferred** | Research says "calm", you said "playful" — yours wins, and conflicts get raised, never resolved silently |
| **Competitors decide what is forbidden** | Differentiation is the logo's primary job. The palette comes out of what is *not* taken |
| **Bilingual is designed, not translated** | Arabic and Latin wordmarks are drawn twice and locked to one symbol. Rules are cross-checked in both languages |
| **Looping is the process working** | A rejected direction costs an afternoon. The same problem found at delivery costs the identity |
| **It says what it cannot do** | Market testing, rollout and monitoring are out of scope, and it tells you so |

---

## Honest limits

**It does not draw your logo.** Two full runs produced fourteen concepts and one usable
mark; the expensive one burned ~750k tokens and the user drew the final mark themselves.
Model-generated SVG marks are not deliverable yet.

So the logo step does what it is genuinely good at: derives the type, turns your mind map
into concept *directions*, and hands you a paste-ready brief to draw with — then verifies
what comes back. Real 16px rasters, monochrome survival, cultural read, the redraw test.

**Mockups on curved surfaces need you or a template.** Flat surfaces and screens it handles;
cups, packaging and leather need Photopea and ten minutes.

**Composited mockups are review artifacts, not print-resolution.**

---

## What is inside

```
skills/visual-identity/
├── SKILL.md                     the runner
├── references/                  13 files — the method
│   ├── brief.md                 what each of the seven asks is FOR
│   ├── naming.md                an 11-step method, run for the user
│   ├── research.md              sources, tested, with what each is for
│   ├── logo-fundamentals.md     what a logo is, and the failure to design against
│   ├── logo-types.md            7 types, 3 treatments, derived not asked
│   ├── logo-generation.md       the handoff, and why it exists
│   ├── color.md                 60/30/10, five harmony methods, four code systems
│   ├── pattern.md               where ownability comes from
│   ├── guidelines.md            6 core + 13 optional sections, with triggers
│   ├── guidelines-analysis.md   three real brand books, read in full
│   └── design-delivery.md       shipping it as a live design system
├── assets/
│   ├── questionnaire.html       47 fields, English/Arabic with RTL, autosave
│   ├── preview.css + pick.js    one stylesheet and one readback layer
│   └── design-system/           the guidelines template
└── scripts/                     8 tools — see scripts/README.md
```

**`palette.py` is the one to try first.** It caught a 2.44:1 pairing that looks fine on a
good monitor, and two colours that become identical under protanopia. Neither is findable
by looking.

---

## Contributing

Contributions welcome — especially these:

- **Run it on a real brand and report what broke.** Every rule in here came from a failure.
  The [test run](harvest/README.md) found seven, and they are all documented.
- **Non-Latin scripts.** Arabic support is real but it is one script. Devanagari, CJK,
  Cyrillic all have their own typographic rules and none are covered.
- **Sources.** `references/research.md` lists museum and archive APIs. Several are marked
  untested — testing one and reporting the pattern is a genuinely useful contribution.
- **The logo step.** If model-generated marks become viable, this design should change. Show
  the evidence.

Open an issue before a large change so we can agree the shape.

---

## Credits

The method is drawn from working practice, from published brand guidelines read in full —
Coca-Cola, Discord, Saudi Founding Day 2026 — and from
[Stripe's guides](https://stripe.com/resources/more/how-to-pick-a-name-for-your-startup-a-step-by-step-guide)
on naming and visual identity.

`scripts/export.sh` is derived from
[neonwatty/logo-designer-skill](https://github.com/neonwatty/logo-designer-skill) (MIT),
modified — see [NOTICE](NOTICE).

MIT licensed. See [LICENSE](LICENSE).
