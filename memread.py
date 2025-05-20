#Luckman21
'''
This file reads from memory addresses to access game values like health and stats.

Memory Structure (memory is contiguous in this order):

--------------------------
Character MP (2 bytes)
Character MP MAX (2 bytes)
Character HP (4 bytes)
Character HP MAX (4 bytes)
--------------------------
'''

#TODO: Remove file from project

import pymem

game = pymem.Pymem("ff7_en.exe")

#Read Party HP Values (4 bytes)
p1_hp = game.base_address + 0x005AB108
p1_hp_max = p1_hp + 0x00000004
p2_hp = game.base_address + 0x005AB170
p2_hp_max = p2_hp + 0x00000004
p3_hp = game.base_address + 0x005AB1D8
p3_hp_max = p3_hp + 0x00000004

#Read Party MP Values (2 bytes)
p1_mp = game.base_address + 0x005AB104
p1_mp_max = p1_mp + 0x00000002
p2_mp = game.base_address + 0x005AB16C
p2_mp_max = p2_mp + 0x00000002
p3_mp = game.base_address + 0x005AB1D4
p3_mp_max = p3_mp + 0x00000002

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

#ead Enemy MP Values
e1_mp = game.base_address + 0x005AB2A4
e1_mp_max = e1_mp + 0x00000002
e2_mp = game.base_address + 0x005AB30C
e2_mp_max = e2_mp + 0x00000002
e3_mp = game.base_address + 0x005AB374
e3_mp_max = e3_mp + 0x00000002
e4_mp = game.base_address + 0x005AB3DC
e4_mp_max = e4_mp + 0x00000002
e5_mp = game.base_address + 0x005AB444
e5_mp_max = e5_mp + 0x00000002
e6_mp = game.base_address + 0x005AB4AC
e6_mp_max = e6_mp + 0x00000002

#Store Party HP to an array for iteration
party_hp = [[p1_hp, p1_hp_max],[p2_hp, p2_hp_max],[p3_hp, p3_hp_max]]

#for i in range (0, len(party_hp)):
#    party_hp[i] = [game.read_int(party_hp[i][0]), game.read_int(party_hp[i][1])]

#Store Party MP to an array for iteration
party_mp = [[p1_mp, p1_mp_max],[p2_mp, p2_mp_max],[p3_mp, p3_mp_max]]

#for i in range (0, len(party_mp)):
#    party_mp[i] = [game.read_short(party_mp[i][0]), game.read_short(party_mp[i][1])]

#store Enemy HP to an array for iteration
enemy_hp = [[e1_hp, e1_hp_max],[e2_hp, e2_hp_max],[e3_hp, e3_hp_max],[e4_hp, e4_hp_max],[e5_hp, e5_hp_max],[e6_hp, e6_hp_max]]

#for i in range (0, len(enemy_hp)):
#    enemy_hp[i] = [game.read_int(enemy_hp[i][0]), game.read_int(enemy_hp[i][1])]

#store Enemy MP to an array for iteration
enemy_mp = [[e1_mp, e1_mp_max],[e2_mp, e2_mp_max],[e3_mp, e3_mp_max],[e4_mp, e4_mp_max],[e5_mp, e5_mp_max],[e6_mp, e6_mp_max]]

#for i in range (0, len(enemy_mp)):
#    enemy_mp[i] = [game.read_short(enemy_mp[i][0]), game.read_short(enemy_mp[i][1])]

def char_alive(id):
    """
    Checks whether a party member is alive.
    """
    if (party_hp[id][0] > 0):
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
    if (enemy_hp[id][0] > 0):
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

'''
while True:
    #p1_hp = game.base_address + 0x005AB108
    #party_hp[0][0] = game.read_int(p1_hp)

    print("Party HP\n________________")
    for i in party_hp:
        if ((i[0] != 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], round(i[0] * 100 / i[1]),"%")
        elif ((i[0] == 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], "0 %")

    print("\n\nParty MP\n________________")
    for i in party_mp:
        if ((i[0] != 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], round(i[0] * 100 / i[1]),"%")
        elif ((i[0] == 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], "0 %")

    print("\n\nEnemy HP\n________________")
    for i in enemy_hp:
        if ((i[0] != 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], round(i[0] * 100 / i[1]),"%")
        elif ((i[0] == 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], "0 %")
    
    print("\n\nEnemy MP\n________________")
    for i in enemy_mp:
        if ((i[0] != 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], round(i[0] * 100 / i[1]),"%")
        elif ((i[0] == 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], "0 %")
    break
    #print("_" * 20)
    #time.sleep(3)
'''