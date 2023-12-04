import numpy as np
from matplotlib import pyplot as plt

#равномерное распределение U(0, 12)
res = np.random.uniform(0, 12, 1000000)
print(res[:10])

#гистограмма
plt.hist(res)
plt.show()

#среднее значение и дисперсия
print(np.mean(res))
print(np.var(res))

#вероятность ожидания автобуса до семи минут
print(len(res[res <= 7])/len(res))