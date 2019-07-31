import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("barh.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    y = np.arange(len(xar))
    
    for eachLine in dataArray:
        if len(eachLine)>0:
            x = eachLine
            xar.append(float(x))
            y = np.arange(len(xar))
            
    ax1.clear()
    ax1.barh(y, xar, allign='center', alpha = 0.5)
    plt.grid(linestyle="-", color="black", zorder = 1)

ani = animation.FuncAnimation(fig, animate, interval=5)
plt.show()
