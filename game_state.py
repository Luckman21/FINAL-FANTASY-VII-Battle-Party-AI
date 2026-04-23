#Luckman21
from dataclasses import dataclass, field
from typing import Optional
from memread import *
from game_info import *

@dataclass
class BattleUnit:
    name: str
    party_index: int
    level: int
    curr_hp: int
    hp_total: int
    curr_mp: int
    mp_total: int
    status: int
    atb: int

    def unit_alive(self) -> bool:
        """
        Checks if the BattleUnit is alive.
        """
        if (self.curr_hp == 0 and (self.status & (1 << status_effects.get("Dead")))):
            return False
        return True
    
    def unit_ready(self) -> bool:
        """
        Determines if a unit can act (ATB bar is full).
        """
        if (self.unit_alive() == False):
            return False
        
        # Cannot act despite full ATB since unit is disabled
        for effect in DISABLE:
            if (self.status & (1 << status_effects.get(effect))):
                return False

        if (self.atb == ATB_MAX):
            return True
        return False

@dataclass
class Stats():
    # Character Stats
    exp: int
    str: int
    dex: int
    vit: int
    mag: int
    spr: int
    lck: int
    att: int
    dfn: int
    mat: int
    mdf: int

@dataclass
class Character(BattleUnit):
    stats: Stats
    limit: int
    limit_level: int
    mood: int

    #TODO: Add materia and equipment data once located

    def limit_available(self) -> bool:
        if (self.limit == LIMIT_MAX):
            return True
        return False

@dataclass
class Party():
    party_size: int
    p1: Character
    p2: Optional[Character] = None
    p3: Optional[Character] = None

    @property
    def members(self) -> list[Character]:
        """
        Returns a list containing the current party members.  Party can have 1-3 members depending on what point of the game the player is in.
        """
        return [member for member in (self.p1, self.p2, self.p3) if member is not None]

    def party_alive(self) -> bool:
        """
        Checks whether there is at least one party member alive in battle.
        """
        for member in self.members:
            if (member.unit_alive() == True):
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