
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



    