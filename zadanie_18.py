# Lekcja 15 - Zadanie 18: normalizacja Fare osobno dla kazdej klasy Pclass
# Wymagane biblioteki: numpy, pandas
from pathlib import Path

import numpy as np
import pandas as pd


# Plik CSV powinien znajdowac sie w tym samym folderze co skrypt.
plik = Path(__file__).resolve().parent / 'titanic.csv'
if not plik.exists():
    raise FileNotFoundError(f'Brak pliku: {plik}')

df = pd.read_csv(plik, usecols=['Fare', 'Pclass']).dropna(subset=['Fare']).copy()
df = df[df['Pclass'].isin([1, 2, 3])].copy()

fare = df['Fare'].to_numpy(dtype=float)
pclass = df['Pclass'].to_numpy()

# Sciezka A: NumPy, indeksowanie logiczne i broadcasting.
group_means = np.empty_like(fare)
group_stds = np.empty_like(fare)
for klasa in (1, 2, 3):
    mask = pclass == klasa
    if not mask.any():
        continue
    group_means[mask] = fare[mask].mean()
    group_stds[mask] = fare[mask].std(ddof=0)

if np.any(group_stds == 0):
    raise ValueError('Nie mozna normalizowac grupy o zerowym odchyleniu standardowym.')

fare_normalized_np = (fare - group_means) / group_stds

# Sciezka B: pandas groupby().transform().
fare_normalized_pd = df.groupby('Pclass')['Fare'].transform(
    lambda x: (x - x.mean()) / x.std(ddof=0)
).to_numpy()

# Porownanie wynikow obu metod.
zgodne = np.allclose(fare_normalized_np, fare_normalized_pd, atol=1e-9)
df['Fare_normalized_np'] = fare_normalized_np
df['Fare_normalized_pd'] = fare_normalized_pd
print('Czy wyniki obu metod sa zgodne?', zgodne)
print('\nPierwsze 10 wierszy:')
print(df.head(10).to_string(index=False))

# Weryfikacja: w kazdej klasie srednia ~0 i odchylenie standardowe ~1.
statystyki = df.groupby('Pclass')['Fare_normalized_np'].agg(
    mean='mean', std=lambda x: x.std(ddof=0)
)
print('\nStatystyki normalizacji dla kazdej klasy:')
print(statystyki.to_string())
assert zgodne, 'Metody NumPy i pandas zwrocily rozne wyniki.'
assert np.allclose(statystyki['mean'], 0, atol=1e-9)
assert np.allclose(statystyki['std'], 1, atol=1e-9)
