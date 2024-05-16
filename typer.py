#Luckman21
'''
FINAL FANTASY VII AI Battles

Check out the README for more information
'''
import pyautogui
import time
from menu_elements import *

def select():
    """
    Defines the "OK" button press.
    """
    pyautogui.keyDown('i')
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

def Summon(summon): #TODO: Select a summon based on the current equipped list.
    """
    Defines the macro for Summon.  Currently selects the topmost Summon in the menu.
    """
    dArrow()
    dArrow()
    select()

    #Scroll down until we reach the desired Summon
    for i in range (0, summon):
        dArrow()
    
    Attack()

def Item(item): #TODO: Update the item array so that items are listed in the correct indexes.
    """
    Defines the macro for Item.  Selects an item based on the item's current specified index position.
    """
    dArrow()
    Summon(item)

def eSkill(skill): #TODO: Create a list to select the correct position.
    """
    Defines the macro for E.Skill.  Selects an Enemy Skill based on the specified index position.
    """
    rArrow()
    select()
    
    #The Enemy Skill menu is broken into 2 columns.  This logic will determine if the skill is found on the left or right column.
    if (skill % 2 == 1):
        rArrow()

    #Scroll down until we reach the desired skill
    for i in range (0, int(skill / 2)):
        dArrow()
    
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