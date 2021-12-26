# -*- coding: utf-8 -*-
"""
@author: vinay
"""
import numpy as np
import math
import matplotlib.pyplot as plt

x1 = np.linspace(0, 2, 1000)
f = 1
y1 = np.sin(2*math.pi*f*x1)
plt.plot(x1,y1, color = "blue")
plt.xlim(0, 2)
plt.ylim(-1.1, 1.1)
#plt.xticks(np.arange(0, 3/50, 0.01))
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude')
plt.title('SINE wave with frequency f = 1Hz')
plt.grid()