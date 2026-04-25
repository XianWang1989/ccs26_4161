
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch data from the database
def get_data():
    conn = sqlite3.connect('your_database.db')  # Connect to your database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")  # Fetch data from your table
    data = cursor.fetchall()  # Get all the rows
    conn.close()
    return data

@app.route('/')
def home():
    data = get_data()  # Get data from the database
    return render_template('index.html', data=data)  # Pass data to HTML template

if __name__ == '__main__':
    app.run(debug=True)
