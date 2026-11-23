# Lekcja 15 — algebra liniowa w Data Science

Zestaw 20 zadań w Pythonie przygotowany do sprawdzenia przez nauczyciela.
Każde zadanie znajduje się w osobnym pliku `zadanie_01.py`–`zadanie_20.py`.

## Zakres zadań

| Zadanie | Temat |
| --- | --- |
| 01 | Działania na wektorach i norma L2 |
| 02 | Normalizacja min–max |
| 03 | Iloczyn skalarny i kąt między wektorami |
| 04 | Transpozycja i zmiana kształtu macierzy |
| 05 | Macierz jednostkowa i diagonalna |
| 06 | Normy L1, L2 i maksimum; wektor jednostkowy |
| 07 | Odległość euklidesowa i Manhattan |
| 08 | Mnożenie macierzy przez wektor |
| 09 | Standaryzacja i odtworzenie danych |
| 10 | Macierz odległości i mapa cieplna w terminalu |
| 11 | Kowariancja i korelacja |
| 12 | Wpływ regularyzacji L1 i L2 na wagi |
| 13 | Klasyfikacja k-NN i macierz pomyłek |
| 14 | Wartości własne i wariancja wyjaśniona w PCA |
| 15 | Redukcja do dwóch składowych PCA |
| 16 | Podobieństwo cosinusowe |
| 17 | Regresja liniowa: równanie normalne i `lstsq` |
| 18 | Standaryzacja `Fare` w grupach `Pclass`: NumPy i pandas |
| 19 | Aproksymacja macierzy za pomocą SVD |
| 20 | Metoda spadku gradientu |

## Uruchomienie

Wymagany jest Python 3 z bibliotekami NumPy i pandas.
W katalogu repozytorium wykonaj:

```bash
python -m pip install -r requirements.txt
python zadanie_01.py
python zadanie_18.py
```

Pozostałe zadania uruchamia się analogicznie, podając numer pliku.
Wyniki i wizualizacje są wypisywane w terminalu; zalecane jest kodowanie UTF-8.

## Dane

Zadania dotyczące pomiarów kwiatów generują syntetyczne dane z ustalonym ziarnem
losowości. Nie korzystają z oryginalnego zbioru Iris.

Plik `titanic.csv` zawiera kolumny `Pclass` i `Fare` i jest dołączony jako wejście
do zadania 18. Skrypt szuka go w tym samym katalogu co plik zadania.
