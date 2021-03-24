import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', animated=False)

def init():
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 160)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(y1(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=200,
                    init_func=init, blit=True)
plt.show()
