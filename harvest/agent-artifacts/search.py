import math

def ellipse_points(cx, cy, rx, ry, rot_deg, n=720):
    rot = math.radians(rot_deg)
    pts = []
    for i in range(n):
        t = 2*math.pi*i/n
        x = rx*math.cos(t)
        y = ry*math.sin(t)
        xr = x*math.cos(rot) - y*math.sin(rot)
        yr = x*math.sin(rot) + y*math.cos(rot)
        pts.append((cx+xr, cy+yr))
    return pts

def min_dist(pts1, pts2):
    best = 1e18
    bp = None
    for p in pts1:
        for q in pts2:
            d = (p[0]-q[0])**2 + (p[1]-q[1])**2
            if d < best:
                best = d
                bp = (p,q)
    return math.sqrt(best), bp

def bbox(pts):
    xs = [p[0] for p in pts]; ys=[p[1] for p in pts]
    return min(xs), max(xs), min(ys), max(ys)

A = ellipse_points(195, 300, 125, 150, 0, 720)

candidates = [
    (355, 175, 78, 100, 50),
    (360, 165, 78, 100, 50),
    (365, 155, 75, 95, 48),
    (370, 150, 75, 95, 45),
    (350, 160, 75, 95, 50),
    (345, 150, 72, 92, 48),
    (355, 145, 72, 92, 45),
]

for c in candidates:
    cx,cy,rx,ry,rot = c
    B = ellipse_points(cx,cy,rx,ry,rot,720)
    d, bp = min_dist(A,B)
    bx = bbox(B)
    print(c, "gap=%.1f" % d, "nearpts=", tuple(round(v,1) for v in bp[0]), tuple(round(v,1) for v in bp[1]), "Bbbox=", tuple(round(v,1) for v in bx))
