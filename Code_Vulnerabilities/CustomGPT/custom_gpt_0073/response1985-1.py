
from flask import Flask, render_template

app = Flask(__name__)

# Sample data (replace this with your database query)
data = [
    {'name': 'Item 1', 'value': 'Value 1'},
    {'name': 'Item 2', 'value': 'Value 2'},
]

@app.route('/')
def home():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
