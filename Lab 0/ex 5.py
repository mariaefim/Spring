import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]
p, v = np.polyfit(x, y, deg=1, cov=True)
b, c = np.polyfit(x, y, deg=2, cov=True)
p1 = np.poly1d(p)
p2 = np.poly1d(b)
plt.plot(x, p1([1, 2, 3, 4, 5, 6]), label=r'$f(x)=ax+b$')
plt.plot(x, p2([1, 2, 3, 4, 5, 6]), label=r'$f(x)=ax^2+bx+c$')
plt.plot(x, y, 'g', label='исходная зависимость')
plt.xlabel(r'$x$', fontsize=14)
plt.ylabel(r'$f(x)$', fontsize=14)
plt.legend(loc='best', fontsize=9)
plt.errorbar(x, y, xerr=0.05, yerr=0.1, ecolor='r')
plt.grid()
plt.show()