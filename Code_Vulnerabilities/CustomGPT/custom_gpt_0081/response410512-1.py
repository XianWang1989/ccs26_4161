
from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/generate_media')
def generate_media():
    # Create a dynamic file (e.g., a PDF, image, etc.)
    file_path = '/path/to/serve/media/my_dynamic_file.txt'

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write some content into the file
    with open(file_path, 'w') as f:
        f.write("This is a dynamically generated file.")

    # Respond with the path to the dynamically created file
    return f"File created at {file_path}. You can access it via /media/my_dynamic_file.txt"

if __name__ == '__main__':
    app.run()
