import math
from PIL import Image, ImageDraw

SS = 4  # supersample factor
CANVAS = 512 * SS

def ellipse_poly(cx, cy, rx, ry, rot_deg, n=120):
    rot = math.radians(rot_deg)
    pts = []
    for i in range(n):
        t = 2 * math.pi * i / n
        x = rx * math.cos(t)
        y = ry * math.sin(t)
        xr = x * math.cos(rot) - y * math.sin(rot)
        yr = x * math.sin(rot) + y * math.cos(rot)
        pts.append((cx + xr, cy + yr))
    return pts

def cubic_flatten(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3*p0[0] + 3*mt**2*t*p1[0] + 3*mt*t**2*p2[0] + t**3*p3[0]
        y = mt**3*p0[1] + 3*mt**2*t*p1[1] + 3*mt*t**2*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

def path_from_cubics(start, cubics):
    # cubics: list of (c1, c2, end)
    pts = [start]
    cur = start
    for c1, c2, end in cubics:
        seg = cubic_flatten(cur, c1, c2, end)
        pts.extend(seg[1:])
        cur = end
    return pts

def mirror_x(pts, axis=256):
    return [(2*axis - x, y) for x, y in pts]

def sc(pts):
    return [(x*SS, y*SS) for x, y in pts]

# ---------- right hand ellipses ----------
right_hand_ellipses = [
    (350, 375, 95, 75, -8),
    (405, 305, 26, 58, 18),
    (362, 283, 28, 64, 2),
    (322, 293, 26, 58, -18),
    (278, 328, 30, 52, -42),
]

# ---------- stone ----------
stone_start = (256, 238)
stone_cubics = [
    ((288, 244), (316, 266), (314, 296)),
    ((312, 326), (300, 350), (283, 372)),
    ((272, 388), (262, 400), (257, 408)),
    ((252, 400), (240, 386), (228, 368)),
    ((210, 344), (198, 320), (198, 292)),
    ((198, 262), (224, 242), (256, 238)),
]

# ---------- stem ----------
stem_start = (246, 240)
stem_cubics = [
    ((242, 205), (246, 165), (250, 128)),
    ((251, 112), (254, 98), (256, 88)),
    ((258, 98), (261, 112), (262, 128)),
    ((266, 165), (270, 205), (266, 240)),
]

# ---------- right leaf ----------
rleaf_start = (264, 186)
rleaf_cubics = [
    ((284, 172), (308, 162), (332, 150)),
    ((316, 168), (296, 184), (274, 202)),
    ((270, 197), (267, 191), (264, 186)),
]

# ---------- left leaf ----------
lleaf_start = (248, 214)
lleaf_cubics = [
    ((226, 202), (202, 194), (180, 186)),
    ((200, 200), (222, 214), (244, 230)),
    ((246, 225), (247, 219), (248, 214)),
]

def build_shapes():
    shapes = []
    for cx, cy, rx, ry, rot in right_hand_ellipses:
        shapes.append(ellipse_poly(cx, cy, rx, ry, rot))
    # mirrored left hand
    for cx, cy, rx, ry, rot in right_hand_ellipses:
        pts = ellipse_poly(cx, cy, rx, ry, rot)
        shapes.append(mirror_x(pts))
    shapes.append(path_from_cubics(stone_start, stone_cubics))
    shapes.append(path_from_cubics(stem_start, stem_cubics))
    shapes.append(path_from_cubics(rleaf_start, rleaf_cubics))
    shapes.append(path_from_cubics(lleaf_start, lleaf_cubics))
    return shapes

def render(out_prefix):
    shapes = build_shapes()
    img = Image.new("L", (CANVAS, CANVAS), 255)
    draw = ImageDraw.Draw(img)
    for s in shapes:
        draw.polygon(sc(s), fill=0)
    for size in [512, 128, 64, 32, 16]:
        resized = img.resize((size, size), Image.LANCZOS)
        resized.save(f"{out_prefix}_{size}.png")
        print(f"wrote {out_prefix}_{size}.png")

if __name__ == "__main__":
    render(r"C:\Users\momab\AppData\Local\Temp\claude\C--Users-momab-Desktop-visual-identity-design\6f06f9a2-844b-40fa-8c9b-3cc689570b86\scratchpad\concept9")
