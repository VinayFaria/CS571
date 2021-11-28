# -*- coding: utf-8 -*-
"""
@author: vinay
"""

import numpy as np
import math
import matplotlib.pyplot as plt

x = np.linspace(0, 4*math.pi, num=100)
y = np.sin(x)
plt.scatter(x,y, color = "cyan")
plt.xlim(0, 4*math.pi)
plt.ylim(-1.25, 1.25)
plt.xticks(np.arange(0, 4*math.pi, math.pi/5))
plt.title('SINE wave')
plt.xlabel('Radians')
plt.ylabel('Amplitude')
plt.grid()
plt.show()