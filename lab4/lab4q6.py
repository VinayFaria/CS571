# -*- coding: utf-8 -*-
"""
@author: vinay
"""

import numpy as np
import matplotlib.pyplot as plt

m1, c1 = -1/5, 7/5 # slope & intercept (line 1)
m2, c2 = -3/4, 10/4 # slope & intercept (line 2)

x = np.arange(-5,5)
y1 = x*m1+c1 # y1 is array
print(y1)
y2 = x*m2+c2 # y1 is array
print(y2)
# np.sin returns -1 if x<0, 0 if x=0, 1 if x>0
print(np.sign(y2 - y1))
# np.diff is calculated as out[i] = a[i+1] - a[i]
print(np.diff(np.sign(y2 - y1)))
# np.argwhere returns position where non-zero value is present.
print(np.argwhere(np.diff(np.sign(y2 - y1))))
# .flatten converts n dimensional array into 1 dimension array
print(np.argwhere(np.diff(np.sign(y2 - y1))).flatten())
plt.plot(x, y1, '-')
plt.plot(x, y2, '-')

idx = np.argwhere(np.diff(np.sign(y2 - y1))).flatten()
print(idx)
plt.plot(x[idx], y1[idx], 'ro')
plt.legend(['x+5y=7', '3x+4y=10', 'Intersection'])
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.grid()
plt.show()