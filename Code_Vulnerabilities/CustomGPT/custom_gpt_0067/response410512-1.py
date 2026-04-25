
from flask import Flask, send_file
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Ensure this directory is writable

@app.route('/generate_file')
def generate_file():
    # Create your dynamic file
    file_path = os.path.join(MEDIA_FOLDER, 'dynamic_file.txt')
    with open(file_path, 'w') as f:
        f.write("This is a dynamically generated file.")

    return f"File created at {file_path}"
