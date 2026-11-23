# Lekcja 15 - Zadanie 12
import numpy as np

w=np.random.default_rng(42).standard_normal(20);print('lambda | niezerowe L1 | norma L1 | norma L2 ridge^2')
for lam in [.01,.1,1.]:
    lasso=np.sign(w)*np.maximum(np.abs(w)-lam,0);ridge=w/(1+lam);n=np.count_nonzero(lasso)
    print(f'{lam:6.2f} | {n:12d} | {np.linalg.norm(lasso,ord=1):8.3f} | {np.linalg.norm(ridge)**2:10.3f}')
    print(f'  {lam}: '+'█'*n)
