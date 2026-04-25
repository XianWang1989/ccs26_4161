
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to get data from the database
def get_data():
    conn = sqlite3.connect('your_database.db')  # Change to your database file
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")  # Change to your table name
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
