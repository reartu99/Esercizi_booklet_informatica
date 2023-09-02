import numpy as np

arraymano = np.array([[1, 20, 30], [2, 200, 0], [3, 280, 10], [4, 20, 100]])


def check(arr, n, m):
    for item in range(n-1):
        array1 = arr[item, :]
        array2 = arr[item + 1, :]
        for ites in range(m):
            if array1[ites] == array2[ites]:
                return False
    return True


print(check(arraymano, 4, 3))
