
from flask import Flask, send_file
import os

app = Flask(__name__)
media_folder = '/path/to/media'

@app.route('/generate_file/<filename>')
def generate_file(filename):
    # Your logic to dynamically create the file
    file_path = os.path.join(media_folder, filename)

    # Example: Writing some content to the file
    with open(file_path, 'w') as f:
        f.write("Hello, this is your dynamic file content.")

    # Return the file path for Nginx to serve
    return f"File created: {filename}. You can access it via /media/{filename}"

if __name__ == '__main__':
    app.run()
