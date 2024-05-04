#Luckman21
'''
FINAL FANTASY VII AI Battles

Check out the README for more information
'''
import pyautogui
import time
from random import randint

def select():
    """
    Defines the "OK" button press.
    """
    pyautogui.keyDown('i')
    time.sleep(0.1)
    pyautogui.keyUp('i')
    time.sleep(0.1)

def uArrow():
    """
    Defines the keypress for Up (W).
    """
    pyautogui.keyDown('w')
    pyautogui.keyUp('w')
    time.sleep(0.1)

def dArrow():
    """
    Defines the keypress for Down (S).
    """
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')
    time.sleep(0.1)

def lArrow():
    """
    Defines the keypress for Left (A).
    """
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    time.sleep(0.1)

def rArrow():
    """
    Defines the keypress for Right (D).
    """
    pyautogui.keyDown('d')
    pyautogui.keyUp('d')
    time.sleep(0.1)

def Attack():
    """
    Defines the macro for Attack.  Attack consists of 2 OK presses.
    """
    select()
    select()

def Magic(): #TODO: Select different magic spells.  Spells will be ordered depending on settings & materia levels.
    """
    Defines the macro for Magic.  Currently selects the topmost magic spell in the menu.
    """
    dArrow()
    select()
    Attack()

def Summon(): #TODO: Select a summon based on the current equipped list.  Currently summons are organized in the menu by name, each has their own index position.
    """
    Defines the macro for Summon.  Currently selects the topmost Summon in the menu.
    """
    dArrow()
    Magic()

def Item(): #TODO: Select different items, give each an index ID to choose from the list.
    """
    Defines the macro for Item.  Currently selects the topmost Item in the menu.
    """
    dArrow()
    Summon()

def eSkill(): #TODO: Select different enemy skills, each is given a fixed index like summons.  Create a list to select the correct position.
    """
    Defines the macro for E.Skill.  Currently selects the topmost E.Skill in the menu.
    """
    rArrow()
    select()
    Attack()

#Sleep for 3 seconds
time.sleep(3)

'''
while(keyboard.is_pressed('q') == False):

    choice = randint(0,100)
    time.sleep(5)

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
'''
#Test code
"""
pyautogui.write('Hello World')

txt = 'The quick brown fox jumps over the lazy dog'

for i in txt:
    pyautogui.write(i)
    time.sleep(0.00005)
"""