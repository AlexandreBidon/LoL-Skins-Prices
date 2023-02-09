from database.database_manager import DataBaseManager
from api.data_model.champion_model import ChampionModel
from api.data_model.skin_model import SkinModel

import logging

class LoLSkinManager():


    def __init__(self):
        self.__db_manager = DataBaseManager()

    def list_all_skins(self):
        return self.__db_manager.skin_list()
    
    def add_champion(self, champion : ChampionModel):
        result = self.__db_manager.add_champion(
            champion_id=champion.champion_id,
            name=champion.name,
            title=champion.title
        )
        return(result)
    
    def add_skin(self, skin : SkinModel):
        result = self.__db_manager.add_skin(
            champion_id=skin.champion_id,
            skin_id=skin.skin_id,
            name=skin.name,
            skin_num=skin.skin_num,
            base_price=skin.base_price
        )
        return(result)