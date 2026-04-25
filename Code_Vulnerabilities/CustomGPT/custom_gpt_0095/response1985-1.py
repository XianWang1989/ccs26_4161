
from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

# HTML template
HTML_TEMPLATE = '''
<html>
    <head><title>User Data</title></head>
    <body>
        <h1>User Database</h1>
        <ul>
            {% for user in users %}
                <li>Name: {{ user.name }}, Age: {{ user.age }}</li>
            {% endfor %}
        </ul>
    </body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, users=data)

if __name__ == '__main__':
    app.run(debug=True)
