import psycopg2

class DataBase():

    def __init__(
        self
        ,host="0.0.0.0"
        ,database="lol_db"
        ,user="postgres"
        ,password="lol_admin"
        ):

        self.conn = psycopg2.connect(
            host="0.0.0.0",
            database="lol_db",
            user="postgres",
            password="lol_admin")

        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()

    def list_tables(self):
        self.cur.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'""")
        for table in self.cur.fetchall():
            print(table)
