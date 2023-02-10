import logging


from database.database_manager import DataBaseManager
from api.data_model.champion_model import ChampionModel
from api.data_model.skin_model import SkinModel



class LoLSkinManager():


    def __init__(self):
        self.__db_manager = DataBaseManager()

    ### CHAMPIONS ###

    def list_all_champions(self):
        return self.__db_manager.champion_list()

    def show_champion(self, champion_id : int):
        return self.__db_manager.show_champion(champion_id= champion_id)

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
        return self.__db_manager.skin_list()
    
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
    
    ### RESET DB ###

    def reset(self):
        logging.info("Resetting the database")
        result = self.__db_manager.reset_db()
        if result:
            logging.info("Database successfully reset!")
        else:
            logging.info("Couldn't reset the database")
        return(result)