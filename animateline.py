import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x = np.arange(0, 10, 1)
y = np.array([1, 3, 2, 5, 4, 6, 5, 7, 6, 8])

fig, ax = plt.subplots()
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)
ax.set_title("Animated Line Chart")

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(x[:i+1], y[:i+1])
    return line,

ani = animation.FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=len(x),
    interval=600,
    blit=True
)

plt.show()
