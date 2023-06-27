import numpy as np


def checks(arry, x, y):
    if arry[x, y] > arry[x + 1, y] and arry[x, y] > arry[x - 1, y]:
        if arry[x, y+1] < arry[x, y] and arry[x, y-1] < arry[x, y]:
            return True
    return False


# n = 5
# m = 3
# arr = np.zeros((n, m))
# lissa = []
# for item in range(n):
#    for ites in range(m):
#        arr[item, ites] = float(input("Enter number here: "))


def check(arrs, a, b):
    lissa1 = []
    for items in range(a)[1:a-1]:
        print("Range ciclo a", items)
        for itess in range(b)[1:b-1]:
            print("Range ciclo b", itess)
            if checks(arrs, items, itess):
                print("Entrato in lissa checks")
                lissa1.append(items)
                lissa1.append(itess)

    return lissa1


arrayprova = np.array([[1, 1, 1, 1, 1], [1, 5, 1, 5, 1], [1, 1, 1, 1, 1]])
lissass = check(arrayprova, 3, 5)
lunghezza = int(len(lissass)/2)
newarry = np.array(lissass).reshape((2, lunghezza))
print(newarry)
