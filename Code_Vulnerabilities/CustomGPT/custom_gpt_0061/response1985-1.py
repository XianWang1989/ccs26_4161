
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Connect to your SQLite database
def get_db_connection():
    conn = sqlite3.connect('your_database.db')  # Replace with your database file
    conn.row_factory = sqlite3.Row  # Allows to access columns by name
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM your_table').fetchall()  # Replace with your table name
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
