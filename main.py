#Luckman21
"""
FINAL FANTASY VII AI Battles

Check out the README for more information
"""

import os
import threading
import keyboard
import time
from queue import Queue
import game_state as g
from random import randint
from typer import *

battle_toggle = False
atb_q = Queue(maxsize=3)    # Queue to keep track of turn order. Anyone in the queue is ready to initiate
                            # an action.  First character is popped from the queue and has their actions executed

class KillSwitch(threading.Thread):
    #Initialize the thread by overwriting the init method
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name #Defines the thread name
        self.thread_ID = thread_ID #Defines the thread ID

    #Overwrite the run method to define the code being run when started
    def run(self):
        while (keyboard.is_pressed('esc') == False):
            continue
        #Run shutdown sequence
        print("--------Shutdown sequence initiated-------")
        #Halt keyboard presses
        print("- Keyboard input halted")
        #Save current learning model
        print("- Learning model updated")
        #quit()
        os._exit(1)

class ATB_observer(threading.Thread):
    """
    An observer thread that updates the ready ATB queue in real time so turn order
    is preserved.
    """
    def __init__(self, thread_name:str, thread_ID:int, atb_q:Queue, battle:g.BattleState):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        self.thread_name = thread_name
        self.thread_ID = thread_ID
        self.atb_q = atb_q
        self.battle = battle

    def run(self):
        while not self.stop_event.is_set():
            team = self.battle.party.get_party_members()

            for player in team:
                if (player.unit_ready() == True and atb_q.__contains__(player) == False):
                    atb_q.put(player)
                    

def battle_init():
    """
    Populates the battle functions based on whether units are active.  Inactive
    units (not present on the field) are determined by a max hp = 0.  Only add
    active units to the current battle.
    """

    characters = [g.p1, g.p2, g.p3]
    monsters = [g.e1, g.e2, g.e3, g.e4, g.e5, g.e6]
    party_members = []
    monster_team = []

    for hero in characters:
        if hero.unit_alive() == True:
            party_members.append(hero)

    for enemy in monsters:
        if enemy.unit_alive() == True:
            monster_team.append(enemy)

    # PARTY DEFINITION
    party = g.Party(
        members = party_members
    )

    # ENEMIES DEFINITION
    enemies = g.Monsters(
        members = monster_team
    )

    # BATTLE STATE DEFINITION
    battle = g.BattleState(
        party = party,
        enemies = enemies
    )

    return battle

def battle_main(battle:g.BattleState):
    """
    Main battle control method.  Sets the flow of control for battle.

    Until battle is finished, keep checking for actionable characters, pass the current
    battle state to AI to determine the next move, execute it and repeat the process.
    """
    while (battle.party_alive() and battle.enemies_alive()):

        # Spinlock for ATB queue to have an actionable party member
        # the outer loop check added here ensures we don't get stuck forever
        while (atb_q.empty() and battle.party_alive() and battle.enemies_alive()):
            continue

        player = atb_q.get()
        # Pass player object to AI along with entire battle state
        # Execute command for player

#Create thread and initialize it
alive = KillSwitch("FFVII Battle AI", 1000)    
alive.start()

while (True):

    if (keyboard.is_pressed('8')):  # Just kept for testing purposes, remove keyboard input battle toggle later
        battle_toggle = True
        #Update the party names in the dictionary

        # Wait and detect battle start
        # Pre-battle setup (spawn ATB thread)
        battle_obj = battle_init()

        # Main battle function
        battle_main(battle_obj)
        # Post-battle cleanup (kill ATB thread)    

        if (keyboard.is_pressed('9')):
            battle_toggle = False