
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)

@app.route('/generate_content')
def generate_content():
    # Create dynamic content
    content = "This is some dynamic content!"

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
        temp_file.write(content.encode())
        temp_file_path = temp_file.name

    # Return the file URL
    return f"File generated at: /media/{os.path.basename(temp_file_path)}"

@app.route('/media/<path:filename>')
def media(filename):
    # Adjust the directory to where your temp files are stored
    return send_from_directory(tempfile.gettempdir(), filename)
