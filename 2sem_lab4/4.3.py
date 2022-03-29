import numpy as np
import re


date = []
name = []
volume = []
comment = []

data = np.zeros(6, dtype = [('date', 'U9'), ('name', 'U9'), ('volume', int), ('comment', 'U9')])


with open('Cell_culture.txt', 'r') as cell:
    for line in cell:
        str1 = line.replace('\n', '\t')
        l = re.split("\t", str1)
        date.append(str(l[0]))
        name.append(str(l[1]))
        volume.append(int(l[2]))
        comment.append(str(l[3]))


data['date'] = date
data['name'] = name
data['volume'] = volume
data['comment'] = comment




summ = 0
names_9_apr = []

for i in range(len(data)):
    if data[i]['date'] == '5-Apr':
        summ += data[i]['volume']
    elif data[i]['date'] == '9-Apr':
        names_9_apr.append(data[i]['name'])



print(summ)
print(names_9_apr)
