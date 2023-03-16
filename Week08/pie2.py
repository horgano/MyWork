# pie.py
# Messing with Histograms
# Author Niall Horgan

import matplotlib.pyplot as plt
import numpy as np

fruit = np.array(['Apples', 'Orange' ,'Pears'])
numbers = np.array([23, 77, 5000])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.savefig("pie.png")
plt.show()
