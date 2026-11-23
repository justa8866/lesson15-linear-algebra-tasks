# Lekcja 15 - Zadanie 10
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

X,*_=make_synthetic_flowers();rng=np.random.default_rng(42);indices=rng.choice(150,size=10,replace=False);D=distances(X[indices],X[indices]);np.fill_diagonal(D,0)
print('Indeksy:',indices,'\nOdleglosci:\n',np.round(D,2));print('Diagonala bliska zeru:',np.allclose(np.diag(D),0))
levels=np.quantile(D,[.2,.4,.6,.8]);chars='·░▒▓█'
print('Heatmapa: · najmniejsza, █ najwieksza')
for row in D:print(''.join(chars[np.searchsorted(levels,val,side='right')] for val in row))
