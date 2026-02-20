import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x
y4 = x**2

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_title("Sine Wave")

axs[0, 1].plot(x, y2, color='green')
axs[0, 1].set_title("Cosine Wave")

axs[1, 0].plot(x, y3, color='red')
axs[1, 0].set_title("Linear")

axs[1, 1].plot(x, y4, color='purple')
axs[1, 1].set_title("Quadratic")

for ax in axs.flat:
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")

plt.tight_layout()
plt.show()
