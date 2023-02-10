from requests.exceptions import HTTPError
from fastapi import FastAPI
import logging

from api.lol_skin_manager import LoLSkinManager
from api.data_model.champion_model import ChampionModel
from api.data_model.skin_model import SkinModel

class Server():

    def __init__(self):
        self.app = FastAPI()
        self.skin_manager = LoLSkinManager()

        @self.app.get("/")
        async def get():
            return "Welcome to the LoL Skin Price API!"

        ### CHAMPIONS ###

        @self.app.get("/champions/all")
        async def show_all_champions():
            logging.info("Listing all champions")
            return self.skin_manager.list_all_champions()

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

        ### RESET

        @self.app.get("/management/reset")
        async def reset():
            result = self.skin_manager.reset()
            return({"success":result})