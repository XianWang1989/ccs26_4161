
from flask import Flask, send_file
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# TEMP_DIR should be an absolute path where temporary files are written
TEMP_DIR = '/path/to/temp/directory'

@app.route('/generate-file/<filename>', methods=['GET'])
def generate_file(filename):
    content = "Sample dynamic content for your file."
    filepath = os.path.join(TEMP_DIR, secure_filename(filename))

    # Write content to the file
    with open(filepath, 'w') as f:
        f.write(content)

    # Return the URL where the file can be accessed
    return {'url': f'/files/{secure_filename(filename)}'}

if __name__ == '__main__':
    app.run()
