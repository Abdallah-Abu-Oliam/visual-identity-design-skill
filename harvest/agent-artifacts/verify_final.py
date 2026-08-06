import numpy as np

def ellipse_points(cx, cy, rx, ry, rot_deg, n=2000):
    rot = np.radians(rot_deg)
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    x = rx*np.cos(t)
    y = ry*np.sin(t)
    xr = x*np.cos(rot) - y*np.sin(rot)
    yr = x*np.sin(rot) + y*np.cos(rot)
    return np.stack([cx+xr, cy+yr], axis=1)

A = ellipse_points(175,300,110,135,0)
B = ellipse_points(388,151,68,88,30)

d2 = ((A[:,None,:]-B[None,:,:])**2).sum(-1)
idx = np.unravel_index(np.argmin(d2), d2.shape)
print("gap:", np.sqrt(d2.min()))
print("A near pt:", A[idx[0]])
print("B near pt:", B[idx[1]])

def bbox(P):
    return P[:,0].min(), P[:,0].max(), P[:,1].min(), P[:,1].max()
print("A bbox:", bbox(A))
print("B bbox:", bbox(B))
allp = np.vstack([A,B])
print("combined bbox:", bbox(allp))
cb = bbox(allp)
print("combined center:", (cb[0]+cb[1])/2, (cb[2]+cb[3])/2)

# scale check at 16px: 512/16=32 -> gap in px at 16x16
print("gap at 16px raster approx:", np.sqrt(d2.min())/32)
