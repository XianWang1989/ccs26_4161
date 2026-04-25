
from flask import Flask, request, send_from_directory
import os
import tempfile

app = Flask(__name__)

# Endpoint to create and serve dynamic content
@app.route('/generate-file')
def generate_file():
    content = "Hello, this is dynamic content!"

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(content.encode())
        temp_file_path = tmp_file.name

    # Return the file path for Nginx
    return {"file_path": temp_file_path}

# Serve files from the temporary directory
@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory('/path/to/temp/dir', filename)

if __name__ == '__main__':
    app.run()
