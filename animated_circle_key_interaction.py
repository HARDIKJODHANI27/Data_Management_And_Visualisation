# Write a python code to make an animated circle with key interactions

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = [0]
y = [0]

fig, ax = plt.subplots()
point, = ax.plot([], [], 'ro', markersize=10)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

def update(frame):
    point.set_data([x[0]], [y[0]])
    return point,

def on_key(event):
    if event.key == 'left':
        x[0] -= 1
    elif event.key == 'right':
        x[0] += 1
    elif event.key == 'up':
        y[0] += 1
    elif event.key == 'down':
        y[0] -= 1

fig.canvas.mpl_connect('key_press_event', on_key)

ani = FuncAnimation(fig, update, interval=50)

plt.show()