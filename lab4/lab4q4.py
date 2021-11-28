# -*- coding: utf-8 -*-
"""
@author: vinay
"""

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(0)
x = np.random.normal(0,0.06,1000)

# interquartile range (IQR) = difference between 75th and 25th percentiles
q25, q75 = np.percentile(x,[.25,.75])
bin_width = 2*(q75 - q25)*len(x)**(-1/3) # Freedman–Diaconis rule for number of bins
bins = round((x.max() - x.min())/bin_width)
plt.hist(x, bins = bins, ec='black') # density=True means y-axis is probability
plt.xticks(np.arange(-0.2, 0.15, 0.02))
plt.ylabel('Number of times that range of error occurs')
plt.xlabel('Ampitude of error')
plt.title("Histogram")
plt.show()