
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_users():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

@app.route('/')
def index():
    users = get_users()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
