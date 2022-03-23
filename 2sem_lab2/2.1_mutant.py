import matplotlib.pyplot as plt
import math as m
import re

x = []
y = []
sp2 = plt.subplot(111)
plt.xlabel('Concentration, nM')
plt.ylabel('Response')
plt.grid(True, axis='y')



with open('mutant.txt', 'r') as mutant:
    for line in mutant:
        string = mutant.readline()
        str1 = string.replace('\n', '\t')
        data = re.split("\t", str1)
        sp2.scatter(data[0], data[1])

plt.show()