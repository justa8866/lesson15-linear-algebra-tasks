# Lekcja 15 - Zadanie 1
import numpy as np

v1=np.array([3,4]);v2=np.array([1,2]);vs=[v1,v2,v1+v2,v1-v2];labels=['v1','v2','suma','roznica']
print('Wektor | wspolrzedne | norma L2')
for name,v in zip(labels,vs):print(f'{name:8} {str(v):15} {np.linalg.norm(v):.3f}')
def narysuj_wektory_2d(vektory, labels):
    symbols=['A','B','S','R'];grid=[['.' for _ in range(8)] for _ in range(7)]
    for v,s in zip(vektory,symbols):grid[6-int(v[1])][int(v[0])]=s
    for i,row in enumerate(grid):print(f'{6-i:2} '+' '.join(row))
    print('   '+' '.join(map(str,range(8))))
    print(dict(zip(symbols,labels)))
narysuj_wektory_2d(vs,labels)
