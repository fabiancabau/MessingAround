from Characters.Character import Character
import json
import Util

class BasePlace:
    unique_place_id = ''
    characters_inside = list()

    def __init__(self):
        self.unique_place_id = Util._generate_unique_id

    def addCharacterInside(self, character):
        if isinstance(character, Character):
            self.characters_inside.append(character)
            return True

    def getCharactersInside(self):
        if self.characters_inside:
            for character in self.characters_inside:
                return character.to_JSON()


    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)



