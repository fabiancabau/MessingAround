from datetime import datetime
from Shops.GeneralStore import GeneralStore
from Characters.Human import Human
from Cities.NewbieWorld import NewbieWorld


class ServerInstance():


    date_started = 0
    server_cities = list()
    server_characters = list()

    def __init__(self):
        self.server_cities = list([NewbieWorld(), NewbieWorld(), NewbieWorld()])
        self.date_started = datetime.utcnow()

    
    def add_character(self, character):
        self.server_characters.append(character)
        return True

    def list_server_cities(self, json=False):

        city_list = list()

        for city in self.server_cities:
            if json:
                city_list.append(city.to_JSON())
            else:
                city_list.append(city)

        return city_list

    def list_server_characters(self, json=False):

        char_list = list()

        for char in self.server_characters:
            if json:
                char_list.append(char.to_JSON())
            else:
                char_list.append(char)

        return char_list




