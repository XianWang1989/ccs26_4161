from jinja2 import Environment, FileSystemLoader
import os

# Mock database (list of dictionaries)
data = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 92}
]

# Load the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render HTML
output = template.render(records=data)

# Write to file
with open("output.html", "w") as f:
    f.write(output)
