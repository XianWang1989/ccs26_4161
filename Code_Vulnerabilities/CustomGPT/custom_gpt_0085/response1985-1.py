
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('your_database.db')  # Replace with your database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")  # Replace with your table name
    data = cursor.fetchall()
    conn.close()
    return data

# Route to display data
@app.route('/')
def index():
    data = fetch_data()
    html = """
    <html>
    <head><title>Data from Database</title></head>
    <body>
        <h1>Database Data</h1>
        <table border="1">
            <tr><th>ID</th><th>Name</th></tr>
            {% for row in data %}
                <tr>
                    <td>{{ row[0] }}</td>
                    <td>{{ row[1] }}</td>
                </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(debug=True)
