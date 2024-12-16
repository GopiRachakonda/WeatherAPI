import sqlite3

def init_db():
    # Connect to the SQLite database (this will create the file if it doesn't exist)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Create the 'searches' table if it doesn't exist already
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS searches (
            id INTEGER PRIMARY KEY,
            city TEXT
        )
    ''')

    # Commit and close the connection
    connection.commit()
    connection.close()
    print("Database initialized.")

if __name__ == '__main__':
    init_db()
