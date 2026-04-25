
from flask import Flask, jsonify
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media/files'

@app.route('/generate-file/<filename>', methods=['GET'])
def generate_file(filename):
    content = "This is dynamically created content."
    file_path = os.path.join(MEDIA_FOLDER, filename)

    # Create the media directory if it doesn't exist
    os.makedirs(MEDIA_FOLDER, exist_ok=True)

    # Save the content to a file
    with open(file_path, 'w') as file:
        file.write(content)

    return jsonify({'message': 'File created', 'url': f'/media/{filename}'})

if __name__ == "__main__":
    app.run()
