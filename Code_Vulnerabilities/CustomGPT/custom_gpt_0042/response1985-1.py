
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('your_database.db')  # replace with your database file
    conn.row_factory = sqlite3.Row
    return conn

# Route for the homepage
@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM your_table_name').fetchall()  # replace with your table name
    conn.close()

    # Create a simple HTML template
    html = """
    <html>
    <head><title>Items</title></head>
    <body>
        <h1>Items List</h1>
        <ul>
            {% for item in items %}
            <li>{{ item['column_name'] }}</li>  # replace with your column name
            {% endfor %}
        </ul>
    </body>
    </html>
    """

    return render_template_string(html, items=items)

if __name__ == '__main__':
    app.run(debug=True)
