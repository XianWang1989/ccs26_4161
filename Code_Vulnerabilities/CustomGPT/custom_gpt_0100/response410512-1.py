
from flask import Flask, send_file
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    file_path = temp_file.name

    # Write some dynamic content to the file
    with open(file_path, 'w') as f:
        f.write("This is some dynamic content.")

    # Return the file path for Nginx to serve
    return f'File generated: <a href="/media/{os.path.basename(file_path)}">Download here</a>'

if __name__ == '__main__':
    app.run()
