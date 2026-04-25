
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Ensure this directory is writable by Flask

@app.route('/generate_media', methods=['POST'])
def generate_media():
    # Example: Create a dynamic file
    media_filename = request.json.get('filename')
    media_path = os.path.join(MEDIA_DIR, media_filename)

    # Generate your content (e.g., write to a file)
    with open(media_path, 'w') as f:
        f.write('This is dynamic content for ' + media_filename)

    return jsonify({"message": "File created", "url": f"/media/{media_filename}"}), 201

if __name__ == '__main__':
    app.run()
