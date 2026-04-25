
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/generate')
def generate_file():
    # Create your dynamic content
    filename = 'dynamic_content.txt'

    with open(filename, 'w') as f:
        f.write('This is dynamic content.')

    # Serve the file using send_file
    return send_file(filename, as_attachment=True)
