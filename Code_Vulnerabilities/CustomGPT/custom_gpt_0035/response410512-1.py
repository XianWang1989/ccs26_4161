
from flask import Flask, jsonify
import os
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = '/path/to/your/temp/directory'

@app.route('/generate-file', methods=['GET'])
def generate_file():
    # Create dynamic content
    file_name = f"{uuid.uuid4()}.txt"
    file_path = os.path.join(UPLOAD_FOLDER, file_name)

    with open(file_path, 'w') as f:
        f.write("This is dynamic content.")

    # Return the public URL to the file
    file_url = f"http://yourdomain.com/temp/{file_name}"
    return jsonify({"file_url": file_url})

if __name__ == "__main__":
    app.run()
