from random import randrange
import json
import Utilities
from Items.BaseItem import BaseItem


class Inventory():

    max_backpack_capacity = 0
    backpack = list()
    armor = None
    legs = None
    helmet = None
    primary_weapon = None
    secondary_weapon = None
    gloves = None
    boots = None



    def __init__(self):
        self.max_backpack_capacity = 6
        self.backpack = list()
        self.armor = None
        self.legs = None
        self.helmet = None
        self.primary_weapon = None
        self.secondary_weapon = None
        self.gloves = None
        self.boots = None

    def get_backpack_items(self, json=False):
        item_list =  list()

        for item in self.backpack:
            if isinstance(item, BaseItem):
                if json:
                    item_list.append(item.to_JSON())
                else:
                    item_list.append(item)

        return item_list

    def add_item_backpack(self, item):
        self.backpack.append(item)

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
