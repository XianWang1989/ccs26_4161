
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Sample function to get data from a SQLite database
def get_data():
    conn = sqlite3.connect('your_database.db')  # Update with your database path
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")  # Update with your table name
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
