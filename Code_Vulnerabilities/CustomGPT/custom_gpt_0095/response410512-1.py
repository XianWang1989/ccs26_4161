
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/generate_file')
def generate_file():
    # Create dynamic content
    content = "This is dynamically generated content."
    file_path = '/path/to/your/static/directory/generated_file.txt'

    # Save the file
    with open(file_path, 'w') as f:
        f.write(content)

    # Return a link to access the file
    return jsonify(url=f'/static/generated_file.txt')

if __name__ == '__main__':
    app.run()
