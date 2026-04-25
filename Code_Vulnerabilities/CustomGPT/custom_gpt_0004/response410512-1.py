
from flask import Flask, send_file
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Directory for storing dynamic files

@app.route('/generate-file')
def generate_file():
    filename = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_FOLDER, filename)

    # Create the file (you can create any dynamic content here)
    with open(file_path, 'w') as f:
        f.write('This is some dynamically generated content.')

    # Return the URL to access the file
    return f'File generated. You can download it <a href="/media/{filename}">here</a>.'

if __name__ == "__main__":
    app.run()
