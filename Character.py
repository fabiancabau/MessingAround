
from random import randrange
import json

class Character:

    unique_id = None
    nickname = ''
    hp = 0
    mana = 0
    str = 0
    dfn = 0
    atk = 0


    def __init__(self, unique_id, nickname, x, y):
        self.unique_id = unique_id
        self.nickname = nickname
        self.hp = 0
        self.mana = 0

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
