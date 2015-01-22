

class BaseQuest():

    unique_id = ''
    name = ''
    characters = list()


    def __init__(self, unique_id, name):
        self.unique_id = unique_id
        self.name = name

