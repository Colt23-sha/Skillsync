import sqlite3

def get_db_connection():
    conn = sqlite3.connect('skillsync.db')
    conn.row_factory=sqlite3.Row
    return conn

def create_projects_table():
    conn = get_db_connection()
    conn.execute('''
             CREATE TABLE IF NOT EXISTS projects(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                tech TEXT NOT NULL
                    )
                    ''')
    conn.commit()
    conn.close()