
from flask import Flask, redirect, url_for
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Create a temporary file
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    with open(tmp_file.name, 'w') as f:
        f.write("This is dynamically created content.")

    # Redirect to the Nginx served path
    return redirect(url_for('serve_file', filename=os.path.basename(tmp_file.name)))

@app.route('/files/<filename>')
def serve_file(filename):
    # This route can be handled by Nginx
    return send_from_directory('/path/to/tmp/files', filename)

if __name__ == '__main__':
    app.run()
