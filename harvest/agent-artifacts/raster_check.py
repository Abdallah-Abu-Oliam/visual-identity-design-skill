import math

# Cubic bezier flatten
def cubic_points(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n+1):
        t = i/n
        mt = 1-t
        x = mt**3*p0[0] + 3*mt**2*t*p1[0] + 3*mt*t**2*p2[0] + t**3*p3[0]
        y = mt**3*p0[1] + 3*mt**2*t*p1[1] + 3*mt*t**2*p2[1] + t**3*p3[1]
        pts.append((x,y))
    return pts

# Outer blob path (from concept-3.svg), anchors + cubic controls
segs = [
    ((280,90),(340,90),(390,110),(400,150)),
    ((400,150),(415,190),(425,240),(420,280)),
    ((420,280),(415,330),(380,390),(330,420)),
    ((330,420),(280,445),(220,445),(170,430)),
    ((170,430),(110,410),(80,340),(90,270)),
    ((90,270),(95,210),(100,170),(120,150)),
    ((120,150),(150,115),(220,90),(280,90)),
]
blob_poly = []
for p0,p1,p2,p3 in segs:
    pts = cubic_points(p0,p1,p2,p3, 40)
    blob_poly.extend(pts[:-1])

# Halo circle (cutout), center 210,305 r=80
def circle_poly(cx,cy,r,n=80):
    return [(cx+r*math.cos(2*math.pi*i/n), cy+r*math.sin(2*math.pi*i/n)) for i in range(n)]

halo_poly = circle_poly(210,305,80)
core_center = (210,305)
core_r = 42

def point_in_poly(x,y,poly):
    n = len(poly)
    inside = False
    j = n-1
    for i in range(n):
        xi,yi = poly[i]
        xj,yj = poly[j]
        if ((yi>y) != (yj>y)) and (x < (xj-xi)*(y-yi)/(yj-yi+1e-12)+xi):
            inside = not inside
        j = i
    return inside

def in_core(x,y):
    dx = x-core_center[0]; dy = y-core_center[1]
    return dx*dx+dy*dy <= core_r*core_r

def filled(x,y):
    in_blob = point_in_poly(x,y,blob_poly)
    in_halo = point_in_poly(x,y,halo_poly)
    evenodd = in_blob != in_halo   # xor
    return evenodd or in_core(x,y)

def render(n):
    size = 512
    step = size/n
    rows = []
    for j in range(n):
        row = ""
        y = (j+0.5)*step
        for i in range(n):
            x = (i+0.5)*step
            row += "#" if filled(x,y) else "."
        rows.append(row)
    return "\n".join(rows)

print("=== 64x64 preview ===")
print(render(64))
print()
print("=== 16x16 preview (favicon scale) ===")
print(render(16))

# bounding box + margin checks
xs = [p[0] for p in blob_poly]; ys=[p[1] for p in blob_poly]
print()
print("blob bbox x:",min(xs),max(xs)," y:",min(ys),max(ys))

# min distance from halo boundary to blob boundary (sampled)
mind = 1e9
for hx,hy in halo_poly:
    # find nearest blob boundary point (brute force sample)
    for bx,by in blob_poly:
        d = math.hypot(hx-bx, hy-by)
        if d < mind:
            mind = d
print("min distance halo-boundary to blob-boundary (approx):", round(mind,1))
