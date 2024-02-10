import sqlite3

con = sqlite3.connect('file_database.db')
cur = con.cursor()

"Creating the database"
# query = "CREATE TABLE files(File_Unique_ID, File_Name, Lvl_1, Lvl_2, Lvl_3)"
# cur.execute(query)

"Verifying the creation of tables"
# res = cur.execute("SELECT name FROM sqlite_master")
# print(res.fetchone())

"Inserting the Initial Set of Values"
# query = """INSERT INTO files VALUES
#         ('20240209-A23bC87dE1','dandakosaurus','text','information','dianosaur'),
#         ('20240209-Xyz456Pqrs','indosaurus','text','information','dianosaur'),
#         ('20240209-Lmno789Abc','saurian_rellic_01','text','information','dianosaur'),
#         ('20240209-DfgHij012K','thar_desert_ovum','text','information','dianosaur'),
#         ('20240209-ZzxYyWwVvU','tharosaurus_indicus','text','information','dianosaur'),
#         ('20240209-Klm876NopQ','hamsa_damyanti_rrv','text','information','paintings'),
#         ('20240209-Jkl321XyZa','shakuntalam_rrv','text','information','paintings'),
#         ('20240209-PqR543lmno','the_milkmaid_rrv','text','information','paintings'),
#         ('20240209-AbC98dEfGh','there_comes_papa_rrv','text','information','paintings'),
#         ('20240209-UVWxyz12Ab','yashoda_krishna_rrv','text','information','paintings'),
#         ('20240209-XyZ67AbCde','balochistan_pot','text','information','history'),
#         ('20240209-Lkji21NhgF','dancing_girl_harappa','text','information','history'),
#         ('20240209-GHTre098Fg','deedarganj_yakshini','text','information','history'),
#         ('20240209-567BcdEfgH','samudragupta_coin','text','information','history'),
#         ('20240209-Pqrs90AaBc','sarnath_pillar','text','information','history')"""

# cur.execute(query)

# con.commit()

"Displaying the data"
# res = cur.execute("SELECT File_Name FROM files")
# print(res.fetchall())