#Luckman21
"""
FINAL FANTASY VII AI Battles

Check out the README for more information
"""

ATB_MAX = 65535
LIMIT_MAX = 255

#Python Dict (Hashtable) to return the position (Top / Leader = 1, Middle = 2, Bottom = 3) of the Party Member based on their name
party_names = {
}

#Stat offsets from base stat address
stat_offset = {
    "STR":0,
    "DEX":1,
    "VIT":2,
    "MAG":3,
    "SPR":4,
    "LCK":5,
    "ATT":6,
    "DFN":8,
    "MAT":10,
    "MDF":12
}

#Python Dict (Hashtable) to return the number of down arrow presses to select the summon in the Summon menu.
summons = {
    "Choco/Mog":0,
    "Shiva":1,
    "Ifrit":2,
    "Ramuh":3,
    "Titan":4,
    "Odin":5,
    "Leviathan":6,
    "Bahamut":7,
    "Kujata":8,
    "Alexander":9,
    "Phoenix":10,
    "Neo Bahamut":11,
    "Hades":12,
    "Typhon":13,
    "Bahamut ZERO":14,
    "Knights of Round":15
}

#Python Dict (Hashtable) to return the number of down arrow presses to select the skill in the Enemy Skill menu.
eskill = {
    "Frog Song":0,
    "L4 Suicide":1,
    "Magic Hammer":2,
    "White Wind":3,
    "Big Guard":4,
    "Angel Whisper":5,
    "Dragon Force":6,
    "Death Force":7,
    "Flame Thrower":8,
    "Laser":9,
    "Matra Magic":10,
    "Bad Breath":11,
    "Beta":12,
    "Aqualung":13,
    "Trine":14,
    "Magic Breath":15,
    "????":16,
    "Goblin Punch":17,
    "Chocobuckle":18,
    "L5 Death":19,
    "Death Sentence":20,
    "Roulette":21,
    "Shadow Flare":22,
    "Pandora's Box":23
}

#Pythong Dict (Hashtable) to return the flag index for each status effect in the game.
status_effects = {
    "Dead":0,
    "NearDeath":1,
    "Sleep":2,
    "Poison":3,
    "Sadness":4,
    "Fury":5,
    "Confusion":6,
    "Silence":7,
    "Haste":8,
    "Slow":9,
    "Stop":10,
    "Frog":11,
    "Small":12,
    "SlowNumb":13,
    "Petrify":14,
    "Regen":15,
    "Barrier":16,
    "MBarrier":17,
    "Reflect":18,
    "Dual":19,
    "Shield":20,
    "DeathSentence":21,
    "Berserk":22,
    "Peerless":23,
    "Paralyze":24,
    "Darkness":25
}

DISABLE = ["Dead", "Sleep", "Stop", "Petrify", "Paralyze"]
CONTROL_LOSS = ["Confusion", "Berserk"]
DANGER =["NearDeath", "Poison", "SlowNumb", "Dual", "DeathSentence"]
BUFFS = ["Haste", "Regen", "Barrier", "MBarrier", "Reflect", "Shield", "Berserk", "Peerless"]
DEBUFFS = ["Sleep", "Poison", "Confusion", "Silence", "Slow", "Stop", "Frog", "Small", "SlowNumb", "Petrify", "Paralyze", "Darkness"]
MOOD = ["Sadness", "Fury", "Berserk"]

#For testing
#curr_summons = ["Neo Bahamut", "Phoenix", "Kujata", "Shiva", "Bahamut", "Choco/Mog", "Ramuh", "Titan", "Alexander"]
#curr_eskill = ["Frog Song", "L4 Suicide", "Magic Hammer", "Big Guard", "Flame Thrower", "Matra Magic", "Bad Breath", "Beta", "Aqualung", "Trine", "Death Sentence"]