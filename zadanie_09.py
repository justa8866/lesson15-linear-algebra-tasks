# Lekcja 15 - Zadanie 9
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

X,*_=make_synthetic_flowers();mean=X.mean(axis=0);std=X.std(axis=0);Z=(X-mean)/std;restored=Z*std+mean
print('Ksztalt:',Z.shape,'\nSrednie:',Z.mean(axis=0),'\nOdchylenia:',Z.std(axis=0));print('Max blad:',np.abs(restored-X).max())
assert np.allclose(Z.mean(axis=0),0) and np.allclose(Z.std(axis=0),1)
