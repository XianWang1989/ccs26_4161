
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to your database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Replace this with your actual query
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()

    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
