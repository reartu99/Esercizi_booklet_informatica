import numpy as np


def check(arrs, m, n):
    newass = arrs.T
    print(newass)

    for items in range(n-1):
        print("ciclo n " + str(items))
        if np.array_equal(arrs[items], arrs[items+1]):
            for itemss in range(m-1):
                print("ciclo m " + str(itemss))
                if np.array_equal(newass[itemss], newass[itemss + 1]):
                    return True

    return False


n = 3
m = 3
arr = np.zeros((n, m))
for item in range(n):
    for ites in range(m):
        arr[item, ites] = float(input("Enter number here: "))
print(check(arr, m, n))
