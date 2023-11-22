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
    name_window.save('hp.png')
    pyautogui.keyUp('|')
    values = pytesseract.image_to_string(name_window, config=myconfig)
    #name_window.show()

    pixel = name_window.load()
    #print(pixel[100,100])

    values = hpCorrect(values)
    
    return values

def getHPstate(charNum):
    """
    Return the current HP state based on HP colour
        Red - 0 HP / KO'ed (returns 0)
        Yellow - Critical HP (below 25%) (returns 1)
        White - Healthy (returns 2 [default])
    """

    img = PIL.Image.open('hp.png')
    #crop_img = (0, 0, 420, 310) #Default HP image size
    max_colours = img.size[0] * img.size[1] #Max num of colours is num of pixels in the image

    if (charNum == 1):
        crop_img = (0, 16, 420, 72)

    elif (charNum == 2):
        crop_img = (0, 122, 420, 178)

    elif (charNum == 3):
        crop_img = (0, 228, 420, 284)

    img = img.crop(crop_img) 

    for i in (img.getcolors(max_colours)):
        if i[1] == (189, 0, 0): #Red health bar = KOed
            return 0
        elif i[1] == (230, 230, 0): #Yellow health bar = Critical Health
            return 1
    return 2

def getHPvalues(nums, dens):
    """
    Parses through text blob to seperate numerator and denominator values.
    Returns an array containing 2 internal arrays; numerators and denominators.
    (Not fully implemented)
    """
    hpArray = [nums, dens]
    return hpArray

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
    nums = []
    dens = []
    newValues = ""

    #Splice string to distinguish numerator and denomintator values from a single string
    for i in range (0, num_of_chars):
        startLine = endLine + 1
        endLine = startLine + values[startLine:].find('\n')
        slash = startLine + values[startLine:].find('/')

        num = values[startLine:slash]
        den = values[slash+1:endLine]

    #print text as compiler sees it (includes \n, \t, etc.)
    #print(repr(values))
        num = int(num)
        den = int(den)

    #Check for any impossible cases
        #Current HP > Max HP
        if (num > den):
            
            #KO'ed status when HP > 0
            if (getHPstate(i+1) == 0): #Set HP to 0 if HP bar is red
                num = 0

            #Yellow health but HP is above yellow threshold
            elif (getHPstate(i+1) == 1): #Set HP to 25% of max health fo HP bar is yellow
                num = int(den * 0.25)
            else:
                #Reduce HP until current HP < Max HP
                '''
                    This solution is not ideal, there may be times where the HP read and the correction made are innacurate
                    For example:
                        Actual current HP: 2564 / 3561
                        Read current HP: 3564 / 3561

                        Innacuracy difference: 3564 - 2564 = 1000
                        Current solution difference: 3564 - 3561 = 3
                        
                        Only 3 points in total will be subtracted from the total HP, the AI may be incorrectly rewarded for
                        increasing it's health state when not performing an action that supports healing.  There are more 
                        instances like this, but this current solution will prevent impossible cases to the best of it's ability.
                '''
                while (num > den):
                    if ((num - den) >= 1000):
                        num -= 1000
                    elif ((num - den) >= 100):
                        num -= 100
                    elif ((num - den) >= 10):
                        num -= 10
                    elif ((num - den >= 1)):
                        num -= 1

        #If HP is above threasholds when actually critial / KO'ed
        elif (getHPstate(i+1) != 2):
            if (getHPstate(i+1) == 0):
                num = 0
            elif (getHPstate(i+1) == 1):
                if (num > den * 0.25):
                    num = int(den * 0.25)
        
        #Healthy but HP is below the healthy threshold
        elif (getHPstate(i+1) == 2):
            if (num <= (den * 0.25)):
                num = int(den * 0.5)

        nums.append(str(num))
        dens.append(str(den))
                
    #Copy correction changes by manipulating values string indexes
    for i in range (0, num_of_chars):
        newValues += nums[i] + "/" + dens[i] + "\n"

    #Return the corrected values as a string
    return newValues
    
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

printer(party())
printer(HP())
printer(MP())