from user.user_account import UserAccount
from typing import List
from api.data_model.price_model import Price

class UserAlert():
    """
    User subscribe to this class to be alerted when a skin is in sale
    """

    def __init__(self):
        self.subscribers = []

    def subscribe(self, user : UserAccount):
        self.subscribers.append(user)
    
    def notify(self, sales_data : List[Price]):
        for user in self.subscribers:
            user.notify(sales_data)
        
    def reset(self):
        self.subscribers = []