# plotting2.py
# Author Niall HORGAN

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

#plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, label = "xsquared", color = "red")
plt.plot(xpoints, xpoints, label = "straight", color = "green")
#?plt.plot(ypoints, ypoints, label = "vertical", color = "orange")
plt.legend()

random_points = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, random_points, label = "random")

plt.show()
plt.savefig('scatter.png')