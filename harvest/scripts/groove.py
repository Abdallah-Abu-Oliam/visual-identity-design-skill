import math, random, sys
W=H=400.0
def build(seed=5,n=54,out="groove.svg",ink="#2A211C"):
    rnd=random.Random(seed); pts=[]; tries=0
    while len(pts)<n and tries<n*500:
        tries+=1
        x,y=rnd.uniform(0,W),rnd.uniform(0,H); ok=True
        for px,py in pts:
            dx=abs(px-x);dy=abs(py-y);dx=min(dx,W-dx);dy=min(dy,H-dy)
            if dx*dx+dy*dy<44*44: ok=False;break
        if ok: pts.append((x,y))
    els=[]
    for (x,y) in pts:
        a=(math.sin(x/150.0)*0.9+math.cos(y/130.0)*0.8)*40-20+rnd.uniform(-16,16)
        L=rnd.uniform(26,62); w=rnd.uniform(5.5,10.5); bow=rnd.uniform(-18,18)
        ra=math.radians(a); dx,dy=math.cos(ra),math.sin(ra); nx,ny=-dy,dx
        x0,y0=x-dx*L,y-dy*L; x1,y1=x+dx*L,y+dy*L
        cx,cy=x+nx*bow,y+ny*bow
        els.append(('g',x0,y0,cx,cy,x1,y1,w,min(x0,x1)-L,max(x0,x1)+L,min(y0,y1)-L,max(y0,y1)+L))
        if rnd.random()<0.5:
            r=rnd.uniform(3.0,5.5); ox,oy=x+nx*rnd.uniform(-26,26)+dx*rnd.uniform(-20,20),y+ny*rnd.uniform(-26,26)+dy*rnd.uniform(-20,20)
            els.append(('p',ox,oy,r))
    body=[]
    for ox in (-W,0,W):
        for oy in (-H,0,H):
            for e in els:
                if e[0]=='g':
                    _,x0,y0,cx,cy,x1,y1,w,ax,bx,ay,by=e
                    if bx+ox<-70 or ax+ox>W+70 or by+oy<-70 or ay+oy>H+70: continue
                    body.append(f'<path d="M{x0+ox:.1f} {y0+oy:.1f} Q{cx+ox:.1f} {cy+oy:.1f} {x1+ox:.1f} {y1+oy:.1f}" fill="none" stroke="currentColor" stroke-width="{w:.1f}" stroke-linecap="round"/>')
                else:
                    _,px,py,r=e
                    if px+ox<-20 or px+ox>W+20 or py+oy<-20 or py+oy>H+20: continue
                    body.append(f'<circle cx="{px+ox:.1f}" cy="{py+oy:.1f}" r="{r:.1f}"/>')
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400" color="{ink}">
  <title>Le Grain — groove variant. Seamless 400x400 tile.</title>
  <g id="grain" fill="currentColor">
    {chr(10)+"    ".join(body)}
  </g>
</svg>
'''
    open(out,"w",encoding="utf-8").write(svg); return len(els),len(body)
if __name__=="__main__":
    print(build(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]))
