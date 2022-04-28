import numpy as np
def result(x):
    for i in range(3):
        y = np.log((np.e ** (1 / np.sin(x[i])) / (5 / 4 + 1 / x[i] ** 15)) / np.log(1 + x[i] ** 2))
        print (y)
    return y

x=[1, 10, 100]
z=result(x)
