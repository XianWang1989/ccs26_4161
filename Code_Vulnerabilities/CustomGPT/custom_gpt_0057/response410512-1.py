
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    filename = 'dynamic_file.txt'
    file_path = os.path.join('/path/to/dynamic/media/', filename)

    with open(file_path, 'w') as f:
        f.write('This is some dynamically generated content.')

    return f"File created: <a href='/media/{filename}'>Download here</a>"

@app.route('/media/<path:filename>', methods=['GET'])
def serve_media(filename):
    return send_from_directory('/path/to/dynamic/media/', filename)

if __name__ == '__main__':
    app.run()
