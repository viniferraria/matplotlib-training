import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
fig.patch.set_facecolor('lightgrey')

def animate(i):
    pullData = open("donut.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []

    for eachLine in dataArray:
        if len(eachLine)>0:
            x = eachLine
            xar.append(float(x))
            
    ax1.clear()
    ax1.pie(xar)

    donut = plt.Circle((0,0),0.7, color = 'lightgrey')
    p = plt.gcf()
    p.gca().add_artist(donut)
    plt.grid(linestyle="-", color="black")

ani = animation.FuncAnimation(fig, animate, interval=5)
plt.show()
