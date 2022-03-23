import math as m

x = input().split()

for i in range(len(x)):
    x[i] = int(x[i])
x.sort()

x_med = 0
for i in range(len(x)):
    x_med += x[i]

x_med /= len(x)


def med_square():
    """среднеквадратичное отклонение"""
    x_med_sq = 0
    for i in range(len(x)):
        x_med_sq += (x[i]-x_med)**2


    x_med_sq = m.sqrt(x_med_sq/(len(x)-1))
    print(x_med_sq)



def quartille():
    """межквартильный размах"""
    y1 = []
    y2 = []
    if len(x) % 2 != 0:
        med = int(len(x) / 2)
        x_median = x[med]
    else:
        med = int(len(x) // 2)
        x_median = (x[med] + x[med - 1]) / 2


    for i in range(len(x)):
        if x[i] <= x_median:
            y1.append(x[i])
        else:
            y2.append(x[i])

    if len(y1) % 2 != 0:
        med = int(len(y1) / 2)
        y1_med = y1[med]
    else:
        med = int(len(y1) / 2)
        y1_med = (y1[med] + y1[med - 1]) / 2


    if len(y2) % 2 != 0:
        med = int(len(y2) / 2)
        y2_med = y2[med]
    else:
        med = int(len(y2) / 2)
        y2_med = (y2[med] + y2[med - 1]) / 2


    x_quartile = y2_med - y1_med
    print(x_quartile)

med_square()
quartille()