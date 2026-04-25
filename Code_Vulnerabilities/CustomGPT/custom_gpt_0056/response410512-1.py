
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
TEMP_DIR = '/path/to/temp/directory'

@app.route('/generate-file/<filename>')
def generate_file(filename):
    # Create your dynamic content and save it
    file_path = os.path.join(TEMP_DIR, filename)
    with open(file_path, 'w') as f:
        f.write("This is the content of the file.")

    # Return the URL to access the file
    return f'File created! Access it at /media/{filename}'

@app.route('/media/<path:filename>')
def serve_media(filename):
    return send_from_directory(TEMP_DIR, filename)
