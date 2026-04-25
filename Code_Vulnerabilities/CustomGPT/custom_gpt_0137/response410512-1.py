
from flask import Flask, send_from_directory, request
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Create a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt', dir='/path/to/your/temp/dir')

    # Write content to the file
    with open(temp_file.name, 'w') as f:
        f.write("This is the dynamically created content!")

    # Return the filename to the client
    # In a real-world scenario, consider sending the appropriate URL instead
    return f'File generated: {temp_file.name}'

@app.route('/serve-file/<path:filename>')
def serve_file(filename):
    # Serve the file from the temporary directory
    return send_from_directory('/path/to/your/temp/dir', filename)

if __name__ == '__main__':
    app.run()
