import matplotlib.pyplot as plt
import numpy as np

x = list(map(int, input("Enter X values: ").split()))
y = list(map(int, input("Enter Y values: ").split()))

x = np.array(x)
y = np.array(y)

plt.plot(x, y, marker='o')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Chart")

plt.show()
