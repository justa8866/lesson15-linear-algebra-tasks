# Lekcja 15 - Zadanie 15
import numpy as np

def make_synthetic_flowers(seed=42):
    rng = np.random.default_rng(seed)
    centers = np.array([[5.,3.4,1.5,.2],[5.9,2.8,4.3,1.3],[6.6,3.,5.6,2.]])
    stds = np.array([.35,.35,.45,.25])
    X = np.vstack([rng.normal(c,stds,size=(50,4)) for c in centers])
    y = np.repeat(np.arange(3),50)
    return X,y,['sepal_length','sepal_width','petal_length','petal_width'],np.array(['A','B','C'])

def distances(A,B):
    A=np.asarray(A);B=np.asarray(B)
    return np.sqrt(np.maximum(0,((A[:,None,:]-B[None,:,:])**2).sum(axis=2)))

X,y,_,_=make_synthetic_flowers();C=X-X.mean(axis=0);vals,vecs=np.linalg.eigh(C.T@C/(len(X)-1));W=vecs[:,np.argsort(vals)[::-1][:2]];Z=C@W
print('Ksztalt PCA:',Z.shape,'\nPierwsze 10:\n',np.round(Z[:10],3))
h,w=20,50;grid=[[' ']*w for _ in range(h)];lo=Z.min(axis=0);hi=Z.max(axis=0);coords=np.rint((Z-lo)/(hi-lo)*[w-1,h-1]).astype(int)
for (x,yy),cls in zip(coords,y):
    row=h-1-yy;ch='ABC'[cls];grid[row][x]=ch if grid[row][x]==' ' else '*'
print('Scatter PCA (A/B/C gatunki, * nakladanie):')
for row in grid:print(''.join(row))
print('Klasy sa w duzej mierze rozdzielone w przestrzeni dwoch pierwszych skladowych.')
