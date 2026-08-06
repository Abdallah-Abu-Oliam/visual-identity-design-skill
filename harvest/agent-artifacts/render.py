import numpy as np
from PIL import Image, ImageDraw

def ellipse_points(cx, cy, rx, ry, rot_deg, n=400):
    rot = np.radians(rot_deg)
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = rx*np.cos(t)
    y = ry*np.sin(t)
    xr = x*np.cos(rot) - y*np.sin(rot)
    yr = x*np.sin(rot) + y*np.cos(rot)
    return [(float(cx+xr[i]), float(cy+yr[i])) for i in range(n)]

SS = 8  # supersample factor for clean downscale
size = 512*SS

img = Image.new("L", (size,size), 255)
draw = ImageDraw.Draw(img)

A = [(x*SS,y*SS) for x,y in ellipse_points(175,300,110,135,0)]
B = [(x*SS,y*SS) for x,y in ellipse_points(388,151,68,88,30)]

draw.polygon(A, fill=0)
draw.polygon(B, fill=0)

img_full = img.resize((512,512), Image.LANCZOS)
img_full.save("concept1_full.png")

img_16 = img.resize((16,16), Image.LANCZOS)
img_16.save("concept1_16.png")
# also a scaled-up view of the 16px version so it's actually visible when read
img_16_big = img_16.resize((256,256), Image.NEAREST)
img_16_big.save("concept1_16_big.png")

img_32 = img.resize((32,32), Image.LANCZOS)
img_32_big = img_32.resize((256,256), Image.NEAREST)
img_32_big.save("concept1_32_big.png")

print("done")
