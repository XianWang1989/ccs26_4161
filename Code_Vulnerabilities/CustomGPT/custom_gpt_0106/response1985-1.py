
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to your database
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM your_table')  # Change 'your_table' to your table name
    data = cursor.fetchall()
    connection.close()
    return data

@app.route('/')
def index():
    records = get_data()
    return render_template('index.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
