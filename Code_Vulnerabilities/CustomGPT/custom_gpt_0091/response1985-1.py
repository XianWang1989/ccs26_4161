
import sqlite3

def setup_database():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)''')
    c.execute("INSERT INTO items (name) VALUES ('Example Item 1')")
    c.execute("INSERT INTO items (name) VALUES ('Example Item 2')")
    conn.commit()
    conn.close()

setup_database()
