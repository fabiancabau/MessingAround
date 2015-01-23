from BaseEnemy import BaseEnemy
import json

class Rat(BaseEnemy):

    def __init__(self):
        BaseEnemy.__init__(self, 'rat123', 'Rat', 100, 0, 50, 2, 0, 1, None)


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)