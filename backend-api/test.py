from database.database import DataBase
from database.database_manager import DataBaseManager
import datetime

test = DataBase()
manager = DataBaseManager()

test.list_tables()

print(test.query("SELECT * FROM champions"))

manager.add_champion(15,"Teemo","Le boss")
manager.add_champion(14,"Teema","Le boss")

print(test.query("SELECT * FROM champions"))

