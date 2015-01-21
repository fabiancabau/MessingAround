import json


class BaseItem():

    name = ''
    icon = ''

    damage = 0
    cooldown = 0


    def __init__(self, name, icon):
        self.name = name
        self.icon = icon


    def onEquip(self, character):
        return True


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

