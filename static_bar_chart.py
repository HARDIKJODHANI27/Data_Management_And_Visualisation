import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D", "E"])
y = np.array([10, 25, 15, 30, 20])

plt.bar(x, y, color='skyblue', edgecolor='black')

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Static Bar Chart")

plt.show()
