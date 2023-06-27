"""
Scrivere un programma che legge il contenuto del file “data.txt” ed esegue i seguenti passi:
1) visualizza in uno scatter plot i punti di cui x e y rappresentano la prima e la terza colonna del file “data.txt”;
2) visualizza la somma dei valori contenuti in una colonna scelta dall’utente.

"""

# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

f = pd.read_csv("data.txt")
print(f.head(0))
xs = f.iloc[:, 0]
print(xs)
ys = f.iloc[:, 2]
print(ys)

plt.scatter(xs, ys)
plt.show()

colsy = int(input("Enter a column: "))
cols = f.iloc[:, colsy]
sums = 0
for item in cols:
    sums += item
print(sums)
