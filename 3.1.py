import matplotlib.pyplot as plt
import re


def norma(data):
    min_data = min(data)
    max_data = max(data)
    for i in range(len(data)):
        data[i] = (data[i] - min_data) / (max_data - min_data)
    return data


x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
sp1 = plt.subplot(111)

with open('melting.txt', 'r') as melting:
    for line in melting:
        str1 = line.replace('\n', '\t')
        data = re.split("\t", str1)
        x.append(float(data[0]))
        y1.append(float(data[1]))
        y2.append(float(data[2]))
        y3.append(float(data[3]))
        y4.append(float(data[4]))
        y5.append(float(data[5]))

sp1.plot(x, norma(y1))
sp1.plot(x, norma(y2))
sp1.plot(x, norma(y3))
sp1.plot(x, norma(y4))
plt.show()