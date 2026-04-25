
from flask import Flask, render_template
import json

app = Flask(__name__)

# Sample data structure, could be loaded from a database
data = {
    "items": [
        {"name": "Item 1", "description": "Description for Item 1"},
        {"name": "Item 2", "description": "Description for Item 2"},
        {"name": "Item 3", "description": "Description for Item 3"},
    ]
}

@app.route('/')
def home():
    return render_template('index.html', items=data['items'])

if __name__ == '__main__':
    app.run(debug=True)
