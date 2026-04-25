
from flask import Flask, render_template

app = Flask(__name__)

# Sample data simulating a database query
sample_data = [
    'Item 1',
    'Item 2',
    'Item 3',
]

@app.route('/')
def index():
    return render_template('index.html', data=sample_data)

if __name__ == '__main__':
    app.run(debug=True)
