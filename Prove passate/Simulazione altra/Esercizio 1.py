"""
Scrivere una funzione Python che prenda in input una stringa l1 di caratteri.
La funzione restituisce l’elenco delle consonanti contenute nella stringa e la relativa frequenza.
Se la stringa l1 in input contiene una vocale o uno spazio bisogna lanciare un’eccezione.
Infine, scrivere un breve main che legga una stringa e stampi a video ogni consonante della stringa con
la relativa frequenza
"""


def main():
    l1 = input("Enter a string of charachters: ")
    vocali = ["a", "e", "i", "o", "u"]
    consonanti = {"b": 0, "c": 0, "d": 0, "f": 0, "g": 0, "k": 0, "l": 0, "m": 0, "n": 0, "p": 0, "q": 0, "r": 0,
                  "s": 0, "t": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for item in vocali:
        if item in l1 or " " in l1:
            raise Exception("Vocale o spazio presente!")

    for item in l1:
        if item in consonanti.keys():
            print("bono", item)
            consonanti[item] += 1

    print(consonanti)


if __name__ == "__main__":
    main()
