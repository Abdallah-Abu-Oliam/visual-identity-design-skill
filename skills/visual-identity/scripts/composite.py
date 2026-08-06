"""Composite Noyau artwork onto blank-surface photographs.

Perspective-warps real vector artwork onto a photo, then blends with MULTIPLY so the
surface's own folds, shadows and texture show through the ink. The logo is never
redrawn — the actual exported artwork is placed, so the mark stays exact.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont

PAPER=(251,245,236); SAND=(237,220,198); INK=(42,33,28)
APRICOT=(222,133,96); TERRA=(156,63,38); OLIVE=(79,92,70)

def fr(size, wght=600, opsz=None, soft=45, wonk=1):
    f=ImageFont.truetype('fonts/fraunces-var.ttf', size)
    f.set_variation_by_axes([opsz if opsz else min(144,max(9,size)), wght, soft, wonk])
    return f

def at(size, wght=400):
    f=ImageFont.truetype('fonts/atkinson-var.ttf', size)
    f.set_variation_by_axes([wght]); return f

def tile(img, path, scale):
    t=Image.open(path).convert('RGBA')
    t=t.resize((scale,scale), Image.LANCZOS)
    for y in range(0,img.height,scale):
        for x in range(0,img.width,scale):
            img.alpha_composite(t,(x,y))
    return img

def logo(path, h, ):
    l=Image.open(path).convert('RGBA')
    return l.resize((h,h), Image.LANCZOS)

def wrap(d, text, font, maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t, font=font) <= maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

def draw_lines(d, xy, lines, font, fill, lh):
    x,y=xy
    for ln in lines:
        d.text((x,y), ln, font=font, fill=fill); y+=lh
    return y

# ---------- artworks ----------
def art_card(W=1600,H=1000):
    im=Image.new('RGBA',(W,H),PAPER+(255,))
    tile(im,'art/tile-sand.png',int(W*0.30))
    d=ImageDraw.Draw(im)
    d.rectangle([90,H-330,1080,H-90], fill=PAPER+(255,))
    lg=logo('art/logo-ink.png',210); im.alpha_composite(lg,(90,110))
    d.text((130,H-310), 'Noyau', font=fr(120,600,96,45,0), fill=INK)
    d.text((134,H-165), "On reste auprès d'eux.", font=at(48,400), fill=INK)
    d.text((134,H-108), 'noyau.eu  ·  Association loi 1901', font=at(38,400), fill=(110,100,92))
    return im

def art_poster(W=1400,H=2000):
    im=Image.new('RGBA',(W,H),PAPER+(255,))
    tile(im,'art/tile-apricot.png',int(W*0.42))
    d=ImageDraw.Draw(im)
    f=fr(150,600,144,45,1)
    lines=wrap(d,"Ce qu'on craint est ce qui soigne.",f,W-260)
    box_h=len(lines)*168+90
    d.rectangle([90,150,W-90,150+box_h], fill=PAPER+(255,))
    draw_lines(d,(130,196),lines,f,INK,168)
    lg=logo('art/logo-ink.png',300); im.alpha_composite(lg,(W//2-150,H-560))
    d.rectangle([180,H-230,W-180,H-100], fill=PAPER+(255,))
    b=at(60,400)
    t="La même science, tous les jours, dans les hôpitaux français."
    ls=wrap(d,t,b,W-460)
    draw_lines(d,(210,H-210),ls,b,INK,72)
    return im

def art_print(W=1200,H=1200,col='ink'):
    im=Image.new('RGBA',(W,H),(0,0,0,0))
    d=ImageDraw.Draw(im)
    fill=INK if col=='ink' else PAPER
    lg=logo('art/logo-%s.png'%col,760); im.alpha_composite(lg,(W//2-380,40))
    f=fr(190,600,96,45,0)
    w=d.textlength('Noyau',font=f); d.text(((W-w)/2,H-330),'Noyau',font=f,fill=fill)
    b=at(58,400); t='on reste auprès d\'eux'
    w2=d.textlength(t,font=b); d.text(((W-w2)/2,H-140),t,font=b,fill=fill)
    return im

# ---------- perspective ----------
def coeffs(dst, src):
    """dst/src: 4 (x,y) pairs TL,TR,BR,BL. Returns PIL PERSPECTIVE coeffs (dst->src)."""
    M=[]
    for (dx,dy),(sx,sy) in zip(dst,src):
        M.append([dx,dy,1,0,0,0,-sx*dx,-sx*dy])
        M.append([0,0,0,dx,dy,1,-sy*dx,-sy*dy])
    A=np.array(M,dtype=float)
    B=np.array([c for p in src for c in p],dtype=float)
    return np.linalg.solve(A,B)

def place(photo_path, art, quad_pct, out, mode='multiply', strength=1.0):
    ph=Image.open(photo_path).convert('RGB')
    W,H=ph.size
    dst=[(x/100*W, y/100*H) for x,y in quad_pct]
    src=[(0,0),(art.width,0),(art.width,art.height),(0,art.height)]
    c=coeffs(dst,src)
    warped=art.transform((W,H), Image.PERSPECTIVE, c, Image.BICUBIC)
    a=np.asarray(warped.split()[-1],dtype=float)/255.0*strength
    base=np.asarray(ph,dtype=float)
    top=np.asarray(warped.convert('RGB'),dtype=float)
    if mode=='multiply':
        blended=base*top/255.0
    else:
        blended=255.0-(255.0-base)*(255.0-top)/255.0
    outarr=base*(1-a[...,None])+blended*a[...,None]
    Image.fromarray(np.clip(outarr,0,255).astype('uint8')).save(out, quality=92)
    return out
