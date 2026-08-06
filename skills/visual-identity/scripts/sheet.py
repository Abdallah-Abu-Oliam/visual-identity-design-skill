import sys, os, glob
from PIL import Image, ImageDraw

BASE = r"C:\Users\momab\Desktop\nuclear-nonprofit-brand\brand\research\audience"
OUT  = r"C:\Users\momab\AppData\Local\Temp\claude\C--Users-momab-Desktop-visual-identity-design\6f06f9a2-844b-40fa-8c9b-3cc689570b86\scratchpad"

TW, TH, COLS, PAD = 150, 108, 7, 3

def sheet(folder):
    files = []
    for ext in ("jpg", "jpeg", "png", "webp"):
        files += glob.glob(os.path.join(BASE, folder, "*." + ext))
    files.sort()
    if not files:
        print(folder, "EMPTY"); return
    rows = (len(files) + COLS - 1) // COLS
    W = COLS * (TW + PAD) + PAD
    H = rows * (TH + PAD) + PAD
    canvas = Image.new("RGB", (W, H), (24, 24, 24))
    d = ImageDraw.Draw(canvas)
    manifest = []
    for i, f in enumerate(files):
        try:
            im = Image.open(f).convert("RGB")
        except Exception as e:
            print("  skip", os.path.basename(f), e); continue
        # cover-crop to thumb aspect
        sr, tr = im.width / im.height, TW / TH
        if sr > tr:
            nw = int(im.height * tr)
            im = im.crop(((im.width - nw) // 2, 0, (im.width + nw) // 2, im.height))
        else:
            nh = int(im.width / tr)
            im = im.crop((0, (im.height - nh) // 2, im.width, (im.height + nh) // 2))
        im = im.resize((TW, TH), Image.LANCZOS)
        x = PAD + (i % COLS) * (TW + PAD)
        y = PAD + (i // COLS) * (TH + PAD)
        canvas.paste(im, (x, y))
        lbl = str(i + 1)
        d.rectangle([x, y, x + 8 + 7 * len(lbl), y + 13], fill=(0, 0, 0))
        d.text((x + 4, y + 3), lbl, fill=(255, 255, 255))
        manifest.append(f"{i+1}\t{os.path.basename(f)}")
    p = os.path.join(OUT, "sheet-" + folder + ".png")
    canvas.save(p, quality=88)
    with open(os.path.join(OUT, "sheet-" + folder + ".txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(manifest))
    print(folder, len(files), "imgs ->", p, canvas.size)

for f in sys.argv[1:]:
    sheet(f)
