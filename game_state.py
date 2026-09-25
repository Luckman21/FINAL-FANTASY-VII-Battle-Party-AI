#Luckman21
from dataclasses import dataclass, field
from typing import Optional
import memread as m
from game_info import *

@dataclass
class BattleUnit:
    """
    Defines the object structure for a battle unit.  A battle unit is any field unit
    (character or enemy).  For dynamic values such as curr_hp or atb, the values stored
    at these attributes are the memory addresses for this unit, not the values themselves.
    Values can be read by using their respective "read" functions.  I''ve chosen
    to structure it this way since Python is pass-by-value and not pass-by-pointer.
    """
    name: str           # FIND
    id: int             # FIND
    party_index: int
    level: int          # FIND
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
        if (m.read_hp(self.curr_hp) == 0 and (m.read_status(self.status) & (1 << status_effects.get("Dead")))):
            return False
        return True
    
    def unit_ready(self) -> bool:
        """
        Determines if a unit can act (ATB bar is full).
        """
        if (self.unit_alive() == False):
            return False
        
        # Cannot act despite full ATB since unit is disabled
        unit_status = m.read_status(self.status)
        for effect in DISABLE:
            if (unit_status & (1 << status_effects.get(effect))):
                return False

        if (m.read_atb(self.atb) == ATB_MAX):
            return True
        return False

    def unit_prepare(self) -> int:
        """
        Returns an int value based on the ATB gauge, ranging from 0 to ATB_MAX.

        If ready, return ATB_MAX.  If hindered by a status effect that makes them unable to act
        (DISABLE), return -1.  Otherwise, return the current ATB value.
        """

        if (self.unit_ready()):
            return ATB_MAX

        # Cannot act despite full ATB since unit is disabled, return -1
        unit_status = m.read_status(self.status)
        for effect in DISABLE:
            if (unit_status & (1 << status_effects.get(effect))):
                return -1

        else:
            return m.read_atb(self.atb)

# Deprecated
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
    #stats: Stats
    stats = int
    limit: int
    limit_level: int    # FIND
    mood: int           # part of stats, determine how to implement
    exp: int            # FIND

    #TODO: Add materia and equipment data once located

    def limit_available(self) -> bool:
        if (m.read_limit(self.limit) == LIMIT_MAX):
            return True
        return False

@dataclass
class Party:
    members: list[Character]

    @property
    def get_party_size(self) -> int:
        """
        Returns the number of current party members.
        """
        return len(self.members)

    def get_party_members(self) -> list[Character]:
        """
        Returns the array of party members.
        """
        return self.members

    def get_member(self, id:int) -> Character:
        """
        Get a Character object of one specific party member by their index.
        """
        return self.members[id]

    def is_party_alive(self) -> bool:
        """
        Checks whether there is at least one party member alive in battle.
        """
        return any(member.unit_alive() for member in self.members)

@dataclass
class Monsters:
    members: list[BattleUnit]

    def get_num_enemies(self) -> int:
        """
        Returns the number of enemies on the field.
        """
        return len(self.members)

    def get_enemies(self) -> list[BattleUnit]:
        """
        Returns an array of enemies.
        """
        return self.members

    def get_enemy(self, id:int) -> BattleUnit:
        """
        Get a specific field monster based on their position index.
        """
        return self.members[id]

    def is_enemy_alive(self) -> bool:
        """
        Checks whether at least one enemy is alive.
        """
        return any(enemy.unit_alive() for enemy in self.members)

@dataclass
class BattleState:
    party: Party
    enemies: Monsters

    def units(self) -> list[BattleUnit]:
        """
        Create a list of all units in a battle.
        """
        return self.party.get_party_members() + self.enemies.get_enemies()

    def party_alive(self) -> bool:
        return self.party.is_party_alive()

    def enemies_alive(self) -> bool:
        return self.enemies.is_enemy_alive()

    def get_atb_order(self) -> dict[int, list[BattleUnit]]:
        """
        Returns a snapshot of the current ATB gauges and orders units by how
        far their ATB has progressed.
        """
        order = {}

        for unit in self.units():
            if (unit.unit_prepare() == -1):
                continue
            elif (unit.unit_prepare() not in order):
                order[unit.unit_prepare()] = [unit]
            else:
                order[unit.unit_prepare()].append(unit)

        return order

