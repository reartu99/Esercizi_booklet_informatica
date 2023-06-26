"""
Write a program which repeatedly reads numbers until the user enters the string done. Once done is entered,
print out the total, count, and average of the numbers. If the user enters anything other than a number,
detect his mistake using try...except statement and print an error message and skip to the next number
"""


def nums():
    liss = []
    cnd = True

    while cnd:
        elm = input("Enter a number or enter done to finish: ")
        try:
            elm = int(elm)
        except (Exception, ):
            if elm == "done":
                print("Finishing")
                cnd = False
            else:
                print("Non numerical value!")
        else:
            liss.append(elm)
    return liss


numss = nums()
average = sum(numss)/len(numss)
print("The total is " + str(numss) + " the average is " + str(average) + " and the count is " + str(len(numss)))
