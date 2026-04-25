
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/media'  # Make sure Nginx can serve this directory

@app.route('/generate-and-serve')
def generate_media():
    # Create a temporary filename
    temp_file = os.path.join(MEDIA_FOLDER, 'dynamic_content.txt')

    # Generate your dynamic content and write it to the file
    with open(temp_file, 'w') as f:
        f.write('This is some dynamically generated content.')

    # Return the URL to access the file
    return f'File available at: /media/dynamic_content.txt'

@app.route('/media/<path:filename>')
def serve_media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
