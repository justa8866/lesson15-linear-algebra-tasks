# Lekcja 15 - Zadanie 2
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

X,y,names,targets=make_synthetic_flowers();x=X[:,2];z=(x-x.min())/(x.max()-x.min())
print('Przed:',np.round(x[:10],3));print('Po:',np.round(z[:10],3));print('min/max:',z.min(),z.max());assert np.isclose(z.min(),0) and np.isclose(z.max(),1)
