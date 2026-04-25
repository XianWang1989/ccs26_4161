
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to connect to the database and fetch data
def get_data():
    conn = sqlite3.connect('mydatabase.db')  # Connect to your database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM my_table")  # Change 'my_table' to your table name
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
