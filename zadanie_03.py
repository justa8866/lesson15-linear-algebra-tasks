# Lekcja 15 - Zadanie 3
import numpy as np

a=np.array([1,2,3]);b=np.array([4,5,6]);dot=np.dot(a,b)
angle=np.degrees(np.arccos(np.clip(dot/(np.linalg.norm(a)*np.linalg.norm(b)),-1,1)))
print('Iloczyn skalarny:',dot,'kat [stopnie]:',round(angle,3))
