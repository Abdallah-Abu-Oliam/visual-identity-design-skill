import math, random, sys

W = H = 400.0

def build(seed=7, n=150, out="grain.svg", ink="#2A211C"):
    rnd = random.Random(seed)
    marks = []

    # Poisson-ish sampling so marks never collide but stay dense
    pts = []
    tries = 0
    while len(pts) < n and tries < n * 400:
        tries += 1
        x, y = rnd.uniform(0, W), rnd.uniform(0, H)
        ok = True
        for px, py in pts:
            dx = abs(px - x); dy = abs(py - y)
            dx = min(dx, W - dx); dy = min(dy, H - dy)   # toroidal distance
            if dx * dx + dy * dy < 22 * 22:
                ok = False; break
        if ok:
            pts.append((x, y))

    for (x, y) in pts:
        # flow field — grain runs in slow curves rather than scattering
        a = (math.sin(x / 118.0) * 0.9 + math.cos(y / 96.0) * 0.7) * 34 - 24
        a += rnd.uniform(-11, 11)
        L = rnd.uniform(9, 30)              # half-length
        t = rnd.uniform(2.6, 4.4)           # half-width
        if rnd.random() < 0.16:             # occasional pit
            L = t = rnd.uniform(2.8, 4.6)
        marks.append((x, y, L, t, a))

    def emit(x, y, L, t, a):
        return (f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{L:.1f}" ry="{t:.1f}" '
                f'transform="rotate({a:.1f} {x:.1f} {y:.1f})"/>')

    body = []
    for (x, y, L, t, a) in marks:
        for ox in (-W, 0, W):
            for oy in (-H, 0, H):
                nx, ny = x + ox, y + oy
                if -L - 6 < nx < W + L + 6 and -L - 6 < ny < H + L + 6:
                    body.append(emit(nx, ny, L, t, a))

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" height="{H:.0f}" color="{ink}">
  <title>Le Grain — Noyau surface pattern. Seamless {W:.0f}x{H:.0f} tile.</title>
  <g id="grain" fill="currentColor">
    {chr(10) + "    ".join(body)}
  </g>
</svg>
'''
    open(out, "w", encoding="utf-8").write(svg)
    return len(marks), len(body)

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 150
    out = sys.argv[3] if len(sys.argv) > 3 else "grain.svg"
    m, b = build(seed, n, out)
    print(f"{out}: {m} marks, {b} drawn (with wrap copies)")
