
from random import randrange
from Character import Character


class Human(Character):

    def __init__(self, unique_id, nickname):
        Character.__init__(self, unique_id, nickname, 'NWBCTY')
