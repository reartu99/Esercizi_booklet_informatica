"""
Write a program that gets an integerN>1from the user and computes the average of all integers i=1,...,N.
The computation should be done in a function that takesNas input parameter.
Print the result to the screen with an appropriate text.
"""


def check(ints):
    k = ints
    sums = 0
    while ints > 0:
        sums = sums + ints
        ints = ints - 1
    return sums/k


submitted = input("Enter number: ")
try:
    submitted = int(submitted)
except (Exception, ):
    print("Non numerical value")
else:
    print(check(submitted))
