
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Directory where you save dynamic files

@app.route('/generate-file', methods=['POST'])
def generate_file():
    content = request.json.get('content', 'Default content')
    file_name = 'dynamic_file.txt'

    # Save the content to a file
    file_path = os.path.join(MEDIA_FOLDER, file_name)
    with open(file_path, 'w') as f:
        f.write(content)

    # Generate a public URL to the file
    file_url = f'/media/{file_name}'
    return jsonify({'url': file_url}), 201

if __name__ == '__main__':
    app.run()
