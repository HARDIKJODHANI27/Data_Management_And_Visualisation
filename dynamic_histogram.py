import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

data = []

fig, ax = plt.subplots()

bins = 20

def update(frame):

    new_data = np.random.normal(loc=0, scale=1, size=5)

    data.extend(new_data)

    ax.clear()

    ax.hist(data, bins=bins, color='skyblue', edgecolor='black')

    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    
    ax.set
ani = FuncAnimation(fig, update, interval=500)

plt.show()

