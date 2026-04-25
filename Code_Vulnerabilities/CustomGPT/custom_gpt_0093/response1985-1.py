
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to your database (replace 'your_database.db' with your db file)
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")  # Replace with your table
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    data = get_data()
    return render_template_string('''
        <h1>Data from Database</h1>
        <ul>
        {% for row in data %}
            <li>{{ row }}</li>
        {% endfor %}
        </ul>
    ''', data=data)

if __name__ == '__main__':
    app.run(debug=True)
