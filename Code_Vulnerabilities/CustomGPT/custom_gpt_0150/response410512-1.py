
from flask import Flask, send_from_directory
import os
import uuid

app = Flask(__name__)
MEDIA_FOLDER = 'media'

# Ensure the media folder exists
os.makedirs(MEDIA_FOLDER, exist_ok=True)

@app.route('/generate-file')
def generate_file():
    # Example of dynamic file creation
    filename = f"{uuid.uuid4()}.txt"
    file_path = os.path.join(MEDIA_FOLDER, filename)

    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    # Return the URL of the file for Nginx to serve
    return f"/media/{filename}", 201

@app.route('/media/<path:filename>')
def serve_media(filename):
    # Serve the file directly using Flask
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
