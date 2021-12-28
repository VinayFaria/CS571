# @author: vinay

import soundfile as sf
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import math

# packing audio signal samples in frames
def enframe(x, winsize, hoplength, fs, wintype):
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
    frames = pad_signal[indices.astype(np.int64, copy=False)]
    return frames, num_frames

# Load data from wav file
y, srl = librosa.load('should.wav',sr=None) #Default Setting - sub-sampling to default 22,050 Hz, Explicitly Setting sr=None ensures original sampling preserved
#y, srl = sf.read('should.wav')
print('duration of audio is:',librosa.get_duration(y=y, sr=srl))
print('sampling rate of audio is:',srl)

# defining parameters for frame
window_size = 0.03
hop_length = 0.03
window='hann'
winsize = int(math.ceil(window_size * srl))

# calling enframe function
windowed_frames,num_frames = enframe(y, window_size, hop_length, srl, window)

# calculating energy of each frame
energy = np.zeros(num_frames)
j = 0
for single_window in windowed_frames:
    dummy = 0
    for sample in single_window:
        dummy += abs(sample)*abs(sample)
    energy[j] = dummy
    j +=1
    
# plotting energy graph
plt.figure()
plt.plot(np.linspace(0,num_frames-1,num=num_frames),energy)
plt.xlabel('frame index')
plt.ylabel('Energy')
plt.grid()

# finding frame index for which energy is greater than threshold
start_list = []
end_list = []
average_energy = sum(energy)/len(energy)
for i in range(len(energy)-1):
    if energy[i+1]>= average_energy and energy[i]<average_energy :
        start_list.append(i+1)
    if energy[i+1]< average_energy and energy[i]>=average_energy :
        end_list.append(i+1)

# saving the truncated audio based on energy segmentation
j = 0
for start,end in zip(start_list,end_list):
    segmented_audio_array = []
    for i in range(start,end+1):
        for sample in windowed_frames[i]:
            segmented_audio_array.append(sample)
    segmented_audio_array = np.asarray(segmented_audio_array)
    
    # saving as .wav format
    sf.write('segmented_audio{}.wav'.format(j),segmented_audio_array ,samplerate=srl)
    j += 1