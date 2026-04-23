#Luckman21
from typer import *

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