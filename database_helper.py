import sqlite3


class DB_Helper:
    def __init__(self) -> None:
        self.con = sqlite3.connect('file_database.db')
        self.cur = self.con.cursor()