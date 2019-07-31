import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1, y2, y3 = np.cos(x), np.cos(x + 1), np.cos(x + 2)
names = ['Signal 1', 'Signal 2', 'Signal 3']

fig, axes = plt.subplots(nrows=3, ncols=1)


axes[0].plot(x,y1)
axes[1].plot(x,y2)
axes[2].plot(x,y3)

count = 1

for ax in axes.flat:
    ax.set(xticks=[], yticks=[], title ='Signal ' +str(count))
    count+=1
    
plt.show()
plt.tight_layout()
