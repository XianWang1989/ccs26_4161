
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_data():
    # Connect to your SQLite database (or any other type)
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Execute a query to fetch data
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()

    # Close the database connection
    conn.close()
    return data

@app.route('/')
def home():
    # Get data from the database
    db_data = get_db_data()

    # Render the data using an HTML template
    return render_template('index.html', data=db_data)

if __name__ == '__main__':
    app.run(debug=True)
