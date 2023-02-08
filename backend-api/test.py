from database.database import DataBase
import datetime

test = DataBase()

test.list_tables()

print(test.query("SELECT * FROM champions"))

print(test.query("SELECT * FROM champions WHERE ChampionId=266"))

print(datetime.date.today())