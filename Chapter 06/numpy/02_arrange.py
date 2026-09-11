import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
y = x * 2

plt.plot(x, y)

plt.title("X × 2")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()