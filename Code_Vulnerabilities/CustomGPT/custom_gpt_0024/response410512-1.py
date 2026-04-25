
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MEDIA_FOLDER = "/path/to/media"  # Change to your media path

@app.route('/generate', methods=['POST'])
def generate_file():
    content = request.json.get('content', 'Hello, World!')
    filename = 'dynamic_file.txt'
    filepath = os.path.join(MEDIA_FOLDER, filename)

    # Write content to file
    with open(filepath, 'w') as f:
        f.write(content)

    # Return the URL to access the file
    return jsonify(url=f'/media/{filename}')

if __name__ == '__main__':
    app.run()
