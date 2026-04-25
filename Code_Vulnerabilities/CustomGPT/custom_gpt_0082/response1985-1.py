
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to your database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Retrieve data from the database
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()

    # Close the connection
    conn.close()
    return data

@app.route('/')
def index():
    # Get data from the database
    data = get_data()
    # Render the HTML template with the data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
