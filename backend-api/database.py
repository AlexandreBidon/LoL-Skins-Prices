import psycopg2


conn = psycopg2.connect(
    host="0.0.0.0",
    database="lol_db",
    user="postgres",
    password="lol_admin")

cursor = conn.cursor()
        
cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""")
for table in cursor.fetchall():
    print(table)

cursor.execute("""SELECT * FROM champions""")
champions = cursor.fetchall()
print(champions)

cursor.close()