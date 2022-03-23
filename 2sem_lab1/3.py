import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
sp = plt.subplot(111)
plt.plot(x, x*x - x - 6)
plt.scatter(-2, 0)
plt.scatter(3, 0)
plt.show()