
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# A function to read your database (CSV file in this case)
def read_database():
    # Assuming you have a CSV file called 'data.csv'
    return pd.read_csv('data.csv')

@app.route('/')
def index():
    # Read your database content
    data = read_database()
    # Convert the data to a list of dictionaries for rendering in HTML
    data_list = data.to_dict(orient='records')
    return render_template('index.html', data=data_list)

if __name__ == '__main__':
    app.run(debug=True)
