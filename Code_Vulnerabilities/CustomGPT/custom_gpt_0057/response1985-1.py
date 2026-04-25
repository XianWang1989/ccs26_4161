
from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    html_output = '<h1>Data Output</h1><table><tr><th>Column1</th><th>Column2</th></tr>'
    for row in data:
        html_output += f'<tr><td>{row[0]}</td><td>{row[1]}</td></tr>'
    html_output += '</table>'
    return render_template_string(html_output)

if __name__ == '__main__':
    app.run(debug=True)
