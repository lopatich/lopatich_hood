import numpy as np



def sum(x):
    con = 0
    for i in range(len(x)):
        con += int(x[i])
    return  con


square = np.array([
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
])

print('по столбцам')
for i in range(4):
    print(square[:, i])
    print(sum(square[:, i]))


print('по строкам')
for i in range(4):
    print(square[i, :])
    print(sum(square[i, :]))
    


print('по всем квадратам')
for i in range(3):
    for j in range(3):

        l = square[i:i + 2, j:j + 2]
        print(l)
        l = list((np.array(l)).reshape(4, ))
        print(sum(l))



