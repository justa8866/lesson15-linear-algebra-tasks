# Lekcja 15 - Zadanie 4
import numpy as np

A=np.arange(1,13).reshape(3,4)
for name,M in [('oryginalna',A),('transpozycja',A.T),('2x6',A.reshape(2,6)),('6x2',A.reshape(6,2))]:print(name,M.shape,'\n',M)
