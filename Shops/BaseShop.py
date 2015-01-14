from Base.BasePlace import BasePlace


class BaseShop(BasePlace):

    shop_name = ''
    shop_owner_name = ''
    shop_item_list = list()
    shop_welcome_text = ''
    shop_options = list(['Buy', 'Sell', 'Quit'])

    def __init__(self, name, owner_name, item_list, welcome_text):
        BasePlace.__init__(self)
        self.shop_name = name
        self.shop_owner_name = owner_name
        self.shop_item_list = item_list
        self.shop_welcome_text = welcome_text

    def buy(self):
        message = "Item list: \n"
        message += "Item ID: Name - Price --- Quantity Available\n"

        for key, item in enumerate(self.shop_item_list):
            message += "{0}: {1} - {2} Gold --- {3}\n".format(key, item.get('name'), item.get('price'), item.get('qty'))

        return message


