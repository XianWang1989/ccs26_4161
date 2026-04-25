
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)
TEMP_DIR = '/path/to/temp/directory'  # Update this with your actual path

@app.route('/generate-media')
def generate_media():
    # Generate dynamic content (e.g., a text file)
    file_name = 'dynamic_content.txt'
    file_path = os.path.join(TEMP_DIR, file_name)

    # Save the content to the file
    with open(file_path, 'w') as f:
        f.write('This is some dynamically created content.')

    # Return the URL where Nginx will serve the file
    return f'File created. You can download it <a href="/media/{file_name}">here</a>.'

@app.route('/media/<path:filename>')
def serve_media(filename):
    # Serve the file from TEMP_DIR
    return send_from_directory(TEMP_DIR, filename)

if __name__ == '__main__':
    app.run()
