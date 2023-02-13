# from database.database import DataBase

# db = DataBase()

# skin_id = "245001"
# champ_id =  db.query("""SELECT ChampionId FROM Champions_Skins WHERE SkinId={} LIMIT 1""".format(skin_id))[0][0]

# print(champ_id)

# result =  db.query("""SELECT Name FROM champions WHERE ChampionId={} LIMIT 1""".format(champ_id))[0][0]

# print(result)

# skin_num =  db.query("""SELECT Num FROM Skins WHERE SkinId={} LIMIT 1""".format(skin_id))[0][0]

# print(skin_num)

# last_2prices =  db.query("""SELECT * FROM SkinPrices WHERE SkinId={} ORDER BY ChangedOn DESC LIMIT 2""".format(skin_id))

# print(last_2prices)
# print(last_2prices[0][1])
# print(last_2prices[1][1])

test = '  test'

test_ = """atere atere"""

test3 = test + test_

print(test3)