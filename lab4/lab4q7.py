# -*- coding: utf-8 -*-
"""
@author: vinay
"""
import random
import matplotlib.pyplot as plt
import numpy as np

#-------------------------Fair Die
arr1 = np.array([])
trials = 10000
for i in range(trials):
    roll = random.choice([1,2,3,4,5,6])
    arr1 = np.append(arr1, [roll])

#-------------------------Biased Die
arr2 = np.array([])
for i in range(trials):
    roll = random.choice([1,1,2,3,3,4,5,5,6])
    arr2 = np.append(arr2, [roll])

plt.hist(arr1,density=True,bins=range(1,8),color ="cyan",edgecolor='white',linewidth=10,align='left',alpha=0.5,label="Fair Die")
plt.hist(arr2,density=True,bins=range(1,8),color ="red",edgecolor='white',linewidth=10,align='left',alpha=0.5,label="Biased Die")
plt.xlim([0, 7])
plt.legend()
plt.ylabel('Probability')
plt.xlabel('Outcome of Die')
plt.show()