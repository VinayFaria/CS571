# -*- coding: utf-8 -*-
"""
@author: vinay
"""
import numpy as np
import math
import matplotlib.pyplot as plt

x1 = np.linspace(0, 3/50, num=100)
y1 = 3*np.sin(2*math.pi*50*x1)
plt.subplot(2,1,1)
plt.plot(x1,y1, color = "cyan")
plt.xlim(0, 3/50)
plt.ylim(-5.5, 5.5)
plt.xticks(np.arange(0, 3/50, 0.01))
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude')
plt.title('SINE wave with frequency f = 50Hz')
plt.tight_layout()
plt.grid()

x2 = np.linspace(0, 3/75, num=100)
y2 = 5*np.sin(2*math.pi*75*x2)
plt.subplot(2,1,2)
plt.plot(x2,y2, color = "red")
plt.xlim(0, 3/50)
plt.ylim(-5.5, 5.5)
plt.xticks(np.arange(0, 3/50, 0.01))
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude')
plt.suptitle('SINE wave')
plt.title('SINE wave with frequency f = 75Hz')
plt.tight_layout()
plt.grid()
plt.show()