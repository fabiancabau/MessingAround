from datetime import datetime
from Shops.GeneralStore import GeneralStore
from Characters.Human import Human
from Cities.NewbieWorld import NewbieWorld
from Utilities import *

class QuestInstance():

    def __init__(self, quest):
        self.room_id = _generate_unique_id()
        self.quest_characters = list()
        self.quest = quest
        self.date_started = datetime.utcnow()


    def add_character(self, character):
        self.quest_characters.append(character)
        return True


    def list_quest_characters(self, json=False):

        char_list = list()

        for char in self.quest_characters:
            if json:
                char_list.append(char.to_JSON())
            else:
                char_list.append(char)

        return char_list




