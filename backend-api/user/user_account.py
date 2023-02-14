from typing import List
from api.data_model.price_model import Price
from mail_service.mail_manager import MailManager
from database.database import DataBase
import logging
import os
import re
from email_validator import validate_email, EmailNotValidError

logger = logging.getLogger('python_logs')

class UserAccount():

    def __init__(
        self
        ,name :str
        ,email : str
        ,skin_list : list):
        try:
            # validate and get info
            v = validate_email(email)
            # replace with normalized form
            email = v["email"] 
            self.name = name
            self.email = email
            self.skin_list = skin_list
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            raise(e)

    def __check_email(self, email):   
        regex = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""" 
        if(re.search(regex,email)):   
            return True
        else:   
            return False  
        
    def update(self,name,email,skin_list):
        if self.name == name:
            if self.__check_email(email):
                self.email = email
                self.skin_list = skin_list
            else:
                raise(SyntaxError("Email not valid"))

    def add_skins(self, new_skins : list):
        for skin_id in new_skins:
            if skin_id not in self.skin_list:
                self.skin_list.append(skin_id)

    def notify(self,sales_data : List[Price]):
        skin_updated = []
        for price in sales_data:
            if price.skin_id in self.skin_list:
                skin_updated.append(price.skin_id)
        logger.info("User {} could be interested in {} sales on the skins he wanted!".format(self.name,len(skin_updated)))
        logger.info("Skin list : {}".format(skin_updated))
        skin_info = []
        db_access = DataBase(
            host = os.getenv("POSTGRES_HOST"),
            database = os.getenv("POSTGRES_DB"),
            user = os.getenv("POSTGRES_USER"),
            password = os.getenv("POSTGRES_PASSWORD")
        )
        for skin_id in skin_updated:
            try:
                champion_id = db_access.query("""SELECT ChampionId FROM Champions_Skins WHERE SkinId={} LIMIT 1""".format(skin_id))[0][0]
                champion_name = db_access.query("""SELECT Name FROM champions WHERE ChampionId={} LIMIT 1""".format(champion_id))[0][0]
                skin_name =  db_access.query("""SELECT Name FROM Skins WHERE SkinId={} LIMIT 1""".format(skin_id))[0][0]
                skin_num =  db_access.query("""SELECT Num FROM Skins WHERE SkinId={} LIMIT 1""".format(skin_id))[0][0]
                price_list = db_access.query("""SELECT * FROM SkinPrices WHERE SkinId={} ORDER BY ChangedOn DESC LIMIT 2""".format(skin_id))
                current_price = price_list[0][1]
                last_price = price_list[1][1]
                if current_price < last_price:
                    skin_info.append(
                        {
                            "champion_id" : champion_id,
                            "champion_name" : champion_name,
                            "skin_num" : skin_num,
                            "skin_name" : skin_name,
                            "current_price" : current_price,
                            "last_price" : last_price
                        }
                    )
            except:
                logger.warning("Couldn't find the skin with id {}".format(skin_id))
        if len(skin_info) >0:
            logger.info("User {} will be notified of {} sales on the skins he wants!".format(self.name,len(skin_info)))
            logger.info("Skin list : {}".format(skin_info))
            MailManager().send_sale_mail(sales_data=skin_info, to_mail= self.email)
        else:
            logger.info("No skins were in sales for user {}".format(self.name))