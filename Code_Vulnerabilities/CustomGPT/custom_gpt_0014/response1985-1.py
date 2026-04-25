
from flask import Flask, render_template

app = Flask(__name__)

# Sample data (you can replace this with your database query)
data = [
    {"name": "Item 1", "description": "This is item 1"},
    {"name": "Item 2", "description": "This is item 2"},
    {"name": "Item 3", "description": "This is item 3"},
]

@app.route('/')
def home():
    return render_template('index.html', items=data)

if __name__ == '__main__':
    app.run(debug=True)
