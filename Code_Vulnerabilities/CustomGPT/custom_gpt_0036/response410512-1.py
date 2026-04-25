
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
media_dir = '/path/to/media'  # Change this to your media directory path

# Ensure the media directory exists
if not os.path.exists(media_dir):
    os.makedirs(media_dir)

@app.route('/generate_media', methods=['POST'])
def generate_media():
    # Simulated dynamic content creation (e.g., a report or a file)
    content = "This is some dynamically generated content."
    file_name = f"dynamic_file.txt"
    file_path = os.path.join(media_dir, file_name)

    # Write content to file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL where the file can be accessed
    file_url = f"/media/{file_name}"  # Assuming Nginx is set up to serve /media/
    return jsonify({'file_url': file_url})

if __name__ == '__main__':
    app.run()
