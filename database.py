import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def execute(self, query, params=None):
        self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        last_id = self.cursor.lastrowid
        self.conn.commit()
        self.conn.close()
        return last_id

    def fetchall(self, query, params):
        self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        rows = self.cursor.fetchall()

        self.conn.close()
        return rows
