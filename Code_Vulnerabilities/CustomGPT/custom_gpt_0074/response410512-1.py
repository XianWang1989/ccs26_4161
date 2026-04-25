
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

MEDIA_DIRECTORY = '/tmp/media/'

@app.route('/createfile/<filename>', methods=['GET'])
def create_file(filename):
    # This is where you would create your media file dynamically
    with open(os.path.join(MEDIA_DIRECTORY, filename), 'w') as f:
        f.write('This is some dynamically created content.')

    return f'File {filename} created!'

@app.route('/media/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(MEDIA_DIRECTORY, filename)

if __name__ == '__main__':
    app.run()
