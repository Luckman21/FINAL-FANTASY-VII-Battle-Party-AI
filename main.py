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

def testModule():
    
    pHP = HP()
    enemyHP = eHP()

    print("_" * 20)

    for i in pHP:
        if ((i[0] != 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], round(i[0] * 100 / i[1]),"%")
        elif ((i[0] == 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], "0 %")

    print("-" * 20)

    for i in enemyHP:
        if ((i[0] != 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], round(i[0] * 100 / i[1]),"%")
        elif ((i[0] == 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], "0 %")

    print("=" * 15)

    if (((pHP[0][0] + pHP[1][0] + pHP[2][0]) != 0) & ((enemyHP[0][0] + enemyHP[1][0] + enemyHP[2][0] + enemyHP[3][0] + enemyHP[4][0] + enemyHP[5][0]) != 0)):
        
        if ((pHP[0][0] * 100 / pHP[0][1] <= 25) | (pHP[1][0] * 100 / pHP[1][1] <= 25) | (pHP[2][0] * 100 / pHP[2][1] <= 25)):
            print("Item")
            Item(2)
        
        else:
            move = randint(0,9)
            
            if (move <= 3):
                print("Attack")
                Attack()
            
            elif (move == 4):
                skill = randint(0, len(curr_eskill)-1)
                print("Enemy Skill: "+ curr_eskill[skill])
                eSkill(eskill.get(curr_eskill[skill]))
            
            elif (move == 5):
                sum = randint(0, len(curr_summons)-1)
                print("Summon: "+ curr_summons[sum])
                Summon(int(summons.get(curr_summons[sum])))
            
            else:
                print("Magic")
                Magic()

#Create thread and initialize it
alive = KillSwitch("FFVII Battle AI", 1000)    
alive.start()

while (True):

    if (keyboard.is_pressed('8')):
        battle_toggle = True

    while (battle_toggle):
        #Run battle method
        testModule()
        time.sleep(10)
        #num += 1
        #print(num)

        if (keyboard.is_pressed('9')):
            battle_toggle = False