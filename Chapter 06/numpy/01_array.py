import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 15, 30, 25])

plt.plot(x, y)

plt.title("Simple Line Graph")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()
