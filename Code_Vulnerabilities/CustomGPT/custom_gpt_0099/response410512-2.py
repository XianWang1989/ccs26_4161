
from flask import Flask
import os
import tempfile

app = Flask(__name__)

@app.route('/dynamic-media')
def dynamic_media():
    # Generate dynamic content
    dynamic_content = "This is dynamically generated content."

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
        temp_file.write(dynamic_content.encode('utf-8'))
        temp_file_path = temp_file.name

    # Use Nginx to serve the file
    return f"http://your_server_name/dynamic-media/{os.path.basename(temp_file_path)}"
