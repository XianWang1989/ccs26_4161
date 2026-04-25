
import sqlite3

# Connect to SQLite database (it will create it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# Create a simple table
c.execute('''CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, name TEXT)''')

# Insert some sample data
c.execute("INSERT INTO records (name) VALUES ('Alice')")
c.execute("INSERT INTO records (name) VALUES ('Bob')")

# Commit and close the connection
conn.commit()
conn.close()
