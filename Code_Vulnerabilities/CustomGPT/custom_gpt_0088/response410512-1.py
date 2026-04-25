
from flask import Flask, request
import os

app = Flask(__name__)
MEDIA_DIR = '/path/to/media'

@app.route('/generate-file')
def generate_file():
    # Assume we generate a file named 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_DIR, 'dynamic_file.txt')

    # Generate dynamic content and write to the file
    with open(file_path, 'w') as f:
        f.write("This is some dynamic content.")

    # Return the URL to access the file
    return f"File created! You can access it at http://your-domain.com/media/dynamic_file.txt"
