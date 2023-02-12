from typing import List
from api.data_model.price_model import Price

class UserAccount():

    def __init__(
        self
        ,name :str
        ,mail : str
        ,skin_list : list):
        self.name = name
        self.mail = mail
        self.skin_list = skin_list
    
    def update(self,name,mail,skin_list):
        if self.name == name:
            self.mail = mail
            self.skin_list = skin_list

    def notify(self,sales_data : List[Price]):
        new_price = []
        for price in sales_data:
            if price.skin_id in self.skin_list:
                pass
