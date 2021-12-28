# @author: vinay

import soundfile as sf
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import math

# packing audio signal samples in frames
#def enframe(x, winsize, hoplength, fs, wintype):
def enframe(x, winsize, hoplength, fs):
    # compute frame length and frame step (convert from seconds to samples)
    winsize = int(math.ceil(winsize * fs))
    hop_size = int(math.ceil(hoplength * fs))
    signal_length = len(x)
    frames_overlap = winsize - hop_size
    
    num_frames = np.abs(signal_length - frames_overlap) // np.abs(winsize - frames_overlap)
    rest_samples = np.abs(signal_length - frames_overlap) % np.abs(winsize - frames_overlap)
    
    # Pad Signal to make sure that all frames have equal number of samples without truncating any samples from the original signal
    if rest_samples != 0:
        pad_signal_length = int(hop_size - rest_samples) # Dividend = Divisor × Quotient + Remainder
        z = np.zeros((pad_signal_length))
        pad_signal = np.append(x, z)
        num_frames += 1
    else:
        pad_signal = x
    
    num_frames = int(num_frames)
    # making index for each sample in each frame row contain particular frame particular frame contain number of samples i.e. frame length
    idex1 = np.tile(np.arange(0, winsize), (num_frames, 1))
    idex2 = np.tile(np.arange(0, num_frames * hop_size, hop_size),(winsize, 1)).T
    indices = idex1 + idex2
    frames = pad_signal[indices.astype(np.int64)]#, copy=False)]
    
    rect_frames = frames.copy()
    hamming_frames = frames.copy()
    
    # modifying frames for hamming
    for i in range(len(hamming_frames)):
        dummy = np.hamming(winsize)
        hamming_frames[i] = hamming_frames[i]*dummy
    """
    j = 0
    # checking window type and then modifying frames accordingly
    for frame in frames:
        if wintype == 'rect':
            pass
        elif wintype == 'hamm':
            dummy = np.hamming(winsize)
            frames[j] = frames[j]*dummy
        j += 1
    """
    return rect_frames,hamming_frames, num_frames

# Load data from wav file
#y, srl = librosa.load('should.wav',sr=None) #Default Setting - sub-sampling to default 22,050 Hz, Explicitly Setting sr=None ensures original sampling preserved
y, srl = sf.read('should.wav')
print('duration of audio is:',librosa.get_duration(y=y, sr=srl))
print('sampling rate of audio is:',srl)

axis = np.linspace(0, 2, num=len(y))

window_size = 0.03
hop_length = 0.015
"""
# asking window type rectangular or hamming
while True:
    window = input('Which window you want rectangular window (press: 1) or Hamming window (press: 2):')
    if window == '1':
        window = 'rect'
        break
    elif window == '2':
        window = 'hamm'
        break
    else:
        print('Enter valid input')
winsize = int(math.ceil(window_size * srl))
"""
# Plot sound wave
plt.figure(1)
plt.plot(axis, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sound wave of should.wav')
plt.grid()

#windowed_frames,num_frames = enframe(y, window_size, hop_length, srl, window)
rect_window_frames,hamming_window_frames,num_frames = enframe(y, window_size, hop_length, srl)

while True:
    frame_number = input('Enter any frame number from 0 to {} to get its magnitude spectrum or press enter to exit: '.format(num_frames-1))
    if not frame_number or int(frame_number)> num_frames:
        break
    single_frame_rect = rect_window_frames[int(frame_number)]
    single_frame_hamm = hamming_window_frames[int(frame_number)]
    #S = np.abs(librosa.stft(single_frame))
    #X = single_frame_rect
    #Y = single_frame_hamm
    X = np.abs(np.fft.fft(single_frame_rect))
    Y = np.abs(np.fft.fft(single_frame_hamm))
    
    X_log_magnitude = np.log10(X)
    Y_log_magnitude = np.log10(Y)
    
    #n = np.array(np.linspace(0, len(single_frame)-1, num=len(single_frame)))
    freq = np.array(np.linspace(0, srl, num=len(X_log_magnitude)))
    
    X_log_magnitude = X_log_magnitude[0:len(X_log_magnitude)//2]
    Y_log_magnitude = Y_log_magnitude[0:len(Y_log_magnitude)//2]
    
    #freq = n#*(2*np.pi/len(n))
    freq = freq[0:len(freq)//2]
    
    plt.figure(int(frame_number))
    #plt.plot(freq/np.pi,log_magnitude)
    plt.plot(freq,X_log_magnitude)
    plt.plot(freq,Y_log_magnitude)
    plt.title('frame number {}'.format(int(frame_number)))
    plt.legend(['rect', 'hamm'])
    plt.xlabel('Freq in Hz')
    #plt.xlabel(r'freq in $\pi$ units')
    plt.ylabel('Log Magnitude Spectrum')
    plt.grid()
    plt.show()
    plt.pause(0.05)
    """
    fig, ax = plt.subplots()
    img = librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), y_axis='log', x_axis='time', ax=ax)
    ax.set_title('Power spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")
    """

"""
#References
https://superkogito.github.io/blog/SignalFraming.html
"""