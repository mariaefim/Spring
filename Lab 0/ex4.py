import numpy as np
import matplotlib.pyplot as plt


with plt.xkcd():
    x = np.arange(-10, 10, 1)
    y = np.arange(-10, 10, 1)
    x = eval(input("Введите функцию: "))
    plt.plot(x, y)


plt.show()