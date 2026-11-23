# Lekcja 15 - Zadanie 6
import numpy as np

v=np.array([3,-4,12,0,-5]);l2=np.linalg.norm(v);unit=v/l2
for label,order in [('L1',1),('L2',2),('Linf',np.inf)]:print(label,np.linalg.norm(v,ord=order))
print('Jednostkowy:',unit,'norma:',np.linalg.norm(unit));assert np.isclose(np.linalg.norm(unit),1)
