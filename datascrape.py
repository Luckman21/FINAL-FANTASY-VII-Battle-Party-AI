#Luckman21
"""
FINAL FANTASY VII AI Battles

Check out the README for more information
"""

#Useful resource for this part https://youtu.be/PY_N1XdFp4w?si=VLq-9ABWQJEfXxbV

import PIL
import pyautogui
import pytesseract
import pyscreenshot
import time

def printer(text):
    """
    Prints out information fed to the function in a box format.
    """

    name = ''

    print('\n ___________________')
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
            print('| ' + name)
            name = ''
        
    print(' ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')

def party():
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
    Returns a string of HP values.
    """

    myconfig = r"--psm 4 -c tessedit_char_whitelist=0123456789/"

    #Left, Up, Right, Down
    pyautogui.keyDown('|')
    name_window = pyscreenshot.grab(bbox=(1080, 1140, 1500, 1450))
    pyautogui.keyUp('|')
    values = pytesseract.image_to_string(name_window, config=myconfig)
    #name_window.show()

    pixel = name_window.load()
    #print(pixel[100,100])

    values = hpCorrect(values)
    
    return values

def hpCorrect(values):
    """
    pytesseract's ability to accurately read the in game font is decent, but not perfect.
    Until the model is trained on this font, the current implementation of this method will
    serve to "correct" the mistakes as best as possible.  The values still may not be accurate,
    but the purpose is to prevent impossible cases (like current HP > total HP, KO'ed status 
    when HP > 0, etc.).

    Returns the corrected values.
    """

    #Count the number of party members in battle (min 1, max 3)
    
    num_of_chars = 1

    for i in values:
        if (i == '\n'):
            if (num_of_chars >= 3):
                continue
            else:
                num_of_chars += 1

    #///Correct values///

    #Index values for each HP line
    startLine = 0
    slash = 0
    endLine = -1

    #Numerator and Denominator for HP values
    num = ""
    den = ""

    #Splice string to distinguish numerator and denomintator values from a single string
    for i in range (0, num_of_chars):
        startLine = endLine + 1
        endLine = startLine + values[startLine:].find('\n')
        slash = startLine + values[startLine:].find('/')

        num = values[startLine:slash]
        den = values[slash+1:endLine]

    #print text as compiler sees it (includes \n, \t, etc.)
    #print(repr(values))

    #Check for any impossible cases
        #Current HP > Max HP
        #KO'ed status when HP > 0
        #Yellow health but HP is above yellow threshold
        #Alive but HP = 0

    #Copy correction changes by manipulating values string indexes

    #Return the corrected values as a string
    return values
    
def MP():
    """
    Returns a string of MP values.
    """

    myconfig = r"--psm 11 -c tessedit_char_whitelist=0123456789"

    #Left, Up, Right, Down
    name_window = pyscreenshot.grab(bbox=(1520, 1150, 1719, 1435))
    values = pytesseract.image_to_string(name_window, config=myconfig)
    #name_window.show() #Show screenshot being taken

    return values

time.sleep(2.5)

#printer(party())
#printer(HP())
#printer(MP())
HP()