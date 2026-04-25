
# app.py
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load data from CSV file
    data = pd.read_csv('data.csv')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
