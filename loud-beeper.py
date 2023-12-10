import sounddevice as sd
from numpy import linalg as LA
import numpy as np
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

threshold = 45

def print_sound(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if int(volume_norm) > threshold:
        print ("Volume exceeded threshold - Volume: ", int(volume_norm))
        pygame.mixer.init()
        pygame.mixer.music.load('beep.wav')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)
        
    #print (int(volume_norm))

stream = sd.InputStream(channels=1, callback=print_sound,
                        blocksize=0, samplerate=4000)

with stream:
    while True:
        time.sleep(0.1)