
from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Assuming you have logic to create a file
    file_name = 'dynamic_file.txt'
    file_path = os.path.join('/path/to/static/files', file_name)

    # Write dynamic content to the file
    with open(file_path, 'w') as f:
        f.write("This is dynamically generated content.")

    # Return the URL to access the file
    return redirect(url_for('serve_static_file', filename=file_name))

@app.route('/files/<filename>')
def serve_static_file(filename):
    # Note: Nginx will serve this file
    return f"File available at: /files/{filename}"

if __name__ == '__main__':
    app.run()
