from pydantic import BaseModel


class SkinModel(BaseModel):
    champion_id : int
    skin_id : int
    name : str
    skin_num :int
    base_price : int