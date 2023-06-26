"""
Write a program that reads an integer from the user and displays a message indicating whether the integer is negative,
positive or zero. The check task must be made in a function.
"""


def check(ints):
    if ints > 0:
        print("Integer is positive")
    elif ints < 0:
        print("Integer is negative")
    else:
        print("Integers is 0")


check(-1)
check(1)
check(0)
