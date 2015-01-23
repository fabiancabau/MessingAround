
from random import randrange
import json
import Utilities
from Inventory import Inventory


class Character():

    unique_id = None
    nickname = ''
    hp = 100
    money = 0
    buffs = list()
    debuffs = list()
    dead = False
    incapacitated = False
    turns_dead = 0
    speed = 0
    current_place_id = ''
    inventory = None
    atk = 0
    dfn = 0
    atk_speed = 0


    def __init__(self, unique_id, nickname, current_place_id):
        self.unique_id = Utilities._generate_unique_id()
        self.nickname = nickname
        self.hp = 100
        self.money = 0
        self.buffs = list()
        self.debuffs = list()
        self.dead = False
        self.incapacitated = False
        self.turns_dead = 0
        self.speed = 0
        self.current_place_id = current_place_id
        self.inventory = Inventory()
        self.atk = 0
        self.dfn = 0
        self.atk_speed = 0


    def enter_shop(self, shop):
        shop.addCharacterInside(self)


    def equip_item(self, item):
        if self.inventory.primary_weapon is None:
            print 'Equipando item'
            print item.name
            self.inventory.primary_weapon = item
            item.onEquip(self)


    def unequip_item(self, position):
        if self.inventory.primary_weapon is not None:
            print 'Desequipando item'
            print self.inventory.primary_weapon.name
            item_removed = self.inventory.primary_weapon
            self.inventory.primary_weapon = None
            item_removed.onUnequip(self)


    def receive_damage(self, damage):

        final_dmg = damage - self.dfn
        self.hp -= final_dmg

        if self.hp > 0:
            return True
        else:
            return False


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
