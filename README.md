# Loud Beeper
I wanted a program that would beep at me when it was likely that the microphone was clipping, a GUI is included to change the threshold and it is saved when the script is closed.

Run using Python 3, various modules are required (sounddevice, numpy, tkinter, pygame)

There is some Windows specific code in yhe GUI script to minimise the console window, this can be commented out to use it on other systems.
```
kernel32 = ctypes.WinDLL('kernel32')
user32 = ctypes.WinDLL('user32')
SW_HIDE = 0
hWnd = kernel32.GetConsoleWindow()
user32.ShowWindow(hWnd, SW_HIDE)
```
