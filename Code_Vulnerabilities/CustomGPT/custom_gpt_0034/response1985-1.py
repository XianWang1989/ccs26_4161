
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to your SQLite database
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Query to fetch data
    cursor.execute("SELECT * FROM my_table")
    data = cursor.fetchall()

    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
