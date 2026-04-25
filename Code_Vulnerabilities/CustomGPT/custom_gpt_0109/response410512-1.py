
from flask import Flask, send_file
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media/'  # Directory where dynamic media will be stored

@app.route('/generate-media/<filename>', methods=['GET'])
def generate_media(filename):
    # Example: Generate your file and save it
    file_path = os.path.join(MEDIA_FOLDER, filename)
    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    # Return the generated file path (can also return a URL)
    return f'Media generated at: {file_path}', 200
