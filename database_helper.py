import sqlite3


class DB_Helper:
    def __init__(self) -> None:
        self.con = sqlite3.connect('file_database.db')
        self.cur = self.con.cursor()


    def add_file_record(self, tuple):
        ''' Inserts new data into the files table. '''
        query = "INSERT INTO files VALUES(?, ?, ?, ?)"
        self.cur.execute(query, tuple)
        self.con.commit()
        return True
    

    def add_to_history(self, data):
        ''' Inserts data into the history table. '''
        pass
