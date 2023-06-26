"""
Begin by reading the cost of a meal ordered at a restaurant from the user.
Then compute the tax and tip for the meal. Use your local tax rate when computing the amount of tax owing.
Computethe tip as 18 percent of the meal amount (without the tax). The output from your program should incloude
the tax amount, the tip amount, and the grand total for the meal including both the taxand the tip.
"""

cost = input("Il costo del piatto è:")
try:
    cost = float(cost)
except (Exception,):
    print("Non numerical values...")
else:
    print("The cost of the meal is ", str(cost))
    tax = round(cost*0.22, 3)
    tip = round(cost*0.18, 3)
    total = round(cost + tax + tip, 3)
    print("The cost was " + str(cost) + "$ the tax is " + str(tax) + "$ the tip is " + str(tip) + '$')
    print("The grand total comes to: " + str(total))
