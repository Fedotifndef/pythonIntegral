import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#дифференциальное уравнение 1-го порядка
#y' = -y(t) * t

def diff(y, t):
    return -y * t

t = np.linspace(-2, 2, 51)
y0 = 1
y = odeint(diff, y0, t)
y = np.array(y).flatten()
plt.plot(t, y, '-sr', linewidth = 3)
plt.show()

#автономная система дифференциальных уравнений 1-го порядка
#y'1 = y2
#y'2 = -y2 - y1
#y1(0) = 0
#y2(0) = 1

def f(y, t):
    y1, y2 = y
    return [y2, -y2 - y1]

t = np.linspace(0, 10, 41)
y0 = [0, 1]
w = odeint(f, y0, t)
y1 = w[:, 0]
y2 = w[:, 1]
fig = plt.figure(facecolor = 'white')
plt.plot(t, y1, '-o', t, y2, '-o', linewidth = 2)
plt.ylabel("z")
plt.xlabel("t")
plt.grid(True)
plt.show()

#фазовая траектория
fig2 = plt.figure(facecolor = 'white')
plt.plot(y1, y2, linewidth = 2)
plt.grid(True)
plt.show()