
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Create a table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            value INTEGER NOT NULL
        )
    ''')

    # Insert sample data (remove if already populated)
    cursor.execute("INSERT INTO my_table (name, value) VALUES ('Sample', 42)")
    conn.commit()

    # Query data
    cursor.execute("SELECT * FROM my_table")
    data = cursor.fetchall()

    # Close the connection
    conn.close()

    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
