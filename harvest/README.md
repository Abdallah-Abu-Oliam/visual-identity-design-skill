# Harvest — reusable work from the Noyau run

Everything here was written during one real run of the skill and then rescued from the
session scratchpad, which does not survive. **Nothing in this folder is wired into the skill
yet** — it is raw material for deciding what to promote into `skill/scripts/` and
`skill/assets/`.

---

## `scripts/` — the seven worth shipping

| Script | Run it | Does | Needed at |
|---|---|---|---|
| **`palette.py`** | `python palette.py` | WCAG contrast for every pairing · CMYK conversion · **protanopia/deuteranopia/tritanopia simulation** · distance from occupied competitor colours | 3.2 Colour |
| **`logosheet.py`** | `python logosheet.py 1 2 3` | Full size + 48px + **real rasterised 16px magnified**, side by side per concept | 3.1 Logo |
| **`sheet.py`** | `python sheet.py folder1 folder2` | Numbered contact sheet PNG from an image folder, plus an index txt mapping number → filename | 2.3 Research |
| **`composite.py`** | import | Perspective-warps real vector artwork onto a photo and blends **multiply**, so folds and grain show through the ink. The mark is never redrawn | 4 Mockups |
| **`grain.py`** | `python grain.py SEED N out.svg` | Seamless tile — toroidal Poisson sampling, flow-field angles, wrap copies on every edge | 3.5 Pattern |
| **`groove.py`** | `python groove.py SEED N out.svg` | Coarser tile variant, curved tapered strokes. Kept because *offering two and rejecting one* is the method | 3.5 Pattern |
| **`fixwreath.py`** | `python fixwreath.py` | Boolean subtraction in draw order — punch a gap out of what is behind, then union the shape. Converts painted-white separations into real negative space | Logo repair |

### Ship `palette.py` first

It caught two failures that would otherwise have shipped:

- **`#FBF5EC` on `#DE8560` = 2.44:1.** Fails outright. On a good monitor the pair looks fine — which is exactly how it reaches print.
- **Apricot vs Olive = 1.22:1 under protanopia.** The same colour to a meaningful share of people. Fixed by separating on *value* instead of hue.

Neither is findable by looking.

### Dependencies

`Pillow` (all) · `numpy` (`composite.py`) · `shapely` (`fixwreath.py`) · `sharp` via npm for
`export.sh`. Note `pip` and `python` resolved to **different interpreters** on this machine —
use `python -m pip install <pkg>`.

---

## `agent-artifacts/` — evidence, not tools

**18 files the subagents wrote for themselves.** Do not reuse them; read them as a
diagnosis.

- **Six separate rasterisers** — `render.py`, `render9.py`, `render9b.py`, `render9c.py`,
  `render_c7.py`, `raster_check.py`, plus `verify_svg9.py` and `verify_final.py`. One logo
  agent drove headless Chrome, one wrote a Pillow renderer, one hand-wrote a bezier
  flattener with point-in-polygon sampling — **because none of them could see their own
  work.** Each rebuilt the same thing, independently, inside its own token budget.
- **Six search helpers** — `search.py` … `search6.py`, `openverse_fetch.py`, `wm_parse.py`,
  `wm_titles.py`. Same story on the research side.

**The fix is one line in each agent prompt:** give them a render command instead of letting
them invent one. The agents that built a rasteriser caught real misreadings — a bear's paw
print, a seed fused invisibly into a body. The ones that did not build one shipped
**Pac-Man**.

---

## `design-system-bundle/` — the delivered guidelines

The full 29-file Claude Design bundle: **10 pages sharing one `styles.css`.**

This is the proof that the eleven bespoke preview pages elsewhere in the run were avoidable
— every one of them re-declared the same colours, the same `.why` block, the same card grid
inline.

Useful as a **worked example** alongside `skill/assets/design-system/`, which is the blank
template. Between them you have the structure and one complete filling of it.

Note the conventions that matter: the first-line `<!-- @dsCard group="…" -->` marker builds
the gallery index, and the `.why` block carries each decision's derivation inline.

⚠ Two things this bundle got wrong on first upload, both worth adding to the template's own
checklist:

1. **A named font with no source** (`Cascadia Mono` in `--font-mono`) makes the design system
   report a missing brand font. Use generic families unless the face actually loads.
2. **The cover broke two of the book's own rules** — the mark and the body copy were laid
   straight onto the pattern. A guideline that contradicts itself teaches people to ignore
   all of it. Sweep for self-contradiction, not just for `TBC`.

---

## `samples/`

- `grain-7.svg` — the accepted pattern tile
- `groove-5.svg` — the rejected coarse variant, kept so the comparison survives
- `noyau-mark-fixed.svg` — the mark after the boolean gap repair
