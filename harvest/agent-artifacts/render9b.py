import math
from PIL import Image, ImageDraw

SS = 4
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

# ---------- RIGHT PALM (wedge, heel touches center at bottom) ----------
palm_start = (256, 434)
palm_cubics = [
    ((270, 400), (280, 370), (300, 347)),   # up inner edge to thumb-base junction
    ((330, 333), (368, 328), (398, 336)),   # across top edge (finger attachment zone)
    ((418, 344), (430, 368), (428, 396)),   # outer side down
    ((426, 415), (412, 430), (388, 436)),   # outer-bottom heel
    ((350, 444), (296, 444), (256, 434)),   # bottom edge back to center point
]

# ---------- RIGHT THUMB ----------
thumb_cx, thumb_cy, thumb_rx, thumb_ry, thumb_rot = 296, 338, 25, 44, -34

# ---------- RIGHT FINGERS ----------
fingers = [
    (412, 302, 23, 50, 24),   # pinky
    (372, 274, 25, 56, 6),    # middle
    (332, 284, 23, 50, -12),  # index
]

# ---------- STONE ----------
stone_start = (256, 250)
stone_cubics = [
    ((284, 255), (306, 274), (304, 298)),
    ((302, 320), (292, 340), (278, 358)),
    ((269, 370), (261, 380), (257, 388)),
    ((253, 380), (245, 370), (236, 358)),
    ((222, 340), (212, 320), (210, 298)),
    ((208, 274), (230, 255), (256, 250)),
]

# ---------- STEM ----------
stem_start = (249, 252)
stem_cubics = [
    ((245, 218), (248, 180), (252, 145)),
    ((253, 130), (255, 116), (256, 106)),
    ((258, 116), (260, 130), (261, 145)),
    ((264, 180), (267, 218), (263, 252)),
]

# ---------- LEAVES ----------
rleaf_start = (261, 200)
rleaf_cubics = [
    ((280, 187), (302, 178), (324, 167)),
    ((309, 184), (290, 199), (270, 216)),
    ((266, 211), (263, 205), (261, 200)),
]

lleaf_start = (247, 226)
lleaf_cubics = [
    ((226, 216), (204, 209), (183, 202)),
    ((202, 215), (223, 228), (244, 242)),
    ((246, 237), (247, 231), (247, 226)),
]

def build_shapes():
    shapes = []
    shapes.append(("palm_r", path_from_cubics(palm_start, palm_cubics)))
    shapes.append(("thumb_r", ellipse_poly(thumb_cx, thumb_cy, thumb_rx, thumb_ry, thumb_rot)))
    for i, (cx, cy, rx, ry, rot) in enumerate(fingers):
        shapes.append((f"finger_r{i}", ellipse_poly(cx, cy, rx, ry, rot)))

    mirrored = []
    for name, pts in shapes:
        mirrored.append((name.replace("_r", "_l"), mirror_x(pts)))
    shapes.extend(mirrored)

    shapes.append(("stone", path_from_cubics(stone_start, stone_cubics)))
    shapes.append(("stem", path_from_cubics(stem_start, stem_cubics)))
    shapes.append(("rleaf", path_from_cubics(rleaf_start, rleaf_cubics)))
    shapes.append(("lleaf", path_from_cubics(lleaf_start, lleaf_cubics)))
    return shapes

def render(out_prefix):
    shapes = build_shapes()
    img = Image.new("L", (CANVAS, CANVAS), 255)
    draw = ImageDraw.Draw(img)
    for name, s in shapes:
        draw.polygon(sc(s), fill=0)
    for size in [512, 128, 64, 32, 16]:
        resized = img.resize((size, size), Image.LANCZOS)
        resized.save(f"{out_prefix}_{size}.png")
        print(f"wrote {out_prefix}_{size}.png")

if __name__ == "__main__":
    render(r"C:\Users\momab\AppData\Local\Temp\claude\C--Users-momab-Desktop-visual-identity-design\6f06f9a2-844b-40fa-8c9b-3cc689570b86\scratchpad\concept9b")
