# Lekcja 15 - Zadanie 8
import numpy as np

rng=np.random.default_rng(0);A=rng.standard_normal((4,3));w=rng.standard_normal(3);y=A@w
print('A=',A,'\nw=',w,'\ny=',y);print('Ksztalty:',A.shape,w.shape,y.shape)
# (4,3) @ (3,) -> (4,), bo kazdy z 4 wierszy daje jeden iloczyn skalarny.
assert y.shape==(4,)
