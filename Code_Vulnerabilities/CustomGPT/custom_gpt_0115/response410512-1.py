
from flask import Flask, send_file, request
import os

app = Flask(__name__)

@app.route('/generate')
def generate_file():
    # Create dynamic content
    content = "Hello, World!"

    # Save it to a temporary file
    file_path = '/path/to/your/media/dynamic_file.txt'
    with open(file_path, 'w') as f:
        f.write(content)

    # Return the URL to the generated file
    return f"/media/dynamic_file.txt"

if __name__ == '__main__':
    app.run()
