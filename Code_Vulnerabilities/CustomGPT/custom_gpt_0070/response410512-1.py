
from flask import Flask, request
import os

app = Flask(__name__)
MEDIA_FOLDER = 'media'  # Folder where files will be stored

@app.route('/generate', methods=['POST'])
def generate_file():
    content = request.form['content']  # Get content from form
    file_name = 'dynamic_file.txt'
    file_path = os.path.join(MEDIA_FOLDER, file_name)

    # Generate and save the file
    with open(file_path, 'w') as f:
        f.write(content)

    return f"File saved as {file_name}. You can access it at /media/{file_name}"

if __name__ == '__main__':
    if not os.path.exists(MEDIA_FOLDER):
        os.makedirs(MEDIA_FOLDER)
    app.run()
