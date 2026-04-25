
from flask import Flask, send_file
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Directory to save dynamic files
MEDIA_DIR = '/path/to/media'

@app.route('/generate')
def generate_file():
    file_name = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_DIR, secure_filename(file_name))

    # Write dynamic content to the file
    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    # Return a URL to access the file
    return f"File created: /media/{file_name}"

if __name__ == '__main__':
    app.run()
