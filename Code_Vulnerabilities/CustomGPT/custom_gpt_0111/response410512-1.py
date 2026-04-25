
from flask import Flask, send_from_directory, request
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media/folder'

@app.route('/create_file')
def create_file():
    # Dynamically generate content
    content = "Hello, this is dynamically created content."
    filename = "dynamic_file.txt"

    # Save file to MEDIA_FOLDER
    with open(os.path.join(MEDIA_FOLDER, filename), 'w') as f:
        f.write(content)

    return f'File created: <a href="/media/{filename}">Download here</a>'

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
