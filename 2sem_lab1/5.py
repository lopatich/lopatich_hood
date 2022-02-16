import matplotlib.pyplot as plt
import numpy as np
x =[]
h1 = [8.7, 8.6, 9.0, 9.1, 9.25, 9.4, 9.6, 9.8, 9.9, 10.1, 10.3, 10.5, 10.7, 11.0, 11.2, 11.4, 11.6, 12.0]
h2 = [4.9, 4.7, 4.6, 4.4, 4.3, 4.1, 3.9, 3.7, 3.55, 3.4, 3.1, 2.9, 2.75, 2.5, 2.2, 2.0, 1.7, 1.5]
for i in range(len(h1)):
    x.append(h1[i] - h2[i])
y = [21.0, 22.0, 23.2, 24.2, 25.2, 26.2, 27.2, 28.2, 29.2, 30.2, 31.2, 32.2, 33.2, 34.2, 35.5, 36.2, 37.2, 38.2]
p, v = np.polyfit(x, y, deg=1, cov=True)
p2, v2 = np.polyfit(x, y, deg=2, cov=True)
p_f = np.poly1d(p)
p_f2 = np.poly1d(p2)
plt.plot(x, p_f2(x))
plt.plot(x, p_f(x))
print(p_f)
print(v)
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()
plt.show()

