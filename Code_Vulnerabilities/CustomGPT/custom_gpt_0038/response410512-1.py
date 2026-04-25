
from flask import Flask, send_from_directory
import os
import tempfile

app = Flask(__name__)

@app.route('/generate')
def generate_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'dynamic_file.txt')

        # Write some dynamic content
        with open(file_path, 'w') as f:
            f.write("This is some dynamic content.")

        # Move the file to a more permanent location if needed
        permanent_path = '/path/to/serve/'  # Change to your static serving directory
        os.rename(file_path, os.path.join(permanent_path, 'dynamic_file.txt'))

        # Return the URL to access the file through Nginx
        return f'File generated. Access it <a href="/files/dynamic_file.txt">here</a>'

@app.route('/files/<path:filename>')
def serve_file(filename):
    return send_from_directory('/path/to/serve/', filename)

if __name__ == '__main__':
    app.run()
