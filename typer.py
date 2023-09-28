import pyautogui
import time

#Sleep for 5 seconds
time.sleep(3)
pyautogui.write('Hello World')

txt = 'The quick brown fox jumps over the lazy dog'

for i in txt:
    pyautogui.write(i)
    time.sleep(0.00005)