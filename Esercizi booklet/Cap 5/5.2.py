"""
Write a Python program to build a string by concatenating(separated by a space)
two strings given by the user after swapping the first two characters of the given strings.
"""


def swap(oldstring):
    nstring = list(oldstring)
    temp = nstring[0]  # Non ho la minima idea perchè dia errorre su class list ??? E
    nstring[0] = nstring[1]  # Nonostante lo strano errore funziona, sembra un problema di pycharm
    nstring[1] = temp
    finstring = "".join(nstring)
    return finstring


s1 = input("Inserisci stringa 1")
s2 = input("Inserisci stringa 2")
s1f = swap(s1)
s2f = swap(s2)
finalstring = s1f + s2f
print(finalstring)
