"""
• legge il contenuto del file “data.txt”. Il file “data.txt” contiene quattro colonne di numeri reali.
Ogni riga del file rappresenta due punti: la prima colonna e la seconda sono rispettivamente l’ascissa
e l’ordinata del primo punto, mentre, la terza e la quarta colonna sono rispettivamente l’ascissa e l’ordinata del
secondo punto. I numeri sono separati da virgola.

• Visualizzare, in uno scatter plot, i punti del primo insieme (quelli con ascissa e ordinata nella prima e seconda
colonna) in blu e quelli del secondo insieme (con ascissa e ordinata nella terza e quarta colonna) in verde;

• calcola i baricentri geometrici dei due insiemi di punti e li visualizza sul plot con il colore rosso e con
il simbolo “*”. NOTA: il baricentro è il punto le cui coordinate sono date dalla media aritmetica delle
rispettive coordinate dei punti

"""

import pandas as pd
import matplotlib.pyplot as plt


def mediacor(x, y):
    sums = 0
    for item in x:
        sums += item
    x1 = sums / len(x)
    sums = 0
    for item in y:
        sums += item
    y1 = sums / len(y)
    return x1, y1


df = pd.read_csv("data2.txt")
print(df)
plt.scatter(df.iloc[:, 0], df.iloc[:, 1], color="b")
plt.scatter(df.iloc[:, 2], df.iloc[:, 3], color="g")
x11, y11 = mediacor(df.iloc[:, 0], df.iloc[:, 1])
x12, y12 = mediacor(df.iloc[:, 2], df.iloc[:, 3])
print(x11, y11)
plt.plot(x11, y11, color="red", marker="*")
plt.plot(x12, y12, color="red", marker='*')
plt.show()
