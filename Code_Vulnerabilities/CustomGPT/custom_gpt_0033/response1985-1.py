
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Database setup (replace with your actual database)
def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM my_table').fetchall()  # Replace 'my_table' with your table name
    conn.close()

    # Simple HTML template
    html_template = '''
    <!doctype html>
    <html>
    <head><title>Database Data</title></head>
    <body>
      <h1>Data from Database</h1>
      <table border="1">
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Value</th>
        </tr>
        {% for row in data %}
          <tr>
            <td>{{ row.id }}</td>
            <td>{{ row.name }}</td>
            <td>{{ row.value }}</td>
          </tr>
        {% endfor %}
      </table>
    </body>
    </html>
    '''

    return render_template_string(html_template, data=data)

if __name__ == '__main__':
    app.run(debug=True)
