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

Acx,Acy,Arx,Ary = 175, 300, 110, 135
A = ellipse_points(Acx,Acy,Arx,Ary, 0, 720)

Brx,Bry = 68, 88
best_results=[]
for rot in range(30,71,5):
    for angdeg in range(-75,-14,5):
        ang = math.radians(angdeg)
        for dist in range(190,331,5):
            cx = Acx + dist*math.cos(ang)
            cy = Acy + dist*math.sin(ang)
            B = ellipse_points(cx,cy,Brx,Bry,rot,300)
            d,bp = min_dist(A,B)
            if 55 <= d <= 68:
                bx = bbox(B)
                allpts = A+B
                cb = bbox(allpts)
                if bx[0]>=20 and bx[1]<=492 and bx[2]>=20 and bx[3]<=492:
                    ccx = (cb[0]+cb[1])/2
                    ccy = (cb[2]+cb[3])/2
                    balance = math.hypot(ccx-256, ccy-256)
                    best_results.append((round(balance,1), rot, angdeg, dist, round(cx,1), round(cy,1), round(d,1), tuple(round(v,1) for v in cb)))

best_results.sort()
for r in best_results[:20]:
    print(r)
