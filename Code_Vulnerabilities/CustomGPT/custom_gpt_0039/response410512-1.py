
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)

# Define where to store temporary files
TEMP_DIR = '/path/to/temp/directory'

@app.route('/generate_file')
def generate_file():
    # Create a dynamic file (e.g., a text file)
    filename = 'dynamic_file.txt'
    file_content = 'This is dynamically generated content.'

    # Save to a temporary location
    file_path = os.path.join(TEMP_DIR, filename)
    with open(file_path, 'w') as f:
        f.write(file_content)

    # Return the URL to the file instead of sending it directly
    return f'File generated at: /serve/{filename}'

@app.route('/serve/<path:filename>')
def serve_file(filename):
    # Serve the file directly using Nginx
    return send_from_directory(TEMP_DIR, filename)

if __name__ == "__main__":
    app.run()
