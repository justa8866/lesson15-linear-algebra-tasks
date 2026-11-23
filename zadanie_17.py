# Lekcja 15 - Zadanie 17
import numpy as np

rng=np.random.default_rng(42);x=np.linspace(0,10,100);y=2*x+3+rng.normal(0,1,100);A=np.column_stack([np.ones_like(x),x]);w1=np.linalg.inv(A.T@A)@A.T@y;w2=np.linalg.lstsq(A,y,rcond=None)[0]
print('Metoda | intercept | slope | MSE')
for name,w in [('normal equations',w1),('lstsq',w2)]:print(f'{name:16} | {w[0]:9.4f} | {w[1]:6.4f} | {np.mean((y-A@w)**2):.5f}')
print('Max roznica parametrow:',np.max(np.abs(w1-w2)))
