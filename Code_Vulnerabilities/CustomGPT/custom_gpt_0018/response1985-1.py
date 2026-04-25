
from flask import Flask, render_template

app = Flask(__name__)

# Sample data that you might be retrieving from your database
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]

@app.route('/')
def index():
    # Pass the data to the HTML template
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
