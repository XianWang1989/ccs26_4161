
from flask import Flask
import os

app = Flask(__name__)

# Define a directory for dynamic files
DYNAMIC_FILE_DIR = '/path/to/your/dynamic/files'

@app.route('/create-file/<filename>')
def create_file(filename):
    # Ensure the directory exists
    os.makedirs(DYNAMIC_FILE_DIR, exist_ok=True)

    # Create your content
    content = "This is dynamically created content"
    file_path = os.path.join(DYNAMIC_FILE_DIR, filename)

    with open(file_path, 'w') as f:
        f.write(content)

    return f"File created: {file_path}"

if __name__ == '__main__':
    app.run()
