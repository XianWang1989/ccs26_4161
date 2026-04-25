
from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data (you can replace this with your database query)
data = [
    {"name": "Item 1", "info": "This is the first item."},
    {"name": "Item 2", "info": "This is the second item."},
]

# Basic HTML template
html_template = """
<!doctype html>
<html>
<head><title>My Data</title></head>
<body>
<h1>Data from Database</h1>
<ul>
{% for item in items %}
    <li><strong>{{ item.name }}</strong>: {{ item.info }}</li>
{% endfor %}
</ul>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template, items=data)

if __name__ == '__main__':
    app.run(debug=True)
