import matplotlib.pyplot as plt
v, x, t = [], [], []
for i in range(1, 6):
    xt = 3 * i
    v2 = xt / i
    v.append(v2)
    t.append(i)
    x.append(xt)
print('Скорость равна:', v2, 'м/с')
print('Расстояние равно:', v2 * 3, 'м')
plt.grid()
plt.plot(t, x)
plt.show()
plt.grid()
plt.plot(t, v)
plt.show()