"""
Scrivere il programma Python che permette di definire due classi: una classe “Triangolo”
e una classe “Punto” di cui le istanze costituiranno i vertici del triangolo. I metodi
della classe “Triangolo” permettono di:
    -inizializzare il triangolo con le posizioni dei 3 vertici;
    -restituire in una stringa le coordinate dei vertici;
    -calcolare il perimetro del triangolo;
    -controllare se i tre vertici del triangolo possono essere effettivamente i vertici di un triangolo.
Scrivere, inoltre, un breve main che mostri il funzionamento dei metodi definiti.

"""

import numpy as np


def distanza(x1, x2, y1, y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangolo:
    def __init__(self, list1, list2, list3):
        self.p1 = list1
        self.p2 = list2
        self.p3 = list3
        self.d12 = distanza(self.p1[0], self.p2[0], self.p1[1], self.p2[1])
        self.d23 = distanza(self.p2[0], self.p3[0], self.p2[1], self.p3[1])
        self.d31 = distanza(self.p3[0], self.p1[0], self.p3[1], self.p1[1])

    def ricrea(self, p1n, p2n, p3n):
        self.p1 = p1n
        self.p2 = p2n
        self.p3 = p3n

    def posizioni(self):
        print("Le posizioni sono: ", self.p1, self.p2, self.p3)
        return self.p1 + self.p2 + self.p3

    def perimetro(self):
        dsum = self.d12 + self.d23 + self.d31
        print("The perimeter is ", dsum)
        return dsum

    def check(self):
        if self.d12 < self.d23 + self.d31 and self.d23 < self.d12 + self.d31 and self.d31 < self.d23 + self.d12:
            return True
        else:
            return False


def main():

    p11 = Punto(0, 1)
    p22 = Punto(1, 0)
    p33 = Punto(0, 0)

    t1 = Triangolo([p11.x, p11.y], [p22.x, p22.y], [p33.x, p33.y])
    t1.posizioni()
    t1.perimetro()
    print(t1.check())


if __name__ == "__main__":
    main()
