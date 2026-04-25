
from flask import Flask, jsonify
import os
import time

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media/folder'

@app.route('/generate_media')
def generate_media():
    # Simulate file generation
    filename = f'media_file_{int(time.time())}.txt'
    file_path = os.path.join(MEDIA_FOLDER, filename)

    with open(file_path, 'w') as f:
        f.write('This is some dynamically generated content.')

    # Return the URL where the file can be accessed
    media_url = f'http://your-nginx-server/media/{filename}'
    return jsonify({'media_url': media_url})

if __name__ == '__main__':
    app.run()
