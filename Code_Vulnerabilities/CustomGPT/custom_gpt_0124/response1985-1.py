
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Connect to your SQLite database
def get_db_connection():
    conn = sqlite3.connect('your_database.db')  # Change to your database file
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM your_table').fetchall()  # Change to your table name
    conn.close()

    # Simple HTML template as a string
    html_template = '''
    <html>
        <head><title>Database Items</title></head>
        <body>
            <h1>Items from Database</h1>
            <ul>
            {% for item in items %}
                <li>{{ item['column_name'] }}</li>  <!-- Change 'column_name' to your actual column -->
            {% endfor %}
            </ul>
        </body>
    </html>
    '''
    return render_template_string(html_template, items=items)

if __name__ == '__main__':
    app.run(debug=True)
