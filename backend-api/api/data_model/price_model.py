from pydantic import BaseModel


class Price(BaseModel):
    skin_id : int
    new_price : int

