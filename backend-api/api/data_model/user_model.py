from pydantic import BaseModel
from typing import List


class UserModel(BaseModel):
    name: str
    mail : str
    skin_list : List[int]