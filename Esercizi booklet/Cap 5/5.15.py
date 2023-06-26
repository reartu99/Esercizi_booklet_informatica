"""
Write a program that reads a word and displays it in reverse.
For example, if the user supplies the string "Harry", the program must display: "yrraH"
"""
strs = input("Enter the name: ")
nstrs = list(strs)[::-1]
nstrs = "".join(nstrs)
print(nstrs)
