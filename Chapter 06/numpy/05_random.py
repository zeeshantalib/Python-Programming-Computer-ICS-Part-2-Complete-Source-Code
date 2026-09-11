import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(1, 100, 20)
y = np.random.randint(1, 100, 20)

plt.scatter(x, y)

plt.title("Random Data")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()