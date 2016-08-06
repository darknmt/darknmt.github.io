import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

x = range(100)
colors = cm.rainbow(np.linspace(0,1,100))
for i in range(100):
    plt.scatter(i, i, c=colors[i])

plt.show()
