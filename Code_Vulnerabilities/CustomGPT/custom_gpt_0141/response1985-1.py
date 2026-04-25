
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('your_database.db')  # Change this to your database file
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    # Connect to the database and fetch data
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM your_table').fetchall()  # Change 'your_table' to your database table
    conn.close()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
