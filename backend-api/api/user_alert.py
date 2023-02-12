from api.user_account import UserAccount

class UserAlert():
    """
    User subscribe to this class to be alerted when a skin is in sale
    """

    def __init__(self):
        self.subscribers = []

    def subscribe(self, user : UserAccount):
        self.subscribers.append(user)
    
    def notify(self, sales_data):
        for user in self.subscribers:
            user.notify(sales_data)
        
    def reset(self):
        self.subscribers = []