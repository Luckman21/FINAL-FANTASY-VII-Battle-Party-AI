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
from game_state import *

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
        print("- Keyboard input halted")
        #Save current learning model
        print("- Learning model updated")
        #quit()
        os._exit(1)

def temp_battle_method():
    move = randint(0,100)

    if (move >= 0 and move < 50):
        Attack()
    elif (move >= 50 and move < 75):
        Magic()
    elif (move >= 75 and move < 90):
        Summon(10)
    elif (move >= 90):
        Item(0)

def battle_status():
    if (party_alive() and enemies_alive()):
        print("Battle ongoing...")
    elif (party_alive()):
        print("Battle won!")
    elif (enemies_alive()):
        print("Game Over")
    else:
        print("Undefined state")

def Player(name): #TODO: Implement
    party_names.get(name)

    #Remove party member from the queue
    #Load character data
    #Perform action

#Create thread and initialize it
alive = KillSwitch("FFVII Battle AI", 1000)    
alive.start()

#Creates the Queue for characters to take control of the controls
atb_queue = []
atb_queue_maxsize = 3

while (True):

    if (keyboard.is_pressed('8')):
        battle_toggle = True
        #Update the party names in the dictionary

    while (battle_toggle or (party_alive() and enemies_alive())):
        #Run battle method
        time.sleep(10)
        temp_battle_method()
        hp_stat_printer("Party HP", party_hp)
        hp_stat_printer("Enemy HP", enemy_hp)
        battle_status()
        #num += 1
        #print(num)
        #party()

        if (keyboard.is_pressed('9')):
            battle_toggle = False