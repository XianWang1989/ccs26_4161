
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    content = "This is some dynamic content."
    file_path = '/tmp/dynamic_file.txt'

    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL where Nginx can serve the file
    return jsonify({"url": f"/files/dynamic_file.txt"})

if __name__ == '__main__':
    app.run()
