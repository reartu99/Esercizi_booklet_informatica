"""
Scrivere un programma che legge il contenuto del file “data.txt” ed esegue i seguenti passi:
1) visualizza in uno scatter plot i punti di cui x e y rappresentano la prima e la terza colonna del file “data.txt”;
2) visualizza la somma dei valori contenuti in una colonna scelta dall’utente.

"""

import numpy as np

with open("data.txt", "r") as f:

