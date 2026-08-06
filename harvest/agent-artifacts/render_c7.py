from PIL import Image, ImageDraw

SS = 4
CANVAS = 512 * SS

def cubic_flatten(p0, p1, p2, p3, n=60):
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

def sc(pts):
    return [(x*SS, y*SS) for x, y in pts]

vessel_start = (166, 448)
vessel_cubics = [
    ((150,462),(362,462),(346,448)),
    ((366,440),(384,418),(378,404)),
    ((372,366),(322,326),(298,288)),
    ((282,262),(350,220),(366,195)),
    ((372,172),(358,128),(352,110)),
    ((330,96),(280,150),(256,200)),
    ((232,150),(182,96),(160,110)),
    ((154,128),(140,172),(146,195)),
    ((162,220),(230,262),(214,288)),
    ((190,326),(140,366),(134,404)),
    ((128,418),(146,440),(166,448)),
]

seed_start = (256,118)
seed_cubics = [
    ((276,122),(284,140),(276,158)),
    ((270,172),(262,184),(256,192)),
    ((250,184),(242,172),(236,158)),
    ((228,140),(236,122),(256,118)),
]

rleaf_start = (256,118)
rleaf_cubics = [
    ((242,106),(229,82),(237,61)),
    ((248,73),(256,94),(256,118)),
]

lleaf_start = (256,118)
lleaf_cubics = [
    ((270,106),(283,82),(275,61)),
    ((264,73),(256,94),(256,118)),
]

def build_shapes():
    shapes = []
    shapes.append(path_from_cubics(vessel_start, vessel_cubics))
    shapes.append(path_from_cubics(seed_start, seed_cubics))
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
    render(r"C:\Users\momab\AppData\Local\Temp\claude\C--Users-momab-Desktop-visual-identity-design\6f06f9a2-844b-40fa-8c9b-3cc689570b86\scratchpad\concept7")
