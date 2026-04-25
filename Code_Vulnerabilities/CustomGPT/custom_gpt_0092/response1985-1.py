
from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data (replace with your database queries later)
data = [
    {'name': 'Item 1', 'description': 'Description for Item 1'},
    {'name': 'Item 2', 'description': 'Description for Item 2'},
]

# HTML template
template = """
<html>
<head><title>My Data</title></head>
<body>
    <h1>Data List</h1>
    <ul>
        {% for item in items %}
            <li>{{ item.name }}: {{ item.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template, items=data)

if __name__ == '__main__':
    app.run(debug=True)
