from typing import List
from api.data_model.price_model import Price
from mail_service.mail_manager import MailManager
import logging

class UserAccount():

    def __init__(
        self
        ,name :str
        ,mail : str
        ,skin_list : list):
        self.name = name
        self.mail = mail
        self.skin_list = skin_list
        self.mail_manager = MailManager()

    def update(self,name,mail,skin_list):
        if self.name == name:
            self.mail = mail
            self.skin_list = skin_list

    def notify(self,sales_data : List[Price]):
        skin_updated = []
        for price in sales_data:
            if price.skin_id in self.skin_list:
                skin_updated.append(price.skin_id)
        logging.info("User {} was notified of {} sales on the skins he wanted!".format(self.name,len(skin_updated)))
        logging.info("Skin list : {}".format(skin_updated))