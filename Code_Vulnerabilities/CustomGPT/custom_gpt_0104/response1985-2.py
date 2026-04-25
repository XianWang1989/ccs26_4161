
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    records = conn.execute('SELECT * FROM records').fetchall()  # Fetch all records
    conn.close()
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
