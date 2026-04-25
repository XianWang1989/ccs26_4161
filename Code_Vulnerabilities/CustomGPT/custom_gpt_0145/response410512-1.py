
from flask import Flask, jsonify, send_from_directory
import os
import tempfile

app = Flask(__name__)

@app.route('/generate_media')
def generate_media():
    # Create a temporary file for demonstration
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    temp_file.write(b'This is a dynamically created file content.')
    temp_file.close()

    # File URL should point to where Nginx serves files.
    file_url = f"http://your-nginx-server/media/{os.path.basename(temp_file.name)}"
    return jsonify({"file_url": file_url})

if __name__ == '__main__':
    app.run()
