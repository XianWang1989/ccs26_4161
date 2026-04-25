
from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

# Directory where files will be saved
MEDIA_DIR = '/path/to/media/files'

@app.route('/create_file/<filename>', methods=['GET'])
def create_file(filename):
    # Simulate file generation and saving
    filepath = os.path.join(MEDIA_DIR, filename)
    with open(filepath, 'w') as f:
        f.write('This is a dynamically created file content.')

    # Create a URL for the file to access it through Nginx
    file_url = f'http://your.domain.com/media/{filename}'
    return jsonify({"file_url": file_url})

if __name__ == '__main__':
    app.run()
