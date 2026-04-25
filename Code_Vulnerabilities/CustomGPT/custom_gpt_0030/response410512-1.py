
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)

# Directory to store dynamic files
DYNAMIC_MEDIA_DIR = '/path/to/dynamic/media'

@app.route('/generate-file/<filename>', methods=['GET'])
def generate_file(filename):
    # Create dynamic content
    content = f"This is dynamic content for {filename}"

    # Save to a temporary file
    file_path = os.path.join(DYNAMIC_MEDIA_DIR, filename)
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL where Nginx can serve it
    return f"File generated: <a href='/media/{filename}'>Download here</a>"

@app.route('/media/<filename>', methods=['GET'])
def media(filename):
    # Serve file directly through Nginx
    return send_from_directory(DYNAMIC_MEDIA_DIR, filename)

if __name__ == '__main__':
    app.run()
