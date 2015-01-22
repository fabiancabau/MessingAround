import json

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
