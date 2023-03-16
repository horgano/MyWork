# hist.py
# Messing with Histograms
# Author Niall Horgan

import matplotlib.pyplot as plt
import numpy as np

# Seed to keep same random output for this command
# np.random.seed(1)
norm_data = np.random.normal(size=10000)

plt.hist(norm_data)
plt.show()


