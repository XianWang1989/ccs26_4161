
from flask import Flask, render_template_string

app = Flask(__name__)

# Example data (replace this with your database logic)
data = [
    {"name": "Item 1", "description": "Description 1"},
    {"name": "Item 2", "description": "Description 2"},
]

# Simple HTML template
html_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Data</title>
</head>
<body>
    <h1>Data List</h1>
    <ul>
        {% for item in data %}
        <li>{{ item.name }}: {{ item.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, data=data)

if __name__ == '__main__':
    app.run(debug=True)
