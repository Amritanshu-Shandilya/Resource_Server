import sqlite3

# conn = sqlite3.connect('museum.db')
# cur = conn.cursor()

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
# query = "SELECT name FROM sqlite_master WHERE type='table';"
# res = cur.execute(query)
# print(res.fetchall())
# conn.commit()

"Entering values inside files table"
# query = '''
# INSERT INTO files VALUES('20240209-A23bC87dE1','dandakosaurus','text','information','dianosaur','EXH-A-001'),
#                         ('20240209-Xyz456Pqrs','indosaurus','text','information','dianosaur','EXH-A-002'),
#                         ('20240209-Lmno789Abc','saurian_rellic_01','text','information','dianosaur','EXH-A-003'),
#                         ('20240209-DfgHij012K','thar_desert_ovum','text','information','dianosaur','EXH-A-004'),
#                         ('20240209-ZzxYyWwVvU','tharosaurus_indicus','text','information','dianosaur','EXH-A-005'),
#                         ('20240209-Klm876NopQ','hamsa_damyanti_rrv','text','information','paintings','EXH-B-001'),
#                         ('20240209-Jkl321XyZa','shakuntalam_rrv','text','information','paintings','EXH-B-002'),
#                         ('20240209-PqR543lmno','the_milkmaid_rrv','text','information','paintings','EXH-B-003'),
#                         ('20240209-AbC98dEfGh','there_comes_papa_rrv','text','information','paintings','EXH-B-004'),
#                         ('20240209-UVWxyz12Ab','yashoda_krishna_rrv','text','information','paintings','EXH-B-005'),
#                         ('20240209-XyZ67AbCde','balochistan_pot','text','information','history','EXH-C-001'),
#                         ('20240209-Lkji21NhgF','dancing_girl_harappa','text','information','history','EXH-C-002'),
#                         ('20240209-GHTre098Fg','deedarganj_yakshini','text','information','history','EXH-C-003'),
#                         ('20240209-567BcdEfgH','samudragupta_coin','text','information','history','EXH-C-004'),
#                         ('20240209-Pqrs90AaBc','sarnath_pillar','text','information','history','EXH-C-005')'''

"Entering values inside users table"
# query = '''
# INSERT INTO users VALUES('amrit_01', 'Amritanshu'),
#                         ('rocky_05', 'Deepak'),
#                         ('nobi_003', 'Sameer')'''



# conn.close()



"Creating a table to store admin data"

import hashlib
conn = sqlite3.connect('admin.db')
cur = conn.cursor()

# query = '''
# CREATE TABLE IF NOT EXISTS admin (
#     name TEXT,
#     admin_id TEXT,
#     email TEXT,
#     password TEXT
# );
# '''

"Seeing the structure of admin table"
# cur.execute(f"PRAGMA table_info({'admin'})")

# # Fetch and print the results
# columns = cur.fetchall()
# for column in columns:
#     print(column)

# conn.close()

"Inserting data into admin table"
# name = 'Amritanshu'
# admin_id ='amrit_admin_01'
# email = 'sandyamritanshu9715@gmail.com'
# password = hashlib.sha256('uhsNatirma1342!'.encode()).hexdigest()


# data = (name, admin_id, email, password)

# query = '''
# INSERT INTO admin VALUES(?,?,?,?)
# '''
            # "For deleting duplicate values"
            # query = '''CREATE TABLE IF NOT EXISTS your_table (
            #     rowid INTEGER PRIMARY KEY,
            #     name TEXT,
            #     admin_id TEXT,
            #     email TEXT,
            #     password TEXT
            # );
            # '''

# query = "SELECT * FROM admin"

# query = "DELETE FROM admin"
# cur.execute(query, data)
# conn.commit()



# res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchall())

conn.close()