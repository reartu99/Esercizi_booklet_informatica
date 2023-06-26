"""
Read a collection of integers from the user.
Display all the negative numbers, followed by all the zeros, followed by all the positive numbers.
"""


def listen():
    cond = True
    lis = []
    while cond:
        try:
            lis.append(int(input("Enter a number or anything else to stop: ")))
        except (Exception, ):
            cond = False
            print("Stopping")
    return lis


def divid(lists):
    pos = []
    neg = []
    zers = []
    for item in lists:
        if item > 0:
            pos.append(item)
        elif item < 0:
            neg.append(item)
        else:
            zers.append(item)
    return pos, zers, neg


def main():
    lista = listen()
    positivi, zeri, negativi = divid(lista)
    print(negativi)
    print(zeri)
    print(positivi)


if __name__ == "__main__":
    main()
