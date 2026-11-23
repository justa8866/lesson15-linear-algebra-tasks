# Lekcja 15 - Zadanie 19
import numpy as np

rng=np.random.default_rng(42);x=np.linspace(-1,1,64);y=np.linspace(-1,1,64);xx,yy=np.meshgrid(x,y);img=np.exp(-(xx**2+yy**2)*2)+.05*rng.standard_normal((64,64));U,S,Vt=np.linalg.svd(img,full_matrices=False)
print('k | stored values | compression ratio | MSE')
for k in [5,10,20,64]:
    rec=U[:,:k]@np.diag(S[:k])@Vt[:k,:];mse=np.mean((img-rec)**2);stored=k*(64+64+1)
    print(f'{k:2} | {stored:13} | {4096/stored:17.3f} | {mse:.8f}')
    if k==10:img10=rec
chars='·░▒▓█';levels=np.quantile(img10,[.2,.4,.6,.8]);print('Heatmapa rekonstrukcji k=10:')
for row in img10[::2,::2]:print(''.join(chars[np.searchsorted(levels,v,side='right')] for v in row))
print('k=64 daje praktycznie zerowy blad; k=20 czesto wystarcza dla malego bledu wzgledem szumu.')
