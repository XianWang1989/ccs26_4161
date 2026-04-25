
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Directory to save files temporarily
UPLOAD_FOLDER = '/path/to/temp/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/create_file')
def create_file():
    # Simulate file creation
    filename = 'dynamic_content.txt'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    with open(file_path, 'w') as f:
        f.write('This is some dynamic content!')

    # Return the URL where the file can be accessed
    file_url = f'http://yourdomain.com/media/{filename}'
    return jsonify({'file_url': file_url})
