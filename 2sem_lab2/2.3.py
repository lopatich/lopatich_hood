import math as m
import re

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

def covariance(xs, ys):
    cov = 0
    for i in range(len(xs)):
        cov += (xs[i]-median(xs))*(ys[i]-median(ys))
        cov = cov/(len(xs)-1)
    return cov

def correlation(xs, ys):
    corr = covariance(xs, ys) / (med_square(xs)*med_square(ys))
    print(corr)

x = []
y = []
with open('wild_type.txt', 'r') as wild:
    for line in wild:
        string = wild.readline()
        str1 = string.replace('\n', '\t')
        data = re.split("\t", str1)
        x.append(float(data[0]))
        y.append(float(data[1]))

correlation(x, y)