import sqlite3

def drop_all_tables(database_path):
    try:
        # Connect to the database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Get a list of all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Drop each table in the list
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            print(f"Table '{table_name}' dropped.")

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("All tables dropped successfully.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")

# Specify the path to your database
database_path = 'path_to_your_database.db'

# Call the function to drop all tables
drop_all_tables('file_database.db')
