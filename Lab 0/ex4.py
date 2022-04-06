import numpy as np
import matplotlib.pyplot as plt


with plt.xkcd():
    x = np.arange(10)
    y = np.arange(10)
    x = eval(input("Введите функцию: "))
    plt.plot(y, x)
    plt.xlabel('x')
    plt.ylabel('y')


plt.show()
