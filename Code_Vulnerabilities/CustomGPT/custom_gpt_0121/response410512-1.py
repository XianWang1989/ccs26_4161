
from flask import Flask, send_file
import os
import tempfile

app = Flask(__name__)

@app.route('/download')
def download_file():
    # Example of generating content dynamically
    content = "This is a dynamically generated file."

    # Write content to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(content.encode())
        tmp_file_path = tmp_file.name

    # Return the path to the file that Nginx can serve
    return {'file_url': f'/media/{os.path.basename(tmp_file_path)}'}

if __name__ == '__main__':
    app.run()
