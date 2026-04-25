
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to your database (this example uses SQLite)
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM your_table')  # Modify with your table name
    data = cursor.fetchall()
    connection.close()
    return data

@app.route('/')
def index():
    data = get_data()  # Fetch data from the database
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
