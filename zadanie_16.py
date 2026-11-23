# Lekcja 15 - Zadanie 16
import numpy as np

X=np.random.default_rng(42).integers(0,11,size=(5,10));norms=np.linalg.norm(X,axis=1,keepdims=True);Z=X/np.maximum(norms,1e-12);S=Z@Z.T
mask=S.copy();np.fill_diagonal(mask,-np.inf);i,j=np.unravel_index(np.argmax(mask),mask.shape)
print('Macierz TF:\n',X,'\nCosine similarity:\n',np.round(S,3));print('Najbardziej podobne:',i,j,'wartosc:',S[i,j]);assert np.allclose(np.diag(S),1)
