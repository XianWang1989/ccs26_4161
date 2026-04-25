
from flask import Flask, request, jsonify
import os
from werkzeug.utils import send_from_directory

app = Flask(__name__)
MEDIA_DIRECTORY = '/path/to/media'  # Make sure this directory is accessible by Nginx

@app.route('/generate-media', methods=['POST'])
def generate_media():
    # Here you create the file dynamically based on your logic
    media_filename = "dynamic_media.mp4"  # Example filename
    media_path = os.path.join(MEDIA_DIRECTORY, media_filename)

    # Create your media file (this is just an example, replace with actual media generation logic)
    with open(media_path, 'wb') as f:
        f.write(b'Your dynamic media content goes here.')

    # Return the URL to the generated media
    return jsonify({"media_url": f"/media/{media_filename}"}), 201

# This will allow Nginx to serve the media files
@app.route('/media/<path:filename>', methods=['GET'])
def serve_media(filename):
    return send_from_directory(MEDIA_DIRECTORY, filename)

if __name__ == '__main__':
    app.run()
