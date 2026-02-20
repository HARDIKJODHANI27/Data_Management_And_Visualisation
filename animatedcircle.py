import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

circle = plt.Circle((0, 5), 0.5)
ax.add_patch(circle)

def init():
    circle.center = (0, 5)
    return circle,

def animate(frame):
    x = frame * 0.1
    y = 5
    circle.center = (x, y)
    return circle,

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=100,
    init_func=init,
    interval=30,
    blit=True
)

plt.show()
