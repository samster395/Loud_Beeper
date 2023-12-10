import numpy as np
from scipy.io.wavfile import write

sps = 44100
freq_hz = 440.0
duration = 0.3
vol = 0.3

esm = np.arange(duration * sps)
wf = np.sin(2 * np.pi * esm * freq_hz / sps)
wf_quiet = wf * vol
wf_int = np.int16(wf_quiet * 32767)
write("beep.wav", sps, wf_int)