import json
from Enemies.Enemies import Rat

class QuestMap():

    unique_id = ''
    name = ''
    path = 'quest.html'
    enemies = list()


    def __init__(self, unique_id, name, path, enemies):
        self.unique_id = unique_id
        self.name = name
        self.path = path
        self.enemies = enemies


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
