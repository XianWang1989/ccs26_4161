
import sqlite3

connection = sqlite3.connect('database.db')

with connection:
    connection.execute('CREATE TABLE your_table (id INTEGER PRIMARY KEY, name TEXT, description TEXT)')
    connection.execute('INSERT INTO your_table (name, description) VALUES (?, ?)', ('Example Item', 'This is an example description.'))

connection.close()
