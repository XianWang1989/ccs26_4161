
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Create a temporary file
    temp_dir = tempfile.gettempdir()
    file_path = os.path.join(temp_dir, 'dynamic_file.txt')

    # Write content to the file
    with open(file_path, 'w') as f:
        f.write("This is a dynamically generated file.")

    # Return the file path for Nginx to serve
    return f"File generated at: {file_path}"

@app.route('/download-file/<filename>')
def download_file(filename):
    temp_dir = tempfile.gettempdir()
    return send_from_directory(temp_dir, filename)

if __name__ == '__main__':
    app.run()
