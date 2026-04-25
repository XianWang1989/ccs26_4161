
from flask import Flask, render_template

app = Flask(__name__)

# Sample data simulating a database
data = [
    {"id": 1, "name": "Item 1", "description": "This is item 1."},
    {"id": 2, "name": "Item 2", "description": "This is item 2."}
]

@app.route('/')
def index():
    return render_template('index.html', items=data)

if __name__ == '__main__':
    app.run(debug=True)
