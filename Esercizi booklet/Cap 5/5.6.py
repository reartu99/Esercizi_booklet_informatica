"""
Write a program that displays all numbers divisible by 7 between 0 and N where N is typed by the user.
"""

n = int(input("Entra il numero finale"))
while n > 0:
    if n % 7 == 0:
        print(n)
    n = n-1
