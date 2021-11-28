# -*- coding: utf-8 -*-
"""
@author: vinay
"""
import numpy as np
import math
import matplotlib.pyplot as plt

x1 = np.linspace(0, 5/50, num=1000)
np.random.seed(0)
noisy_sine = np.sin(2*math.pi*50*x1) + np.random.normal(0,0.06,1000)
plt.subplot(3,1,1)
plt.plot(x1, noisy_sine, color = "cyan")
plt.xlim(0, 5/50)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, 5/50, 0.005))
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude')
plt.title('Noisy SINE')
plt.tight_layout()
plt.grid()

clean_sine = np.sin(2*math.pi*50*x1)
plt.subplot(3,1,2)
plt.plot(x1, clean_sine, color = "red")
plt.xlim(0, 5/50)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, 5/50, 0.005))
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude')
plt.title('Clean SINE')
plt.tight_layout()
plt.grid()

error = noisy_sine - clean_sine
plt.subplot(3,1,3)
plt.plot(x1, error, color = "blue")
plt.xlim(0, 5/50)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, 5/50, 0.005))
plt.xlabel('Time(sec)')
plt.ylabel('Amplitude')
plt.title('Error')
plt.tight_layout()
plt.grid()
plt.show()