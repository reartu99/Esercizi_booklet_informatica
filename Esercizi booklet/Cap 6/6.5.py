"""
Write a Python program to calculate the value of a**b recursively.
Write a main program that reads two numbers a and b and displays a**b.
"""


def pw(base, esponente):
    if esponente != 0:
        n = base * pw(base, esponente - 1)
        return n
    else:
        return 1


print("Il risultato è ", pw(4, 2))
