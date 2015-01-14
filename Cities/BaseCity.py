import json

class BaseCity():

    city_id = ''
    city_name = ''
    characters_list = list()

    def __init__(self, city_id, city_name):
        self.city_id = city_id
        self.city_name = city_name

    def list_all_characters(self):
        if self.characters_list:
            for character in self.characters_list:
                print character

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
