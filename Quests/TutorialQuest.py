import json
from BaseQuest import BaseQuest
from QuestMap import QuestMap
from Enemies.Enemies import Rat

class DenOfEvil(QuestMap):

    def __init__(self):
        QuestMap.__init__(self, 'DenOfEvil', 'Den Of Evil', 'den_of_evil.html')




class TutorialQuest(BaseQuest):

    maps = {}
    current_map = 0

    def __init__(self):
        BaseQuest.__init__(self, 'q1', 'TutorialQuest')
        self.current_map = 0

        enemies = list()
        enemies.append(Rat())

        self.maps = {
            '0': QuestMap('DenOfEvil', 'Den Of Evil', 'den_of_evil.html', enemies)
        }



    def get_current_map(self):
        return self.maps.get('0')

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



