
from flask import Flask, render_template_string

app = Flask(__name__)

# Simulated database
data = [
    {'name': 'Item 1', 'description': 'Description of Item 1'},
    {'name': 'Item 2', 'description': 'Description of Item 2'},
]

# HTML template
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Database Output</title>
</head>
<body>
    <h1>My Data</h1>
    <ul>
        {% for item in items %}
            <li><strong>{{ item.name }}</strong>: {{ item.description }}</li>
        {% endfor %}
    </ul>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, items=data)

if __name__ == '__main__':
    app.run(debug=True)
