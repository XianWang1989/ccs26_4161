
import sqlite3

# Create a new SQLite database (or connect if it exists)
conn = sqlite3.connect('data.db')
cur = conn.cursor()

# Create a table
cur.execute('''
CREATE TABLE IF NOT EXISTS info (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    value TEXT NOT NULL
)
''')

# Insert example data
cur.execute("INSERT INTO info (name, value) VALUES ('Item1', 'Value1')")
cur.execute("INSERT INTO info (name, value) VALUES ('Item2', 'Value2')")
cur.execute("INSERT INTO info (name, value) VALUES ('Item3', 'Value3')")
conn.commit()
conn.close()
