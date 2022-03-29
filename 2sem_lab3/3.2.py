import numpy as n


x1 = []
x2 = []

with open('ex2_1.txt', 'r') as wild:
    for line in wild:
        x1.append(list(map(int, line.split())))

with open('ex2_2.txt', 'r') as wild:
    for line in wild:
        x2.append(list(map(int, line.split())))


print(n.mean(x1, axis = 0))
print(n.mean(x2, axis = 0))



