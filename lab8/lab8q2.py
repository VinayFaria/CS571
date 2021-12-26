# @author: vinay

import numpy as np
import matplotlib.pyplot as plt

dummy = 0
x_axis = np.arange(-1, 21, 1)
signal = []
for n in x_axis:
    if n>=0 and n<10:
        signal.append(dummy)
        dummy += 1
    elif n>=10 and n<20:
       signal.append(10*np.exp(-0.3*(n-10)))
    else:
        signal.append(0)

plt.stem(x_axis, signal)
plt.xticks(np.arange(-1, 21, 1))
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Complicated signal')
plt.grid()
plt.show()