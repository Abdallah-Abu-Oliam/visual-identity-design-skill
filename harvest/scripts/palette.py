import itertools

def hx(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

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
    if k >= 1: return (0, 0, 0, 100)
    c = (1 - r - k) / (1 - k); m = (1 - g - k) / (1 - k); y = (1 - b - k) / (1 - k)
    return tuple(round(v * 100) for v in (c, m, y, k))

# Brettel-style simplified dichromacy simulation (LMS pipeline)
def simulate(h, kind):
    r, g, b = [lin(c) for c in hx(h)]
    L = 17.8824*r + 43.5161*g + 4.11935*b
    M = 3.45565*r + 27.1554*g + 3.86714*b
    S = 0.0299566*r + 0.184309*g + 1.46709*b
    if kind == 'protan':   L2, M2, S2 = 0.0*L + 2.02344*M - 2.52581*S, M, S
    elif kind == 'deutan': L2, M2, S2 = L, 0.494207*L + 0.0*M + 1.24827*S, S
    else:                  L2, M2, S2 = L, M, -0.395913*L + 0.801109*M + 0.0*S
    r2 = 0.0809444479*L2 - 0.130504409*M2 + 0.116721066*S2
    g2 = -0.0102485335*L2 + 0.0540193266*M2 - 0.113614708*S2
    b2 = -0.000365296938*L2 - 0.00412161469*M2 + 0.693511405*S2
    def out(c):
        c = max(0.0, min(1.0, c))
        c = 12.92*c if c <= 0.0031308 else 1.055*(c**(1/2.4)) - 0.055
        return int(round(max(0, min(1, c)) * 255))
    return '#%02X%02X%02X' % (out(r2), out(g2), out(b2))

P = {
    'Paper':     '#FBF5EC',
    'Sand':      '#EDDCC6',
    'Apricot':   '#E08A52',
    'Terracotta':'#A8462A',
    'Ink':       '#2A211C',
    'Sage':      '#79876C',
}

OCCUPIED = {
    'SDN amber':'#F5A800', 'Orano yellow':'#FFE600', 'EDF navy':'#001A70',
    'EDF blue':'#005BFF', 'UNICEF cyan':'#00AEEF', 'SFEN navy':'#004D91',
    'IfM indigo':'#342A7B', 'IfM magenta':'#E6007E',
}

print('=== SWATCHES ===')
for n, h in P.items():
    print(f'{n:11s} HEX {h}  RGB {hx(h)}  CMYK {cmyk(h)}')

print('\n=== CONTRAST (WCAG) ===')
pairs = [('Ink','Paper'),('Ink','Sand'),('Ink','Apricot'),('Terracotta','Paper'),
         ('Terracotta','Sand'),('Paper','Terracotta'),('Paper','Apricot'),
         ('Paper','Ink'),('Sage','Paper'),('Paper','Sage'),('Ink','Sage'),('Apricot','Ink')]
seen=set()
for a,b in pairs:
    k=tuple(sorted((a,b)))
    if k in seen: continue
    seen.add(k)
    r=ratio(P[a],P[b])
    body = 'AAA' if r>=7 else 'AA' if r>=4.5 else 'AA-large' if r>=3 else 'FAIL'
    print(f'{a:11s} on {b:11s} {r:5.2f}:1   {body}')

print('\n=== DISTANCE FROM OCCUPIED COLOURS (sRGB euclidean) ===')
def dist(a,b):
    return sum((x-y)**2 for x,y in zip(hx(a),hx(b)))**0.5
for n,h in OCCUPIED.items():
    best=min(P.items(), key=lambda kv: dist(kv[1],h))
    print(f'{n:14s} {h}  nearest ours: {best[0]:11s} {best[1]}  distance {dist(best[1],h):6.1f}')

print('\n=== COLOUR BLINDNESS ===')
for kind in ('protan','deutan','tritan'):
    print(f'-- {kind}')
    sim={n:simulate(h,kind) for n,h in P.items()}
    for n in P: print(f'   {n:11s} {P[n]} -> {sim[n]}')
    r=ratio(sim['Apricot'],sim['Paper'])
    r2=ratio(sim['Apricot'],sim['Sage'])
    print(f'   accent vs paper: {r:.2f}:1   accent vs sage: {r2:.2f}:1')
