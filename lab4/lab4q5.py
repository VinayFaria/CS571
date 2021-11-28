# -*- coding: utf-8 -*-
"""
@author: vinay
"""

import numpy as np
import matplotlib.pyplot as plt

m1, c1 = -1/5, 7/5 # slope & intercept (line 1)
m2, c2 = -3/4, 10/4 # slope & intercept (line 2)

x = np.arange(-5,5)
y1 = x*m1+c1
y2 = x*m2+c2

plt.plot(x, y1, '-')
plt.plot(x, y2, '-')

#Intersection point, x*m1+c1 = x*m2+c2, x=(c1-c2)/(m2-m1)
xi=(c1-c2)/(m2-m1)
yi = xi*m1+c1
plt.scatter(xi,yi)
plt.legend(['x+5y=7', '3x+4y=10', 'Intersection'])
plt.ylabel('Y-axis')
plt.xlabel('X-axis')
plt.grid()
plt.show()