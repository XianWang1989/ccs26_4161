
from flask import Flask, render_template

app = Flask(__name__)

# Simulated database (in a real scenario, you'd connect to your actual database here)
data = [
    {'name': 'John Doe', 'age': 30},
    {'name': 'Jane Smith', 'age': 25},
    {'name': 'Alice Johnson', 'age': 29}
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
