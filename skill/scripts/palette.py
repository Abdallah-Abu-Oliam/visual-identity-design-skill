#!/usr/bin/env python3
"""
palette.py — audit a brand palette. Ship this one first.

    python palette.py [palette.json]

Reads a JSON file; writes nothing. Defaults to brand/identity/palette.json.

    {
      "palette":  { "Ink": "#2A211C", "Paper": "#FBF5EC", ... },
      "occupied": { "Competitor name": "#00AEEF", ... }
    }

`occupied` is optional — the colours the competitor audit found already taken.

Checks every pairing, not a hand-picked list. Two real failures were found this way and
neither is findable by looking:

  - a 2.44:1 pairing that looks fine on a good monitor, which is exactly how it reaches print
  - two colours collapsing to 1.22:1 under protanopia — the same colour to a meaningful
    share of people. Fixed by separating on value instead of hue.
"""
import json, sys, itertools, os

# ---------- colour maths ----------------------------------------------------------

def hx(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def lum(rgb):
    r, g, b = (lin(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = lum(hx(a)), lum(hx(b))
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def cmyk(h):
    r, g, b = [c / 255 for c in hx(h)]
    k = 1 - max(r, g, b)
    if k >= 1:
        return (0, 0, 0, 100)
    c = (1 - r - k) / (1 - k); m = (1 - g - k) / (1 - k); y = (1 - b - k) / (1 - k)
    return tuple(round(v * 100) for v in (c, m, y, k))

def simulate(h, kind):
    """Brettel-style dichromacy simulation through an LMS pipeline."""
    r, g, b = [lin(c) for c in hx(h)]
    L = 17.8824 * r + 43.5161 * g + 4.11935 * b
    M = 3.45565 * r + 27.1554 * g + 3.86714 * b
    S = 0.0299566 * r + 0.184309 * g + 1.46709 * b
    if kind == 'protan':
        L2, M2, S2 = 2.02344 * M - 2.52581 * S, M, S
    elif kind == 'deutan':
        L2, M2, S2 = L, 0.494207 * L + 1.24827 * S, S
    else:
        L2, M2, S2 = L, M, -0.395913 * L + 0.801109 * M
    r2 = 0.0809444479 * L2 - 0.130504409 * M2 + 0.116721066 * S2
    g2 = -0.0102485335 * L2 + 0.0540193266 * M2 - 0.113614708 * S2
    b2 = -0.000365296938 * L2 - 0.00412161469 * M2 + 0.693511405 * S2
    def out(c):
        c = max(0.0, min(1.0, c))
        c = 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055
        return int(round(max(0, min(1, c)) * 255))
    return '#%02X%02X%02X' % (out(r2), out(g2), out(b2))

def dist(a, b):
    return sum((x - y) ** 2 for x, y in zip(hx(a), hx(b))) ** 0.5

# ---------- input -----------------------------------------------------------------

TEMPLATE = {
    "palette":  {"Ink": "#000000", "Paper": "#FFFFFF", "Accent": "#CC5500"},
    "occupied": {"Competitor A": "#0055CC"},
}

path = sys.argv[1] if len(sys.argv) > 1 else 'brand/identity/palette.json'
if not os.path.exists(path):
    print(f"No palette file at: {path}\n")
    print("Create one in this shape, then run again:\n")
    print(json.dumps(TEMPLATE, indent=2))
    sys.exit(1)

data = json.load(open(path, encoding='utf-8'))
P = data.get('palette') or {}
OCCUPIED = data.get('occupied') or {}
if not P:
    print(f"'{path}' has no 'palette' object."); sys.exit(1)

W = max(len(n) for n in P) + 1
fails, warnings = [], []

# ---------- swatches --------------------------------------------------------------

print('=== SWATCHES ===')
for n, h in P.items():
    c, m, y, k = cmyk(h)
    print(f'{n:{W}s} HEX {h.upper()}  RGB {hx(h)}  CMYK {c},{m},{y},{k}')
print('\nAdd a PMS number to each before delivery — CMYK drifts between print runs, Pantone does not.')

# ---------- contrast, every pairing -----------------------------------------------

print('\n=== CONTRAST - every pairing (WCAG) ===')
print('Not every pair is meant to carry text. What matters is that a pair you INTEND')
print('for text clears 4.5:1, and that nothing sits in the invisible band below 3:1.\n')
for a, b in itertools.combinations(P, 2):
    r = ratio(P[a], P[b])
    if   r >= 7:   verdict = 'AAA  - any text'
    elif r >= 4.5: verdict = 'AA   - body text ok'
    elif r >= 3:   verdict = 'large text / UI only'
    else:
        verdict = 'DECORATIVE ONLY - never text'
        fails.append(f'{a} on {b} is {r:.2f}:1 - decorative only, never text')
    print(f'{a:{W}s} on {b:{W}s} {r:5.2f}:1   {verdict}')

# ---------- occupied territory ----------------------------------------------------

if OCCUPIED:
    print('\n=== DISTANCE FROM OCCUPIED COLOURS (sRGB euclidean) ===')
    for n, h in OCCUPIED.items():
        near, nh = min(P.items(), key=lambda kv: dist(kv[1], h))
        d = dist(nh, h)
        flag = '  ⚠ TOO CLOSE' if d < 60 else ''
        if d < 60:
            warnings.append(f'{near} sits {d:.0f} from {n} — the category already owns it')
        print(f'{n:18s} {h.upper()}  nearest ours: {near:{W}s} {nh.upper()}  distance {d:6.1f}{flag}')

# ---------- colour blindness ------------------------------------------------------

print('\n=== COLOUR BLINDNESS - pairs that collapse ===')
blind = []
for kind in ('protan', 'deutan', 'tritan'):
    sim = {n: simulate(h, kind) for n, h in P.items()}
    collapsed = []
    for a, b in itertools.combinations(P, 2):
        before, after = ratio(P[a], P[b]), ratio(sim[a], sim[b])
        if after < 1.5 and before >= 1.5:
            collapsed.append((a, b, before, after))
            blind.append(f'{a} and {b} become one colour under {kind} '
                         f'({before:.2f}:1 -> {after:.2f}:1)')
    if collapsed:
        for a, b, before, after in collapsed:
            print(f'  {kind}: {a} / {b}  {before:.2f}:1 becomes {after:.2f}:1')
    else:
        print(f'  {kind}: no collapses')

# ---------- verdict ---------------------------------------------------------------
# Ranked. Colour blindness first: rarer, more serious, and invisible to everyone testing.

print('\n=== WHAT TO ACT ON ===')
acted = False

if blind:
    acted = True
    print('\n  COLOUR BLINDNESS - fix these:')
    for w in blind:
        print(f'    ! {w}')
    print('    Separate them on VALUE (lightness), not hue. Hue is what is lost.')

if warnings:
    acted = True
    print('\n  OCCUPIED TERRITORY - check these:')
    for w in warnings:
        print(f'    ! {w}')

if fails:
    acted = True
    print(f'\n  {len(fails)} pairing(s) below 3:1 - decorative only, never text:')
    for f in fails:
        print(f'    - {f}')
    print('    This is normal for decorative pairs. It is a defect only if you')
    print('    intended one of them to carry text.')

if not acted:
    print('  Clean.')

sys.exit(2 if blind else 0)
