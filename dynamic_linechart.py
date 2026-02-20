import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []


fig, ax = plt.subplots()

def update(frame):

    x_data.append(frame)

    y_data.append(np.random.randint(0, 100))

    ax.clear()

    ax.plot(x_data, y_data, marker='o', color='blue')

    ax.set_title("Dynamic Animated Line Chart")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")

    ax.set_xlim(0, 50)
    ax.set_ylim(0, 100)

ani = FuncAnimation(fig, update, interval=500)

plt.show()
