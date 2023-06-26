"""
Display a list of integers entered by the user in ascending order
"""


def lista():
    num = []
    cond = True
    while cond:
        try:
            num.append(int(input("Insert a number, or anything else to stop:")))
        except (Exception, ):
            print("Stopping")
            cond = False

    return num


nlist = lista()
print(nlist)
nlist = sorted(nlist)
print(nlist)