# BATTLE UNIT DEFINITIONS
p1 = Character(
    name = "CHAR_1",
    id = 0,
    party_index = 1,
    level = 1,
    curr_hp = m.p1_hp,
    hp_total = m.p1_hp_max,
    curr_mp = m.p1_mp,
    mp_total = m.p1_mp_max,
    status = m.p1_status,
    atb = m.p1_atb,
    stats = m.p1_stat_add,
    limit = m.p1_limit,
    limit_level = 1,
    mood = 0,
    exp = 1
)

p2 = Character(
    name = "CHAR_2",
    id = 2,
    party_index = 2,
    level = 2,
    curr_hp = m.p2_hp,
    hp_total = m.p2_hp_max,
    curr_mp = m.p2_mp,
    mp_total = m.p2_mp_max,
    status = m.p2_status,
    atb = m.p2_atb,
    stats = m.p2_stat_add,
    limit = m.p2_limit,
    limit_level = 1,
    mood = 0,
    exp = 1
)

p3 = Character(
    name = "CHAR_3",
    id = 3,
    party_index = 3,
    level = 1,
    curr_hp = m.p3_hp,
    hp_total = m.p3_hp_max,
    curr_mp = m.p3_mp,
    mp_total = m.p3_mp_max,
    status = m.p3_status,
    atb = m.p3_atb,
    stats = m.p3_stat_add,
    limit = m.p3_limit,
    limit_level = 1,
    mood = 0,
    exp = 1
)

e1 = BattleUnit(
    name = "MONSTER_1",
    id = 0,
    party_index = 1,
    level = 0,
    curr_hp = m.e1_hp,
    hp_total = m.e1_hp_max,
    curr_mp = m.e1_mp,
    mp_total = m.e1_mp_max,
    status = m.e1_status,
    atb = m.e1_atb
)

e2 = BattleUnit(
    name = "MONSTER_2",
    id = 0,
    party_index = 2,
    level = 0,
    curr_hp = m.e2_hp,
    hp_total = m.e2_hp_max,
    curr_mp = m.e2_mp,
    mp_total = m.e2_mp_max,
    status = m.e2_status,
    atb = m.e2_atb
)

e3 = BattleUnit(
    name = "MONSTER_3",
    id = 0,
    party_index = 3,
    level = 0,
    curr_hp = m.e3_hp,
    hp_total = m.e3_hp_max,
    curr_mp = m.e3_mp,
    mp_total = m.e3_mp_max,
    status = m.e3_status,
    atb = m.e3_atb
)

e4 = BattleUnit(
    name = "MONSTER_4",
    id = 0,
    party_index = 4,
    level = 0,
    curr_hp = m.e4_hp,
    hp_total = m.e4_hp_max,
    curr_mp = m.e4_mp,
    mp_total = m.e4_mp_max,
    status = m.e4_status,
    atb = m.e4_atb
)

e5 = BattleUnit(
    name = "MONSTER_5",
    id = 0,
    party_index = 5,
    level = 0,
    curr_hp = m.e5_hp,
    hp_total = m.e5_hp_max,
    curr_mp = m.e5_mp,
    mp_total = m.e5_mp_max,
    status = m.e5_status,
    atb = m.e5_atb
)

e6 = BattleUnit(
    name = "MONSTER_6",
    id = 0,
    party_index = 6,
    level = 0,
    curr_hp = m.e6_hp,
    hp_total = m.e6_hp_max,
    curr_mp = m.e6_mp,
    mp_total = m.e6_mp_max,
    status = m.e6_status,
    atb = m.e6_atb
)