from fastapi import FastAPI, HTTPException
import logging
from typing import List

from api.lol_skin_manager import LoLSkinManager

from api.data_model.champion_model import ChampionModel
from api.data_model.skin_model import SkinModel
from api.data_model.user_model import UserModel
from api.data_model.price_model import Price

from user.user_alert import UserAlert
from user.user_account import UserAccount

logger = logging.getLogger('python_logs')

class Server():

    def __init__(self):
        self.app = FastAPI()
        self.skin_manager = LoLSkinManager()
        self.user_alert = UserAlert()

        @self.app.get("/")
        async def get():
            return "Welcome to the LoL Skin Price API!"

        ### CHAMPIONS ###

        @self.app.get("/champions/all")
        async def show_all_champions():
            logger.info("Listing all champions")
            try :
                return self.skin_manager.list_all_champions()
            except:
                return HTTPException(status_code=404, detail="Couldn't list all champions")

        @self.app.get("/champions/champion_id={championID}")
        async def show_champion(championID : int):
            logger.info("Listing champion with id : {}".format(championID))
            try:
                return self.skin_manager.show_champion(champion_id=championID)
            except:
                return HTTPException(status_code=404, detail="Couldn't find this champion")

        @self.app.post("/champions")
        async def create_champion(champion : ChampionModel):
            result = self.skin_manager.add_champion(champion=champion)
            return({"success":result})

        @self.app.delete("/champions/champion_id={championID}")
        async def delete_champion(championID : int):
            result = self.skin_manager.delete_champion(championId=championID)
            return({"success":result})
        
        ### SKINS ###

        @self.app.post("/skins")
        async def create_skin(skin : SkinModel):
            result = self.skin_manager.add_skin(skin=skin)
            return({"success":result})

        @self.app.get("/skins/all")
        async def show_all_skins():
            logger.info("Listing all skins")
            try :
                return self.skin_manager.list_all_skins()
            except:
                return HTTPException(status_code=404, detail="Couldn't list all skins")


        @self.app.get("/skins/champion_id={championID}") #TODO
        async def show_champion_skins(championID):
            logger.info("Listing all skins from champion {}".format(championID))
            return
        
        ### SKINS PRICES ###

        @self.app.post("/prices")
        async def update_price(price_list : List[Price]):
            logger.info("Updating skins prices")
            updated_skin_list = []
            for price in price_list:
                if self.skin_manager.update_price(skin_id=price.skin_id,new_price=price.new_price):
                    updated_skin_list.append(price)
            self.user_alert.notify(updated_skin_list)
            return({"skins_prices_updated" : [price.skin_id for price in updated_skin_list]})

        @self.app.get("/prices/history/skin_id={skinID}")
        async def price_history(skinID):
            logger.info("Listing price history for skin id {}".format(skinID))
            try:
                return self.skin_manager.skin_price_history(skin_id= skinID)
            except:
                return HTTPException(status_code=404, detail= "Couldn't find price history for skin id {}".format(skinID)) 

        @self.app.get("/prices/current/skin_id={skinID}")
        async def current_price(skinID):
            logger.info("SHowing current price for skin id {}".format(skinID))
            try:
                return self.skin_manager.current_price(skin_id= skinID)
            except:
                return HTTPException(status_code=404, detail= "Couldn't find current price for skin id {}".format(skinID))

        ### USERS ###

        @self.app.post("/users")
        async def create_user(user : UserModel):
            logger.info("Creating new user with name {}".format(user.name))
            account = UserAccount(
                name = user.name,
                mail= user.mail,
                skin_list= user.skin_list
            )
            self.user_alert.subscribe(account)
            return({"success":True})

        ### MANAGEMENT ###

        @self.app.get("/management/reset")
        async def reset():
            self.user_alert.reset()
            result = self.skin_manager.reset()
            return({"success":result})