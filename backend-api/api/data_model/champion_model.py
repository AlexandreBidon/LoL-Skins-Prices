from pydantic import BaseModel


class ChampionModel(BaseModel):
    champion_id: int
    name : str
    title : str