# @author: vinay

import numpy as np
import math
import matplotlib.pyplot as plt
# plot of unit step from n=15
n_start=15
step1 = []
n = np.arange(0, 40, 1)   #numpy.arange([start, ]stop, [step, ])
f=1
f_s = 20 # Sampling frequency
T= 1/f_s
for i in n:
    if i>=n_start:
        step1.append(1)
    else:
        step1.append(0)      
n_start=25
step2 = []
for i in n:
    if i>=n_start:
        step2.append(1)
    else:
        step2.append(0)
gate = []
for i,j in zip(step1,step2):
    gate.append(i-j)

y1 = gate*np.sin(2*math.pi*f*n*T)
plt.stem(n,y1)
plt.xlim(0, 30)
plt.ylim(-1.1, 1.1)
plt.xticks(np.arange(0, 40, 1))
plt.xlabel('n')
plt.ylabel('Amplitude')
#plt.title('Sampled SINE wave')
plt.grid()