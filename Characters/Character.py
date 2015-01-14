
from random import randrange
import json
import Util

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

    def __init__(self, unique_id, nickname, current_place_id):
        self.unique_id = Util._generate_unique_id()
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


    def enter_shop(self, shop):
        shop.addCharacterInside(self)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
