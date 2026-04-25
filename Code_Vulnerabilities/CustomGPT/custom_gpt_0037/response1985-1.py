
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Connect to your database
def get_data():
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table;")  # change 'your_table' to your actual table name
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    # Simple HTML template
    html = '''
    <h1>Database Records</h1>
    <table border="1">
        <tr><th>ID</th><th>Name</th></tr>
        {% for id, name in data %}
        <tr><td>{{ id }}</td><td>{{ name }}</td></tr>
        {% endfor %}
    </table>
    '''
    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(debug=True)
