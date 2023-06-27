import numpy as np

arraymano = np.array([[0, 20, 30], [0, 20, 0], [0, 20, 0], [0, 20, 100]])
voti = np.array([10, 10, 10])
print(arraymano)


def sup(arr, prove, p, m):
    fallimento = 0
    tot = 0
    for item in range(m):
        if arr[p, item] < prove[item]:
            fallimento += 1
            if fallimento >= m/2:
                return 0
        else:
            tot += arr[p, item]

    return tot


for ites in range(4):
    print(sup(arraymano, voti, ites, 3))
