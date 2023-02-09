from database.database import DataBase
import logging
import datetime

class DataBaseManager(DataBase):

    def __init__(
        self
        ,host="0.0.0.0"
        ,database="lol_db"
        ,user="postgres"
        ,password="lol_admin"
        ):
        super().__init__(host=host,database=database,user=user,password=password)
    
    def add_champion(self, champion_id : int, name : str, title : str):
        """
        Adds a champion into the champions table
        
        Return
        -----
        Result : bool
        A bool to inform if the new champion was successfully added to the table
        """
        try:
            self.execute(
                """INSERT INTO champions VALUES ({}, '{}', '{}')""".format(champion_id,name,title))
            return True
        except Exception as e:
            print(e)
            return False

    def delete_champion(self, champion_id):
        try:
            self.execute("""DELETE FROM champions WHERE ChampionId={}""".format(champion_id))
        except Exception as e:
            print(e)

    def add_skin(self, champion_id : int, skin_id : int, name : str, skin_num :int, base_price : int):
        try:
            #First we check if the champion exist
            champion_result = self.query(
                """SELECT * FROM champions WHERE ChampionId={}""".format(champion_id))
            if len(champion_result) == 0:
                # Can't add a skin with no matching champion
                print("error : no matching champion found")
                return False
            #The champions exists so we can add the skin
            self.execute(
                """INSERT INTO Skins VALUES ({}, '{}', {})""".format(skin_id, name, skin_num))
            self.execute(
                """INSERT INTO Champions_Skins VALUES ({}, {})""".format(champion_id, skin_id))
            # Lastly we add the price
            self.execute(
                """INSERT INTO SkinPrices VALUES ({}, {}, '{}')""".format(skin_id, base_price, datetime.date.today()))
            return True
        except Exception as e:
            print(e)
            return False

    def delete_skin(self, skin_id :int):
        try:
            self.execute("""DELETE FROM Champions_Skins WHERE SkinId={}""".format(skin_id))
            self.execute("""DELETE FROM SkinPrices WHERE SkinId={}""".format(skin_id))
            self.execute("""DELETE FROM Skins WHERE SkinId={}""".format(skin_id))
        except Exception as e:
            print(e)

    def update_price(self, skin_id : int, new_price : int):
        try:
            self.execute(
                    """INSERT INTO SkinPrices VALUES ({}, {}, {})""".format(skin_id, new_price, datetime.date.today()))
        except Exception as e:
            print(e)
            return False
    
    def skin_price_history(self, skin_id : int):
        try:
            result = self.query(
                        """SELECT * FROM SkinPrices WHERE SkinId={}""".format(skin_id))
            return result
        except Exception as e:
            print(e)
            return False
