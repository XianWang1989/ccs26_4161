
from flask import Flask, render_template_string

app = Flask(__name__)

# Simulating a database with a dictionary
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Web App</title>
</head>
<body>
    <h1>User Database</h1>
    <ul>
        {% for user in users %}
            <li>{{ user.name }} is {{ user.age }} years old.</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, users=data)

if __name__ == '__main__':
    app.run(debug=True)
