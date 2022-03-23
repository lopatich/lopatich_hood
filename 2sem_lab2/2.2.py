
import matplotlib.pyplot as plt
import re

x = []
y = []
plt.xlabel('Time (min)')
plt.ylabel('Value (mAU)')

with open('Chromo.txt', 'r') as chromo:
    for line in chromo:
        string = chromo.readline()
        str1 = string.replace('\n', '\t')
        data = re.split("\t", str1)
        x.append(data[0])
        y.append(data[1])

plt.scatter(x, y, s=1, alpha=0.1)
plt.show()