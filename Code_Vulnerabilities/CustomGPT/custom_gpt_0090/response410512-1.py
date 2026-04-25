
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
MEDIA_FOLDER = 'media'  # Folder where media files are stored

@app.route('/generate')
def generate_file():
    # Simulate generating a dynamic file
    file_name = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_FOLDER, file_name)

    # Create a sample file
    with open(file_path, 'w') as f:
        f.write('This is a dynamically generated file.')

    return f'File generated: <a href="/media/{file_name}">Download here</a>'

@app.route('/media/<path:filename>')
def serve_media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
