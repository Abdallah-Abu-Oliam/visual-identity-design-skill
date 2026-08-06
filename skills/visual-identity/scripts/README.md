# Scripts

Tools the process needs at specific steps. **They were written during a real run and
rescued from a session scratchpad, which does not survive.** Without them here, every run
rewrites them at full cost.

---

## Install

```bash
python -m pip install Pillow numpy shapely
npm install sharp
```

**Use `python -m pip`, not `pip`.** On at least one machine they resolved to different
interpreters, so `pip install Pillow` succeeded and `python` still could not import it.

| Package | Needed by |
|---------|-----------|
| Pillow | every Python script |
| numpy | `composite.py` |
| shapely | `fixwreath.py` |
| sharp (npm) | `export.sh` |

---

## The tools

| Script | Step | Does |
|--------|------|------|
| **`palette.py`** | 3.2 Colour | WCAG contrast on **every** pairing · CMYK · dichromacy simulation · distance from occupied competitor colours |
| **`export.sh`** | 3.1 Logo | SVG to PNG at 7 sizes, plus a monochrome version. Refuses live `<text>`. Verifies its own output |
| **`logosheet.py`** | 3.1 Logo | Full size + 48px + **real rasterised 16px, magnified**, side by side per concept |
| **`sheet.py`** | 2.3 Research | Numbered contact sheet from an image folder, plus an index mapping number to filename |
| **`grain.py`** | 3.5 Pattern | Seamless tile — toroidal Poisson sampling, flow-field angles, wrap copies on every edge |
| **`groove.py`** | 3.5 Pattern | Coarser tile variant, curved tapered strokes. Kept because *offering two and rejecting one* is the method |
| **`composite.py`** | 4 Mockups | Perspective-warps real vector artwork onto a photo and blends **multiply**, so folds and grain show through. The mark is never redrawn |
| **`fixwreath.py`** | Logo repair | Boolean subtraction in draw order — punch the gap out of what sits behind, then union. Converts painted-white separations into real negative space |

---

## `palette.py` — run this one first

```bash
python palette.py brand/identity/palette.json
```

```json
{
  "palette":  { "Ink": "#2A211C", "Paper": "#FBF5EC", "Accent": "#E08A52" },
  "occupied": { "Competitor name": "#00AEEF" }
}
```

`occupied` is optional — the colours the competitor audit found already taken.

**It checks every pairing, not a hand-picked list.** That is how it found both of these,
and neither is findable by looking:

- **`#FBF5EC` on `#E08A52` = 2.44:1.** On a good monitor the pair looks fine. That is
  exactly how it reaches print.
- **Two colours collapsing to 1.22:1 under protanopia** — the same colour to a meaningful
  share of people. Fixed by separating on *value* rather than hue.

Output is ranked: colour-blindness collapses first, because they are rarer, more serious,
and invisible to everyone testing on their own screen. Exits `2` if any collapse is found.

A low-contrast pair is **not automatically a defect** — decorative pairs are supposed to sit
close. It is a defect only if you intended one of them to carry text.

---

## `export.sh` — and the bug it now guards against

```bash
bash export.sh <input.svg> <output-dir> [--allow-text] [--no-mono]
```

Run it on **every concept before presenting**, never only at the end. A browser-scaled SVG
is not a favicon; the rasteriser is the only thing that tells the truth.

Three fixes were made to this script after it silently failed on a real run:

1. **Git Bash paths.** The shell speaks `/c/Users/...`; node, Inkscape and rsvg-convert are
   Windows-native and cannot resolve it. Now converted with `cygpath`.
2. **Silent failure.** Every render is checked for a non-empty output file.
3. **Final count.** The run verifies it produced the expected number of files and fails
   loudly otherwise — *"expected 11 files, found 1."*

Before those, a failed run copied the SVG, skipped every PNG, and **looked like it had
worked.** That is worse than no script: it converts *unverified* into *falsely verified*.

---

## Honest state — what still carries brand-specific defaults

`palette.py`, `export.sh`, `logosheet.py` and `sheet.py` are generic.

The rest still carry values from the run they were written in, and need their brand
specifics passed in or edited before reuse:

| Script | Carries |
|--------|---------|
| `grain.py` · `groove.py` | Default ink colour, and a title string naming the source brand |
| `composite.py` | A brand name drawn into the mockup, its palette, and tile paths |
| `fixwreath.py` | Geometry specific to one wreath mark |

**They are worth keeping anyway.** The technique in each is the valuable part — the
boolean-subtraction approach in `fixwreath.py` applies to any mark with painted
separations, and the multiply-blend warp in `composite.py` applies to any mockup. Read them
as method, adapt the specifics.
