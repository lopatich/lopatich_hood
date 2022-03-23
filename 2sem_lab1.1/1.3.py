import matplotlib.pyplot as plt

data1 = [16, 18, 20, 22, 24]
data2 = [20, 20, 18, 22, 20]
data3 = [24, 22, 20, 18, 16]
x = [1, 2, 3, 4, 5]

colors = ['lightseagreen', 'orchid', 'salmon', 'aquamarine', 'coral']
labels = ['A.', 'Б.', 'В.', 'Г.', 'Д.']

plt.subplot(231)
plt.title('#1', size=14)
plt.pie(data1, labels=labels)


plt.subplot(232)
plt.title('#2', size=14)
plt.pie(data2, labels=labels)


plt.subplot(233)
plt.title('#3', size=14)
plt.pie(data3, labels=labels)


plt.subplot(234)
plt.bar(x, data1, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')

plt.subplot(235)
plt.bar(x, data2, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')

plt.subplot(236)
plt.bar(x, data3, color=colors, edgecolor='k', tick_label=labels)
plt.grid(True, axis='y')

plt.show()
"""Для колличественной оценки лучше подходят столбчатые и на них сразу видно кто набрал больше"""
