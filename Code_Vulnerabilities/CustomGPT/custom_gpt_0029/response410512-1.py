
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/upload/folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/generate_file', methods=['POST'])
def generate_file():
    # Create dynamic content (for example, a simple text file)
    dynamic_content = "This is dynamically generated content."
    filename = 'dynamic_file.txt'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Save the file
    with open(file_path, 'w') as f:
        f.write(dynamic_content)

    # Return the URL to the file
    file_url = f"http://yourdomain.com/static/{filename}"  # Adjust based on your Nginx config
    return jsonify({'file_url': file_url})

if __name__ == '__main__':
    app.run()
