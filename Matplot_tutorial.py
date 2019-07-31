#%%
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.backends.backend_pdf import PdfPages

#data
data_1 = np.array([2,3,4,5])
data_2 = np.array([2,3,4,5])
data_3 = np.array([1,2,3])
data_4 = np.array([num+1 for num in data_3])

#               Figura com id 1
plt.figure(1,facecolor = 'lightgreen', edgecolor='red',frameon =True)

#               Plot 1
plt.axes([0, 0, 1, 1])
plt.xlabel("Label eixo x")
plt.ylabel("Label eixo y")
plt.ylim(0,0.5)
plt.twinx()
plt.ylabel("Principal direito")
plt.plot(data_1,data_2,'r-',data_1,data_2,'yo',label = 'bubble')
plt.text(4, 4, r'$\mu=100, \ \sigma=15$')
plt.ylim(1, 10)
plt.grid(axis = 'y')
plt.legend(loc = 'center')


#               inset Plot 1
plt.axes([0.7, 0.0, 0.3, 0.4], facecolor = 'coral')
plt.ylabel("menor")
plt.xticks(np.arange(0, 1, 0.2))
plt.yticks([])
plt.hist(data_3, data_4, color = 'purple', density=True, label = ['purple'])
plt.grid(True)
plt.legend()


#               Gera uma figura com id 2
plt.figure(2, facecolor = 'coral')

#               Plot 2
labels = ['a', 'b', 'c']
plt.pie(data_4, colors = ['lightblue', 'lightgreen', 'lightyellow'], labels = labels)
plt.legend()

#               Gera uma figura com id 3
figure_3 = plt.figure(3, facecolor = 'lightgrey')

#               Plot 3 (OOP)
ax1 = figure_3.add_axes([0.1, 0.1, 0.8, 0.8]) 
ax1.plot([4, 3, 2],[2, 3, 4],'g--',label = 'outter graph')
ax1.grid()
ax1.set(xticks = list(range(5)), xticklabels = ["zero", "one", "two", "three", "four"], title = "my graph")
ax1.legend()

#               Axe 2 da figura com id 3
ax2 = figure_3.add_axes([0.72, 0.5, 0.16, 0.16])
ax2.plot([1, 2, 3], [5, 6, 7], color = 'brown', label = 'inner graph')
ax2.set(xticks = ([]), yticks = [], title="A title", xlabel="x", ylabel="y")
ax2.grid()
ax2.legend()


#               Gera uma figura com id 4'
plt.figure(4, facecolor = 'lightblue')

#               Graph 4 (OOP)
plt.subplot(1, 1, 1)
plt.pie([0.9,0.1], colors = ['yellow', 'lightblue'], labels = ['pac','man'])
plt.legend()
f = plt.gcf()
print(f)
plt.rc('xtick', color = 'red')
plt.rc('ytick', color = 'blue')
plt.show()
plt.tight_layout()

#               Fecha a figura 3
plt.close(figure_3) 
figure_3.savefig("lol.png")

# pp = PdfPages('multipage.pdf')
# pp.savefig()
# pp.close

#%%
