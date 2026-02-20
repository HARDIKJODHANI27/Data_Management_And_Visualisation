import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

labels = ['A', 'B', 'C', 'D', 'E']
fig, ax = plt.subplots()

def update(frame):
    values = np.random.randint(10, 100, size=len(labels))
    ax.clear()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Dynamic Animated Pie Chart")
    ax.axis('equal')

ani = FuncAnimation(fig, update, interval=1000)
plt.show()
