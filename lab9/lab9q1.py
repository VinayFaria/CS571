# @author: vinay

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# generating cosine signal
duration = 2
# sine wave discrete
fs = 8000
ns = int(duration*fs)
f = 1/32
n = np.array(np.linspace(0, ns, num=ns+1))
y1 = np.cos(2*np.pi*f*n)

# saving as .wav format
sf.write('sound1.wav',y1,samplerate=fs)

# plotting in discrete
duration1 = 0.01
fs = 8000
ns1 = int(duration1*fs)
f = 1/32
n1 = np.array(np.linspace(0, ns1, num=ns1+1))
y2 = np.cos(2*np.pi*f*n1)
plt.figure(1)
plt.stem(n1, y2)
plt.xlabel('n')
plt.ylabel('Amplitude')

# plotting in time
t = np.array(np.linspace(0, duration1, 1000))
y2 = np.cos(2*np.pi*250*t)
plt.figure(2)
plt.plot(t, y2)
plt.xlabel('time')
plt.ylabel('Amplitude')

# finding DFT
X = np.abs(np.fft.fft(y1))

# plotting magnitude spectrum
X = X[0:len(X)//2]
fft_fre = np.fft.fftfreq(n=y1.size, d=1/fs)
fft_fre = fft_fre[0:len(fft_fre)//2]
plt.figure(3)
plt.plot(fft_fre,X)
plt.title(['x1(n)','x2(n)'])
plt.xlabel(r'freq in $pi$ units')
plt.ylabel('Magnitude spectrum')
plt.grid()
plt.show()