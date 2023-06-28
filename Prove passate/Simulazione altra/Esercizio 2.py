"""
Scrivere il programma Python che permetta di definire una classe “Articolo”.
La classe “Articolo” ha i seguenti attributi: titolo, testo, tipologia (di default è la stringa “Scientifico”),
lista di parole chiavi (vuota all’atto dell’inizializzazione). I metodi della classe “Articolo” permettono di:
    • inizializzare un oggetto della classe “Articolo” con i suoi attributi;
    • restituire in una stringa le informazioni relative ad un oggetto “Articolo”;
    • inserire la lista di parole chiavi (l’utente può inserire una parola chiave fino a quando non inserisce
    la parola “fine”);
    • comparare la lista di parole chiavi con quella di un altro oggetto della classe “Articolo” e
    restituire True se i due oggetti hanno una parola chiave in comune.
Scrivere, inoltre, un breve main che mostri il funzionamento dei metodi definiti
"""

import dataclasses


class Articolo:
    def __init__(self, titolo, testo):
        self.titolo = titolo
        self. testo = testo
        self.tipologia = "Scientifico"
        self.parole_chiave = []

    def recreate(self, titolo, testo, tipologia, parole_chiavi):
        self.titolo = titolo
        self.testo = testo
        self.tipologia = tipologia
        self.parole_chiave = parole_chiavi

    def __dir__(self):
        return str(self.titolo) + " " + str(self.tipologia) + " " + str(self.testo) + " " + str(self.parole_chiave)

    def parolechiave(self):
        while True:
            x = input("Inserire parola chiave")
            if x == "fine":
                break
            else:
                self.parole_chiave.append(x)


@dataclasses.dataclass
class Articolo2:
    titolo: str
    testo: str
    tipologia: str = "scientifico"
    parole_chiave: list = dataclasses.field(default_factory=list)

    def parolechiave(self):
        while True:
            x = input("Inserire parola chiave")
            if x == "fine":
                break
            else:
                self.parole_chiave.append(x)


# A = Articolo("La vendetta di bu", "Ciao sono un testo")
# print(A.__dir__())
# A.parolechiave()
# print(A.__dir__())

A2 = Articolo2("La vendetta di bu", "Ciao sono un testo")
print(A2)
A2.parolechiave()
print(A2)
A3 = Articolo2("La vendetta di bu", "Ciao sono un testo")

print(A2.__eq__(A3))
