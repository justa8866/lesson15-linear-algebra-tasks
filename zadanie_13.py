# Lekcja 15 - Zadanie 13
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

X,y,_,names=make_synthetic_flowers();rng=np.random.default_rng(42);idx=rng.permutation(150);tr=idx[:120];te=idx[120:];D=distances(X[te],X[tr]);k=5
pred=np.array([np.bincount(y[tr][np.argsort(d)[:k]],minlength=3).argmax() for d in D]);cm=np.zeros((3,3),dtype=int)
np.add.at(cm,(y[te],pred),1)
print('Accuracy:',(pred==y[te]).mean());print('Macierz pomylek (wiersze=prawda, kolumny=predykcja):\n',cm)
