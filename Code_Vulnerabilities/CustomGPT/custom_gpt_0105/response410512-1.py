
from flask import Flask, send_file
import tempfile
import os

app = Flask(__name__)

@app.route('/dynamic-content')
def dynamic_content():
    # Generate your dynamic content
    content = "This is dynamically generated content."

    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as temp_file:
        temp_file.write(content.encode())
        temp_file_path = temp_file.name

    # Return the file path as a URL for Nginx to serve
    return f'File created: {temp_file_path}. You can access it via Nginx.'

if __name__ == '__main__':
    app.run()
