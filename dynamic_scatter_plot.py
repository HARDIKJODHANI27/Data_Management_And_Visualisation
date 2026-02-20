import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x_data, y_data = [], []
sc = ax.scatter([], [])

def update(frame):
    x_data.append(np.random.randint(0, 50))
    y_data.append(np.random.randint(0, 100))
    ax.clear()
    ax.scatter(x_data, y_data, color='blue')
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 100)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_title("Dynamic Scatter Plot")

ani = FuncAnimation(fig, update, interval=500)
plt.show()
