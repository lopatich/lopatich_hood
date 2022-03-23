import matplotlib.pyplot as plt
import math as m
import re

x = []
y = []
sp1 = plt.subplot(111)

plt.xlabel('Concentration, nM')
plt.ylabel('Response')
plt.grid(True, axis='y')

with open('wild_type.txt', 'r') as wild:
    for line in wild:
        string = wild.readline()
        str1 = string.replace('\n', '\t')
        data = re.split("\t", str1)
        sp1.scatter(data[0], data[1])

with open('mutant.txt', 'r') as mutant:
    for line in mutant:
        string = mutant.readline()
        str1 = string.replace('\n', '\t')
        data = re.split("\t", str1)
        sp1.scatter(data[0], data[1])

plt.show()




