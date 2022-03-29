import numpy as np


b = np.array([
    [79, 85, 24, 46],
    [1, 57, 98, 30],
    [6, 13, 54, 37],
    [99, 3, 21, 4]
])


b_sort = np.sort(b, axis=0)
b_sort_trans = b_sort.T
# сортировка столбцов
print(b_sort)

# транспонирование
print(b_sort_trans)

print(np.concatenate((b_sort, b_sort_trans), axis=None))
print(np.concatenate((b_sort, b_sort_trans), axis=0))
print(np.concatenate((b_sort, b_sort_trans), axis=1))


