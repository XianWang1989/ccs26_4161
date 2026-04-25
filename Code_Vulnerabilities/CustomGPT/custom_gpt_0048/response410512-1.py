
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)
UPLOAD_FOLDER = 'your_temp_directory'  # Set your temporary directory here
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/generate-file')
def generate_file():
    # Generate your content and save it to a file
    file_content = "This is dynamically generated content"
    file_path = os.path.join(UPLOAD_FOLDER, "dynamic_file.txt")

    with open(file_path, 'w') as f:
        f.write(file_content)

    # Return the URL for Nginx to serve the file
    return f"/media/dynamic_file.txt"
