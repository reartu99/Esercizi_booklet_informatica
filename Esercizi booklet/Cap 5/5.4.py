"""
Write a program that asks the user to enter the identification number of a month
(1 for January, 2 for February, and so on), to then display the number of days from which the selected month is made up.
 In the case of February, display the message "28 or 29days".  Enter a month:  5 30 days Do not use a different
 if / else branch for each month, but compose the conditions using the appropriate Boolean operators.
"""

Mesi = {"january": 31, "february": 28, "march": 31, "april": 30, "may": 31}
# Non volevo scrivere altri mesi perchè sono estremamente pigro

mese = input('Insert month: ')
try:
    mese = mese.lower()
except (Exception,):
    print("Not a valid month!")
else:
    if Mesi.get(mese) is None:
        print("Not a valid month!")
    else:
        print(Mesi.get(mese))
