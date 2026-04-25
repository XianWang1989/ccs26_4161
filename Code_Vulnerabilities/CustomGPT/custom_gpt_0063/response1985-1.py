
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('my_database.db')  # Replace with your database file
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM my_table').fetchall()  # Replace 'my_table' with your table name
    conn.close()
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
