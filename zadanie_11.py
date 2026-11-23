# Lekcja 15 - Zadanie 11
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

X,y,names,_=make_synthetic_flowers();cov=np.cov(X,rowvar=False);corr=np.corrcoef(X,rowvar=False)
def table(M):
    print(' '*15+''.join(f'{s:>15}' for s in names))
    for name,row in zip(names,M):print(f'{name:15}'+''.join(f'{v:15.3f}' for v in row))
print('Kowariancja:');table(cov);print('Korelacja:');table(corr)
abs_corr=np.abs(corr).copy();np.fill_diagonal(abs_corr,-np.inf);i,j=np.unravel_index(np.argmax(abs_corr),corr.shape)
print('Najsilniejsza para:',names[i],names[j],f'r={corr[i,j]:.3f}', 'dodatnia' if corr[i,j]>0 else 'ujemna')
print('Pierwsze 10 wartosci:');print(np.round(X[:10,[i,j]],3))
