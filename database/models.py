import sqlite3

def create_table_users():
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                telegram_id INTEGER NOT NULL UNIQUE,
                username TEXT NOT NULL UNIQUE,
                created_at TEXT
            )
        ''')
        conn.commit()
    
