import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'output', 'asana_simulation.sqlite')
SCHEMA_PATH = os.path.join(BASE_DIR, 'schema.sql')

def get_connection():
    """Returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Reads schema.sql and rebuilds the database from scratch."""
    
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    if os.path.exists(DB_PATH):
        try:
            os.remove(DB_PATH)
            print(f"Removed old database.")
        except PermissionError:
            print(f"Close 'DB Browser for SQLite' before running this script.")
            return

    conn = get_connection()
    with open(SCHEMA_PATH, 'r') as f:
        schema_script = f.read()
    
    conn.executescript(schema_script)
    conn.commit()
    conn.close()
    print(f"Database successfully created at: {DB_PATH}")