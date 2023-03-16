# plotting2.py
# Author Niall HORGAN

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

#plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, label = "xsquared", color = "red")
plt.plot(xpoints, xpoints, label = "straight", color = "green")
#plt.plot(ypoints, ypoints, label = "vertical", color = "orange")
plt.legend()
plt.show()
plt.savefig('plots.png')