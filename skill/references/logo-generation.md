# Logo Generation

Engine adapted from **neonwatty/logo-designer-skill** (MIT) —
https://github.com/neonwatty/logo-designer-skill

**Take the engine. Reject the interview.** That skill's mechanics are sound and solve
exactly what we lacked. Its Phase 1 interview asks for style, colour, and format as
preferences, which contradicts the method this skill is built on. Ours derives all three.

---

## Where this sits

Step 13 of the process, and it does not begin until the art direction gate has passed.

Inputs already in hand by then — no interview required:

| Input | Comes from | Decides |
|-------|-----------|---------|
| Logo type | `logo-types.md`, derived | Wordmark, lettermark, pictorial, abstract, combination, emblem, mascot |
| Creative directions | Mind map's drawable nodes | What each concept actually depicts |
| Forbidden territory | Values, "what do you stand against" | What must never appear |
| Occupied territory | Competitor audit | What we cannot look like |
| Register | Look & Feel and Tone axes | Loud or quiet, sharp or soft |
| Required applications | Q13 | Whether it must survive engraving, co-branding, favicons |
| Language | Q1 | Whether the wordmark is drawn once or twice |

**Colour is not an input here.** Concepts are generated in black on white. The palette is
step 14 and arrives after the form is chosen.

---

## Phase A — Concepts (divergence)

Three to five **genuinely different** concepts. Not variations — different metaphors,
different constructions. Each one traces to a different node on the mind map.

**Generate in parallel.** One subagent per concept, all dispatched in a single message.
Each agent receives the full brief, its assigned direction, the SVG conventions, and its
target path. Agents share no context, so each prompt must be complete.

```
logos/
  concepts/
    concept-1.svg … concept-5.svg
  preview.html
```

**Every concept is monochrome — black on white.** Colour rescues weak forms and flatters
bad ones. Judge the shape alone or the judgement is worthless.

Present the preview, describe each concept in one sentence **with its derivation** — "the
falcon's eye, where the curve doubles as a blade edge" — and ask which direction to
pursue. The reasoning is part of the presentation; a concept nobody can trace back to the
brief cannot be defended later.

## Phase B — Iterations (refinement)

Once a direction is chosen, iterate within it.

- **Single change** — apply it directly, write the next numbered iteration.
- **Batch exploration** — parallel agents again, each receiving the full base SVG inline.

```
logos/
  iterations/
    iteration-1.svg …
  preview.html      (regenerated, newest first)
```

Keep group IDs stable across iterations so changes stay traceable.

## Phase C — Export

`scripts/export.sh <input.svg> <output-dir>` — produces PNG at 16, 32, 48, 192, 512,
1024, 2048. Detects resvg, npx resvg, sharp, Inkscape, or rsvg-convert, in that order.
Fails with install instructions if none is present.

---

## SVG conventions

Adopted from the source skill; all of these are correct.

- **`viewBox="0 0 W H"` with no fixed `width`/`height`.** 512×512 for icons, 1024×512 for
  wordmarks and combination marks.
- **Self-contained.** No external fonts, images, or cross-file `<use>` references.
- **Text** — system fonts with a generic fallback, or converted to `<path>`. For any
  finished mark, convert to paths: a logo that depends on an installed font is not a logo.
- **Meaningful group IDs** — `id="icon"`, `id="wordmark"`, `id="tagline"`. Makes "enlarge
  the icon" a one-line edit instead of a rewrite.
- **Flat fills by default.** Gradients only when the direction genuinely calls for them.
- **Small-size survival** — solid fills over thin strokes, `stroke-width` 6 or greater, no
  detail that dies at 32px.
- **Clean markup** — no stray transforms, no empty groups.

### Additions our method requires

- **Monochrome during concepts.** `fill="#000"` on white. No colour until step 14.
- **A single-colour version is mandatory, not optional.** Engraving, embossing, foil,
  stamping, and one-colour print all need it. Al-Nissal's brief requires it outright.
- **Bilingual marks are drawn twice.** Arabic and Latin wordmarks are separate drawings
  that lock to the same symbol — never one translated at the end.
- **Clear space defined in relative units**, derived from the mark itself. Every reference
  guideline does this; see `guidelines-analysis.md`.

---

## The favicon size check — keep this

The source skill renders each option at 64px, 32px, and 16px beneath the preview grid.

This is the **versatility rule made visible**. "It must survive at favicon size" is an
aspiration until you can see it failing. Include it during iterations, always, and act on
what it shows: thin strokes that vanish get thickened, fine detail that turns to mush gets
removed.

---

## What was deliberately discarded

| Discarded | Why |
|-----------|-----|
| "What style direction?" — minimal / playful / bold | A blank taste question. Style is derived from strategy, feelings, and competitor whitespace |
| "Any colour preferences? Surprise me" | Destroys the derivation chain in `color.md` |
| "What format?" — icon / wordmark / combination | Derived in `logo-types.md` from name, recognition, and applications |
| Coloured concepts | Contradicts judging form first |
| Repo integration phase | Aimed at software projects; irrelevant here |

**The absence that matters most: no competitor input anywhere.** That skill will happily
produce a mark resembling the category leader, because nothing in it knows what is already
taken. Differentiation is the logo's primary job, so this cannot be inherited as-is.
