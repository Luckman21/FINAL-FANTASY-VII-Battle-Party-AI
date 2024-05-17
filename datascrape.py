#Luckman21
"""
FINAL FANTASY VII AI Battles

Check out the README for more information
"""

#Useful resource for this part https://youtu.be/PY_N1XdFp4w?si=VLq-9ABWQJEfXxbV

import pymem
import PIL
import pyautogui
import pytesseract
import pyscreenshot
import time
from menu_elements import *

game = pymem.Pymem("ff7_en.exe")

#Creates the Queue for characters to take control of the controls
atb_queue = []
atb_queue_maxsize = 3
atb_state = True

def printer(text): #TODO: Depricate
    """
    Prints out information fed to the function in a box format.
    """

    name = ''

    print('.___________.')
    for i in text:
        if (i != '\n'):
            name += i

        elif (name == '\n'):
            name = ''

        elif (name == '_'):
            name = ' '

        elif (name == ''):
            continue
        
        else:
            print('| ' + name + (12 - (len(name) + 2))*' ' + '|')
            name = ''

    print('˙‾‾‾‾‾‾‾‾‾‾‾˙')

def party(): #TODO: Find values in memory that hold these values and read them
    """
    Returns a string containing party member names.  Takes 2 screenshots (in case the name gets "greyed out"
    by UI), compares which string is longer (theoretically the longer string should be the one with all 3 names)
    and returns the output.  This method makes reading names more consistient and accurate.
    """

    myconfig = r"--psm 4 --oem 3"

    #Party Names
    #Left, Up, Right, Down
    pyautogui.keyDown('|')
    name_window1 = pyscreenshot.grab(bbox=(200, 1150, 600, 1450))
    pyautogui.keyUp('|')
    inverted_image1 = PIL.ImageOps.invert(name_window1)
    #inverted_image1.save('test.png')
    text1 = pytesseract.image_to_string(inverted_image1, config=myconfig)

    pyautogui.keyDown('|')
    name_window2 = pyscreenshot.grab(bbox=(200, 1150, 600, 1450))
    pyautogui.keyUp('|')
    inverted_image2 = PIL.ImageOps.invert(name_window2)
    #inverted_image2.save('test2.png')
    text2 = pytesseract.image_to_string(inverted_image2, config=myconfig)

    if (len(text1) >= len(text2)):
        names = text1
    else:
        names = text2

    return names

def HP():
    """
    Returns an array of current and max HP values.
    """
    #Read Party HP Values
    p1_hp = game.base_address + 0x005AB108
    p1_hp_max = p1_hp + 0x00000004
    p2_hp = game.base_address + 0x005AB170
    p2_hp_max = p2_hp + 0x00000004
    p3_hp = game.base_address + 0x005AB1D8
    p3_hp_max = p3_hp + 0x00000004

    #Store Party HP to an array for iteration
    party_hp = [[p1_hp, p1_hp_max],[p2_hp, p2_hp_max],[p3_hp, p3_hp_max]]

    for i in range (0, len(party_hp)):
        party_hp[i] = [game.read_int(party_hp[i][0]), game.read_int(party_hp[i][1])]

    return party_hp
    
def MP(): #TODO: Find values in memory that hold these values and read them
    """
    Returns a string of MP values.
    """

    myconfig = r"--psm 11 -c tessedit_char_whitelist=0123456789"

    #Left, Up, Right, Down
    name_window = pyscreenshot.grab(bbox=(1520, 1150, 1719, 1435))
    values = pytesseract.image_to_string(name_window, config=myconfig)
    #name_window.show() #Show screenshot being taken

    return values

def eHP():
    """
    Returns an array of current and max enemy HP values.
    """
    #Read Enemy HP Values
    e1_hp = game.base_address + 0x005AB2A8
    e1_hp_max = e1_hp + 0x00000004
    e2_hp = game.base_address + 0x005AB310
    e2_hp_max = e2_hp + 0x00000004
    e3_hp = game.base_address + 0x005AB378
    e3_hp_max = e3_hp + 0x00000004
    e4_hp = game.base_address + 0x005AB3E0
    e4_hp_max = e4_hp + 0x00000004
    e5_hp = game.base_address + 0x005AB448
    e5_hp_max = e5_hp + 0x00000004
    e6_hp = game.base_address + 0x005AB4B0
    e6_hp_max = e6_hp + 0x00000004
    
    #store Enemy HP to an array for iteration
    enemy_hp = [[e1_hp, e1_hp_max],[e2_hp, e2_hp_max],[e3_hp, e3_hp_max],[e4_hp, e4_hp_max],[e5_hp, e5_hp_max],[e6_hp, e6_hp_max]]

    for i in range (0, len(enemy_hp)):
        enemy_hp[i] = [game.read_int(enemy_hp[i][0]), game.read_int(enemy_hp[i][1])]

    return enemy_hp

def eMP(): #TODO: Implement
    return "Not implmented"

def ATB():
    """
    Manages the ATB Queue to queue party member actions.
    """
    while True:

        time.sleep(0.1)

        if (len(atb_queue) == atb_queue_maxsize):
            continue

        elif (len(atb_queue) == 0):
            if (atb1()):
                atb_queue.append(party_names.get(1))
            elif (atb2()):
                atb_queue.append(party_names.get(2))
            elif (atb3()):
                atb_queue.append(party_names.get(3))

        elif (len(atb_queue) < atb_queue_maxsize):
            
            #If Member 1 is not in the ATB Queue
            try:
                atb_queue.index(party_names.get(1))
            except ValueError:
                if (atb1()):
                    atb_queue.append(party_names.get(1))

            #If Member 2 is not in the ATB Queue
            try:
                atb_queue.index(party_names.get(2))
            except ValueError:
                if (atb2()):
                    atb_queue.append(party_names.get(2))

            #If Member 3 is not in the ATB Queue
            try:
                atb_queue.index(party_names.get(3))
            except ValueError:
                if (atb3()):
                    atb_queue.append(party_names.get(3))

def atb1(): #TODO: Implement
    """
    Checks if Party Member 1 is ready to select an action.  Returns false otherwise.
    """
    return False

def atb2(): #TODO: Implement
    """
    Checks if Party Member 2 is ready to select an action.  Returns false otherwise.
    """
    return False

def atb3(): #TODO: Implement
    """
    Checks if Party Member 3 is ready to select an action.  Returns false otherwise.
    """
    return False

#printer(party())
#printer(HP())
#printer(MP())