#Luckman21
'''
This file reads from memory addresses to access game values like health and stats.
'''

import pymem
import time

game = pymem.Pymem("ff7_en.exe")

#Read Party HP Values
p1_hp = game.base_address + 0x005AB108
p1_hp_max = p1_hp + 0x00000004
p2_hp = game.base_address + 0x005AB170
p2_hp_max = p2_hp + 0x00000004
p3_hp = game.base_address + 0x005AB1D8
p3_hp_max = p3_hp + 0x00000004

#Read Party MP Values

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

#Store Party HP to an array for iteration
party_hp = [[p1_hp, p1_hp_max],[p2_hp, p2_hp_max],[p3_hp, p3_hp_max]]

for i in range (0, len(party_hp)):
    party_hp[i] = [game.read_int(party_hp[i][0]), game.read_int(party_hp[i][1])]

#Store Party MP to an array for iteration

#store Enemy HP to an array for iteration
enemy_hp = [[e1_hp, e1_hp_max],[e2_hp, e2_hp_max],[e3_hp, e3_hp_max],[e4_hp, e4_hp_max],[e5_hp, e5_hp_max],[e6_hp, e6_hp_max]]

for i in range (0, len(enemy_hp)):
    enemy_hp[i] = [game.read_int(enemy_hp[i][0]), game.read_int(enemy_hp[i][1])]

while True:
    #p1_hp = game.base_address + 0x005AB108
    #party_hp[0][0] = game.read_int(p1_hp)

    for i in enemy_hp:
        if ((i[0] != 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], round(i[0] * 100 / i[1]),"%")
        elif ((i[0] == 0) & (i[1] > 0)):
            print(i[0] , "|" , i[1], "0 %")
    break
    #print("_" * 20)
    #time.sleep(3)