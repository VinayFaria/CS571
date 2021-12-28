# -*- coding: utf-8 -*-
"""
@author: vinay
"""
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

duration = 5
# sine wave discrete
fs = 8000
ns = int(duration*fs)
f1 = 1/32
f2 = 1/64
n = np.array(np.linspace(0, ns, num=ns+1))
y1 = 4*np.cos(2*np.pi*f1*n) + np.cos(2*np.pi*f2*n)

sf.write('sound2.wav',y1,samplerate=fs)

duration1 = 0.01
# sine wave discrete
fs = 8000
ns1 = int(duration1*fs)
f1 = 1/32
f2 = 1/64
n1 = np.array(np.linspace(0, ns1, num=ns1+1))
y2 = 4*np.cos(2*np.pi*f1*n1) + np.cos(2*np.pi*f2*n1)
plt.figure(1)
plt.stem(n1, y2)
plt.xlabel('n')
plt.ylabel('Amplitude')

# plotting in time
t = np.array(np.linspace(0, duration1, 1000))
y2 = 4*np.cos(2*np.pi*250*t) + np.cos(2*np.pi*125*t)
plt.figure(2)
plt.plot(t, y2)
plt.xlabel('time')
plt.ylabel('Amplitude')

X = np.abs(np.fft.fft(y1))
X = X[0:len(X)//2]

freq = n*(2*np.pi/len(n))
freq = freq[0:len(freq)//2]

plt.figure(3)
plt.plot(freq/np.pi,X)
plt.title(['x1(n)','x2(n)'])
plt.xlabel(r'freq in $pi$ units')
plt.ylabel('Magnitude spectrum')
plt.grid()

plt.show()