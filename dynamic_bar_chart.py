import numpy as np
import matplotlib.pyplot as plt
import time

categories = ["A", "B", "C", "D"]
n = len(categories)

values = np.array([10, 20, 15, 25])

plt.ion()
fig, ax = plt.subplots()
bars =  ax.bar(categories, values, color="skyblue")
ax.set_ylim(0, 50)
ax.set_title("Dynamic Bar Chart")
ax.set_ylabel("Value")

for _ in range(20):
    values = values + np.random.randint(-5, 6, size = n)
    values = np.clip(values, 0, 50)

    for bar, val in zip(bars, values):
        bar.set_height(val)

    plt.pause(0.5)

plt.ioff()
plt.show()