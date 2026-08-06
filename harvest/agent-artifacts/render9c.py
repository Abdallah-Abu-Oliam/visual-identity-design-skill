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

# ---------- RIGHT PALM: wide, low, sloping DOWN toward center (valley) ----------
palm_start = (256, 448)
palm_cubics = [
    ((300, 452), (360, 452), (405, 438)),   # bottom edge out to outer heel
    ((424, 430), (436, 412), (440, 388)),   # outer side rising, smooth (no spike)
    ((443, 362), (440, 340), (428, 322)),   # upper outer (finger attach zone, base)
    ((402, 332), (348, 356), (300, 392)),   # top edge sloping DOWN toward center (the valley)
    ((280, 408), (266, 428), (256, 448)),   # inner edge back down to center touch point
]

# ---------- RIGHT THUMB: bigger, clearly curling toward the stone ----------
thumb_cx, thumb_cy, thumb_rx, thumb_ry, thumb_rot = 300, 380, 17, 36, -24

# ---------- RIGHT FINGERS: even width, gentle consistent fan, real gaps ----------
fingers = [
    (372, 270, 15, 48, -14),  # index (innermost)
    (412, 256, 15, 54, 2),    # middle (tallest)
    (450, 268, 15, 46, 18),   # pinky (outermost)
]

# ---------- STONE: elongated pit, narrow point at bottom, higher up, irregular ----------
stone_start = (256, 196)
stone_cubics = [
    ((286, 198), (304, 222), (299, 252)),
    ((296, 280), (284, 312), (269, 342)),
    ((261, 360), (258, 380), (256, 398)),
    ((254, 380), (249, 360), (240, 342)),
    ((223, 310), (213, 280), (214, 252)),
    ((215, 224), (230, 198), (256, 196)),
]

# ---------- STEM: thicker, rounded blunt top (no sharp spike) ----------
stem_start = (247, 205)
stem_cubics = [
    ((244, 175), (246, 148), (250, 128)),
    ((251, 120), (253, 114), (256, 110)),
    ((259, 114), (261, 120), (262, 128)),
    ((266, 148), (268, 175), (265, 205)),
]

# ---------- LEAVES: fuller, rounder petal shapes with blunt tips ----------
rleaf_start = (262, 165)
rleaf_cubics = [
    ((282, 150), (300, 142), (314, 140)),
    ((322, 142), (328, 148), (324, 156)),
    ((308, 172), (286, 182), (262, 165)),
]

lleaf_start = (250, 190)
lleaf_cubics = [
    ((230, 176), (212, 168), (198, 166)),
    ((190, 168), (184, 174), (188, 182)),
    ((204, 198), (226, 208), (250, 190)),
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
    render(r"C:\Users\momab\AppData\Local\Temp\claude\C--Users-momab-Desktop-visual-identity-design\6f06f9a2-844b-40fa-8c9b-3cc689570b86\scratchpad\concept9c")
