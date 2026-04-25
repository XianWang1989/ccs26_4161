
from flask import Flask, request, jsonify
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file', methods=['GET'])
def generate_file():
    # Generate dynamic content
    content = "This is some dynamically generated content."

    # Create a temporary file
    temp = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
    with open(temp.name, 'w') as f:
        f.write(content)

    # Return the path of the newly created file
    return jsonify({'file_path': temp.name})

if __name__ == "__main__":
    app.run()
