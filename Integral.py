import matplotlib as matplotlib
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.axes3d import Axes3D
from scipy import integrate

#f(x) = x + 1
def f(x):
    return x + 1

v, err = integrate.quad(f, 1, 2)
print(v)

#f(x) = ax + b
def f(x, a, b):
    return a * x + b

v, err = integrate.quad(f, 1, 2, args = (-1, 1))
print(v)

import numpy as np

def f(x):
    return 1 / np.sqrt(abs(x))

v, err = integrate.quad(f, -1, 1, points = [0])
print(v)

#график
fig, ax = plt.subplots(figsize = (8, 3))
x = np.linspace(-1, 1, 10000)
ax.plot(x, f(x), lw = 2)
ax.fill_between(x, f(x), color = 'green', alpha = 0.5)
ax.set_xlabel("x x", fontsize = 18)
ax.set_ylabel("f(x) f(x)", fontsize = 18)
ax.set_ylim(0, 25)
plt.show()

def f(x):
    return np.sqrt(x)

x = np.linspace(0, 2, 10)
y = f(x)
v = integrate.trapz(y, x)
print(v)

#dblquad
def f(x, y):
    return x * y

def h(x):
    return x

v, err = integrate.dblquad(f, 1, 2, lambda x: 1, h)
print(v)

#tplquad
f = lambda x, y, z : x
g = lambda x : 0
h = lambda x : (1 - x) / 2
q = lambda x, y : 0
r = lambda x, y : 1 - x - 2 * y
v, err = integrate.tplquad(f, 0, 1, g, h, q, r)
print(v)