
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_data():
    # Connect to the SQLite database
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()

    # Query your data (modify as needed)
    cursor.execute('SELECT * FROM your_table')
    data = cursor.fetchall()

    # Close the connection
    connection.close()

    return data

@app.route('/')
def index():
    data = get_db_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
