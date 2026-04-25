
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('data.db')  # Replace with your database file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM my_table")  # Replace with your table name
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    records = get_data()
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
