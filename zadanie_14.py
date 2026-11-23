# Lekcja 15 - Zadanie 14
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

X,*_=make_synthetic_flowers();C=X-X.mean(axis=0);cov=C.T@C/(len(X)-1);vals,vecs=np.linalg.eigh(cov);order=np.argsort(vals)[::-1];vals=vals[order];vecs=vecs[:,order];ratio=vals/vals.sum()
print('Komponent | eigenvalue | ratio | cumulative')
for i,(v,r,c) in enumerate(zip(vals,ratio,np.cumsum(ratio)),1):print(f'{i:9d} | {v:10.5f} | {r:6.2%} | {c:6.2%} '+'█'*int(round(r*40)))
print('Liczba komponentow dla 95%:',np.searchsorted(np.cumsum(ratio),.95)+1)
