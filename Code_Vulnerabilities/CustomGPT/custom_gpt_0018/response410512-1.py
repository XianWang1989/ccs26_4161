
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Set up a directory for saving files
MEDIA_FOLDER = 'media'
os.makedirs(MEDIA_FOLDER, exist_ok=True)

@app.route('/create-file/<filename>')
def create_file(filename):
    # Here you would create your dynamic file
    file_path = os.path.join(MEDIA_FOLDER, filename)
    with open(file_path, 'w') as f:
        f.write("This is some dynamically generated content.")
    return f"File {filename} created!"

@app.route('/media/<path:filename>')
def serve_media(filename):
    # Use send_from_directory to serve files directly from your media folder
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
