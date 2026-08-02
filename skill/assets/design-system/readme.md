# Brand Identity Kit

A reusable structure for **delivering** a brand's visual identity — the guidelines and the
presentation, as living pages rather than a flat PDF.

Every page reads from `styles.css`. Swap the tokens at the top of that file and the whole
kit re-renders in the new brand. That is the point: a template you parameterise, not a
document you edit page by page.

The demonstration content throughout is **Jamrah (جمرة)** — an ember. Replace it.

---

## How to use this

- **Link the one stylesheet from every page** — `<link rel="stylesheet" href="styles.css">`,
  adjusting the relative path — and take every colour, font, space and radius from its
  variables (`var(--color-*)`, `var(--font-*)`, `var(--space-*)`, `var(--radius-*)`).
  Never hard-code a hex, a font name or a pixel value a token already carries.
- **To rebrand, edit only `:root` in `styles.css`,** and keep `theme.json` in step so the
  machine-readable record does not drift from what the CSS actually does.
- **The pages are plain HTML.** View source and copy the markup rather than inventing
  parallel classes.

---

## The rule this kit is built on

**Brand identity is decided first; visual identity expresses it.** Every visual decision
traces back to a strategy decision. Blue is not "nice" — it is trust, which came from a
value, which came from the brief.

So every page carries its reasoning. The `.why` block exists for exactly this: the
derivation travels with the decision. A choice nobody can trace back to the brief cannot
be defended later, and will be overturned by the first person who dislikes it.

---

## Structure

| Group | Page | Covers |
|-------|------|--------|
| **Logo** | `logo/anatomy.html` | Structure, clear space in X units, minimum sizes, ranked colourways |
| | `logo/misuses.html` | Eight wrong versions, shown not described; positioning |
| **Foundations** | `foundations/color.html` | Three colours at 60/30/10, four codes each, contrast |
| | `foundations/type.html` | Two scripts set separately, scale, fallbacks, line-height |

Still to come: brand essence, pattern, imagery, layout templates, applications, and the
presentation deck.

---

## Colour

Three colours in fixed proportion — **60 / 30 / 10 by area, not importance.** The 60% is
the colour the eye rests on and is usually the calmest; the 10% is where the eye *goes*.
Palettes fail most often by making the loudest colour dominant, which exhausts the eye and
leaves the accent nowhere to go.

Every swatch carries **four codes**: HEX for web, RGB for screen, CMYK for process
printing, and **PMS for spot colour**. PMS is the one that gets dropped and the one that
matters most for physical goods — CMYK is mixed on press and drifts between runs, papers
and suppliers, while Pantone is pre-mixed ink that is identical from every supplier in
every country.

**Check contrast, and account for colour blindness.** None of Coca-Cola, Discord or Saudi
Founding Day states a ratio. Requiring it here improves on all three.

---

## Type

**A bilingual identity sets two typefaces, not one typeface with a fallback.** Arabic has
its own rhythm, baseline behaviour and leading needs; the line-height that reads
comfortably in Latin reads cramped in Arabic.

**Name a fallback for every face.** Without one the guideline breaks the moment somebody
opens a document on a machine without the licensed font.

**Line-height varies by copy length** — a two-word headline and a two-line headline need
different leading to look equally considered.

**In the logo, type becomes outline.** A finished wordmark contains no live text.
Rasterisers substitute whatever font they find, which distorts Latin letterforms and can
break Arabic letter joining outright, since Arabic shaping is contextual.

---

## Logo

**A logo does not carry meaning; it collects it.** The mark is a signature, not an
explanation, and it should never try to depict what the business does.

- **Clear space is stated in X**, where X is the height of the symbol — never a fixed
  millimetre value. One rule then scales from business card to billboard.
- **Minimum sizes are given for print and digital both.** If the mark dies at 16px it is
  not finished, and that is cheaper to discover before the concept is chosen.
- **Colourways are ranked, not listed**, so an unanticipated situation still has an answer.
- **The single-colour version is mandatory.** Engraving, embossing, foil, stamping and
  one-colour print all need it.
- **Bilingual wordmarks are drawn twice**, locking to one symbol — never translated at the
  end.

**Cross-check bilingual rules against each other.** A real national brand guideline shipped
an edition whose Arabic forbade placing the logo at the bottom while its English permitted
it. Translating and shipping is how that happens.

---

## Do

- Attach the derivation to every decision — use `.why`.
- Keep the accent to its 10%.
- Show misuses as pictures, beside the correct version.
- State every rule with its reason.

## Don't

- Do not hard-code a value a token already carries.
- Do not let a wordmark ship with live `<text>`.
- Do not treat Arabic as a fallback slot on a Latin face.
- Do not state a rule in one language without checking it in the other.

---

## Files

- `styles.css` — the only stylesheet: tokens in `:root`, then the component layer.
- `theme.json` — the parameters this kit was derived from, machine-readable.
- `thumbnail.html` — the project cover.
- `readme.md` — this guide.
