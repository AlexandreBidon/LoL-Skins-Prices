from database.database import DataBase
import logging
import datetime

logger = logging.getLogger('python_logs')

class DataBaseManager(DataBase):
    # TODO : raise HTTP Error (404 or others) when it's an error
    
    def __init__(
        self
        ,host="0.0.0.0"
        ,database="lol_db"
        ,user="postgres"
        ,password="lol_admin"
        ):
        super().__init__(host=host,database=database,user=user,password=password)
    
    ### CHAMPIONS ###

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
            logger.error(e)
            return False

    def delete_champion(self, champion_id):
        try:
            logger.info("Deleting skins associated with champion {}".format(champion_id))
            related_skins = self.query("""SELECT SkinID FROM Champions_Skins WHERE ChampionId={}""".format(champion_id))
            logger.info(related_skins)
            if len(related_skins)>0:
                self.delete_skin_tuple(related_skins[0])
            self.execute("""DELETE FROM Champions_Skins WHERE ChampionId={}""".format(champion_id))
            self.execute("""DELETE FROM champions WHERE ChampionId={}""".format(champion_id))
            return True
        except Exception as e:
            logger.error(e)
            return False

    def champion_list(self):
        try:
            result = self.query("""SELECT * FROM champions""")
            return(result)
        except Exception as e:
            logger.error(e)
    
    def show_champion(self, champion_id):
        try:
            result = self.query("""SELECT * FROM champions WHERE ChampionId={}""".format(champion_id))
            return(result)
        except Exception as e:
            logger.error(e)
            return({'champion not found'})

    ### SKINS ###

    def add_skin(self, champion_id : int, skin_id : int, name : str, skin_num :int, base_price : int):
        try:
            #First we check if the champion exist
            champion_result = self.query(
                """SELECT * FROM champions WHERE ChampionId={}""".format(champion_id))
            if len(champion_result) == 0:
                # Can't add a skin with no matching champion
                logging.error("error : no matching champion found")
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
            logger.error(e)
            return False

    def delete_skin_tuple(self, skin_id_tuple :tuple):
        try:
            for skin_id in skin_id_tuple:
                self.delete_skin(skin_id=skin_id)
        except Exception as e:
            logger.error(e)

    def delete_skin(self, skin_id :int):
        try:
            self.execute("""DELETE FROM Champions_Skins WHERE SkinId={}""".format(skin_id))
            self.execute("""DELETE FROM SkinPrices WHERE SkinId={}""".format(skin_id))
            self.execute("""DELETE FROM Skins WHERE SkinId={}""".format(skin_id))
        except Exception as e:
            logger.error(e)

    def skin_list(self):
        try:
            result = self.query("""SELECT * FROM Skins""")
            return(result)
        except Exception as e:
            logger.error(e)

    ### SKIN PRICE ###

    def update_price(self, skin_id : int, new_price : int):
        try:
            self.execute(
                    """INSERT INTO SkinPrices VALUES ({}, {}, '{}')""".format(skin_id, new_price, datetime.date.today()))
            return True
        except Exception as e:
            logger.error(e)
            return False
    
    def skin_price_history(self, skin_id : int):
        try:
            result = self.query(
                        """SELECT * FROM SkinPrices WHERE SkinId={} ORDER BY ChangedOn DESC""".format(skin_id))
            return result
        except Exception as e:
            logger.error(e)
            return False
    
    def current_price(self, skin_id : int):
        try:
            result = self.query(
                        """SELECT * FROM SkinPrices WHERE SkinId={} ORDER BY ChangedOn DESC""".format(skin_id))
            return result[0]
        except Exception as e:
            return False

    ### RESET DATABASE ###
    
    def reset_db(self):
        try:
            self.execute("""DELETE FROM SkinPrices""")
            self.execute("""DELETE FROM Champions_Skins""")
            self.execute("""DELETE FROM Skins""")
            self.execute("""DELETE FROM champions""")
            return True
        except Exception as e:
            logger.error(e)
            return False