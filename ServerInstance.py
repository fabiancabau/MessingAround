from Shops.GeneralStore import GeneralStore
from Characters.Human import Human
from Cities.NewbieWorld import NewbieWorld


class ServerInstance():

    server_cities = list()
    server_characters = list()

    def __init__(self):
        self.server_cities = list([NewbieWorld(), NewbieWorld(), NewbieWorld()])

    
    def add_character(self, character):
        self.server_characters.append(character)
        return True

    def list_server_cities(self):
        for city in self.server_cities:
            print city.to_JSON()


