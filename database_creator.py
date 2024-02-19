import sqlite3

conn = sqlite3.connect('museum.db')
cur = conn.cursor()

"Create the files table to hold data about files"
# query = '''
# CREATE TABLE IF NOT EXISTS files (
#     file_unique_id TEXT PRIMARY KEY,
#     file_name TEXT,
#     lvl1 TEXT,
#     lvl2 TEXT,
#     lvl3 TEXT,
#     tag_id TEXT UNIQUE
# );'''

"Create the users table to hold data about users"
# query='''
# CREATE TABLE IF NOT EXISTS users (
#     user_id TEXT PRIMARY KEY,
#     user_name TEXT
# );
# '''

"Create the request_history database for storing the history of the markers scanned"
# query = '''
# CREATE TABLE IF NOT EXISTS history (
#     user_id TEXT,
#     file_unique_id TEXT,
#     timestamp TEXT,
#     FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
#     FOREIGN KEY (file_unique_id) REFERENCES files(file_unique_id) ON DELETE CASCADE ON UPDATE CASCADE
# );'''

"Verify the creation of the tables"
query = "SELECT name FROM sqlite_master WHERE type='table';"
res = cur.execute(query)
print(res.fetchall())
# conn.commit()
