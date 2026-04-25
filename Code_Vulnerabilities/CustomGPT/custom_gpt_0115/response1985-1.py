
from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data
data = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# HTML template as a string
template = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My Database</title>
</head>
<body>
    <h1>Users</h1>
    <ul>
        {% for user in users %}
        <li>{{ user.name }} is {{ user.age }} years old.</li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# Route to display data
@app.route('/')
def home():
    return render_template_string(template, users=data)

if __name__ == '__main__':
    app.run(debug=True)
