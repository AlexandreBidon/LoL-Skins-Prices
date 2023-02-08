from database.database import DataBase


test = DataBase()

test.list_tables()

print(test.query("SELECT * FROM champions"))

print(test.query("SELECT * FROM champions WHERE ChampionId=266"))

result = test.query("SELECT * FROM champions WHERE ChampionId=300")
print(result)
print(len(result))