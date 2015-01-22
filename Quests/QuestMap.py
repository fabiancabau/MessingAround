import json

class QuestMap():

    unique_id = ''
    name = ''
    path = 'quest.html'
    enemies = list()


    def __init__(self, unique_id, name, path):
        self.unique_id = unique_id
        self.name = name
        self.path = path


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
