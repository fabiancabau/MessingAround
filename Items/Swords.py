from BaseItem import BaseItem
from Constants import *


class StarterSword(BaseItem):
    
    stat_atk = 2
    stat_def = 0
    stat_atk_speed = ATK_SPEED_NORMAL

    def __init__(self):
        BaseItem.__init__(self, 'Starter Sword', 'newsword.png')
        
    def onEquip(self, character):
        character.atk = character.atk + self.stat_atk
        print 'Item equiped'
        print self.name
        print 'Equiped on'
        print character.nickname
        print character.atk


    def onUnequip(self, character):
        character.atk = character.atk - self.stat_atk


class FireSword(BaseItem):

    stat_atk = 10
    stat_def = 0
    stat_atk_speed = ATK_SPEED_NORMAL

    def __init__(self):
        BaseItem.__init__(self, 'Fire Sword', 'firesword.gif')

    def onEquip(self, character):
        character.atk = character.atk + self.stat_atk
        print 'Item equiped'
        print self.name
        print 'Equiped on'
        print character.nickname
        print character.atk


    def onUnequip(self, character):
        character.atk = character.atk - self.stat_atk
        
        




