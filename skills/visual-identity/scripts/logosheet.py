import os, sys
from PIL import Image, ImageDraw

EXP = r"C:\Users\momab\Desktop\nuclear-nonprofit-brand\brand\logos\export"
OUT = r"C:\Users\momab\AppData\Local\Temp\claude\C--Users-momab-Desktop-visual-identity-design\6f06f9a2-844b-40fa-8c9b-3cc689570b86\scratchpad\logo-compare.png"

names = sys.argv[1:]
BIG, MID, ZOOM = 300, 96, 8          # ZOOM: 16px * 8 = 128
ROW_H = BIG + 46
W = 40 + BIG + 30 + MID + 20 + (16 * ZOOM) + 40
H = 30 + ROW_H * len(names)

canvas = Image.new("RGB", (W, H), (255, 255, 255))
d = ImageDraw.Draw(canvas)

def load(folder, size):
    p = os.path.join(EXP, folder, f"logo-{size}.png")
    im = Image.open(p)
    if im.mode in ("RGBA", "LA"):
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    return im.convert("RGB")

for i, n in enumerate(names):
    y = 30 + i * ROW_H
    folder = "concept-" + n
    try:
        big = load(folder, 512).resize((BIG, BIG), Image.LANCZOS)
        mid = load(folder, 48).resize((MID, MID), Image.NEAREST)
        tiny = load(folder, 16)
        zoom = tiny.resize((16 * ZOOM, 16 * ZOOM), Image.NEAREST)
    except Exception as e:
        d.text((40, y + 20), f"concept {n}: {e}", fill=(200, 0, 0)); continue

    d.text((40, y - 16), f"CONCEPT {n}", fill=(0, 0, 0))
    canvas.paste(big, (40, y))
    x2 = 40 + BIG + 30
    canvas.paste(mid, (x2, y + (BIG - MID) // 2))
    d.text((x2, y + (BIG - MID) // 2 + MID + 6), "48px actual", fill=(90, 90, 90))
    x3 = x2 + MID + 20
    zy = y + (BIG - 16 * ZOOM) // 2
    canvas.paste(zoom, (x3, zy))
    d.rectangle([x3 - 1, zy - 1, x3 + 16 * ZOOM, zy + 16 * ZOOM], outline=(200, 200, 200))
    d.text((x3, zy + 16 * ZOOM + 6), "REAL 16px, magnified 8x", fill=(90, 90, 90))
    d.line([(30, y + ROW_H - 22), (W - 30, y + ROW_H - 22)], fill=(225, 225, 225))

canvas.save(OUT)
print("wrote", OUT, canvas.size)
