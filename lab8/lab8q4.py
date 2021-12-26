# -*- coding: utf-8 -*-
"""
@author: vinay
"""
import numpy as np
import math
import matplotlib.pyplot as plt

n = np.arange(0, 40, 1)   #numpy.arange([start, ]stop, [step, ])
f=1
f_s = 20 # Sampling frequency
T= 1/f_s
y1 = np.sin(2*math.pi*f*n*T)
plt.stem(n,y1)
plt.xlim(0, 40)
plt.ylim(-1.1, 1.1)
plt.xticks(np.arange(0, 40, 1))
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Sampled SINE wave')
plt.grid()