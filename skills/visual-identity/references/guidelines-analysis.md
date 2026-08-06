# What Three Real Brand Guidelines Do

Read in full: Coca-Cola Brand Manual (18pp) · Discord Brand Guidelines v1.0 (73pp) ·
Saudi Founding Day 2026 (73pp, bilingual).

Files in `design-guidelines-examples/`.

---

## The contradiction we caught was real, and they fixed it

The 2024 Founding Day guideline said, in section 01.6:

- **Arabic:** upper corners or center, *وعدم استخدامه في الأسفل إطلاقاً* — never at the bottom.
- **English:** "can be placed at the top, **bottom**, center or the four corners."

The 2026 edition:

> "The Founding Day logo may be placed in either upper corner or at the center.
> **It must not be used at the bottom.**"

English now matches Arabic. A national brand team shipped the contradiction, then
corrected it a year later. Cross-checking bilingual rules is not a theoretical concern —
it is a defect class that reaches production.

---

## Structure — all three converge

| | Coca-Cola | Discord | Founding Day |
|---|-----------|---------|--------------|
| **Essence** | Tone of voice, 4 pillars | Mission, vision, positioning, brand values, tone | Introduction, strategy |
| **Logo** | 2 formats, clear space, min size, correct/incorrect | Logo, icon, wordmark, tagline, clear space, placement, partnership lockups, misuses | Structure, colors, variations, clear space, misuses, positioning, co-branding ×2 |
| **Color** | Primary, product, flavor | Palette, pairings, schemes, forbidden combos, UI colors | Named primaries + 8 secondaries, Pantone-first |
| **Type** | Primary/secondary, hierarchy in pt | 2 families + fallbacks, typestyles, line-heights, measure | Arabic + English faces, type color rules |
| **Visual language** | 3 heritage assets, photography, illustration | Community Pattern | 9 icons + 4 seasonal, 3D icons, modular and circular patterns |
| **Applications** | Campaign history | Brand lines, user quotes, chat dialogs, end cards, stationery | 7 templates with percentage grids |

The six-element structure holds across all three. What differs is depth, and where each
brand spends it.

---

## Techniques worth stealing

### 1. Clear space is always derived from the mark itself

- **Coca-Cola** — the height of the capital C in the script.
- **Discord** — "pick the letter *o*, rotate it 90°, duplicate it."
- **Founding Day** — symbol height = X.

None uses an arbitrary measurement. The unit comes out of the logo, so it scales with it
automatically. Adopt this without exception.

### 2. Discord forbids color pairings, with reasons

Most guidelines list approved combinations. Discord also lists banned ones, each with a
stated cause:

> Blurple + Fuchsia — "too hard to read." Fuchsia + Green — "too vibrant when combined,
> creating an uncomfortable reading experience." Yellow + Green, White + Yellow,
> Fuchsia + Red — "too similar, don't create enough contrast."

A rule with a reason survives contact with a designer who wants to break it. A rule
without one gets broken.

### 3. Discord orders the color scheme layers

> Decorative Color · Text Color · Background Color
> "The order of these layers matters and cannot be shuffled around."

This is 60/30/10 made operational — roles assigned, not just proportions.

### 4. Discord specifies fallback fonts

> Ginto Nord → Poppins Black (all caps). Whitney → Roboto Normal.

Almost always missing, and the guideline breaks without it the moment someone outside the
company opens a document without the licensed font. **Every typography section we produce
must name fallbacks.**

### 5. Discord varies line-height by copy length

| Style | Short copy | Longer copy |
|-------|-----------|-------------|
| Ultra Headline | 80% | 95% |
| Primary Headline | 90% | 110% |

Conditional rules, not one number. Plus a measure spec: paragraphs run 50–75 characters,
about 11 words in English, at 135% line-height.

### 6. Coca-Cola scales the ® by application

The registered trademark symbol scales with the context — large-scale signage, packaging,
stationery — and a small-scale script needs a **1.5X** symbol to stay legible. A legal
requirement treated as a design variable.

### 7. Founding Day builds templates in percentages

> 04% margin · 08% logo · 17% margin · 19% text · 45.5% margin · 2.5% link · 04% margin

Percentages, never pixels. One template then works at any output size, and every format —
vertical, long vertical, square, square ads, horizontal — carries its own breakdown. This
is directly implementable and should be how we specify layout.

### 8. Founding Day quantifies photography direction

> Portraits: **40% men, 40% women, 20% children.** Black and white, chest up, eyes to
> camera, traditional dress, regional settings, no studio.
> Events: **60% daytime, 40% night.**

Photography direction as a measurable spec rather than adjectives. Most guidelines say
"authentic and warm" and leave everything to interpretation. This can be checked.

### 9. Founding Day derives its pattern from an icon set

Nine icons — Arabian horse, architectural ornament, calligraphy strokes, falcon, fanjal,
first Saudi State flag, date palm, majlis, market — plus four seasonal. "These icons can
be used individually or repeated together to create a new pattern."

The pattern is generated by a system rather than drawn once. Compare Jamrah's لهب, which
came from the brand's material. Both routes work; this one scales further.

### 10. Discord's logo colorway hierarchy is ranked, not listed

> 1. White Clyde on blurple — preferred. 2. Blurple on white — when option one does not
> work. 3. White on black — when blurple is not possible. 4. Black on white — when white
> does not work.

A ranked fallback chain, so a designer in an unanticipated situation still knows what to
reach for next.

---

## What none of them do

**No contrast ratios.** Discord comes closest — it reasons about contrast constantly and
bans pairings for failing it — but no guideline here states a measurable threshold or
mentions color blindness. Our `color.md` requirement stands, and it is a genuine
improvement on all three references rather than an invention.

---

## A caution about the Coca-Cola file

It is not a reliable reference and should not be cited as authoritative practice:

- It names **Inter** as the primary typeface while displaying **Aeonik** in the same
  section, then reverses the two in the following paragraph.
- The Diet Coke Caffeine Gold swatch reads `RGB TBC`, `CMYK TBC`, and `HEX #000000` —
  black, for a color named gold.
- A "Georgia Green PANTONE" swatch carries no Pantone number.

Placeholders left in and contradictory type assignments mean this is a study or
recreation rather than a shipped manual. **Its structure is still instructive; its
details are not trustworthy.** Worth remembering that a document looking like a brand
guideline does not make it one — which is exactly why the model should verify a reference
before following it.
