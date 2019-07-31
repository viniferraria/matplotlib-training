#%%
#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ax_x = np.array([23,1,23123,123,12,2,122])
ax_y = [num*0.39 for num in ax_x]

plot = plt.figure(1, facecolor='coral')
ax = plot.add_axes([1,1,1,1])
ax.plot(ax_x,ax_y)

index = ['Arctic',  'Atlantic', 'Indian', 'Pacific', 'Southern']
avg_ocean_depth = pd.Series([1205, 3646, 3741, 4080, 3270], index=index)

fig = plt.figure()
ax1 = fig.add_axes([1,1,1,1])

ax1.pie(avg_ocean_depth)
ax1.legend(index)
ax1.close(fig)#fecha a imagem
ax1.savefig("lol.png")
