
from flask import Flask, request
import os

app = Flask(__name__)

# Directory to store dynamically created files
MEDIA_DIR = '/path/to/media_directory'

@app.route('/generate-file')
def generate_file():
    # Generate your content here (for example, a text file)
    filename = 'dynamic_file.txt'
    content = 'This is a dynamically generated file.'

    # Save the file to the specified directory
    file_path = os.path.join(MEDIA_DIR, filename)
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL for the dynamically created file
    file_url = f'/media/{filename}'  # This path should be served by Nginx
    return {'file_url': file_url}
