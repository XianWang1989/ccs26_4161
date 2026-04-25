
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'

# Ensure the media folder exists
os.makedirs(MEDIA_FOLDER, exist_ok=True)

@app.route('/create_media', methods=['POST'])
def create_media():
    # Assume content is sent in request data
    content = request.json.get('content')
    filename = request.json.get('filename', 'default.txt')
    file_path = os.path.join(MEDIA_FOLDER, filename)

    with open(file_path, 'w') as f:
        f.write(content)

    return jsonify({"message": "File created", "url": f"/media/{filename}"}), 201

if __name__ == "__main__":
    app.run()
