import numpy as np
import re
import math as m

def median(x):
    x_med = 0
    for i in range(len(x)):
        x_med += x[i]

    x_med /= len(x)
    return x_med

def med_square(x):
    """среднеквадратичное отклонение"""
    x_med_sq = 0

    for i in range(len(x)):
        x_med_sq += (x[i]-median(x))**2


    x_med_sq = m.sqrt(x_med_sq/(len(x)-1))
    return x_med_sq


def q1(x):
    y1 = []



    for i in range(len(x)):
        if x[i] <= median(x):
            y1.append(x[i])


    if len(y1) % 2 != 0:
        med = int(len(y1) / 2)
        y1_med = y1[med]
    else:
        med = int(len(y1) / 2)
        y1_med = (y1[med] + y1[med - 1]) / 2


    return y1_med

def q3(x):
    y2 = []

    for i in range(len(x)):
        if x[i] >= median(x):
            y2.append(x[i])


    if len(y2) % 2 != 0:
        med = int(len(y2) / 2)
        y2_med = y2[med]
    else:
        med = int(len(y2) / 2)
        y2_med = (y2[med] + y2[med - 1]) / 2

    return y2_med

def iqr(x):
    """межквартильный размах"""

    iqr = q3(x) - q1(x)
    return iqr


x =[]
xs = []

with open('ex4.txt', 'r') as wild:
    for line in wild:
        l = list(map(int, line.split()))
        x.append(l[0])

print(med_square(x)) # с выбросами

for i in range(len(x)):
    if x[i] < (q1(x) - 1.5 * iqr(x)) or x[i] > (q3(x) + 1.5 * iqr(x)):
       pass
    else:
        xs.append(x[i])

print(med_square(xs)) # без выбросов

