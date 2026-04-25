
from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data - replace with your database access code
data = [
    {"name": "Item 1", "value": "Value 1"},
    {"name": "Item 2", "value": "Value 2"},
]

# HTML template
html_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Database Output</title>
</head>
<body>
    <h1>Data from Database</h1>
    <ul>
        {% for item in data %}
            <li>{{ item.name }}: {{ item.value }}</li>
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
