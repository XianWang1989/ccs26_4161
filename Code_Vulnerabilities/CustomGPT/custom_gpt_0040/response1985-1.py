
from flask import Flask, render_template

app = Flask(__name__)

# Example data from your database (replace this with actual data retrieval)
data = [
    {"name": "Item 1", "description": "Description of Item 1"},
    {"name": "Item 2", "description": "Description of Item 2"},
]

@app.route('/')
def index():
    return render_template('index.html', items=data)

if __name__ == '__main__':
    app.run(debug=True)
