import random
import time
import string
import sqlite3

class UtilityTool:
    def __init__(self):
        self.exhibit_code = {'dinosaur':'EXH-A', 'paintings':'EXH-B', 'history':'EXH-C'}

    def generate_unique_id(self):
        '''This functions generates a unique id for the records that are inserted inside the database'''
        timestamp = time.strftime("%Y%m%d")
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        unique_id = f"{timestamp}-{random_string}"
        return unique_id

    def get_tag_id(self, lvl3):
        '''This function returns the tag id of a specific record'''
        conn = sqlite3.connect('museum_database.db', check_same_thread=False)
        cur = conn.cursor()
        
        code = self.exhibit_code[lvl3]

        query = "SELECT COUNT(*) FROM files WHERE lvl3 = ?;"
        res = cur.execute(query, (lvl3,))
        
        num = res.fetchone()[0] + 1

        conn.close()

        return f"{code}-{num:03d}"






if __name__ == '__main__':
    util = UtilityTool()
    # print(util.generate_unique_id())
    util.get_tag_id("paintings")