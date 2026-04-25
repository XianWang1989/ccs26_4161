
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
MEDIA_FOLDER = '/path/to/your/media/directory/'

@app.route('/generate_file/<filename>')
def generate_file(filename):
    # Simulate dynamic content generation
    content = "This is the dynamically created content."

    # Save the file to the media folder
    file_path = os.path.join(MEDIA_FOLDER, filename)
    with open(file_path, 'w') as file:
        file.write(content)

    return f"File generated: {filename}. You can access it <a href='/media/{filename}'>here</a>."

@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run()
