import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('wavfile.wav','r')
spf2 = wave.open('wavfile2.wav','r')
#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
signal2 = spf2.readframes(-1)
signal2 = np.fromstring(signal2, 'Int16')


#If Stereo
if spf.getnchannels() == 2:
    print 'Just mono files'
    sys.exit(0)

plt.figure(1)
plt.title('Signal Wave...1')
plt.plot(signal)
plt.savefig('First Wave')


plt.figure(2)
plt.title('Signal Wave...2')
plt.plot(signal2)
plt.savefig('Second Wave')