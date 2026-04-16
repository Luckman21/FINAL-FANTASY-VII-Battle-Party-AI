#Luckman21

from memread import *

status_effects = {
    0:"Dead",
    1:"NearDeath",
    2:"Sleep",
    3:"Poison",
    4:"Sadness",
    5:"Fury",
    6:"Confusion",
    7:"Silence",
    8:"Haste",
    9:"Slow",
    10:"Stop",
    11:"Frog",
    12:"Small",
    13:"SlowNumb",
    14:"Petrify",
    15:"Regen",
    16:"Barrier",
    17:"MBarrier",
    18:"Reflect",
    19:"Dual",
    20:"Shield",
    21:"DeathSentence",
    22:"Berserk",
    23:"Peerless",
    24:"Paralyze",
    25:"Darkness"
}

DISABLE = ["Dead", "Sleep", "Stop", "Petrify", "Paralyze"]
CONTROL_LOSS = ["Confusion", "Berserk"]
DANGER =["NearDeath", "Poison", "SlowNumb", "Dual", "DeathSentence"]
BUFFS = ["Haste", "Regen", "Barrier", "MBarrier", "Reflect", "Shield", "Berserk", "Peerless"]
DEBUFFS = ["Sleep", "Poison", "Confusion", "Silence", "Slow", "Stop", "Frog", "Small", "SlowNumb", "Petrify", "Paralyze", "Darkness"]
MOOD = ["Sadness", "Fury", "Berserk"]

def char_alive(id):
    """
    Checks whether a party member is alive.
    """
    if (read_hp(party_hp[id][0]) > 0):
        return True
    return False

def party_alive():
    """
    Checks whether there is at least one party member alive in battle.
    """
    for i in range (0, len(party_hp)):
        if char_alive(i) == True:
            return True
    return False

def enemy_alive(id):
    """
    Checks whether a specified enemy is alive.
    """
    if (read_hp(enemy_hp[id][0]) > 0):
        return True
    return False

def enemies_alive():
    """
    Checks whether there is at least one enemy alive in battle.
    """
    for i in range (0, len(enemy_hp)):
        if enemy_alive(i) == True:
            return True
        return False

def status_to_vector(status_address):
    """
    Converts the status integer value into an array of vectors to show which statuses are in effect.
    """
    return [(status_address >> i) & 1 for i in range (32)]

def active_status(status_addresss):
    """
    Maps status vector to status names to represent which statues are applied and currently active.

    e.g.
    {
        ...
        "Sleep":1,
        "Poison":0,
        "Sadness":1,
        ...
    }
    """
    vec = status_to_vector(status_address=status_addresss)

    return {
        name: vec[i] for i, name in status_effects.items()
    }