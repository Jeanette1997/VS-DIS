import sqlite3
import os

DATABASE = 'music_events.db'


with open("VS-DIS/Database.sql", "r") as sql_file:
    content = sql_file.read()


def init_db():
    """Initialize the database and insert test data."""
    if not os.path.exists(DATABASE):
        print("Creating database...")
        db = sqlite3.connect(DATABASE)
        
        # Create table
        db.execute(f'''
            {content}
            )
        ''')
        
        db.commit()
        db.close()
        print("Database initialized with test data!")