from BaseEnemy import BaseEnemy
import json

class Rat(BaseEnemy):

    def __init__(self):
        BaseEnemy.__init__(self, 'rat123', 'Rat', 100, 0, 50, 2, 0, 1, None)