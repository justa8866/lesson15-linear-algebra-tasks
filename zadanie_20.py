# Lekcja 15 - Zadanie 20
import numpy as np

def f(x):return (x-3)**2+5
def grad(x):return 2*(x-3)
x=-2.;alpha=.1;trajectory=[(x,f(x))]
for iteration in range(50):
    if abs(grad(x))<.01:break
    x=x-alpha*grad(x);trajectory.append((x,f(x)))
print('Koncowe x:',x,'f(x):',f(x),'iteracje:',len(trajectory)-1,'gradient:',grad(x))
width,height=50,15;xmin,xmax=-3.,7.;ymin,ymax=5.,42.
grid=[[' ']*width for _ in range(height)]
def cell(x,y):
    col=int(round((x-xmin)/(xmax-xmin)*(width-1)));row=int(round((ymax-y)/(ymax-ymin)*(height-1)))
    return max(0,min(height-1,row)),max(0,min(width-1,col))
for xx in np.linspace(xmin,xmax,500):
    row,col=cell(xx,f(xx));grid[row][col]='·'
for xx,yy in trajectory:
    row,col=cell(xx,yy);grid[row][col]='*'
print('Krzywa · | trajektoria gradient descent *')
for row in grid:print(''.join(row))
print(f'Zakres x=[{xmin},{xmax}], y=[{ymin},{ymax}]')
