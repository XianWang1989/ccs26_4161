
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Replace 'your_database.db' with your database file
DATABASE = 'your_database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # To be able to access columns by name
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM your_table').fetchall()  # Replace 'your_table' with your actual table name
    conn.close()
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
