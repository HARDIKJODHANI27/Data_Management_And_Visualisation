import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 20, 40, 60, 80, 100])

y = np.array([67, 68, 79, 39, 50, 60, 20, 10, 59, 72])

plt.hist(y, bins=x, edgecolor='black')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Static Histogram")

plt.show()
