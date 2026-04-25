
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Directory to store dynamically created files
MEDIA_DIR = '/path/to/media/directory'

@app.route('/create_file', methods=['POST'])
def create_file():
    content = request.json.get('content')
    filename = 'dynamic_file.txt'
    filepath = os.path.join(MEDIA_DIR, filename)

    # Create and write content to the file
    with open(filepath, 'w') as f:
        f.write(content)

    # Return the URL to access the file
    return jsonify({'url': f'/media/{filename}'}), 201

if __name__ == '__main__':
    app.run()
