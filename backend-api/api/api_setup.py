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

        @self.app.get("/skin/all")
        async def show_all_skins():
            logging.info("Listing all skins")
            return self.skin_manager.list_all_skins()

        @self.app.get("/skin/champion={}")
        async def show_champion_skins(championID):
            logging.info("Listing all skins from champion {}".format(championID))
            return

        @self.app.post("/champion")
        async def create_champion(champion : ChampionModel):
            logging.info("Creating the following champion : {}".format(champion))
            result = self.skin_manager.add_champion(champion=champion)
            if result:
                logging.info("Champion successfully created!")
            else:
                logging.info("Couldn't create champion")
            return({"success":result})

        @self.app.post("/skin")
        async def create_skin(skin : SkinModel):
            logging.info("Creating the following skin : {}".format(skin))
            result = self.skin_manager.add_skin(skin=skin)
            if result:
                logging.info("Skin successfully created!")
            else:
                logging.info("Couldn't create skin")
            return({"success":result})