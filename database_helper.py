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
    
    def fetch_record(self, unique_id):
        '''This function extracts the records from the files database and forms a path using it.'''
        query = f"SELECT * FROM files WHERE File_Unique_ID = '{unique_id}';"
        res = self.cur.execute(query)
        return res.fetchall()
        

    def add_to_history(self, data):
        ''' Inserts data into the history table. '''
        pass




if __name__ == '__main__':
    db_helper = DB_Helper()
    # record = db_helper.fetch_record('20240209-XyZ67AbCde')
    # print(record)