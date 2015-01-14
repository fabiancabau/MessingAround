
from random import randrange
import json
from Character import Character


class Human(Character):

    def __init__(self, unique_id, nickname):
        Character.__init__(self, unique_id, nickname, 'NWBCTY')

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
