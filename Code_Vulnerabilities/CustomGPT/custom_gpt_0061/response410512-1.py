
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Set this to the directory where you want to save files

@app.route('/generate-file', methods=['POST'])
def generate_file():
    data = request.json
    filename = 'dynamic_file.txt'
    filepath = os.path.join(MEDIA_FOLDER, filename)

    with open(filepath, 'w') as f:
        f.write(data.get('content', 'Default content'))

    # Return the URL to access the file
    return jsonify({'url': f'/media/{filename}'})

if __name__ == '__main__':
    app.run()
