"""
    Write a program that asks the user to enter his or her name.
    The programshould respond with a message that says hello to the user, using his or her name
"""

print("Enter your name")
nome = input()
try:
    ciao = float(nome)
except (Exception,):
    print("Hello " + nome)
else:
    print("Non è un nome /:")
