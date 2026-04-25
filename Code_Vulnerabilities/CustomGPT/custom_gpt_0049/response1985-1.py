
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to get data from the database
def get_data():
    conn = sqlite3.connect('your_database.db')  # Connect to your database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")  # Query the data
    data = cursor.fetchall()  # Fetch all results
    conn.close()
    return data

@app.route('/')
def homepage():
    data = get_data()  # Get data for the homepage
    return render_template('index.html', data=data)  # Pass data to the template

if __name__ == '__main__':
    app.run(debug=True)
