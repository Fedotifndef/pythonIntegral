import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

#точка отсчета
np.random.seed(42)

#100 000 значений нормального распределения величины с матожиданием 180 см и СКО 10см
height_men = np.round(np.random.normal(180, 10, 100000))
height_women = np.round(np.random.normal(160, 10, 100000))
print(height_men[:10])
print(height_women[:10])

#гистрограмма
plt.figure(figsize = (10,6))

#зададим 18 интервалов и уровень прозрачности графиков
plt.hist(height_men, 18, alpha = 0.5, label = 'Рост мужчин')
plt.hist(height_women, 18, alpha = 0.5, label = 'Рост женщин')
plt.legend(loc = 'upper left', prop = {'size': 14})
plt.xlabel('Рост см', fontsize = 16)
plt.ylabel('Количество людей', fontsize = 16)
plt.title('Распределение роста мужчин и женщин в России', fontsize = 18)
plt.show()

plt.figure(figsize = (10, 6))

#график функции плотности
sns.kdeplot(height_men, fill = True, label = 'Рост мужчин')
sns.kdeplot(height_women, fill = True, label = 'Рост женщин')
plt.legend(loc = 'upper left', prop = {'size': 14})
plt.xlabel('Рост см', fontsize = 16)
plt.ylabel('Количество людей', fontsize = 16)
plt.title('Распределение роста мужчин и женщин в России', fontsize = 18)
plt.show()

data = pd.DataFrame({'Мужчины' : height_men, 'Женщины' : height_women})
data.head()

plt.figure(figsize = (10, 6))
#два вертикальных boxplots, передав датафрейм с данными в параметр data
sns.boxplot(data = data)
plt.xticks(fontsize = 14)
plt.ylabel('Рост, см', fontsize = 16)
plt.title('Распределение роста мужчин и женщин в России', fontsize = 17)
plt.show()

#совмещение boxplot c гистограммой
f, (ax_box, ax_hist) = plt.subplots(nrows = 2,
                                    ncols = 1,
                                    sharex = True,
                                    gridspec_kw = {'height_ratios': (.15, .85)},
                                    figsize = (12, 8))
#boxplot
sns.boxplot(x = height_men, ax = ax_box)
#гистограмма
sns.histplot(data = height_men, bins = 15, ax = ax_hist)

ax_box.set_title('Распределение роста мужчин и женщин в России', fontsize = 17)
ax_hist.set_xlabel('Рост, см', fontsize = 15)
ax_hist.set_ylabel('Количество людей', fontsize = 15)
plt.show()