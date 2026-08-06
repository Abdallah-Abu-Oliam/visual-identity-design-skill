import math

def ellipse_points(cx, cy, rx, ry, rot_deg, n=2000):
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

A = ellipse_points(195, 300, 125, 150, 0, 1000)
B = ellipse_points(340, 195, 78, 100, 55, 1000)

d, bp = min_dist(A, B)
print("min gap:", d, "at", bp)
print("A bbox:", bbox(A))
print("B bbox:", bbox(B))
allpts = A+B
print("combined bbox:", bbox(allpts))
