
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Create a temporary file
    temp_file_path = os.path.join(tempfile.gettempdir(), 'dynamic_content.txt')

    with open(temp_file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    return f"File created: <a href='/files/dynamic_content.txt'>Download here</a>"

@app.route('/files/<path:filename>')
def serve_file(filename):
    # Serve the file using Nginx
    return send_from_directory(tempfile.gettempdir(), filename)

if __name__ == '__main__':
    app.run()
