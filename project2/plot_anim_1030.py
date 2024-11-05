import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

start=time.time()
pi=np.pi

# Preliminary setup of the plots
fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], 'b-') 
ax.set_xlim(-10, 0)
ax.set_ylim(-1.5, 1.5)

# Initialize the plot
def init():
    line.set_data([], [])
    return line,

# Update the plot with new data
def update(frame):
    t=time.time()-start
    xdata.append(t)
    ydata.append(np.sin(2*pi*t/10))

    # Keep only the latest 100 data points
    if len(xdata) > 100:
        xdata.pop(0)
        ydata.pop(0)

    if len(xdata)==0:
        ax.set_xlim(-10,0)
    else:
        # ax.set_xlim(xdata[0], xdata[-1])  # dynamically update x-axis range
        ax.set_xlim(np.min(xdata), np.max(xdata))
    line.set_data(xdata, ydata)
    
    return line,

# Animate with FuncAnimation
ani = FuncAnimation(fig, update, 
                    init_func=init, interval=100,cache_frame_data=False)

plt.show()