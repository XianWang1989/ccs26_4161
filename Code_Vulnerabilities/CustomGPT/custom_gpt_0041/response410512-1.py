
from flask import Flask, send_file, request
import os
import tempfile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Create some dynamic content
    content = "Dynamic content here"
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")

    with open(temp_file.name, 'w') as f:
        f.write(content)

    # Return the URL to access the file via Nginx
    return {'file_url': f'/media/{os.path.basename(temp_file.name)}'}

if __name__ == '__main__':
    app.run()
