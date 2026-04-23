#Luckman21
"""
FINAL FANTASY VII AI Battles

Check out the README for more information
"""
#TODO: Remove class when determined safe to do so, redundant
#Useful resource for this part https://youtu.be/PY_N1XdFp4w?si=VLq-9ABWQJEfXxbV

import pymem
#import PIL
import pyautogui
#import pytesseract
#import pyscreenshot
import time
from game_info import *

game = pymem.Pymem("ff7_en.exe")

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

def name_format(text):
    """
    Based on the printer function, formats text into seperate words / names by identifying newlines.
    """

    names = []
    name = ''

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
            names.append(name)
            name = ''
    
    return names

def party(): #TODO: Find values in memory that hold these values and read them
    """
    Returns a string containing party member names.  Reads names from game memory.
    """

    #Add party names to the hashtable
    #for i in range (0, len(names)):
        #party_names.update({i+1:names[i]})

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
    name_window = pyscreenshot.grab(bbox=(1520, 1180, 1719, 1470))
    values = pytesseract.image_to_string(name_window, config=myconfig)
    name_window.show() #Show screenshot being taken

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

def ATB(atb_queue, atb_queue_maxsize):
    """
    Manages the ATB Queue to queue party member actions.
    """
    while True:

        time.sleep(0.1)

        if (len(atb_queue) == atb_queue_maxsize):
            continue

        elif (len(atb_queue) == 0):
            if (atb_check(1)):
                atb_queue.append(party_names.get(1))
            elif (atb_check(2)):
                atb_queue.append(party_names.get(2))
            elif (atb_check(3)):
                atb_queue.append(party_names.get(3))

        elif (len(atb_queue) < atb_queue_maxsize):
            
            #If Member 1 is not in the ATB Queue
            try:
                atb_queue.index(party_names.get(1))
            except ValueError:
                if (atb_check(1)):
                    atb_queue.append(party_names.get(1))

            #If Member 2 is not in the ATB Queue
            try:
                atb_queue.index(party_names.get(2))
            except ValueError:
                if (atb_check(2)):
                    atb_queue.append(party_names.get(2))

            #If Member 3 is not in the ATB Queue
            try:
                atb_queue.index(party_names.get(3))
            except ValueError:
                if (atb_check(3)):
                    atb_queue.append(party_names.get(3))

def atb_check(position): #TODO: Implement
    """
    Checks if Party Member n is ready to select an action.  Returns false otherwise.
    n is represented by "position", where the character is in the Top / Leader, Middle or Bottom spot of the field.
    """

    if (position == 1):
        return True

    elif (position == 2):
        return True
    
    elif (position == 3):
        return True

    return False
    """
    Checks if Party Member 3 is ready to select an action.  Returns false otherwise.
    """
    return False

def atb_state():
    """
    Returns the current ATB State.  If TIME, return True.
    Otherwise (WAIT), return False.
    """

    myconfig = r"--psm 11 -c tessedit_char_whitelist=TIMEWA"

    #Left, Up, Right, Down
    name_window = pyscreenshot.grab(bbox=(1990, 1148, 2150, 1190))
    state = pytesseract.image_to_string(name_window, config=myconfig)
    #name_window.show() #Show screenshot being taken

    #print(state)

    if (state == "TIME"):
        return True
    
    else:
        return False

#printer(party())
#printer(HP())
#printer(MP())