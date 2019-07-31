import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])
ax.set_yticks([]), ax.set_xticks([])

ax1 = fig.add_axes([0.0,0.5,0.5,0.5])
ax1.set_xticks([])
ax1.plot([0.8],[0.1])
title = ax1.set_title("My plot", fontsize='large')

ax2 = fig.add_axes([0.5, 0.5, 0.5, 0.5])
ax2.set_yticks([]), ax2.set_xticks([])
ax2.plot([0.8],[0.1])

ax3 = fig.add_axes([0.0,0.0,0.5,0.5])
ax3.plot([0.8],[0.1])

ax4 = fig.add_axes([0.5, 0, 0.5, 0.5])
ax4.set_yticks([])
ax4.plot([0.8],[0.1])

fig2 = plt.figure(facecolor = 'lightblue')
a = fig2.add_axes([0,0,1,1])
a.set_xticks(list(range(10)))
a.set_xticklabels(['one','two','three','four','five','six','seven','eight','nine','ten'])

plt.plot(list(range(10,0,-1)),list(range(10)))

plt.show()