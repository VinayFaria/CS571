# @author: vinay

import numpy as np
import matplotlib.pyplot as plt

# Placing the plots in the plane
plot2 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
plot1 = plt.subplot2grid((3, 3), (0, 2), rowspan=3, colspan=2)
plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2, colspan=2)

# plot of impulse at n=0
n=0
impulse = []
x_axis = np.arange(-10, 101, 1)
for i in x_axis:
    if i==n:
        impulse.append(1)
    else:
        impulse.append(0)

plot1.stem(x_axis, impulse)
plot1.set_xlabel('n')
plot1.set_ylabel('Amplitude')
plot1.set_title('Discrete Impulse')

# plot of unit step from n=0
n=0
step = []
x_axis = np.arange(-10, 101, 1)
for i in x_axis:
    if i>=n:
        step.append(1)
    else:
        step.append(0)

plot2.stem(x_axis, step)
plot2.set_xlabel('n')
plot2.set_ylabel('Amplitude')
plot2.set_title('unit step')

# plot of ramp from n=0
n=0
dummy = 0
ramp = []
x_axis = np.arange(-10, 101, 1)
for i in x_axis:
    if i>=n:
        ramp.append(dummy)
        dummy += 1
    else:
        ramp.append(0)

plot3.stem(x_axis, ramp)
plot3.set_xlabel('n')
plot3.set_ylabel('Amplitude')
plot3.set_title('ramp')
plt.tight_layout()