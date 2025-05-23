import sqlite3

def add_user(username: str, telegram_id: str, created_at: str):
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (telegram_id, username, created_at)
            VALUES (?, ?, ?)
        ''', (telegram_id,username, created_at))
        conn.commit()

    
def get_user(telegram_id: str):
    with sqlite3.connect('ansar.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE telegram_id = ?
        ''', (telegram_id,))
        user = cursor.fetchone()
        return user or None