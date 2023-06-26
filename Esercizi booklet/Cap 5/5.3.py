"""
Write a program that reads three numbers and displays the message"increasing" if they are in increasing order,
"decreasing" if they are in decreasing order and"neither"
if they are neither in increasing order nor in decreasing order.
In this increasing exercise it means strictly increasing, that is, each value must be greater than the previous one
(the same meaning has the term decreasing):  the sequence 3 4 4, therefore, should not be considered increasing.
"""

n1 = float(input("Enter number 1"))
n2 = float(input("Enter number 2"))
n3 = float(input("Enter number 3"))
if n1 < n2 < n3:
    print("Increasing")
elif n3 < n2 < n1:
    print("Decreasing")
else:
    print("Neither")
