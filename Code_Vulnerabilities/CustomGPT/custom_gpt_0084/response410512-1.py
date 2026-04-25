
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Ensure this directory is writable

@app.route('/generate-media', methods=['POST'])
def generate_media():
    # Simulate dynamic media creation
    media_filename = 'dynamic_media.txt'
    file_path = os.path.join(MEDIA_DIR, media_filename)

    with open(file_path, 'w') as f:
        f.write('This is dynamically generated content.')

    media_url = f'http://yourdomain.com/media/{media_filename}'
    return jsonify({'url': media_url})

if __name__ == '__main__':
    app.run()
