"""
Scrivere una funzione Python che prende in input una lista e ritorna una nuova lista con gli
elementi della lista in input senza duplicati.

Esempio:
Lista in input:  [1,2,3,3,3,3,4,5]
Lista in output : [1, 2, 3, 4, 5]
"""

try:
    listain = []
    while True:
        listain.append(float(input()))
except:
    print(listain)

blacklist = []
newlist = []

for item in listain:
    if item not in blacklist:
        newlist.append(item)
        blacklist.append(item)

print(newlist)
