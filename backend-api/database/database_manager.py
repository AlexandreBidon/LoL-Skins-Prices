from database import DataBase
import logging

class DataBaseManager(DataBase):

    def __init__(
        self
        ,host="0.0.0.0"
        ,database="lol_db"
        ,user="postgres"
        ,password="lol_admin"
        ):
        self.__init__(host=host,database=database,user=user,password=password)
    
    def add_champion(self, champion_id : int, name : str, title : str):
        """
        Adds a champion into the champions table
        
        Return
        -----
        Result : bool
        A bool to inform if the new champion was successfully added to the table
        """
        try:
            self.query(
                """INSERT INTO champions VALUES ({}, 'valeur 2', ...)""".format(champion_id,name,title))
            return True
        except Exception as e:
            print(e)
            return False

    def add_skin(self, champion_id : int, skin_id : int, skin_num :int, base_price : int):
        try:
            #First we check if the champion exist
            champion_result = self.query(
                """SELECT * FROM champions WHERE ChampionId={}""".format(champion_id))
            if len(champion_result) == 0:
                # Can't add a skin with no matching champion
                print("error : no matching champion found")
                return False
            return True
        except Exception as e:
            print(e)
            return False

    def update_price(self, skin_id : int, new_price : int):
        pass
