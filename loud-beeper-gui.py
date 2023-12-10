import sounddevice as sd
from numpy import linalg as LA
import numpy as np
import time
import threading
from datetime import datetime
import os
from tkinter import *
import atexit
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import json
import ctypes
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)
window = Tk()

window.title("Loud Beeper")
window.geometry('300x80')

if(os.path.exists('data.json')):
    f = open('data.json')
    data = json.load(f)
    threshold = data['threshold']
else:
    threshold = 45
    
varLE = StringVar()

lbl = Label(window, text="Threshold: " + str(threshold), font=("Arial Bold", 15))
lbl.grid(column=0, row=0, sticky = W, pady = 2)
var = IntVar()
var.set(threshold)
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var, font=("Arial Bold", 15))
spin.grid(column=1,row=0, sticky = W, pady = 2)
def clicked():
    global threshold
    threshold = int(spin.get())
    res = "Threshold: " + spin.get()
    lbl.configure(text= res)

btn = Button(window, text="Set", command=clicked, font=("Arial Bold", 15))
btn.grid(column=2, row=0, sticky = W, pady = 2)

lbl2 = Label(window, text="Last Exceeded: ", font=("Arial Bold", 15))
lbl2.grid(column=0, row=1, sticky = W, pady = 2)
lbl3 = Label(window, textvariable=varLE, font=("Arial Bold", 15))
lbl3.grid(column=1, row=1, sticky = W, pady = 2)

def print_sound(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    if int(volume_norm) > threshold:
        now = datetime.now()
        dt_string = now.strftime("%H:%M:%S")
        print (dt_string + " - Volume exceeded threshold (" + str(threshold) + ") - Volume: ", int(volume_norm))
        pygame.mixer.init()
        pygame.mixer.music.load('beep.wav')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)
        varLE.set(dt_string)
        window.update_idletasks()
    #print (int(volume_norm))

stream = sd.InputStream(channels=1, callback=print_sound, blocksize=0, samplerate=4000)

def task():
    global threshold
    with stream:
        while True:
            time.sleep(0.1)
t1 = threading.Thread(target=task, args=[])
t1.daemon = True
t1.start()

window.mainloop()

def exit_handler():
    data = {'threshold': threshold}
    with open('data.json', 'w') as f:
        json.dump(data, f)
    print ('Application closed, Saving data.')

atexit.register(exit_handler)