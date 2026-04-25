
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_data():
    # Connect to your SQLite database (or any database you're using)
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Execute a simple query
    cursor.execute('SELECT * FROM your_table')
    data = cursor.fetchall()

    conn.close()
    return data

@app.route('/')
def home():
    # Fetch data from the database
    data = get_db_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
