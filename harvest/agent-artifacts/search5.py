import numpy as np

def ellipse_points(cx, cy, rx, ry, rot_deg, n=180):
    rot = np.radians(rot_deg)
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = rx*np.cos(t)
    y = ry*np.sin(t)
    xr = x*np.cos(rot) - y*np.sin(rot)
    yr = x*np.sin(rot) + y*np.cos(rot)
    return np.stack([cx+xr, cy+yr], axis=1)

def min_dist(P, Q):
    d = np.sqrt(((P[:,None,:]-Q[None,:,:])**2).sum(-1))
    return d.min()

def bbox(P):
    return P[:,0].min(), P[:,0].max(), P[:,1].min(), P[:,1].max()

Acx,Acy,Arx,Ary = 175, 300, 110, 135
A = ellipse_points(Acx,Acy,Arx,Ary, 0, 240)

Brx,Bry = 68, 88
best_results=[]
for rot in range(30,71,5):
    for angdeg in range(-75,-14,5):
        ang = np.radians(angdeg)
        for dist in range(190,331,5):
            cx = Acx + dist*np.cos(ang)
            cy = Acy + dist*np.sin(ang)
            B = ellipse_points(cx,cy,Brx,Bry,rot,150)
            d = min_dist(A,B)
            if 55 <= d <= 68:
                bx = bbox(B)
                allpts = np.vstack([A,B])
                cb = bbox(allpts)
                if bx[0]>=20 and bx[1]<=492 and bx[2]>=20 and bx[3]<=492:
                    ccx = (cb[0]+cb[1])/2
                    ccy = (cb[2]+cb[3])/2
                    balance = ((ccx-256)**2+(ccy-256)**2)**0.5
                    best_results.append((round(balance,1), rot, angdeg, dist, round(float(cx),1), round(float(cy),1), round(float(d),1), tuple(round(float(v),1) for v in cb)))

best_results.sort()
for r in best_results[:20]:
    print(r)
