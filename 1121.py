import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange
from scipy.interpolate import interp1d


def normal(x): return 1 / (5 + x*x)


def lagrangeFunc(x, y): return lagrange(x, y)


def cubicSpline(x, y): return interp1d(x, y, kind='cubic')


x1 = np.linspace(-9, 10, 20)
y1 = normal(x1)

f2 = lagrangeFunc(x1, y1)
x2 = np.linspace(-9, 10, 50)
y2 = f2(x2)

f3 = cubicSpline(x1, y1)
y3 = f3(x2)

plt.plot(x1, y1, 'o', x2, y2, '-', x2, y3, '--')
plt.legend(['normal', 'lagrange', 'cubic spline'], loc='best')
plt.show()
