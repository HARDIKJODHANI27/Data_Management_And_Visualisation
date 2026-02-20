import numpy as np
import matplotlib.pyplot as plt
import time

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2*x)
y4 = np.cos(2*x)

plt.ion()
fig, axs = plt.subplots(2, 2, figsize=(10,8))

line1, = axs[0, 0].plot(x, y1, color='blue')
axs[0, 0].set_ylim(-2, 2)
line2, = axs[0, 1].plot(x, y2, color='green')
axs[0, 1].set_ylim(-2, 2)
line3, = axs[1, 0].plot(x, y3, color='red')
axs[1, 0].set_ylim(-2, 2)
line4, = axs[1, 1].plot(x, y4, color='orange')
axs[1, 1].set_ylim(-2, 2)

plt.suptitle('Dynamic Subplots Example')

for _ in range(50):
    y1 = np.sin(x + np.random.rand()*0.2)
    y2 = np.cos(x + np.random.rand()*0.2)
    y3 = np.sin(2*x + np.random.rand()*0.2)
    y4 = np.cos(2*x + np.random.rand()*0.2)
    
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    line3.set_ydata(y3)
    line4.set_ydata(y4)
    
    plt.pause(0.1)

plt.ioff()
plt.show()