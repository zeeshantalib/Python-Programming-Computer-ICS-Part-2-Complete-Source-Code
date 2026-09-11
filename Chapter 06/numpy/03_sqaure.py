import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = x ** 2

plt.plot(x, y)

plt.title("Square of Numbers")
plt.xlabel("Number")
plt.ylabel("Square")

plt.show()