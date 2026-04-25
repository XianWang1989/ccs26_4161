
from flask import Flask, send_file, jsonify
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'

@app.route('/generate_file')
def generate_file():
    # Simulate dynamic file creation
    filename = 'dynamic_file.txt'
    filepath = os.path.join(MEDIA_FOLDER, filename)

    with open(filepath, 'w') as f:
        f.write('This is some dynamic content.')

    # Return the URL to access the file
    return jsonify({'url': f'/media/{filename}'})

if __name__ == '__main__':
    app.run()
