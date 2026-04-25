
import os
from flask import Flask, send_file

app = Flask(__name__)
FILE_DIR = '/path/to/your/files/'  # Ensure this directory exists

@app.route('/generate')
def generate_file():
    # Create your dynamic content
    filename = os.path.join(FILE_DIR, 'dynamic_content.txt')

    with open(filename, 'w') as f:
        f.write('This is dynamic content.')

    return f'File generated at: /files/dynamic_content.txt'
