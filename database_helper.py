import sqlite3


class DB_Helper:
    def __init__(self) -> None:
        self.con = sqlite3.connect('file_database.db',check_same_thread=False)
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
    
    def fetch_name(self, unique_id):
        '''This function extracts the name of the file and send it back to the user'''
        query = f"SELECT File_Name FROM files WHERE File_Unique_ID = '{unique_id}'"
        res = self.cur.execute(query)
        return res.fetchall()[0][0]
        

    def add_to_history(self, data):
        ''' Inserts data into the history table. '''
        pass




if __name__ == '__main__':
    db_helper = DB_Helper()
    # record = db_helper.fetch_name('20240209-XyZ67AbCde')
    # print(record)