
# app.py
from flask import Flask, render_template
from data import data_entries

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('data.html', entries=data_entries)

if __name__ == '__main__':
    app.run(debug=True)
