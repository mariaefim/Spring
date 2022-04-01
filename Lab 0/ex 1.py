import numpy as np
x = int(input("Введите значение переменной x = "))
y = np.log((np.e**(1/np.sin(x))/(5/4 + 1/x**15)) / np.log(1 + x**2))
print(y)