
from flask import Flask, send_file
import os
import tempfile

app = Flask(__name__)

@app.route('/generate')
def generate_file():
    # Create a temporary file with some dynamic content
    temp_file_path = os.path.join(tempfile.gettempdir(), 'dynamic_content.txt')
    with open(temp_file_path, 'w') as f:
        f.write("This is some dynamic content.")

    # Create a URL to access this file
    return f'File created at: {temp_file_path}'

@app.route('/serve/<filename>')
def serve_file(filename):
    file_path = os.path.join(tempfile.gettempdir(), filename)
    return send_file(file_path)

if __name__ == '__main__':
    app.run()
