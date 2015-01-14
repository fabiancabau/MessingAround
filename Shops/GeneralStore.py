from BaseShop import BaseShop
import Util

class GeneralStore(BaseShop):

    def __init__(self):
        item_list = [{'name': 'Potion', 'price': 100, 'qty': 10},{'name': 'Sword', 'price': 50, 'qty': 1}]
        BaseShop.__init__(self, 'General Store', 'Duff', item_list, 'Welcome to Duff General Store!\n')


    def __unicode__(self):
        print ('Welcome to {0}! My name is {1} and I am here to help you, adventurer!\n'
               'What can I help you with?\n').format(self.shop_name,  self.shop_owner_name)

        for option in self.shop_options:
            print '{}\n'.format(option)