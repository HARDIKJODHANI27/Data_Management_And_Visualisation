import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11])
y = np.array([99, 86, 87, 88, 100, 86, 103, 87, 94, 78])

plt.scatter(x, y, color='blue', marker='o')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Static Scatter Plot")

plt.show()
