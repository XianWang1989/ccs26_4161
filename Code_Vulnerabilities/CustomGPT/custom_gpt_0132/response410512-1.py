
from flask import Flask, request, send_file
import os
import tempfile

app = Flask(__name__)

@app.route('/generate_file')
def generate_file():
    # Create dynamic content
    content = "This is some dynamic content."

    # Write to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    with open(temp_file.name, 'w') as f:
        f.write(content)

    # Return the path of the generated file
    return {'file_path': temp_file.name}

@app.route('/download/<path:filename>')
def download_file(filename):
    # Serve the file directly through Nginx
    return send_file(os.path.join('/path/to/static/files', filename))

if __name__ == '__main__':
    app.run()
