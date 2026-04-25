
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_data():
    # Connect to the SQLite database
    conn = sqlite3.connect('your_database.db')  # Replace with your database file
    cursor = conn.cursor()

    # Query your data. Adjust the SQL statement based on your actual table and column names
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()

    conn.close()
    return data

@app.route('/')
def index():
    data = get_db_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
