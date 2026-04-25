
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Configure the directory where files will be stored
UPLOAD_FOLDER = 'path_to_your_upload_folder'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/generate-file', methods=['POST'])
def generate_file():
    # Sample data to create a dynamic file
    data = request.json.get('data')
    filename = 'dynamic_file.txt'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Create and write to the file (you may customize this as needed)
    with open(file_path, 'w') as f:
        f.write(data)

    # Returning a URL that Nginx can serve
    file_url = f"http://your_domain.com/{filename}"
    return jsonify({'file_url': file_url})

if __name__ == '__main__':
    app.run()
