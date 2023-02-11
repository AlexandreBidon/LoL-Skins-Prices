

class user_alert():
    """
    User subscribe to this class to be alerted when a skin is in sale
    """

    def __init__(self):
        self.subscribers = []

    def subscribe(self, user):
        self.subscribers.append(user)
    
    def notify(self, sales_data):
        for user in self.subscribers:
            user.update(sales_data)