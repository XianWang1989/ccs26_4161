
from flask import Flask, send_from_directory
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

    # Return the file path for Nginx to serve it
    return {"file_path": temp_file_path}
