
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

def get_data():
    # Connect to your database
    conn = sqlite3.connect('your_database.db')  # Change to your database file
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM your_table')  # Change to your table name
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def home():
    data = get_data()
    html = '''
    <html>
    <head><title>Database Output</title></head>
    <body>
        <h1>Database Data</h1>
        <table border="1">
            <tr><th>Column1</th><th>Column2</th></tr>
            {% for row in data %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    '''
    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(debug=True)
