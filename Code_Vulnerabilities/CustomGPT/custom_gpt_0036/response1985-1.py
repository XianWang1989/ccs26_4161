
from flask import Flask, render_template_string

app = Flask(__name__)

# Mock database
data = [
    {"name": "Item 1", "description": "Description for item 1"},
    {"name": "Item 2", "description": "Description for item 2"},
    {"name": "Item 3", "description": "Description for item 3"},
]

# HTML template to display data
HTML_TEMPLATE = """
<!doctype html>
<html>
<head><title>My Database</title></head>
<body>
<h1>My Database Items</h1>
<ul>
    {% for item in items %}
        <li><strong>{{ item.name }}</strong>: {{ item.description }}</li>
    {% endfor %}
</ul>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, items=data)

if __name__ == '__main__':
    app.run(debug=True)
