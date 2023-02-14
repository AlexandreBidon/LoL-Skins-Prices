import logging
import os

from database.database_manager import DataBaseManager
from api.data_model.champion_model import ChampionModel
from api.data_model.skin_model import SkinModel


logger = logging.getLogger('python_logs')

class LoLSkinManager():


    def __init__(self):
        self.__db_manager = DataBaseManager(
            host = os.getenv("POSTGRES_HOST"),
            database = os.getenv("POSTGRES_DB"),
            user = os.getenv("POSTGRES_USER"),
            password = os.getenv("POSTGRES_PASSWORD")
        )

    ### CHAMPIONS ###

    def list_all_champions(self):
        result = self.__db_manager.champion_list()
        result_dict = []
        for champion in result:
            champion_dict = {
                "id" : champion[0],
                "name" : champion[1],
                "title" : champion[2] 
            }
            result_dict.append(champion_dict)
        return result_dict

    def show_champion(self, champion_id : int):
        champion = self.__db_manager.show_champion(champion_id= champion_id)[0]
        champion_dict = {
                "id" : champion[0],
                "name" : champion[1],
                "title" : champion[2] 
            }
        return champion_dict

    def add_champion(self, champion : ChampionModel):
        logging.info("Creating the following champion : {}".format(champion))
        result = self.__db_manager.add_champion(
            champion_id=champion.champion_id,
            name=champion.name,
            title=champion.title
        )
        if result:
            logging.info("Champion successfully created!")
        else:
            logging.error("Couldn't create champion")
        return(result)
    
    def delete_champion(self, championId : int):
        logging.info("Deleting the champion with id : {}".format(championId))
        result = self.__db_manager.delete_champion(champion_id=championId)
        if result:
            logging.info("Champion successfully deleted!")
        else:
            logging.error("Couldn't delete champion")
        return result

    ### SKINS ###

    def list_all_skins(self):
        result = self.__db_manager.skin_list()
        result_dict = []
        for skin in result:
            skin_dict = {
                "id" : skin[0],
                "name" : skin[1],
                "num" : skin[2] 
            }
            result_dict.append(skin_dict)
        return result_dict

    def add_skin(self, skin : SkinModel):
        logging.info("Creating the following skin : {}".format(skin))
        result = self.__db_manager.add_skin(
            champion_id=skin.champion_id,
            skin_id=skin.skin_id,
            name=skin.name,
            skin_num=skin.skin_num,
            base_price=skin.base_price
        )
        if result:
            logging.info("Skin successfully created!")
        else:
            logging.info("Couldn't create skin")
        return(result)
    
    def list_all_skins_web(self):
        skins_list = self.list_all_skins()
        for i in range(len(skins_list)):
            skins_list[i]["price"] = self.current_price(skins_list[i]["id"])["price"]
            result = self.__db_manager.query(
                """SELECT champions.Name FROM champions JOIN Champions_Skins USING(ChampionId) WHERE Champions_Skins.SkinId = {}""".format(skins_list[i]["id"]))
            skins_list[i]["imgPath"] = str(result[0][0]) + "_" + str(skins_list[i]["num"]) + ".jpg"
        return(skins_list)

    ### PRICES ###

    def update_price(self, skin_id : int, new_price : int):
        return self.__db_manager.update_price(skin_id=skin_id,new_price=new_price)

    def skin_price_history(self, skin_id : int):
        result = self.__db_manager.skin_price_history(skin_id=skin_id)
        result_dict = []
        for price in result:
            price_dict = {
                "skin_id" : price[0],
                "price" : price[1],
                "changed_on" : price[2] 
            }
            result_dict.append(price_dict)
        return result_dict
        
    def current_price(self, skin_id :int):
        price =  self.__db_manager.current_price(skin_id=skin_id)
        price_dict = {
                "skin_id" : price[0],
                "price" : price[1],
                "changed_on" : price[2] 
            }
        return price_dict

    ### RESET DB ###

    def reset(self):
        logging.info("Resetting the database")
        result = self.__db_manager.reset_db()
        if result:
            logging.info("Database successfully reset!")
        else:
            logging.info("Couldn't reset the database")
        return(result)