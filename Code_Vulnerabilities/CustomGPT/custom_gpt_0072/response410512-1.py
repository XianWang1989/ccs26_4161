
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    file_path = 'path/to/generated/file.txt'

    # Example: Create a file dynamically
    with open(file_path, 'w') as f:
        f.write('This is dynamic content!')

    # Respond with the file path
    return {'file_url': f'/media/file.txt'}

if __name__ == '__main__':
    app.run()
