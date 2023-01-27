from database import DataBase

class DataBaseManager(DataBase):

    def __init__(
        self
        ,host="0.0.0.0"
        ,database="lol_db"
        ,user="postgres"
        ,password="lol_admin"
        ):
        self.__init__(host=host,database=database,user=user,password=password)
    
    def add_champion(self, id : str, name : str, title : str):
        pass

    def add_skin(self, champion_id : int, skin_id : int, skin_num :int, base_price : int):
        pass

    def update_price(self, skin_id : int, new_price : int):
        pass
