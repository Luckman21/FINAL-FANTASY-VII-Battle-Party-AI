#Luckman21
'''
FINAL FANTASY VII AI Battles

Check out the README for more information
'''
import keyboard
import pyautogui
import time
from random import randint

def Attack():
    pyautogui.keyDown('i')
    time.sleep(0.1)
    pyautogui.keyUp('i')
    time.sleep(0.1)
    pyautogui.keyDown('i')
    time.sleep(0.1)
    pyautogui.keyUp('i')
    time.sleep(0.1)

def Magic():
    pyautogui.keyDown('s')
    time.sleep(0.1)
    pyautogui.keyUp('s')
    time.sleep(0.1)
    Attack()

def Summon():
    pyautogui.keyDown('s')
    time.sleep(0.1)
    pyautogui.keyUp('s')
    time.sleep(0.1)
    Magic()

def Item():
    pyautogui.keyDown('s')
    time.sleep(0.1)
    pyautogui.keyUp('s')
    time.sleep(0.1)
    Summon()

def eSkill():
    pyautogui.keyDown('d')
    time.sleep(0.1)
    pyautogui.keyUp('d')
    time.sleep(0.1)
    Attack()

#Sleep for 3 seconds
time.sleep(3)

while(keyboard.is_pressed('q') == False):

    choice = randint(0,100)
    time.sleep(3)

    print(choice)
    
    if ((choice >= 0) and (choice <= 50)):
        Attack()
        print('Attack')

    elif ((choice >= 51) and (choice <= 80)):
        Magic()
        print('Magic')

    elif ((choice >= 81) and (choice <= 90)):
        Summon()
        print('Summon')

    elif ((choice >= 91) and (choice <= 93)):
        Item()
        print('Item')

    elif ((choice >= 94) and (choice <= 100)):
        eSkill()
        print('Enemy Skill')

#Test code
"""
pyautogui.write('Hello World')

txt = 'The quick brown fox jumps over the lazy dog'

for i in txt:
    pyautogui.write(i)
    time.sleep(0.00005)
"""