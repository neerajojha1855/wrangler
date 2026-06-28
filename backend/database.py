import sqlite3
import json
from config import settings

def get_db_connection():
    conn = sqlite3.connect(settings.DATABASE_PATH.replace('sqlite:///', ''))
    conn.row_factory = sqlite3.Row

    return conn

def init_db():
    conn = get_db_connection()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS itineraries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            vibe TEXT NOT NULL,
            payload TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database Initialized")