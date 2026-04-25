
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'  # Directory for media files

@app.route('/create_file', methods=['POST'])
def create_file():
    content = request.json.get('content', '')
    filename = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_DIR, filename)

    # Ensure MEDIA_DIR exists
    os.makedirs(MEDIA_DIR, exist_ok=True)

    # Write content to the file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL to access the file
    file_url = f"http://your_nginx_server/media/{filename}"
    return jsonify({'file_url': file_url})

if __name__ == '__main__':
    app.run()
