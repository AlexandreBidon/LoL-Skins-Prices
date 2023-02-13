import psycopg2
import json
import logging

class DataBase():

    def __init__(
        self
        ,host
        ,database
        ,user
        ,password
        ):

        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password)

        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def execute(self, query):
        """
        Anticiper les erreurs
        """
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            self.cur.execute("ROLLBACK")
            self.conn.commit()
            raise e

    def close(self):
        self.cur.close()
        self.conn.close()

    def list_tables(self):
        self.cur.execute("""SELECT table_name FROM information_schema.tables
            WHERE table_schema = 'public'""")
        for table in self.cur.fetchall():
            print(table)
