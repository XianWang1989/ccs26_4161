
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
TEMP_DIR = '/path/to/temp/files'

@app.route('/create-file', methods=['POST'])
def create_file():
    content = request.form['content']
    filename = 'dynamically_generated_file.txt'
    file_path = os.path.join(TEMP_DIR, filename)

    # Write content to the file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the public URL to access the file
    return f'File created! Access it <a href="/media/{filename}">here</a>.'

if __name__ == '__main__':
    app.run()
