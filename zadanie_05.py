# Lekcja 15 - Zadanie 5
import numpy as np

I=np.eye(5);D=np.diag([1,2,3,4,5]);A=np.arange(25).reshape(5,5)
print('I=\n',I,'\nD=\n',D,'\nA@I=A:',np.allclose(A@I,A));assert np.allclose(A@I,A)
