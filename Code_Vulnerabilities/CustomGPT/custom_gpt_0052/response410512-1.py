
from flask import Flask, send_file
import os
from tempfile import NamedTemporaryFile

app = Flask(__name__)

@app.route('/generate-file')
def generate_file():
    # Generate your dynamic content
    content = "This is dynamic content."

    # Save to a temporary file
    with NamedTemporaryFile(delete=False, suffix='.txt') as tmp_file:
        tmp_file.write(content.encode())
        tmp_file_path = tmp_file.name

    # Return the path where the file can be accessed
    # Ideally, provide a URL to Nginx
    return f'File saved. Access it at: http://your_nginx_server/serve/{os.path.basename(tmp_file_path)}'

if __name__ == '__main__':
    app.run()
