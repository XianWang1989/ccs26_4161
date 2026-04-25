
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to SQLite database
    conn = sqlite3.connect('data.db')  # replace 'data.db' with your database file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")  # replace 'your_table' with your table name
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
