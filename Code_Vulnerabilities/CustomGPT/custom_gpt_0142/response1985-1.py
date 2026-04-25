
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to fetch data from your database
def get_data():
    connection = sqlite3.connect('your_database.db')  # Replace with your database name
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM your_table")  # Replace with your table name
    data = cursor.fetchall()
    connection.close()
    return data

@app.route('/')
def homepage():
    data = get_data()  # Fetch data from database
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
