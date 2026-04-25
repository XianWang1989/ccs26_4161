
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Connect to your database
def get_db_connection():
    conn = sqlite3.connect('your_database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM your_table').fetchall()
    conn.close()

    # Render HTML with the fetched data
    html = '''
    <!doctype html>
    <html>
    <head><title>Data Output</title></head>
    <body>
        <h1>Database Records</h1>
        <ul>
            {% for row in data %}
                <li>{{ row['your_column'] }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    '''
    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(debug=True)
