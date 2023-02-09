from database.database import DataBase
from database.database_manager import DataBaseManager
import datetime

test = DataBase()
manager = DataBaseManager()

test.list_tables()

print(test.query("SELECT * FROM champions"))

manager.add_skin(14,1,"skin test",3,1800)
#manager.delete_skin(1)
print(manager.skin_price_history(1))

