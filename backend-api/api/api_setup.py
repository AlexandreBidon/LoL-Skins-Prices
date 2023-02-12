from requests.exceptions import HTTPError
from fastapi import FastAPI
import logging

from api.lol_skin_manager import LoLSkinManager

from api.data_model.champion_model import ChampionModel
from api.data_model.skin_model import SkinModel
from api.data_model.user_model import UserModel

from api.user_alert import UserAlert
from api.user_account import UserAccount


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
            logging.info("Listing all champions")
            return self.skin_manager.list_all_champions()

        @self.app.get("/champions/{championID}")
        async def show_champion(championID : int):
            logging.info("Listing champion with id : {}".format(championID))
            return self.skin_manager.show_champion(champion_id=championID)

        @self.app.post("/champions")
        async def create_champion(champion : ChampionModel):
            result = self.skin_manager.add_champion(champion=champion)
            return({"success":result})

        @self.app.delete("/champions/{championID}")
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
            logging.info("Listing all skins")
            return self.skin_manager.list_all_skins()

        @self.app.get("/skins/champion={}")
        async def show_champion_skins(championID):
            logging.info("Listing all skins from champion {}".format(championID))
            return
        
        ### USERS ###

        @self.app.post("/users")
        async def create_user(user : UserModel):
            logging.info("Creating new user with name {}".format(user.name))
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