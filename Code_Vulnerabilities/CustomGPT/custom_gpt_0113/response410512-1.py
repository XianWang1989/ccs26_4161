
from flask import Flask, send_from_directory
import os
from tempfile import gettempdir

app = Flask(__name__)

@app.route('/generate-file/<filename>')
def generate_file(filename):
    # Generate your dynamic content
    content = "This is some dynamic content"
    temp_file_path = os.path.join(gettempdir(), filename)

    # Write the content to a file
    with open(temp_file_path, 'w') as f:
        f.write(content)

    return f"File created: <a href='/files/{filename}'>Download</a>"

@app.route('/files/<filename>')
def serve_file(filename):
    # Use send_from_directory to serve the file from the temp directory
    return send_from_directory(gettempdir(), filename)

if __name__ == '__main__':
    app.run()
