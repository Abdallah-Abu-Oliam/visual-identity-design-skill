"""Rebuild the Noyau wheat wreath with REAL gaps instead of painted white strokes.

The white strokes in the original are separations that only need to exist where a grain
overlaps something drawn behind it. So, in draw order:

    result = result.difference(shape.buffer(GAP))   # punch a gap out of what's behind
    result = result.union(shape)                    # then add the shape

That reproduces the painted separations exactly, but as true negative space — so the mark
works on colour, on photographs, and in one-colour print, foil, engraving and embroidery.
"""
import math
from shapely.geometry import Point, LineString, Polygon
from shapely.ops import unary_union
from shapely.affinity import rotate, translate, scale as ashapely

GAP = 2.5          # half the original stroke-width 5
RES = 64           # circle segments

# ---- source geometry, lifted verbatim from the owner's SVG ----
STEM = "M0 0C50-12 96-40 130-92"
GRAINS = [  # cx, cy, rx, ry, rot
    (31, -27, 16, 9, -35), (42, 3, 16, 9, -5), (63, -45, 16, 9, -46),
    (79, -17, 16, 9, -16), (91, -69, 16, 9, -60), (114, -46, 16, 9, -30),
    (130, -92, 18, 10, -57), (141, -109, 18, 10, -57), (152, -126, 18, 10, -57),
]
ARMS = [(296, 400, -30), (296, 420, -12), (296, 440, 6)]

def bezier(p0, p1, p2, p3, n=60):
    out = []
    for i in range(n + 1):
        t = i / n; u = 1 - t
        x = u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        out.append((x, y))
    return out

def stem_shape():
    pts = bezier((0, 0), (50, -12), (96, -40), (130, -92))
    return LineString(pts).buffer(13/2, resolution=RES, cap_style=1)

def grain_shape(cx, cy, rx, ry, rot):
    e = ashapely(Point(cx, cy).buffer(1, resolution=RES), xfact=rx, yfact=ry, origin=(cx, cy))
    return rotate(e, rot, origin=(cx, cy))

def arm_shapes():
    """Return the arm's shapes in draw order: stem first, then grains."""
    return [stem_shape()] + [grain_shape(*g) for g in GRAINS]

def place(shape, tx, ty, rot, mirror=False):
    s = rotate(shape, rot, origin=(0, 0))
    s = translate(s, tx, ty)
    if mirror:
        s = ashapely(s, xfact=-1, yfact=1, origin=(256, 0))
    return s

def build_wreath():
    ordered = []
    for mirror in (False, True):
        for (tx, ty, rot) in ARMS:
            for sh in arm_shapes():
                ordered.append(place(sh, tx, ty, rot, mirror))
    result = None
    for sh in ordered:
        if result is None:
            result = sh
        else:
            result = result.difference(sh.buffer(GAP, resolution=RES))
            result = result.union(sh)
    return result

def to_path(geom, prec=1):
    polys = [geom] if geom.geom_type == "Polygon" else list(geom.geoms)
    d = []
    for p in polys:
        for ring in [p.exterior] + list(p.interiors):
            cs = list(ring.coords)
            d.append("M" + " ".join(f"{x:.{prec}f} {y:.{prec}f}" for x, y in cs[:-1]) + "Z")
    return "".join(d)

if __name__ == "__main__":
    w = build_wreath()
    print("wreath parts:", 1 if w.geom_type == "Polygon" else len(w.geoms),
          "| area:", round(w.area))
    open("wreath-path.txt", "w").write(to_path(w))
    print("path chars:", len(to_path(w)))
