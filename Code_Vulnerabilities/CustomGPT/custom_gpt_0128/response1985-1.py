
import sqlite3

# Create a sample database
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, info TEXT)')
c.execute('INSERT INTO records (info) VALUES ("Sample Data 1"), ("Sample Data 2")')
conn.commit()
conn.close()
