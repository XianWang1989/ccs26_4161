
from flask import Flask, render_template

app = Flask(__name__)

# Sample data simulating a database
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

@app.route('/')
def index():
    # Render the index.html template with the data
    return render_template('index.html', items=data)

if __name__ == '__main__':
    app.run(debug=True)
