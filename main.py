#Luckman21
"""
FINAL FANTASY VII AI Battles

Check out the README for more information
"""

import os
import threading
import keyboard
import time
from random import randint
from datascrape import *
from typer import *

battle_toggle = False
num = 0

class KillSwitch(threading.Thread):
    #Initialize the thread by overwriting the init method
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name #Defines the thread name
        self.thread_ID = thread_ID #Defines the thread ID

    #Overwrite the run method to define the code being run when started
    def run(self):
        while (keyboard.is_pressed('esc') == False):
            continue
        #Run shutdown sequence
        print("--------Shutdown sequence initiated-------")
        #Halt keyboard presses
        print(" - Keyboard input halted")
        #Save current learning model
        print("- Learning model updated")
        #quit()
        os._exit(1)

#Create thread and initialize it
alive = KillSwitch("FFVII Battle AI", 1000)    
alive.start()

while (True):

    if (keyboard.is_pressed('8')):
        battle_toggle = True

    while (battle_toggle):
        #Run battle method
        time.sleep(10)
        #num += 1
        #print(num)

        if (keyboard.is_pressed('9')):
            battle_toggle = False