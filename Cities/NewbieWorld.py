from Cities.BaseCity import BaseCity
from Shops.GeneralStore import GeneralStore



class NewbieWorld(BaseCity):
    shop_list = [GeneralStore()]
    def __init__(self):
        BaseCity.__init__(self, 'NWBCTY', 'Newbie City')


    def list_all_shops(self):
        for shop in self.shop_list:
            print shop.shop_name
