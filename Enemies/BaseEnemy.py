import json
from random import randrange

class BaseEnemy():

    unique_id = ''
    name = ''
    hp = 0
    mana = 0
    exp = 0
    atk = 0
    dfn = 0
    atk_spd = 0


    def __init__(self, unique_id, name, hp, mana, exp, atk, dfn, atk_spd, drop_list):
        self.unique_id = unique_id
        self.name = name
        self.hp = hp
        self.mana = mana
        self.exp = exp
        self.atk = atk
        self.dfn = dfn
        self.atk_spd = atk_spd
        self.drop_list = drop_list


    def attack(self, characters):

        rand = 0
        damage = randrange(0, self.atk)

        if isinstance(characters, list):
            rand = randrange(0, len(characters))
            characters[rand].receive_damage(damage)

        else:
            characters.receive_damage(damage)


    def receive_damage(self, damage):

        final_dmg = damage - self.dfn
        self.hp -= final_dmg

        if self.hp > 0:
            return True
        else:
            return False


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


