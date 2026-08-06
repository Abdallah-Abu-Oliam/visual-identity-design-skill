import re, math
from PIL import Image, ImageDraw

SS = 4
CANVAS = 512 * SS
svg_path = r"C:\Users\momab\Desktop\nuclear-nonprofit-brand\brand\logos\concepts\concept-9.svg"
text = open(svg_path, encoding="utf-8").read()

def cubic_flatten(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        mt = 1 - t
        x = mt**3*p0[0] + 3*mt**2*t*p1[0] + 3*mt*t**2*p2[0] + t**3*p3[0]
        y = mt**3*p0[1] + 3*mt**2*t*p1[1] + 3*mt*t**2*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

def parse_path_d(d):
    # tokens: M x y  C x1 y1 x2 y2 x y  ... Z
    nums = re.findall(r'-?\d+(?:\.\d+)?', d)
    nums = list(map(float, nums))
    # first two are M
    pts = [(nums[0], nums[1])]
    idx = 2
    cur = pts[0]
    while idx + 5 < len(nums) + 1 and idx < len(nums):
        c1 = (nums[idx], nums[idx+1])
        c2 = (nums[idx+2], nums[idx+3])
        end = (nums[idx+4], nums[idx+5])
        seg = cubic_flatten(cur, c1, c2, end, 30)
        pts.extend(seg[1:])
        cur = end
        idx += 6
    return pts

def ellipse_poly(cx, cy, rx, ry, rot_deg, n=100):
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

def sc(pts):
    return [(x*SS, y*SS) for x, y in pts]

img = Image.new("L", (CANVAS, CANVAS), 255)
draw = ImageDraw.Draw(img)

# find top-level (right hand, stone, stem, leaves) paths -- those NOT inside the mirrored <g>
mirror_g_match = re.search(r'<g transform="translate\(512,0\) scale\(-1,1\)">(.*?)</g>', text, re.S)
mirror_block = mirror_g_match.group(1)
main_text = text.replace(mirror_block, '')  # crude removal for path scanning of the rest

def draw_block(block, mirror=False):
    for m in re.finditer(r'<path d="([^"]+)"', block, re.S):
        pts = parse_path_d(m.group(1))
        if mirror:
            pts = [(2*256 - x, y) for x, y in pts]
        draw.polygon(sc(pts), fill=0)
    for m in re.finditer(r'<ellipse cx="([\d.]+)" cy="([\d.]+)" rx="([\d.]+)" ry="([\d.]+)" transform="rotate\((-?[\d.]+) [\d.]+ [\d.]+\)"', block):
        cx, cy, rx, ry, rot = map(float, m.groups())
        pts = ellipse_poly(cx, cy, rx, ry, rot)
        if mirror:
            pts = [(2*256 - x, y) for x, y in pts]
        draw.polygon(sc(pts), fill=0)

draw_block(main_text, mirror=False)
draw_block(mirror_block, mirror=True)

for size in [512, 128, 64, 32, 16]:
    out = img.resize((size, size), Image.LANCZOS)
    out.save(rf"C:\Users\momab\AppData\Local\Temp\claude\C--Users-momab-Desktop-visual-identity-design\6f06f9a2-844b-40fa-8c9b-3cc689570b86\scratchpad\svgcheck9_{size}.png")
    print("wrote", size)
