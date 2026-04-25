
from flask import Flask, render_template
import sqlite3  # Adjust based on your database

app = Flask(__name__)

def get_data():
    # Connect to your database
    connection = sqlite3.connect('your_database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT data_column FROM your_table")  # Adjust the query
    data = cursor.fetchall()
    connection.close()
    return [item[0] for item in data]  # Flatten the results

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
